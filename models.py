#_*_coding:utf-8_*_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

Base = declarative_base()

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    tag_name = Column(String(32))       #标签名

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(Text)            #文章标题
    content = Column(Text)          #文章内容，markdowm文本
    tag = Column(Text)              #文章所属标签（可以有多个标签，用'；'间隔）
    post_time = Column(DateTime, default=datetime.now())    #上传时间


'''
数据库设计
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
