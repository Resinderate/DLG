from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/total/", methods=["POST"])
def total():
    result = {"total": 0}
    return jsonify(result)
