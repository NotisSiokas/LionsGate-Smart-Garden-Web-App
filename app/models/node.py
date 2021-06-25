from app import db


class Node(db.Model):
    __tablename__ = 'node'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    site_id = db.Column(db.Integer,nullable=False)
    name = name= db.Column(db.String(50), nullable=False)
    #latitude =
    #longitude =
    #description =
    #sample_period =
    #average_period =

    def __repr__(self):
        return '{}'.format(self.name)