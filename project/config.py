import os


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../development.db'
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
