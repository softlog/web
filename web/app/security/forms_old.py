from wtforms import StringField, BooleanField, PasswordField, DateField
from flask_wtf.recaptcha import RecaptchaField
from ..idioma import lazy_gettext
from wtforms.validators import DataRequired, EqualTo, Email
from app.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
from app.forms import DynamicForm


class LoginForm_db(DynamicForm):
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    

class LoginForm(DynamicForm):
    ambiente = StringField("Ambiente", validators=[DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    empresa = StringField("Empresa")
    filial = StringField("Filial")


class FormConsultaEntrega(DynamicForm):
    consulta_cte = StringField("Consulta CTe", validators=[DataRequired()])
    consulta_nfe = StringField("Consulta NFe", validators=[DataRequired()])
    consulta_nota = StringField("Consulta Nota", validators=[DataRequired()])
    consulta_destinatario = StringField("Consulta Destinatario", validators=[DataRequired()])
    data1 = StringField("Data Inicio")
    data2 = StringField("Data Fim")
