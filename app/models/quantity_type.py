from app import db


class QuantityType(db.Model):
    __tablename__ = 'quantity_type'

    id =
    name=
    unit =
    symbol =

    def __repr__(self):
        return '{}'.format(self.name)