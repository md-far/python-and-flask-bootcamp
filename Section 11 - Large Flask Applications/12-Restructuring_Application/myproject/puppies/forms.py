# myproject/puppies/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):

    name = StringField("Name of puppy:")
    submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):

    id = IntegerField("ID number of puppy to delete:")
    submit = SubmitField("Delete Puppy")