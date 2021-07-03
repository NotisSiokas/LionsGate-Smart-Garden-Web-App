from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Site


class NodeForm(FlaskForm):
    site_id=QuerySelectField(query_factory=lambda: Site.query.all(), get_label="name", allow_blank=True)
    name = StringField('Name', validators=[DataRequired()])
    latitude = StringField('Latitude',)
    longitude = StringField('Longitude',)
    description = StringField('Description',)
    sample_period = StringField('Sample Period', validators=[DataRequired()])
    average_period = StringField('Average Period',validators=[DataRequired()])
    submit = SubmitField('Save')