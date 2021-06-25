from app import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), index=True, unique=True)
    telephone = db.Column(db.Integer(), unique=True, nullable=False)
    profile_text = db.Column(db.String(200))
    password_hash = db.Column(db.String(128))
    failed_login_attempts = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    archive_date = db.Column(db.DateTime)
    confirmation_token = db.Column(db.String(20))
    display_email_flag = db.Column(db.String(20))
    display_phone_flag = db.Column(db.String(20))
    admin_flag = db.Column(db.String(20))

    def __repr__(self):
        return '{}'.format(self.name)