# FlaskBlog
a blog built by flask


还未解决的问题：markdown中插入图片的路径问题
解决：将图片存放在github仓库中，访问github仓库中的相应图片，获得对应的图片链接地址，利用该链接地址作为图片链接

### python多线程编程

#### 使用threading模块创建线程

通过直接从threading.Thread类继承创建一个新的子类。Thread类提供了以下一些方法：

- run()：用以表示线程活动的方法，即该线程需要完成的一些功能操作
- start()：启动线程活动，即调用run()方法
- join([time])：等待直至线程终止（正常退出、或抛出未处理的异常、或发生超时）
- isAlive()：返回线程是否是活动的
- getName()：返回线程名
- setName()：设置线程名

实例化线程类后，调用类的start()方法启动新的线程：

```python
# -*- coding: utf-8 -*-
import threading
class myThread(threading.Thread):
    '''
    线程类在没有指定线程名时，会默认一个线程名
    '''
    def run(self):
        print("This is " + self.name)

for i in range(3):
    thread = myThread()
    thread.start()
```

输出结果：

```powershell
This is Thread-1
This is Thread-2
This is Thread-3

Process finished with exit code 0
```



#### 多线程同步

##### 锁机制

当多个线程都修改某一个共享数据的时候，需要进行同步控制。线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入锁机制。锁机制为资源引入一个状态：`锁定/非锁定`。某个线程要更改共享数据时，先将其锁定，此时资源的状态为`“锁定”`，其他线程不能更改；直到该线程释放资源，将资源的状态变成`“非锁定”`，其他的线程才能再次锁定该资源。锁机制保证了`每次只有一个线程进行写入操作`，从而保证了多线程情况下数据的正确性。

threading的Lock类，用该类的acquire函数进行加锁，用release函数进行解锁：

```python
# -*- coding: utf-8 -*-
import threading
import time

num = 0
lock = threading.Lock()

class myThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        #加锁
        if lock.acquire():
            num = num + 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            #解锁
            lock.release()

for i in range(5):
    thread = myThread()
    thread.start()
```

输出结果：

```powershell
Thread-2 set num to 1
Thread-3 set num to 2
Thread-4 set num to 3
Thread-1 set num to 4
Thread-5 set num to 5

Process finished with exit code 0
```



##### 条件变量同步

thread.Condition提供了对复杂线程同步问题的支持。Condition被称为条件变量，除了提供与Lock类似的`acquire`和`release`方法外，还提供了`wait`和`notify`方法。线程首先`acquire`一个条件变量，然后判断一些条件。如果条件不满足则`wait`；如果条件满足，进行一些处理改变条件后，通过`notify`方法通知其他线程，其他处于`wait`状态的线程接到通知后会重新判断条件。不断的重复这一过程，从而解决复杂的同步问题。

可以认为Condition对象维护了一个`锁`（Lock/RLock)和一个`waiting池`。线程通过`acquire`获得Condition对象，当调用`wait`方法时，线程会释放Condition内部的锁并进入`blocked`状态，同时在`waiting池`中记录这个线程。当调用`notify`方法时，Condition对象会从`waiting池`中挑选一个线程，通知其调用`acquire`方法尝试取到锁。

除了`notify`方法外，Condition对象还提供了`notifyAll`方法，可以通知`waiting池`中的所有线程尝试`acquire`内部锁。由于上述机制，处于`waiting`状态的线程只能通过`notify`方法唤醒，所以`notifyAll`的作用在于防止有线程永远处于沉默状态。

以生产者-消费者问题作为例子：当存量不足1000时，生产者每次生产100个；当存量不足100时，消费者停止消费，否则消费者每次消费20个。

```python
# -*- coding: utf-8 -*-
import threading
import time

goods = 100
condition = threading.Condition()

class Producer(threading.Thread):
    def __init__(self, condition):
        threading.Thread.__init__(self)
        self.condition = condition

    def run(self):
        global goods
        while True:
            if self.condition.acquire():
                if goods > 1000:
                    self.condition.wait()
                else:
                    goods += 100
                    msg = "Producer Thread" + self.name + " produce 100, now goods = " + str(goods)
                    print(msg)
                    self.condition.notify()
            self.condition.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self, condition):
        threading.Thread.__init__(self)
        self.condition = condition

    def run(self):
        global goods
        while True:
            if self.condition.acquire():
                if goods < 100:
                    self.condition.wait()
                else:
                    goods -= 20
                    msg = "Consumer Thread " + self.name + " consume 20, now goods = " + str(goods)
                    print(msg)
                    self.condition.notify()
            self.condition.release()
            time.sleep(1)

for i in range(2):
    thread = Producer(condition)
    thread.start()

for i in range(8):
    thread = Consumer(condition)
    thread.start()
```



##### 队列同步

考虑更复杂的一种场景：产品是各不相同的。这时只记录一个数量就不够了，还需要记录每个产品的细节。很容易想到需要用一个容器将这些产品记录下来。

Python的Queue模块中提供了`同步的`、`线程安全`的队列类，包括`FIFO`（先入先出)队列`Queue`，`LIFO`（后入先出）队列`LifoQueue`，和优先级队列`PriorityQueue`。这些队列都实现了`锁原语`，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

利用FIFO队列实现生产者消费者问题：

```python
# -*- coding: utf-8 -*-
import threading
import time
from queue import Queue

queue = Queue()
count = 0

class Producer(threading.Thread):
    def run(self):
        global queue
        global count
        while True:
            for i in range(5):
                if queue.qsize() > 100:
                     pass
                else:
                     count = count +1
                     msg = "Producer Thread " + self.name + ' produce: production '+str(count)
                     queue.put(count)
                     print(msg)
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            for i in range(2):
                if queue.qsize() < 50:
                    pass
                else:
                    msg = "Consumer Thread " + self.name + ' consume: production ' + str(queue.get())
                    print(msg)
            time.sleep(1)

def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
if __name__ == '__main__':
    test()
```



