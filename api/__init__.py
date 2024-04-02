#!/usr/bin/python3
"""
Package for API
"""

import os
from flask import Flask
from models import storage
from api.v1 import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close storage
    """
    storage.close()

if __name__ == "__main__":
    # Get host and port from environment variables or use defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)


