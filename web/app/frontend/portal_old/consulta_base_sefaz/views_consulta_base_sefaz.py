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

##Classes construcao views
from app.baseviews import BaseView, expose
from app.views import SimpleFormView, UtilView
from app.views import ModelSoftlogView


from app.models.gerais import ClientesBaseSefaz, CidadesSerpro

class EmpresasBrasil(ModelSoftlogView):
    datamodel = SQLAInterface(ClientesBaseSefaz)    

    label_columns = {'razao_social':'Nome Cliente','inicio_atividade':'Início'}

    show_columns = ['cnpj','razao_social','endereco','numero', 'bairro','nome_cidade','cep','telefones','email','inicio_atividade']

    show_fieldsets = [
        (
            'Dados Gerais',
            {'fields': ['cnpj', 'razao_social','inicio_atividade']}
        ),
        (
            'Endereço',
            {'fields': ['endereco','numero','bairro','nome_cidade','cep','telefones','email']}
        )
    ]

    list_columns = ['cnpj','razao_social','situacao','endereco','numero',
                    'bairro','nome_cidade','cep','telefones','email','cnae','inicio_atividade']

    add_columns = edit_columns = show_columns

    edit_widget = 'frontend/general/model/form_cliente.html'

    qualquer_coisa = 'Testando'

  
appbuilder.add_view(EmpresasBrasil, "Empresas", icon="fa-group", label='Empresas', category="Geral", category_icon="fa-cogs")