# myprojects/puppies/views.py
from flask import Blueprint, redirect, render_template, url_for
from myproject import db                              # from myproject/__init__.py
from myproject.models import Puppy                    # from myproject.models.py
from myproject.models import Owner                    # from myproject/models.py
from myproject.puppies.forms import AddForm, DelForm  # from myproject/puppies/forms.py

puppies_blueprints = Blueprint("puppies", __name__, template_folder="templates/puppies")

@puppies_blueprints.route("/add", methods=["GET", "POST"])  # "/<blueprints_name>/add"
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("puppies.list"))

    return render_template("add.html", form=form)

@puppies_blueprints.route("/delete", methods=["GET", "POST"])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup_del = Puppy.query.get(id)

        if pup_del.owner:
            owner_del = Owner.query.get(pup_del.owner.id)
            db.session.delete(owner_del)

        db.session.delete(pup_del)
        db.session.commit()

        return redirect(url_for("puppies.list"))

    return render_template("delete.html", form=form)

@puppies_blueprints.route("/list")
def list():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)