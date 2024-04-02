#!/usr/bin/python3
"""
Module for index view
"""

# Import app_views Blueprint
from api.v1 import app_views

# Import Flask jsonify
from flask import jsonify

# Import storage
from models import storage

# Create route for status endpoint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Return status: OK
    """
    return jsonify({"status": "OK"})

# Create route for stats endpoint
@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Return the number of objects by type
    """
    stats_dict = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]

    for cls_name in classes:
        cls_count = storage.count(cls_name)
        stats_dict[cls_name] = cls_count

    return jsonify(stats_dict)

