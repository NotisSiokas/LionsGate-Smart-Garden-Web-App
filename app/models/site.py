from app import db


class Site(db.Model):
    __tablename__ = 'site'

    id = db.Column(db.Integer, primary_key=False)
    project_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    description = db.Column(db.VARCHAR(200), unique=True, nullable=False)
    location_polygon = db.Column(db.Integer, unique=True, nullable=True)
    centroid_latitude = db.Column(db.Float(6,4), nullable=True)
    centroid_longitude = db.Column(db.Float(7,4), nullable=True)
    sample_period = db.Column(db.Integer, nullable=False)
    average_period = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)