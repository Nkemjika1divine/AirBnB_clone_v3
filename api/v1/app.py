#!/usr/bin/python3
"""Documentaton for module"""
from api.v1.views import app_views
from flask import Flask, jsonify
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """Handles the error message '404: not found'"""
    message = {
            "error": "Not found"
        }
    return jsonify(message)


@app.teardown_appcontext
def teardown(exception):
    """Call the storage.close() method if an exception is found"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    """runs the file"""
    host = os.getenv("HBNB_API_HOST")
    if host is None:
        host = "0.0.0.0"
    port = os.getenv("HBNB_API_PORT")
    if port is None:
        port = "5000"

    app.run(host=host, port=port, threaded=True)
