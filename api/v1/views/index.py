#!/usr/bin/python3
"""Returns the status"""
from flask import Flask, jsonify, Blueprint
from api.v1.views import app_views


status = {
    'status': 'OK'
}


@app_views.route('/status')
def get_status():
    """Returns the status"""
    return jsonify(status)
