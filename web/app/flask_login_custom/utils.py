# -*- coding: utf-8 -*-
'''
    flask_login.utils
    -----------------
    General utilities.
'''


import hmac
from hashlib import sha512
from functools import wraps
from werkzeug.local import LocalProxy
from werkzeug.security import safe_str_cmp
from werkzeug.urls import url_decode, url_encode

from flask import (_request_ctx_stack, current_app, request, session, url_for,
                   has_request_context)

from ._compat import text_type, urlparse, urlunparse
from .config import COOKIE_NAME, EXEMPT_METHODS
from .signals import user_logged_in, user_logged_out, user_login_confirmed


#: A proxy for the current user. If no user is logged in, this will be an
#: anonymous user
##current_user = LocalProxy(lambda: _get_user())

## Code Custom for Softlog
## Alem de usuario atual, armazena filial atual
current_user = LocalProxy(lambda: _get_user()[0])
current_filial = LocalProxy(lambda: _get_user()[1])




def _get_user():
    if has_request_context() and not hasattr(connection_stack.top, 'user'):
        current_app.login_manager._load_user()

    return [getattr(connection_stack.top, 'user', None),getattr(connection_stack.top, 'filial', None)]

