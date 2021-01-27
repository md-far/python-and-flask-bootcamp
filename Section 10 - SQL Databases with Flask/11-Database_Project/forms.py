from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddPuppy(FlaskForm):

    name = StringField("Name of puppy:")
    submit = SubmitField("Add Puppy")

class DelPuppy(FlaskForm):

    id = IntegerField("ID number of puppy to delete:")
    submit = SubmitField("Delete Puppy")

class AddOwner(FlaskForm):

    name = StringField("Owner's name:")
    puppy_id = IntegerField("ID number of puppy:")
    submit = SubmitField("Adopt")
