#_*_coding:utf-8_*_
class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Devlopment config class."""
    #open DEBUG
    DEBUG = True
    database_url = "mysql://root:password@ip:port/database?charset=utf8"
