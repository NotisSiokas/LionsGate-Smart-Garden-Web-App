from app import db


class SensorType(db.Model):
    __tablename__ = 'sensor_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    manufacturer = db.Column(db.String(60), unique=True, nullable=False)
    url = db.Column(db.String(100))
    #model =
    #datasheet =

    def __repr__(self):
        return '{}'.format(self.name)