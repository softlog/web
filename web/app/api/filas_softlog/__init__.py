from app import app
from flask import request, render_template, session, flash, redirect, \
    url_for, jsonify, request

@app.route('/integracao_softlog/<acesso>/<int:id_db>/<cnpj>/<data>', methods=['GET','POST'])
def integracao_softlog(acesso,id_db,cnpj,data):
    if request.method == 'GET':
        
        try:
            docs = Documentos.get_docs_disponiveis(id_db,cnpj,data,acesso)
        except Exception as e:
            docs = ''
        
        return render_template('integracao_parceiros/docs_disponiveis.html', docs=docs)

