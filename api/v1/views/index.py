#!/usr/bin/python3
"""Returns the status"""
from flask import Flask, jsonify, Blueprinm
from api.v1.views import app_views


status = [
        {
            'status': u'OK'
        }
]
@app_views.route('/status')
def get_status():
    """Returns the status"""
    return jsonify(status)
