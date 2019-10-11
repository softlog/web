from .model import Filter
from app.security.forms import FormConsultaEntrega
from flask import render_template, request, session, redirect, url_for, abort
from app import app
from sqlalchemy import create_engine
from app import get_uri_db
 
@app.route('/portal/webtracking/off/<ambiente>', methods=['GET', 'POST'])
def index_portal_consulta_off(ambiente):

    try:
        engine = create_engine(get_uri_db(ambiente))
        conn = engine.connect()
    except :
       return render_template('portal/consulta_off/error_consulta_off.html', banco = ambiente), 404

    f = Filter()
    form = FormConsultaEntrega()
    dados = [] 
    dictDados = []
    pesquisa = request.form.get('modo_pesquisa')
    consulta_nota = request.form.get('consulta_nota')
    consulta_destinatario = request.form.get('consulta_destinatario')
    consulta_destinatario_cpf_cpnj = request.form.get('consulta_destinatario_cpf_cnpj')


    if consulta_nota or consulta_destinatario or consulta_destinatario_cpf_cpnj:
        render_tabela = True
    else:
        render_tabela = False
     
    if consulta_destinatario_cpf_cpnj and consulta_nota:
        dados = f.filter_by_cpf_cnpj_nnota(consulta_destinatario_cpf_cpnj, consulta_nota, ambiente) 
    elif consulta_nota:  
        dados = f.filter_by_numero_nota(consulta_nota, ambiente) 
    elif consulta_destinatario: 
        dados = f.filter_by_destinatario(consulta_destinatario.upper(), ambiente) 
    elif consulta_destinatario_cpf_cpnj:
        dados = f.filter_by_destinatario_cpf_cnpj(consulta_destinatario_cpf_cpnj, ambiente) 
    

    if dados:

        #transforma dados em um dicionario 
        for row in dados: 
            dictDados.append(dict(row)) 
             
        for dado in dictDados:
            data = dado["data_emissao"] 
            if data:
                dado["data_emissao"] = data.strftime("%d/%m/%Y")

          
    return render_template('portal/consulta_off/consulta_off.html', dados = dictDados, 
                                                               form = form,
                                                               render_tabela = render_tabela,
                                                               pesquisa = pesquisa)

