from app import db


class Projects(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    project_id = db.Column(db.Integer, nullable=False)
    user_id =
    timestamp =
    event_type_id =
    description =

    def __repr__(self):
        return '{}'.format(self.name)