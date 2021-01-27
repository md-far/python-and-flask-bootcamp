from flask import redirect, render_template, url_for
from models import app, db, Puppy, Owner
from forms import AddPuppy, DelPuppy, AddOwner

app.config["SECRET_KEY"] = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_puppy", methods=["GET", "POST"])
def add_pup():
    form = AddPuppy()

    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("list_pups"))

    return render_template("add_pup.html", form=form)

@app.route("/delete_puppy", methods=["GET", "POST"])
def del_pup():
    form = DelPuppy()

    if form.validate_on_submit():
        id = form.id.data
        pup_del = Puppy.query.get(id)

        if pup_del.owner:
            owner_del = Owner.query.get(pup_del.owner.id)
            db.session.delete(owner_del)

        db.session.delete(pup_del)
        db.session.commit()

        return redirect(url_for("list_pups"))

    return render_template("del_pup.html", form=form)

@app.route("/list_puppies")
def list_pups():
    puppies = Puppy.query.all()
    return render_template("list_pups.html", puppies=puppies)

@app.route("/add_owner", methods=["GET", "POST"])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for("list_pups"))

    return render_template("add_owner.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)