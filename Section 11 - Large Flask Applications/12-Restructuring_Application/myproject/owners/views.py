# myproject/owners/views.py
from flask import Blueprint, redirect, render_template, url_for
from myproject import db                    # from myproject/__init__.py
from myproject.models import Owner          # from myproject/models.py
from myproject.owners.forms import AddForm  # from myproject/owners/forms.py

owners_blueprints = Blueprint("owners", __name__, template_folder="templates/owners")

@owners_blueprints.route("/add", methods=["GET", "POST"])  # "/<blueprints_name>/add"
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("puppies.list"))  # <blueprints_name>.<view_function>

    return render_template("add_owner.html", form=form)