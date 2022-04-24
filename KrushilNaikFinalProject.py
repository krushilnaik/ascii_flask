from flask import Flask, render_template, request, redirect, url_for
from models.Letter import Letter

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ascii", methods=["POST"])
def art():
    text = request.form["text"]
    test = Letter.get(Letter.letter == text[0])

    print(*test.representation.split("|"), sep="\n")

    return redirect(url_for('index'))
