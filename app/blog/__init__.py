#_*_coding:utf-8_*_
from flask import Blueprint

blog = Blueprint('blog',__name__)

from . import views