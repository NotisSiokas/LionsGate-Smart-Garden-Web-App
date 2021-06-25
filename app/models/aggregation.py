from app import db


class Aggregation(db.Model):
    __tablename__ = 'aggregation'

    id =
    quantity_id =
    aggregation_type_id =
    value =

    def __repr__(self):
        return '{}'.format(self.name)