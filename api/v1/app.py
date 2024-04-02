#!/usr/bin/python3
"""
Module for v1 app configuration
"""

# Import Flask Blueprint
from flask import Flask

# Import Blueprint app_views from views
from api.v1.views import app_views

# Create Flask app instance
app = Flask(__name__)

# Register Blueprint app_views to Flask instance
app.register_blueprint(app_views)

# This declares a method to handle teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close storage
    """
    from models import storage
    storage.close()

if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)


