#!/usr/bin/python3
"""Returns the places"""

from flask import Flask, jsonify, Blueprint, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from models.place import Place


@app_views.route('/cities/<city_id>/places', strict_slashes=False)
def get_places_by_city(city_id):
    """Returns a list of places of a city"""
    city = storage.get(City, city_id)
    if state is None:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', strict_slashes=False)
def get_place(place_id):
    """Returns a place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict()), 200


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Delets a place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """Creates a new place"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"}), 400
    if data.user_id is None:
        abort(404)
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new_place = Place(**data)
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(city_id):
    """Updates a place by id"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id' 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
