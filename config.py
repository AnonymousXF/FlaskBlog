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
    database_url = ""
