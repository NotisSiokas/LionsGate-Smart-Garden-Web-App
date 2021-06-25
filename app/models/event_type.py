from app import db


class EventType(db.Model):
    __tablename__ = 'event_type'

    id =
    name =
    description =

    def __repr__(self):
        return '{}'.format(self.name)