from app import db


class Node(db.Model):
    __tablename__ = 'node'

    id =
    site_id =
    name =
    latitude =
    longitude =
    description =
    sample_period =
    average_period =

    def __repr__(self):
        return '{}'.format(self.name)