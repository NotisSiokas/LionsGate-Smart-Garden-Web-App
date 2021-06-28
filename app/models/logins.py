from app import db


class Logins(db.Model):
    __tablename__ = 'logins'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id =
    timestamp = 

    def __repr__(self):
        return '{}'.format(self.name)