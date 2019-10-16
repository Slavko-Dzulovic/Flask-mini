from datetime import datetime
from app import db
from sqlalchemy import Column, Integer, String, DateTime


class Measurement(db.Model):
    __tablename__ = 'measurements'

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, nullable=False)
    air_quality = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    created_datetime = Column(DateTime, nullable=False, default=datetime.now)
