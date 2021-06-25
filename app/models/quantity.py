from app import db


class Quantity(db.Model):
    __tablename__ = 'quantity'

    id =
    sensor_id =
    quantity_type_id =
    precision =

    def __repr__(self):
        return '{}'.format(self.name)