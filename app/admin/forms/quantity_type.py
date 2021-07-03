from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Node, Sensor


class Quantity_Type_Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    symbol = StringField('Symbol', validators=[DataRequired()])
    submit = SubmitField('Save')