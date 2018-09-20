#_*_coding:utf-8_*_
from sqlalchemy import *
from models import Base
from config import *

'''
以下操作的前提是数据库是存在的！
'''

def init_tables():
    '''初始化数据表'''
    engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True) #连接数据库
    Base.metadata.create_all(engine)        #建表
    print("Tables init --- Success!")

def drop_tables():
    '''删除所有表'''
    engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True)  # 连接数据库
    Base.metadata.drop_all(engine)
    print("Tables delete --- Success!")

