#!/usr/bin/python3
"""Returns the states"""

from flask import Flask, jsonify, Blueprint, make_response, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', strict_slashes=False)
def get_states():
    """Returns a list of all States"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', strict_slashes=False)
def get_state(state_id):
    """Returns a state by id"""
    state = storage.get(State, state_id)
    if state is None:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Delets a state by idd"""
    state = storage.get(State, state_id)
    if state_id is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a new state"""
    data = request.get_json()
    if data is None:
        abort(404, "Not a JSON")
    if 'name' not in data:
        abort(400, "Missing name")
    new_state = State(**data)
    new_state.save()
    return make_response(jsonify(new_state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a state by id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(404, "Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)
