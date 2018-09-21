目录结构

- app
  - about/
  - blog/
  - home/
    - __ init __.py
    - views.py
  - static/
  - templates/
  - __ init __.py
  - models.py
- .gitignore
- config.py
- main.py
- manage.py

manage.py

```python
#_*_coding:utf-8_*_
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from app.models import Base, Tag
from config import *

'''
以下操作的前提是数据库是存在的！
'''
engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True) #连接数据库
Session = sessionmaker(bind=engine)
db_session = Session()

def init_tables():
    '''初始化数据表'''
    Base.metadata.create_all(engine)        #建表
    print("Tables init --- Success!")

def drop_tables():
    '''删除所有表'''
    Base.metadata.drop_all(engine)
    print("Tables delete --- Success!")

def insert_test_data():
    tag1 = Tag(tag_name='Python')
    tag2 = Tag(tag_name='Selenium')
    tag3 = Tag(tag_name='自动化')
    db_session.add(tag1)
    db_session.add(tag2)
    db_session.add(tag3)
    db_session.commit()
    
def insert_test_artical_data():
    artical1 = Article(title='test1', content='test content1!\n======1======\n*****1*****', tag='Python')
    artical2 = Article(title='test2', content='test content2!\n======2======\n*****2*****', tag='Selenium')
    artical3 = Article(title='test3', content='test content3!\n======3======\n*****3*****', tag='自动化;Python')
    db_session.add(artical1)
    db_session.add(artical2)
    db_session.add(artical3)
    db_session.commit()
```

main.py

```python
#_*_coding:utf-8_*_
from app import creat_app

app = creat_app()

if __name__ == "__main__":
    app.run()
```

app/__ init __.py

```python
#_*_coding:utf-8_*_
from flask import Flask
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from config import *

engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True) #连接数据库
Session = sessionmaker(bind=engine)
db_session = Session()

def creat_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)

    from .home import home
    app.register_blueprint(home)
    return app
```

app/home/__ init __.py

```python
#_*_coding:utf-8_*_
from flask import Blueprint

home = Blueprint('home',__name__)

from . import views
```

app/home/views.py

```python
#_*_coding:utf-8_*_
from flask import render_template

from . import home
from .. import db_session
from ..models import Tag, Article

@home.route('/', methods=['GET'])
def index():
    tags = db_session.query(Tag).all()
    articles = db_session.query(Article).order_by(Article.post_time)
    return render_template('index.html', tags=tags, articles=articles)
```

app/templates/index.html

```html
{% extends 'base.html' %}

{% block content %}
{{ super() }}
<div class="container">
    <div class="row">
        <!--最近几篇文章显示区域-->
        <div class="col-md-9">
            {% for article in articles %}
            <div class="post-preview">
                <a href="#">
                    <h5 class="post-title" style="font-size: x-large">
                        {{ article.title }}
                    </h5>
                </a>
                <p class="post-subtitle">
                    Tags:
                    {% for article_tag in article.tag.split(';') %}
                    <a href="#"><span class="badge badge-success">{{ article_tag }}</span></a>
                    {% endfor %}
                </p>
                <p class="post-meta">
                    {{ "Post at " + article.post_time|string }}
                </p>
            </div>
            <hr>
            {% endfor %}
        </div>
        <!--右侧标签区域-->
        <div class="col-md-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Tags</h5>
                    {% for tag in tags %}
                    <a href="#"><span class="badge badge-success">{{ tag.tag_name }}</span></a>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```
