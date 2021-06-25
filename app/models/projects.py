from app import db


class Projects(db.Model):
    __tablename__ = 'projects'

    id =
    user_id =
    name =
    description =
    sample_period =
    average_period =

    def __repr__(self):
        return '{}'.format(self.name)