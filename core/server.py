from flask import Flask, jsonify

from core.database import Base, engine
from core.feeds import fetch_feeds

app = Flask(__name__)


@app.route("/")
def index():
    # Create all tables defined by the models
    Base.metadata.create_all(engine)

    try:
        fetch_feeds()
        return jsonify({"message": "Success", "status": True})
    except Exception:
        return jsonify({"message": "Fail", "status": False})
