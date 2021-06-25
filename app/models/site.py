from app import db


class Site(db.Model):
    __tablename__ = 'site'

    project_id =
    name =
    description =
    location_polygon =
    centroid_latitude =
    centroid_longitude =
    sample_period =
    average_period =

    def __repr__(self):
        return '{}'.format(self.name)