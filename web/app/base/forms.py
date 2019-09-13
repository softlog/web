from wtforms import StringField, BooleanField, PasswordField
from flask_wtf.recaptcha import RecaptchaField
from ..idioma import lazy_gettext
from wtforms.validators import DataRequired, EqualTo, Email
from app.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
from app.forms import DynamicForm


class FormSearchCidades(DynamicForm):
    nome_cidade = StringField("nome_cidade", validators=[DataRequired()])    
    

class MyForm(DynamicForm):
    field1 = StringField(('Field1'),
        description=('Your field number one!'),
        validators = [DataRequired()], widget=BS3TextFieldWidget())
    field2 = StringField(('Field2'),
        description=('Your field number two!'), widget=BS3TextFieldWidget())


