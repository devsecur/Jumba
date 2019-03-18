class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE = 'db.sqlite' # not a docker link
    SQLALCHEMY_DATABASE_URI = 'sqlite:////app/data/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE = 'db.sqlite' # not a docker link
    SQLALCHEMY_DATABASE_URI = 'sqlite:////app/data/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DATABASE = 'db.sqlite' # not a docker link
