from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import SubjectGroup, Organisation, Project


class SiteForm(FlaskForm):
    project_id = QuerySelectField('Project', query_factory=lambda: Project.query.all(), get_label="name", allow_blank=True)
    name = StringField('Name of the Site', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    location_polygon = StringField('Location Polygon')
    centroid_latitude = StringField('Centroid Latitude')
    centroid_longitude = StringField('Centroid Longitude')
    sample_period = StringField('Sample Period', validators=[DataRequired()])
    average_period = StringField('Average Period', validators=[DataRequired()])
    submit = SubmitField('Save')