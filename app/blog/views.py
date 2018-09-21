#_*_coding:utf-8_*_
from flask import render_template

from . import blog
from .. import db_session
from ..models import Tag, Article

@blog.route('/', methods=['GET','POST'])
def bloglist():
    tags = db_session.query(Tag).all()
    articles = db_session.query(Article.id, Article.title, Article.tag, Article.post_time).order_by(Article.post_time)
    return render_template("bloglist.html", tags=tags, articles=articles)

@blog.route('/article_detail/<article_id>')
def article_detail(article_id):
    article = db_session.query(Article).filter(Article.id == article_id).first()
    return render_template("article.html", article=article)