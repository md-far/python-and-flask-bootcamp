# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template("index.html")


# This page will be the page after the form
@app.route('/report')
def report():
    conditions = [["contain uppercase letter", False],
                 ["contain lowercase letter", False],
                 ["end with a number", False]]

    # Check the user name for the 3 requirements.
    username = request.args.get("username")

    # any(letter.islower() for letter in username)
    # Check for uppercase
    conditions[0][1] = any(letter.isupper() for letter in username)

    # Check for lowercase
    conditions[1][1] = any(letter.islower() for letter in username)

    # Check if it ends with number
    conditions[2][1] = username[-1].isdecimal()

    check_number = sum(condition[1] for condition in conditions)

    unmet = [condition[0] for condition in conditions if not condition[1]]

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    return render_template("report.html", check_number=check_number, unmet=unmet)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
