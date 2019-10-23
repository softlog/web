from .model import Filter
from app.security.forms import FormConsultaEntrega
from flask import render_template, request, session, redirect, url_for
from app import app

@app.route('/portal/webtracking/', methods=['GET', 'POST'])
def index_portal_entregas():

    ambiente = session.get("ambiente")
    if ambiente is None:
        return redirect('/login/')
   

    f = Filter() 
    form = FormConsultaEntrega()
    dados = []
    dictDados = []
    pesquisa = request.form.get('modo_pesquisa')
    consulta_nota = request.form.get('consulta_nota')
    consulta_destinatario = request.form.get('consulta_destinatario')
    consulta_cte = request.form.get('consulta_cte')
    consulta_nfe = request.form.get('consulta_nfe')
    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    url_contato = f.get_url_contato()[0][0]

    if consulta_nfe or consulta_cte or consulta_nota or consulta_destinatario or data1 or data2:
        render_tabela = True
    else: 
        render_tabela = False
   
    if consulta_nota:
        dados = f.filter_by_numero_nota(consulta_nota) 
    elif consulta_destinatario: 
        dados = f.filter_by_destinatario(consulta_destinatario.upper()) 
    elif consulta_nfe:
        dados = f.filter_by_chave_nfe(consulta_nfe)
    elif consulta_cte:
        dados = f.filter_by_chave_cte(consulta_cte)
    elif data1 or data2:

        if data1 and data2:
            dados = f.filter_by_periodo(data1, data2)
        
        elif data1:
            dados = f.filter_by_periodo(data1 , data1)
       
        else:
            dados = f.filter_by_periodo(data2, data2)
    
    if dados:
        #transforma dados em um dicionario 
        for row in dados:
            dictDados.append(dict(row)) 
             
        for dado in dictDados:
            data = dado["data_emissao"] 
            dado["data_emissao"] = data.strftime("%d/%m/%Y")
          
    return render_template('portal/consulta_entregas/consulta_entrega.html', dados = dictDados, 
                                                           form = form,
                                                           render_tabela = render_tabela,
                                                           pesquisa = pesquisa,
                                                           url_contato = url_contato)

