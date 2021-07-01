from app import db


class SensorType(db.Model):
    __tablename__ = 'sensor_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    manufacturer = db.Column(db.VARCHAR(100), unique=True)
    url = db.Column(db.VARCHAR(200), nullable=True)
    model = db.Column(db.VARCHAR(100), nullable=True)
    datasheet = db.Column(db.VARCHAR(200), nullable=True)

    def __repr__(self):
        return '{}'.format(self.name)