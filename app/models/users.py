from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    organisation_id = db.Column(db.VARCHAR(50), nullable=True)
    first_name = db.Column(db.VARCHAR(60), nullable=False)
    last_name = db.Column(db.VARCHAR(60), nullable=False)
    email = db.Column(db.VARCHAR(60), index=True, unique=False)
    telephone = db.Column(db.VARCHAR(12), unique=True, nullable=False)
    profile_text = db.Column(db.VARCHAR(200), nullable=True)
    password_hash = db.Column(db.VARCHAR(100), nullable=True)
    failed_login_attempts = db.Column(db.Integer, nullable=True)
    create_date = db.Column(db.DateTime, nullable=True)
    archive_date = db.Column(db.DateTime, nullable=True)
    confirmation_token = db.Column(db.VARCHAR(100), nullable=True)
    display_email_flag = db.Column(db.Boolean, nullable=True)
    display_phone_flag = db.Column(db.Boolean)
    admin_flag = db.Column(db.Boolean, nullable=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '{Users: {} {}>'.format(self.first_name, self.last_name)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))