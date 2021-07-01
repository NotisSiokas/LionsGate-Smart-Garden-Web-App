from app import db


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity_id = db.Column(db.Integer, nullable=False)
    timestamp_from = db.Column(db.Integer, nullable=False)
    timestamp_to = db.Column(db.Integer, nullable=False)
    mean = db.Column(db.Float(5,2), nullable=False)
    min = db.Column(db.Float(5,2), nullable=False)
    max = db.Column(db.Float(5,2), nullable=False)
    stdev = db.Column(db.Float(5,2), nullable=False)
    records = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)