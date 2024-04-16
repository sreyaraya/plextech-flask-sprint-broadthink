from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def index():
    return "ello"


@app.route("/login")
def login():
    return "ello"


app.run(host="0.0.0.0", port=81)
