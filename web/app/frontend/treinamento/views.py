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

from app.frontend.treinamento.forms import FormSearchBancos 
#from app.models.com_produtos import ComProdutos
#from app.frontend.treinamento.forms import FormSearchProdutos
from app.models.consulta_notas import ConsultaNotas

@app.route('/teste_tabs/')
def teste_tabs():
    return render_template('frontend/treinamento/tabs.html')


@app.route('/consulta_notas/', methods=['GET', 'POST'])
def consulta_notas():
    # instancia classe
    model_notas = ConsultaNotas()
    # chama método para trazer a lista de notas
    lista_notas = model_notas.get_nf()

    #Renderiza o template passando os objetos de dados e de form
    return render_template('frontend/treinamento/lista_notas_grid.html', \
                            notas=lista_notas)
