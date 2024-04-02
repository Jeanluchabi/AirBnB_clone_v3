#!/usr/bin/python3
'''Contains the states views for the API.'''
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage, State

ALLOWED_METHODS = ['GET', 'DELETE', 'POST', 'PUT']

@app_views.route('/states', methods=ALLOWED_METHODS)
@app_views.route('/states/<state_id>', methods=ALLOWED_METHODS)
def handle_states(state_id=None):
    if request.method == 'GET':
        return get_states(state_id)
    elif request.method == 'DELETE':
        return remove_state(state_id)
    elif request.method == 'POST':
        return add_state()
    elif request.method == 'PUT':
        return update_state(state_id)
    else:
        abort(405, 'Method Not Allowed')

def get_states(state_id=None):
    if state_id:
        state = storage.get(State, state_id)
        if state:
            return jsonify(state.to_dict())
        else:
            abort(404)
    else:
        states = storage.all(State).values()
        return jsonify([state.to_dict() for state in states])

def remove_state(state_id=None):
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

def add_state():
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

def update_state(state_id=None):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200

