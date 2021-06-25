from app import db


class NodeHistory(db.Model):
    __tablename__ = 'node_history'

    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, unique=True)
    timestamp = db.Column(db.DateTime)
    #event_type_id =
    description = db.Column(db.String(200))

    def __repr__(self):
        return '{}'.format(self.name)