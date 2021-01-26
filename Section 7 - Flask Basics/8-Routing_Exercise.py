# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route('/')  # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "Please go to /puppy_latin/<name> to get your puppy latin name."


@app.route('/puppy_latin/<name>')  # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] == "y":
        name = name[:-1] + "iful"
    else:
        name += "y"
    return "Your puppy latin name is <strong>{}</strong>".format(name)


if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
