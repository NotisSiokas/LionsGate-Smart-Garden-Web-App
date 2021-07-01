from app import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.VARCHAR(50), nullable=False)
    first_name = db.Column(db.VARCHAR(60), nullable=False)
    last_name = db.Column(db.VARCHAR(60), nullable=False)
    email = db.Column(db.VARCHAR(60), index=True, unique=False)
    telephone = db.Column(db.VARCHAR(), unique=True, nullable=False)
    profile_text = db.Column(db.VARCHAR(200), nullable=False)
    password_hash = db.Column(db.VARCHAR(100), nullable=False)
    failed_login_attempts = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    archive_date = db.Column(db.DateTime, nullable=False)
    confirmation_token = db.Column(db.VARCHAR(100), nullable=False)
    display_email_flag = db.Column(db.Boolean, nullable=False)
    display_phone_flag = db.Column(db.Boolean)
    admin_flag = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return '{}'.format(self.name)