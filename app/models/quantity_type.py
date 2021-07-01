from app import db


class QuantityType(db.Model):
    __tablename__ = 'quantity_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name= db.Column(db.VARCHAR(100), nullable=False)
    unit = db.Column(db.VARCHAR(10), nullable=False)
    symbol = db.Column(db.VARCHAR(10), nullable=True)

    def __repr__(self):
        return '{}'.format(self.name)