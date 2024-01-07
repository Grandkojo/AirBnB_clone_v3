#!/usr/bin/python3
"""Returns the status"""
from flask import Flask, jsonify, Blueprint
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Returns the status"""
    return jsonify({'status': "OK"})
