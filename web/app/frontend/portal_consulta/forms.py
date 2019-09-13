from wtforms import StringField, BooleanField, PasswordField
from flask_wtf.recaptcha import RecaptchaField
from wtforms.validators import DataRequired, EqualTo, Email
from app.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
from app.forms import DynamicForm


class FormConsultaEntrega(DynamicForm):
    consulta_cte = StringField("Consulta CTe", validators=[DataRequired()])
    consulta_nfe = StringField("Consulta NFe", validators=[DataRequired()])
