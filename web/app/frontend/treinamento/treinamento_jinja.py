#Classes utilitarias do Flask
from flask import g, request, render_template, session, flash, redirect, \
    url_for, jsonify, request, abort, Response, session

#Extensao que faz controle do usuario
from flask_login import login_required, current_user
from flask_login import current_user

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

# Classes Views Banco
from app.models.bancos import Banco
from app.frontend.treinamento.forms import FormSearchBancos 


@app.route('/treinamento_jinja', methods=['GET', 'POST'])
def treinamento_jinja():

    menu = ["Teste 1", "Teste 2"]
    return render_template("frontend/treinamento/treinamento_jinja.html", menu=menu)