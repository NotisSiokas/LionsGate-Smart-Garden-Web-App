from app import db


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=True, nullable=False)
    #sample_period
    #average_period

    def __repr__(self):
        return '{}'.format(self.name)