#_*_coding:utf-8_*_
from flask import Blueprint

home = Blueprint('home',__name__)

from . import views