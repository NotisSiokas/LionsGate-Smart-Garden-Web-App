from app import db


class Node(db.Model):
    __tablename__ = 'node'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    site_id = db.Column(db.Integer,nullable=False)
    name = db.Column(db.VARCHAR(50), nullable=False)
    latitude = db.Column(db.Float(6,4), nullable=True)
    longitude = db.Column(db.Float(7,4), nullable=True)
    description = db.Column(db.VARCHAR(200), nullable=True)
    sample_period = db.Column(db.Integer, nullable=False)
    average_period = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)