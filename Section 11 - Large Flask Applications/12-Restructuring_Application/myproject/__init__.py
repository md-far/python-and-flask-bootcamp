# __init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

from myproject.owners.views import owners_blueprints    # from myproject/owners/views.py
from myproject.puppies.views import puppies_blueprints  # from myproject/puppies/views.py

app.register_blueprint(owners_blueprints, url_prefix="/owners")
app.register_blueprint(puppies_blueprints, url_prefix="/puppies")