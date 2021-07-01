from app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    node_id = db.Column(db.Integer, nullable=False)
    sensor_type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    description = db.Column(db.VARCHAR(200), nullable=True)
    sample_period = db.Column(db.Integer, nullable=False)
    average_period = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)