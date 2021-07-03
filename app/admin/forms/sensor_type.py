from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Node


class SensorTypeForm(FlaskForm):
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    url = StringField('Url')
    model = StringField('Model')
    datasheet = StringField('Datasheet')
    submit = SubmitField('Save')