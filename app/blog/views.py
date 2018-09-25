#_*_coding:utf-8_*_
from flask import render_template, request
from sqlalchemy import desc

from . import blog
from .. import db_session
from ..models import Tag, Article

@blog.route('/', methods=['GET'])
def bloglist():
    tags = db_session.query(Tag).all()
    articles = db_session.query(Article.id, Article.title, Article.tag, Article.post_time).order_by(desc(Article.post_time))
    return render_template("bloglist.html", tags=tags, articles=articles)

@blog.route('/list_by_tag', methods=['POST'])
def list_by_tag():
    tag = request.json
    #print(tag)
    tag_name = tag['tag']
    if tag_name == "全部":
        articles = db_session.query(Article.id, Article.title, Article.tag, Article.post_time).order_by(desc(Article.post_time))
    else:
        articles = db_session.query(Article.id, Article.title, Article.tag, Article.post_time).filter(Article.tag.like('%' + tag_name + '%')).order_by(desc(Article.post_time))
    return render_template("list_by_tag.html", articles=articles, tag_name=tag_name)


@blog.route('/article_detail/<article_id>')
def article_detail(article_id):
    article = db_session.query(Article).filter(Article.id == article_id).first()
    return render_template("article.html", article=article)
