#!/usr/bin/python3
"""Returns the status"""
from flask import Flask, jsonify, Blueprint
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Returns the status"""
    return jsonify({'status': "OK"})


objects = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
}


@app_views.route('/stats', strict_slashes=False)
def retrieve_number():
    """Returns the number of each object"""
    return jsonify(objects)
