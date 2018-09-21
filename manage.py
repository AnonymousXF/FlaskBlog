# _*_coding:utf-8_*_
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from app.models import Base, Tag, Article
from config import *

'''
以下操作的前提是数据库是存在的！
'''
engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True)  # 连接数据库
Session = sessionmaker(bind=engine)
db_session = Session()


def init_tables():
    '''初始化数据表'''
    Base.metadata.create_all(engine)  # 建表
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
