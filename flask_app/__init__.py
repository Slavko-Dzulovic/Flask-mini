from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # gde je baza? Uporediti sa to-do app, u terminalu db.createAll()
migrate = Migrate()

from flask_app.measurements.models import Measurement
from flask_app.measurements import measurement_blueprint


def createApp(config):  # glavni config
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(measurement_blueprint)

    return app
