# /myproject/owners/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField("Owner's name:")
    puppy_id = IntegerField("ID number of puppy:")
    submit = SubmitField("Adopt")