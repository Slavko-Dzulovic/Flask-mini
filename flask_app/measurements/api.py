import math

from flask import request
from flask_restplus import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from flask_app import db
from flask_app.measurements import measurements_api
from flask_app.measurements.models import Measurement
from flask_app.measurements.schemas import MeasurementPost, MeasurementGet

from datetime import datetime

measurement_post_validation = MeasurementPost()
measurement_get_validation = MeasurementGet()


@measurements_api.route('/')
@measurements_api.route('/<int:measurement_id>')
class MeasurementApi(Resource):
    def post(self):
        try:
            data = measurement_post_validation.load(request.get_json(force=True))

            measurement = Measurement(
                temperature=data['temperature'],
                air_quality=data['air_quality'],
                humidity=data['humidity'])

            # measurement = Measurement(**data)

            db.session.add(measurement)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': 'Database error.'}, 500
        except ValidationError as validationError:
            print(f"Validation error:: {validationError}")
            return {'message': 'Validation error post'}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500
        return {'message': "Yay! :D"}, 200

    def get(self, measurement_id):
        try:
            measurement = db.session.query(Measurement).filter(Measurement.id == measurement_id).one()

        except NoResultFound as error:
            print(f"No result found for id: {measurement_id}")
            print(f"Error: {error}")
            return {'message': 'No result found.'}, 404
        except MultipleResultsFound as error:
            print(f"Multiple results found for id: {measurement_id}")
            print(f"Error: {error}")
            return {'message': 'Database error.'}, 500
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': 'Database error.'}, 500

        except ValidationError as validationError:
            print(f"Validation error:: {validationError}")
            return {'message': 'Validation error get'}, 500

        except Exception as server_error:
            print(f"Server error:: {server_error}")
            return {'message': 'Server error.'}, 500

        response_data = {'temperature': measurement.temperature,
                         'air_quality': measurement.air_quality,
                         'humidity': measurement.humidity}

        return response_data, 200


@measurements_api.route('/history/<int:start>/<int:end>/<int:limit>')
class MeasurementApi2(Resource):
    def get(self, start, end, limit):
        try:
            start_date = datetime.fromtimestamp(start/1000.0)
            end_date = datetime.fromtimestamp(end/1000.0)
            limit_data = limit

            filtered_measurements = db.session.query(Measurement).\
                filter(Measurement.created_datetime >= start_date, Measurement.created_datetime <= end_date)

            length = filtered_measurements.count()

            if limit_data != 0:
                step = math.ceil(length / limit_data)
            else:
                step = 1

            list_of_measurements = []

            for i in range(0, length, step):
                list_of_measurements.append(measurement_get_validation.dump(filtered_measurements[i]))

        except ValidationError as validationError:
            print(f"Validation error:: {validationError}")
            return {'message': 'Validation error get'}, 500

        except Exception as server_error:
            print(f"Server error:: {server_error}")
            return {'message': 'Server error.'}, 500

        return {"Measurements": list_of_measurements}, 200


@measurements_api.route('/latest')
class MeasurementApi3(Resource):
    def get(self):
        return measurement_get_validation.dump(db.session.
                                               query(Measurement).
                                               order_by(Measurement.id.desc()).first())


# api endpoint, /measurements/history
