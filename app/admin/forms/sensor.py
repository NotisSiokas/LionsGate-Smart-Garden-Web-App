from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Node, Sensor_Type


class SensorForm(FlaskForm):
    node_id=QuerySelectField(query_factory=lambda: Node.query.all(), get_label="name", allow_blank=True)
    sensor_type_id=QuerySelectField(query_factory=lambda: Sensor_Type.query.all(), get_label="name", allow_blank=True)
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description',)
    sample_period = StringField('Sample Period', validators=[DataRequired()])
    average_period = StringField('Average Period',validators=[DataRequired()])
    submit = SubmitField('Save')