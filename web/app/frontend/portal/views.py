from app import app
from flask import g, request, render_template, session, flash, redirect, \
    url_for, jsonify, request, abort, Response, session



#from flask.ext.login import login_required, login_user, logout_user, current_user 
import json
from app import query_db, execute_db

from .model import Rastreamento
 
 
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