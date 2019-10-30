from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'measurements'
measurement_blueprint = Blueprint(APP_NAME, __name__, url_prefix=f"/{APP_NAME}")

measurements_api = Api(measurement_blueprint)

from flask_app.measurements.api import *

# zašto ne pravi cirkularni import?

    # from flask import request
    # from flask_restplus import Resource
    # from sqlalchemy.exc import SQLAlchemyError
    # from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
    #
    # from flask_app import db
    # from flask_app.measurements import measurements_api

