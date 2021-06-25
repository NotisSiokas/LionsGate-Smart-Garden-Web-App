from app import db


class AggregationType(db.Model):
    __tablename__ = 'aggregation_type'

    id =
    name =
    period =

    def __repr__(self):
        return '{}'.format(self.name)