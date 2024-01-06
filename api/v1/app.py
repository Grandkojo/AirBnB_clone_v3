#!/usr/bin/python3
"""A script to register a flask blueprint"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error=None):
    """Calls the close function"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, threaded=True)
