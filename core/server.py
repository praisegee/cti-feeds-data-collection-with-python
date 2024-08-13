import os

from flask import Flask, jsonify

from core.database import Base, engine
from core.feeds import fetch_feeds

app = Flask(__name__)


@app.route("/load")
def index():
    # Create all tables defined by the models
    Base.metadata.create_all(engine)
    try:
        fetch_feeds()
        return jsonify({"message": "Success", "status": True})
    except Exception as e:
        return jsonify({"message": "Fail", "status": False, "data": str(e)})


if __name__ == "__main__":
    host = os.getenv("SERVER_HOST", "localhost")
    port = os.getenv("SERVER_PORT", 8000)
    app.run(debug=True, port=port, host=host)
