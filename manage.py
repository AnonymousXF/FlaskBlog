from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from config import *

engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True)

'''
数据库初步设计
-----------------
--article文章表
-----------------
id              //自增id
title           //文章标题
content         //文章内容，markdown文本
tag             //标签字符串，用';'间隔多个标签
post_time       //上传时间



-----------------
--tag标签表
-----------------
id              //自增id
tag_name        //标签名
'''
