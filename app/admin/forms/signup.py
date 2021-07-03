from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    subject_group = QuerySelectField(query_factory=lambda: SignUpForm.query.all(), get_label="name", allow_blank=True)
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Save')