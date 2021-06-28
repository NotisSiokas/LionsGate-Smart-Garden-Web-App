from app import db


class EventType(db.Model):
    __tablename__ = 'event_type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description =

    def __repr__(self):
        return '{}'.format(self.name)