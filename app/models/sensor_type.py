from app import db


class SensorType(db.Model):
    __tablename__ = 'sensor_type'

    id =
    manufacturer =
    url =
    model =
    datasheet =

    def __repr__(self):
        return '{}'.format(self.name)