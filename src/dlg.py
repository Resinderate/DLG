from flask import Flask

app = Flask(__name__)


@app.route("/total/", methods=["POST"])
def total(self):
    return 0
