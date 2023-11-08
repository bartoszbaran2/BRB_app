from flask import Flask

from flask_config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
