from app import db


class SensorHistory(db.Model):
    __tablename__ = 'sensor_history'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    sensor_id =
    user_id =
    timestamp =
    event_type_id =
    description =
    attribute =
    old_value = 

    def __repr__(self):
        return '{}'.format(self.name)