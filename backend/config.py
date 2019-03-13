class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE = 'db.sqlite' # not a docker link

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE = 'db.sqlite' # not a docker link

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DATABASE = 'db.sqlite' # not a docker link
