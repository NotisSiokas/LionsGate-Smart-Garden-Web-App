from app import db


class Aggregation(db.Model):
    __tablename__ = 'aggregation'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity_id = db.Column(db.Integer, nullable=False)
    aggregation_type_id =
    value =

    def __repr__(self):
        return '{}'.format(self.name)