from wtforms import StringField, BooleanField, PasswordField
from flask_wtf.recaptcha import RecaptchaField
from ..idioma import lazy_gettext
from wtforms.validators import DataRequired, EqualTo, Email
from app.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
from app.forms import DynamicForm


class FormSearchCidades(DynamicForm):
    nome_cidade = StringField("nome_cidade", validators=[DataRequired()])    
    
