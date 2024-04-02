#!/usr/bin/python3
"""
Package for v1 of API
"""

# Import Blueprint from Flask
from flask import Blueprint

# This creates Blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views to register the routes
from api.v1 import views



