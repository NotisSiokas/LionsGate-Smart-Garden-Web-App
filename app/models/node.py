from app import db


class Node(db.Model):
    __tablename__ = 'node'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    site_id = db.Column(db.Integer,nullable=False)
    name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.String(200))
    longitude = db.Column(db.String(200))
    description = db.Column(db.String(200))
    sample_period = db.Column(db.String(200))
    average_period = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.name)