#!/usr/bin/python3
"""A script to create a flask blueprint"""

from flask import Flask, Blueprint, render_template, abort

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
