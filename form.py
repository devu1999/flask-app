from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterForm(FlaskForm):
    website = StringField('Enter The Website To Check Permissions', validators=[DataRequired()])
    submit = SubmitField('Check')