import logging


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True
    LOGLEVEL = logging.DEBUG
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class ProductionConfig(Config):
    DEBUG = False
    LOGLEVEL = logging.ERROR
    logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


class TestingConfig(Config):
    TESTING = True
    LOGLEVEL = logging.WARNING
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}