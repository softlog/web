from flask.views import View
from app import app, login
from flask_login import current_user
from functools import wraps
from flask import render_template


def user_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if not current_user.is_authenticated:
            return login.unauthorized()
            # or, if you're not using Flask-Login
            # return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorator

class BaseView(View):

    

    def __init__(self):
        self.title = None
        self.template = None

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

    def get_template_name(self):
        return self.template

    def get_objects(self):
        return None
    
    

    