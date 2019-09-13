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

@app.route('/cadastros/cliente/list/', methods=['GET', 'POST'])
def cliente_list():
    return "lista de clientes"

@app.route('/cadastros/cliente/add/<int:id>', methods=['GET', 'POST'])
def cliente_add(id):
    return render_template("frontend/cadastros/cliente_add.html")

@app.route('/cadastros/cliente/edit/<int:id>', methods=['GET', 'POST'])
def cliente_edit(id):
    return "edição de clientes"

@app.route('/cadastros/cliente/delete/<int:id>', methods=['GET', 'POST'])
def cliente_delete(id):
    return "exclusão de clientes"

@app.route('/cadastros/cliente/show/<int:id>', methods=['GET', 'POST'])
def cliente_show(id):
    return "visualizacao de clientes"

