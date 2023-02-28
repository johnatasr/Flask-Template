from . import Config


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
