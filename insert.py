import random
from app import createApp, db
from models import Measurement
from server import app


def insert():
    for i in range(1, 990):
        temperature = random.randint(1, 100)
        airQuality = random.randint(1, 100)
        humidity = random.randint(1, 100)

        measurement = Measurement(temperature=temperature,
                                  air_quality=airQuality,
                                  humidity=humidity)
        db.session.add(measurement)
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        try:
            # insert()
            print(Measurement.query.all())
        except Exception as e:
            print(e)
