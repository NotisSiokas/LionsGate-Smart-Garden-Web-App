from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import SubjectGroup, Organisation


class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    sample_period = StringField('Sample Period', validators=[DataRequired()])
    average_period = StringField('Average Period', validators=[DataRequired()])
    submit = SubmitField('Save')