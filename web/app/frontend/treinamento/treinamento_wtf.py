#Classes utilitarias do Flask
from flask import g, request, render_template, session, flash, redirect, \
    url_for, jsonify, request, abort, Response, session

#Classes utilitárias do Framework
from app import app
from app import appbuilder


#Classes para manipular Modelo de Dados
from app import db
from app.sqla.interface import SQLAInterface
from app.sqla.models.filters import BaseFilterConverter
from app.sqla.models.filters import Filters
from app.sqla.filters import *
from app import query_db_2, execute_db
import json

from wtforms.form import Form
from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, PasswordField, HiddenField
from wtforms import validators

class TreinamentoForm(FlaskForm):
     tipo_usuario  = HiddenField(default="teste")
     first_name     = StringField(u'Primeiro Nome', [validators.required(message="O Primeiro Nome é Obrigatório"), validators.length(max=30)])
     last_name      = StringField(u'Último Nome', [validators.required(), validators.length(max=10)])
     email          = StringField(u'Email', [validators.required(),validators.Email()])
     password       = PasswordField(u'Senha', [validators.required(),
                                               validators.length(min=6,max=6, message="A senha deve ter 6 caracteres."),
                                               validators.EqualTo('confirm', message='Confirmação de Senha não confere.')])
     confirm  = PasswordField('Repita a Senha')

@app.route('/treinamento_wtf', methods=['GET', 'POST'])
def treinamento_wtf():
    
    form = TreinamentoForm()
    
    if request.method == 'POST':

        
        
        if form.validate():
            dados = {}
            dados['first_name'] = form.first_name.data
            dados['last_name'] = form.last_name.data
            dados['email'] = form.email.data
            dados['password'] = form.password.data
            dados['confirm'] = form.confirm.data
            dados['tipo_usuario'] = form.tipo_usuario.data
         
            return jsonify({'resultado':dados})

           
    return render_template("/frontend/treinamento/treinamento_wtf.html", form=form)
