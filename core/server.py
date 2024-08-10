from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    # TODO: make request to CTI feeds APIs
    return jsonify({"message": "Fetching...", "status": True})
