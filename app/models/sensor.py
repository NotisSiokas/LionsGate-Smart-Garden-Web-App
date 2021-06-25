from app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    id =
    node_id =
    sensor_type_id =
    name =
    description =
    sample_period =
    average_period =

    def __repr__(self):
        return '{}'.format(self.name)