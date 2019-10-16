from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.development import Development
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def createApp(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    return app




