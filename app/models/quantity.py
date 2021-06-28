from app import db


class Quantity(db.Model):
    __tablename__ = 'quantity'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    sensor_id = db.Column(db.Integer, nullable=False)
    quantity_type_id = db.Column(db.Integer, nullable=False)
    precision = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.name)