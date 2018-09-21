

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
    return render_template('index.html', tags=tags)
```

