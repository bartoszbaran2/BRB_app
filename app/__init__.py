import secrets

from flask import Flask


def create_app():
    secret_key = secrets.token_hex(16)

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    return app
