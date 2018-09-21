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
    from .blog import blog
    app.register_blueprint(home)
    app.register_blueprint(blog, url_prefix="/blog")
    return app