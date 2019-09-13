from flask import Flask, Request
from werkzeug.datastructures import ImmutableOrderedMultiDict


class CustomRequest(Request):
    """Request subclass to override request parameter storage"""
    parameter_storage_class = ImmutableOrderedMultiDict

class Flask(Flask):
    """Flask subclass using the custom request class"""
    request_class = CustomRequest
