from app import db


class SiteHistory(db.Model):
    __tablename__ = 'site_history'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    site_id =
    user_id =
    timestamp =
    event_type_id =
    description =

    def __repr__(self):
        return '{}'.format(self.name)