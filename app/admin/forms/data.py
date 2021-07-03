from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import  Quantity


class DataForm(FlaskForm):
    quantity_id = QuerySelectField(query_factory=lambda: Quantity.query.all(), get_label="name", allow_blank=True)
    timestamp_from = StringField('Name', validators=[DataRequired()])
    timestamp_to = StringField('Description', validators=[DataRequired()])
    mean = StringField('Mean Value', validators=[DataRequired()])
    min = StringField('Minimum Value', validators=[DataRequired()])
    max = StringField('Maximum Value', validators=[DataRequired()])
    stdev = StringField('Standard Deviation', validators=[DataRequired()])
    records = StringField('Records', validators=[DataRequired()])
    submit = SubmitField('Save')