from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

ENVS_MAP = {
    "development": "config.development.DevelopmentConfig",
    "production": "config.production.ProductionConfig",
    "testing": "config.testing.TestingConfig",
}

db = SQLAlchemy()
migrate = Migrate(db=db)
ma = Marshmallow()


def create_app(config_name="development"):
    # create and configure the app
    app = Flask(__name__)
    config_env = ENVS_MAP.get(config_name)
    app.config.from_object(config_env)
    init_logging(app)
    init_extensions(app)

    with app.app_context():
        init_blueprints(app)

    return app


def init_extensions(app):
    CORS(app)
    db.init_app(app)
    migrate.init_app(app)
    ma.init_app(app)


def init_blueprints(app):
    from app.api.infra.v1.apiv1 import blueprint as data_api_blueprint

    app.register_blueprint(data_api_blueprint)


def init_logging(app):
    import logging

    app.logger.setLevel(logging.ERROR)
    return
