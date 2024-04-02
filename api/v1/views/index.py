#!/usr/bin/python3
"""
Module for index view
"""

# Import app_views Blueprint
from api.v1 import app_views

# Import Flask jsonify
from flask import jsonify

# This creates route for status endpoint
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Return status: OK
    """
    return jsonify({"status": "OK"})

