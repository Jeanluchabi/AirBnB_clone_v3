#!/usr/bin/python3
"""
Package for API
"""

# This import Flask
from flask import Flask

# This create Flask app instance
app = Flask(__name__)

# Import storage from models
from models import storage

# Import blueprint for v1
from api.v1 import app_views

# Register blueprint
app.register_blueprint(app_views)

# Teardown app context
@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close storage
    """
    storage.close()

# Run Flask app
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

