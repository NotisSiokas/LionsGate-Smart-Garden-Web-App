from app import db


class AggregationType(db.Model):
    __tablename__ = 'aggregation_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    period =

    def __repr__(self):
        return '{}'.format(self.name)