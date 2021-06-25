from app import db


class Organisation(db.Model):
    __tablename__ = 'organisation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    address =
    city =
    post_code =
    country =
    url =
    telephone =
    email = 

    def __repr__(self):
        return '{}'.format(self.name)