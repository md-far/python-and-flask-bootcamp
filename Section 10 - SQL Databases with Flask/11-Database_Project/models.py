import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#########################
#### Database Models ####
#########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):

    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship("Owner", uselist=False, backref="puppy")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy #{self.id}: '{self.name}', with owner '{self.owner.name}'"
        else:
            return f"Puppy #{self.id}: '{self.name}', no owner yet"

class Owner(db.Model):

    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey("puppies.id"))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
