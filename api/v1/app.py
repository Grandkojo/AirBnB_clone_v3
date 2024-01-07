#!/usr/bin/python3
"""A script to register a flask blueprint"""

from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error=None):
    """Calls the close function"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Returns a JSON error page"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)