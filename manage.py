from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from config import *

engine = create_engine(DevConfig.database_url, encoding='utf-8', echo=True)
