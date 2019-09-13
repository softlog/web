from flask import render_template, session, escape, g, redirect, _app_ctx_stack, request, flash, make_response
from flask_login import login_required, current_user
from flask_restful import Api, Resource, reqparse, marshal, abort
from app import app
from app import db
from app import query_db, execute_db


from pysignfe.nf_e import nf_e

@app.route('/nfe4/danfe/get_pdf') 
def nfe4_get_pdf_danfe():    
    parser = reqparse.RequestParser()
    parser.add_argument('id_db',type=int,help='Parametro Id_db invalido.')
    parser.add_argument('chave_nfe',type=str,help='Parametro chave_nfe invalido.')
    
    args = parser.parse_args()
        
    id_db = args['id_db']
    chave_nfe = args['chave_nfe']

    if chave_nfe is None or id_db is None:
        return "Sem parametros para consulta.",404

    response = get_response_danfe_nfe4(id_db,chave_nfe)



    if response is None:
        return "NFe chave %s com XML invalido" % chave_nfe, 404

    response.headers['Content-Disposition'] = "attachment; filename=%s.pdf" % chave_nfe
    response.mimetype = 'application/pdf'    
    return response    
    


def get_response_danfe_nfe4(id_db, chave_nfe):

    str_sql = "SELECT cstat, chave_eletronica, xml_proc_nfe FROM com_nf WHERE chave_eletronica = '%s'" % chave_nfe 


    registro = query_db(id_db,str_sql,None,True)
    
    if registro['xml_proc_nfe'] is None:
        return None
    try:
        nova_nfe = nf_e()
        danfe = nova_nfe.gerar_danfe(registro['xml_proc_nfe'], nome_sistema=u'Softlog Tecnologia', leiaute_logo_vertical=False, versao='3.10') #logo = 'logo.bmp')
    except:
        return None

    return make_response(danfe)