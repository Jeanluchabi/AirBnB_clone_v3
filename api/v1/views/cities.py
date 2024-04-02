#!/usr/bin/python3
'''Contains the cities views for the API.'''
from flask import jsonify, request
from werkzeug.exceptions import NotFound, MethodNotAllowed, BadRequest

from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State

ALLOWED_METHODS = ['GET', 'DELETE', 'POST', 'PUT']


@app_views.route('/states/<state_id>/cities', methods=ALLOWED_METHODS)
def get_cities(state_id):
    '''Retrieves the list of cities for a given state.'''
    state = storage.get(State, state_id)
    if state is None:
        raise NotFound("State not found")
    
    if request.method == 'GET':
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities)
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return BadRequest("Not a JSON")
        if 'name' not in data:
            return BadRequest("Missing name")
        city = City(**data)
        city.state_id = state_id
        city.save()
        return jsonify(city.to_dict()), 201
    else:
        raise MethodNotAllowed(ALLOWED_METHODS)


@app_views.route('/cities/<city_id>', methods=ALLOWED_METHODS)
def get_city(city_id):
    '''Retrieves a specific city.'''
    city = storage.get(City, city_id)
    if city is None:
        raise NotFound("City not found")

    if request.method == 'GET':
        return jsonify(city.to_dict())
    elif request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            return BadRequest("Not a JSON")
        for key, value in data.items():
            if key not in ['id', 'state_id', 'created_at', 'updated_at']:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        raise MethodNotAllowed(ALLOWED_METHODS)

