#!/usr/bin/python3
"""Documentation for module"""
from api.v1.views import api_views


@app_views.route("/status")
def status():
    """get api status"""
    return {"status": "OK"}
