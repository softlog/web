#Classes utilitarias do Flask
from flask import g, request, render_template, session, flash, redirect, \
    url_for, jsonify, request, abort, Response, session

#Extensao que faz controle do usuario
from flask_login import login_required, current_user
from flask_login import current_user

#Classes do Framework
from app import app
from app import appbuilder
from app import widgets
from app.baseviews import BaseView, expose
from app.views import SimpleFormView
from app.idioma import lazy_gettext as _

#Classes de modelos de dados
from app.models.gerais import Filial, Cidades
from app.security.sqla.models import User

#Classes para manipular Modelo de Dados
from app import db
from app.sqla.interface import SQLAInterface
from app.sqla.models.filters import BaseFilterConverter
from app.sqla.models.filters import Filters
from app.sqla.filters import *
from app import query_db, execute_db


import json

#Classes especificas para de cada rota
from app.base.forms import FormSearchCidades

from .model import Rastreamento
 

class MyView(BaseView):
    route_base = "/myview"

    @expose('/method1/<string:param1>')
    def method1(self, param1):
        # do something with param1
        # and return it
        return param1

    @expose('/method2/<string:param1>')
    def method2(self, param1):
        # do something with param1
        # and render it
        param1 = 'Hello %s' % (param1)
        return param1


 
@app.route('/portal/rastreamento/consulta/<codigo_rastreamento>', methods=['GET'])
def index_portal(codigo_rastreamento):

    rastreamento = Rastreamento() 

    tipo_busca = int(codigo_rastreamento[0:2])
    id_db = int(codigo_rastreamento[2:7])
    if tipo_busca == 1: ## Id Nota Fiscal
        """Codigo Rastreamento composto por 19 digitos
           1-2: tipo pesquisa
           3-7: codigo do banco de dados
           8-19: codigo interno da NFe
        """
        id_doc = int(codigo_rastreamento[7:])
        dados = rastreamento.get_01(id_db,id_doc)
    if tipo_busca == 2: ## Chave NFe
        chave_doc = codigo_rastreamento[7:]
        dados = rastreamento.get_02(id_db,chave_doc)        
        try:
            if dados['situacoes'] is None:
                dados['situacoes'] = []
        except:
            pass
        
    return render_template('portal/rastreamento/consulta.html',dados=dados)


@app.route('/lista_cidades/', methods=['GET', 'POST'])
def lista_cidades():

    #Objeto instanciado da classe SQLAInterface para modelo de dados
    model_cidades = SQLAInterface(Cidades,db.session())    

    #Objeto instanciado da classe Filters, que automatiza a criação de filtros
    filters = Filters(BaseFilterConverter,model_cidades)

    #Objeto de fomrulário
    form = FormSearchCidades()

    #O endpoint pode ser acionado via GET e POST
    
    if request.method == 'POST':
        #Quando o usuário clicar no botão pesquisar, o metodo POST é acionado. 
        #Neste momento é possível fazer a leitura dos inputs do objeto form.
        qry_cidade = form.nome_cidade.data

    #Se o botão pesquisar foi clicado, validate_on_submit() retorna True.
    if form.validate_on_submit():
        
        #Criação do filtro SQL
        filters.add_filter('nome_cidade',FilterStartsWith, \
                                                    qry_cidade)
        #Executa a query no banco de dados
        qt, cidades = model_cidades.query(filters)

        #Renderiza o template passando os objetos de dados e de form
        return render_template('testes/lista_cidades.html', \
                              dados=cidades, form=form)

    if request.method == 'GET':
        return render_template('testes/lista_cidades.html', \
                                          dados=[], form=form)