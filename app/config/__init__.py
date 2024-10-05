from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


environment = BaseConfig()
