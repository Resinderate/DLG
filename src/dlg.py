from flask import Flask, jsonify, request

app = Flask(__name__)


def invalid_request(reason, status_code=400):
    resp = jsonify({"message": reason})
    resp.status_code = status_code
    return resp


@app.route("/total/", methods=["POST"])
def total():
    if not request.is_json:
        return invalid_request("Was expecting a mimetype of application/json")

    numbers_to_sum = request.get_json()

    if not isinstance(numbers_to_sum, list):
        return invalid_request(
            f"Was expecting a list. Given: {type(numbers_to_sum).__name__}"
        )

    try:
        total = sum(numbers_to_sum)
    except TypeError:
        return invalid_request(
            "Provided list of numbers contains a non-numeric element."
        )

    return jsonify({"total": total})
