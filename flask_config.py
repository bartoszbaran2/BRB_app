import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    secret_key = secrets.token_hex(16)
    SECRET_KEY = os.environ.get('SECRET_KEY') or secret_key

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
