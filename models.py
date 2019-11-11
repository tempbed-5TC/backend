from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime

class temperature(db.Model):
    __tablename__ = 'temperature'

    id = db.Column(db.Integer, autoincrement=True)
    sensor_id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, sensor_id, temperature, timestamp):
        self.sensor_id = sensor_id
        self.temperature = temperature
        self.timestamp = timestamp

# serialize method here is needed to return objects in response as JSON.
    def serialize(self):
        return {
            'sensor_id': self.sensor_id,
            'temperature': self.temperature,
            'timestamp': self.timestamp,
        }
