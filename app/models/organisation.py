from app import db
from flask_login import UserMixin



class Organisation(UserMixin,db.Model):
    __tablename__ = 'organisation'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(50), nullable=False)
    address = db.Column(db.VARCHAR(200), nullable=False)
    city = db.Column(db.VARCHAR(200),nullable=False)
    post_code = db.Column(db.VARCHAR(8),nullable=False)
    country = db.Column(db.VARCHAR(50),nullable=False)
    url = db.Column(db.VARCHAR(200), nullable=False)
    telephone = db.Column(db.VARCHAR(200), nullable=True)
    email = db.Column(db.VARCHAR(50), nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)

