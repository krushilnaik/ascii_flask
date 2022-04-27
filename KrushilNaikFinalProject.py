# Krushio Naik
# INF-360 Programming with Python
# Final Project

"""
This builds on my midterm project.
Changes:
    Use Flask instead of http.server
    Revamp the site UI a bit
"""


import json
import os
import sys
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
    art = json.loads(session.setdefault("art", "[]"))

    return render_template("index.html", art=art)


@app.route("/ascii", methods=["POST"])
def art():
    text = request.form["text"]

    letters = []

    for letter in text:
        try:
            char = Letter.get(Letter.letter == letter)
            debug(f"Successfully retrieved ASCII art for '{letter}'")
        except:
            ERROR_MESSAGE = f"Unsupported character '{letter}'"

            debug(ERROR_MESSAGE)

            session["art"] = json.dumps([ERROR_MESSAGE])
            return redirect(url_for('index'))

        letters.append(char.representation.split("|"))

    art = ["".join(line) for line in zip(*letters)]

    session["art"] = json.dumps(art)
    return redirect(url_for("index"))


if __name__ == "__main__":
    os.environ["FLASK_APP"] = "KrushilNaikFinalProject"
    os.system("flask run --port 3000")
