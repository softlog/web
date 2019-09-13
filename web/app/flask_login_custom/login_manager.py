# -*- coding: utf-8 -*-
'''
    flask_login.login_manager
    -------------------------
    The LoginManager class.
'''


import warnings
from datetime import datetime, timedelta

from flask import (_request_ctx_stack, abort, current_app, flash, redirect,
                   has_app_context, request, session)

from flask_login._compat import text_type
from flask_login.config import (COOKIE_NAME, COOKIE_DURATION, COOKIE_SECURE,
                     COOKIE_HTTPONLY, LOGIN_MESSAGE, LOGIN_MESSAGE_CATEGORY,
                     REFRESH_MESSAGE, REFRESH_MESSAGE_CATEGORY, ID_ATTRIBUTE,
                     AUTH_HEADER_NAME, SESSION_KEYS, USE_SESSION_FOR_NEXT)
from flask_login.mixins import AnonymousUserMixin
from flask_login.signals import (user_loaded_from_cookie, user_loaded_from_header,
                      user_loaded_from_request, user_unauthorized,
                      user_needs_refresh, user_accessed, session_protected)
from flask_login.utils import (login_url as make_login_url, _create_identifier,
                    _user_context_processor, encode_cookie, decode_cookie,
    make_next_param, expand_login_view)

from flask_login import LoginManager

class LoginManager(LoginManager):


    def reload_user(self, user=None, filial=None):        
        ctx = connection_stack.top
        
        getattr(ctx,'user',None)
        getattr(ctx,'filial',filial)
        if user is None:
            user_id = session.get('user_id')
            if user_id is None:                               
                setattr(ctx,'user',self.anonymous_user())
                setattr(ctx,'filial',self.anonymous_filial())
            else:
                uri = current_app.config.get('SQLALCHEMY_DATABASE_URI_' + (user_id).upper().split('@')[0])   
                if uri is None:
                    logout_user()
                    return 
                             
                setattr(ctx,'uri_request',uri)                
                auth = self.user_callback(user_id)
                user = auth[0]
                if auth[1] is not None:
                    filial = auth[1]
                if user is None:
                    logout_user()
                else:                    
                    setattr(ctx,'user',user)
                    setattr(ctx,'filial',filial)
        else:            
            setattr(ctx,'user',user)
            setattr(ctx,'filial',filial)
            user_id = session.get('user_id')
            uri = current_app.config.get('SQLALCHEMY_DATABASE_URI_' + (user_id).upper().split('@')[0])
            getattr(ctx,'uri_request',None)
            setattr(ctx,'uri_request',uri)    