from app import app
from flask import request, render_template, session, flash, redirect, \
    url_for, jsonify, request

from flask_mail import Message, Mail
from app import celery
from .tasks import importa_docs_task
from app.api.integracao_parceiros.documentos import Documentos


@app.route('/integracao_softlog/<acesso>/<int:id_db>/<cnpj>/<data>', methods=['GET','POST'])
def integracao_softlog(acesso,id_db,cnpj,data):
    if request.method == 'GET':
        try:
            docs = Documentos.get_docs_disponiveis(id_db,cnpj,data,acesso)
        except Exception as e:
            docs = ''

        return render_template('integracao_parceiros/docs_disponiveis.html', docs=docs)


#Chamada da rotina longtask
@app.route('/integracao_softlog/importa_docs', methods=['POST'])
def importa_docs():
    id_bd = request.form['id_bd']
    lst_notas = request.form['lst_notas']
    lst_clientes = request.form['lst_clientes']
    id_db_main = request.form['id_db_main']
    acesso = request.form['acesso']
    tp_romaneio = request.form['tp_romaneio']

    try:
        task = importa_docs_task.apply_async((id_bd,lst_notas,lst_clientes,id_db_main,acesso,tp_romaneio))
        print("TASK ID: ", task)
    except Exception as e:
        return jsonify({}), 202, {'Location': None}

    return jsonify({}), 202, {'Location': url_for('integracao_status',
                                                  task_id=task.id)}

@app.route('/integracao_softlog/status/<task_id>')
def integracao_status(task_id):
    task = importa_docs_task.AsyncResult(task_id)
    print("TASK ID: ", task)
    if task.state == 'PENDENTE':
        ## job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FALHOU':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)

@app.route('/integracao_softlog/testes', methods=['GET','POST'])
def testes():
    if request.method == 'GET':
        docs = {}
        return render_template('integracao_parceiros/teste2.html', docs=docs)


