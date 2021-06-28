from app import db


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity_id = db.Column(db.Integer, nullable=False)
    timestamp_from = db.Column(db.TIMESTAMP)
    timestamp_to = db.Column(db.TIMESTAMP)
    mean = db.Column(db.String(200))
    min = db.Column(db.String(200))
    max = db.Column(db.String(200))
    stdev = db.Column(db.String(200))
    records = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.name)