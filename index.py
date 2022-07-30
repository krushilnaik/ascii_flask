import json
from models.Letter import Letter
from util.custom_logging import debug

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
