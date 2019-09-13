from wtforms import StringField, BooleanField, PasswordField
from wtforms.form import Form
from flask_wtf.recaptcha import RecaptchaField
from wtforms.validators import DataRequired, EqualTo, Email
from app.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
from app.forms import DynamicForm

