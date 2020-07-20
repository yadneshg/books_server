import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    SECRET_KEY = 'this-really-needs-to-be-changed'
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Cyber123@localhost:5432/db01"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL1']
    print(f"SQLALCHEMY_DATABASE_URI : {SQLALCHEMY_DATABASE_URI}")
    print(f"SECRET_KEY : {SECRET_KEY}")


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True