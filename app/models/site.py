from app import db


class Site(db.Model):
    __tablename__ = 'site'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    location_polygon = db.Column(db.String(60), unique=True, nullable=False)
    #centroid_latitude =
    #centroid_longitude =
    #sample_period =
    #average_period =

    def __repr__(self):
        return '{}'.format(self.name)