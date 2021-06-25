from app import db


class Organisation(db.Model):
    __tablename__ = 'organisation'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(60), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(20),nullable=False)
    post_code = db.Column(db.String(6),nullable=False)
    country = db.Column(db.String(25),nullable=False)
    url = db.Column(db.String(100))
    telephone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
        return '{}'.format(self.name)