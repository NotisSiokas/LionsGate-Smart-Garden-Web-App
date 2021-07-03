from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Node, Sensor, Quantity_Type


class QuantityForm(FlaskForm):
    sensor_id=QuerySelectField(query_factory=lambda: Sensor.query.all(), get_label="name", allow_blank=True)
    quantity_type_id=QuerySelectField(query_factory=lambda: Quantity_Type.query.all(), get_label="name", allow_blank=True)
    precision = StringField('Precision', validators=[DataRequired()])
    submit = SubmitField('Save')