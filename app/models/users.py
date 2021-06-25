from app import db


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    organisation_id =
    first_name =
    last_name =
    email =
    telephone =
    profile_text =
    password_hash =
    failed_login_attempts =
    create_date =
    archive_date =
    confirmation_token =
    display_email_flag =
    display_phone_flag =
    admin_flag =

    def __repr__(self):
        return '{}'.format(self.name)