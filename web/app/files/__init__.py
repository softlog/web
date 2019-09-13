# -*- coding: latin-1 -*-
#!/usr/bin/env python
from flask import Blueprint, request, jsonify, make_response, current_app

static = Blueprint('static',__name__,static_folder='static')

