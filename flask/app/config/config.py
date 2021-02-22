import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    # Session
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)

    # Celery
    CELERY_TIMEZONE = "Asia/Taipei"


class DevelopmentConfig(BaseConfig):
    DEBUG = False

    # SQLALCHEMY_ECHO = True

    # # Flask-sqlalchemy
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("db")
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     "pool_pre_ping": True,
    #     "pool_recycle": 3600,
    #     "pool_timeout": 900,
    #     "pool_size": 10,
    #     "max_overflow": 5,
    # }



class ProductionConfig(BaseConfig):
    DEBUG = False

    # # Flask-sqlalchemy
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get("db")
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     "pool_pre_ping": True,
    #     "pool_recycle": 3600,
    #     "pool_timeout": 900,
    #     "pool_size": 10,
    #     "max_overflow": 5,
    # }



class TestingConfig(BaseConfig):
    TESTING = True

    # # Flask-sqlalchemy
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

    # 關閉 CSRF
    WTF_CSRF_ENABLED = False

config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
