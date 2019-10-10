from flask import Flask
from config.development import Development
# from flask_migrate import Migrate


def createApp(config):
    app = Flask(__name__)
    app.config.from_object(config)

    return app




