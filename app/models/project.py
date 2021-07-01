from app import db


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(60), unique=True, nullable=False)
    description = db.Column(db.VARCHAR(200), unique=True, nullable=True)
    sample_period = db.Column(db.Integer, nullable=False)
    average_period = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)