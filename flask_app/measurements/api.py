from flask import request
from flask_restplus import Resource
from sqlalchemy.exc import SQLAlchemyError

from flask_app import db
from flask_app.measurements import measurements_api
from flask_app.measurements.models import Measurement


@measurements_api.route('/')
class MeasurementApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)

            measurement = Measurement(
                        temperature=data['temperature'],
                        air_quality=data['air_quality'],
                        humidity=data['humidity']
            )

            # measurement = Measurement(**data)

            db.session.add(measurement)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': 'Database error.'}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500
        return {'message':"Yay! :D"}, 200
