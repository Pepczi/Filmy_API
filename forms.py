from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,  BooleanField, IntegerField
from wtforms.validators import DataRequired
from models import collection

class MovieForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    year = StringField('year')
    description = TextAreaField('description')
    done = BooleanField('done')