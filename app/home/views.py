#_*_coding:utf-8_*_
from flask import render_template
from sqlalchemy import desc

from . import home
from .. import db_session
from ..models import Tag, Article

@home.route('/', methods=['GET'])
def index():
    tags = db_session.query(Tag).all()
    articles = db_session.query(Article).order_by(desc(Article.post_time))
    return render_template('index.html', tags=tags, articles=articles)
