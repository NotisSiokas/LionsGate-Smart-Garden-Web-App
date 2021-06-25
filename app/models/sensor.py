from app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    node_id = db.Column(db.Integer, nullable=False)
    sensor_type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    #sample_period =
    #average_period =

    def __repr__(self):
        return '{}'.format(self.name)