from app import db


class QuantityType(db.Model):
    __tablename__ = 'quantity_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name= db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(200))
    symbol = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.name)