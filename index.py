"""
This is a simple website using the current directory as a server.
The frontend is pretty simple;
Enter some text and hit sumbit for an ASCII art representation.
If you typed an unsupported character, it'll alert you.

I chose Flask over Django because of substantially less boilerplate code,
which is better for something being graded by a human

Changes from midterm:
    Use Flask instead of http.server
    Revamp the site UI a bit

To run:
    1) `python KrushilNaikFinalProject.py` from 'ascii_flask' directory
    2) Visit http://localhost:3000 from any browser
"""

import sys
import json
from models.Letter import Letter
from util.custom_logging import critical, debug

try:
    from flask import Flask, render_template, request, redirect, url_for, session
except ImportError:
    critical("Failed to import Flask. Did you install it with pip?")
    sys.exit(1)

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_KEY"


@app.route("/")
def index():
    """
    The frontend
    """

    art = json.loads(session.setdefault("art", "[]"))

    return render_template("index.html", art=art)


@app.route("/ascii", methods=["POST"])
def art():
    """
    The frontend calls this API endpoint
    to get the inputted text's ASCII art
    """

    text = request.form["text"]
    letters = []

    for letter in text:
        try:
            char = Letter.get(Letter.letter == letter)
            debug(f"Successfully retrieved ASCII art for '{letter}'")
        except:
            # If the character we're working on wasn't found in the database
            # Short circuit and alert the user
            ERROR_MESSAGE = f"Unsupported character '{letter}'"

            debug(ERROR_MESSAGE)

            session["art"] = json.dumps([ERROR_MESSAGE])
            return redirect(url_for("index"))

        letters.append(char.representation.split("|"))

    art = ["".join(line) for line in zip(*letters)]
    session["art"] = json.dumps(art)

    return redirect(url_for("index"))
