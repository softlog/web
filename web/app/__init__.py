from app.flask_custom import Flask
from flask import Response, current_app, g, make_response, render_template, request, session
from flask import _app_ctx_stack, escape
from flask_login import current_user

import traceback
import psycopg2
import psycopg2.extensions
from psycopg2.extras import DictCursor
from app.sqla import Model, Base, SQLA
from app.flask_sqlalchemy_tny import SQLAlchemy
from app.baseapp import AppBuilder
from app.models.gerais import Filial  

from flask_httpauth import HTTPBasicAuth
from .idioma import lazy_gettext
from celery import Celery

import pkg_resources
#print('VERSAO ', pkg_resources.get_distribution('flask').version)u
#import sentry_sdk
#from sentry_sdk.integrations.flask import FlaskIntegration

#from flask.ext.login import current_user
#from .my_flask_jsondash.charts_builder import charts


import logging 
import traceback


"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

## Login Especifico para Acesso aos Dashboards
from flask_login import LoginManager
login = LoginManager()
login.login_view = "login_frontend"
#login_manager_dashboard = LoginManager()

##sentry_sdk.init(
##    dsn="https://e199899db7114f39a0d8e53f2876993f@sentry.io/1363140",
##    integrations=[FlaskIntegration()]
##)


app = Flask('app')
app.config.from_object('config')

auth = HTTPBasicAuth()
db = SQLA(app)
db2 = SQLA(app)
login.init_app(app)
appbuilder = AppBuilder(app,db2.session)
#appbuilder = AppBuilder(app,db.session)

#login_manager_dashboard.init_app(app)

 
      
#DSN_MAIN = 'dbname=softlog user=softlog port=5435 password=paulino host=localhost'
def create_app(uri):
    """
        Factory de App
    """
    app = Flask(app)
    app.config.from_object('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    db = SQLA(app)
    appbuilder = AppBuilder(app,db.session,static_folder="files/static")
       
    from frontend import views
    
    return app 

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
     
celery = make_celery(app)


@app.after_request
def after_request(response):
    #print("************** Encerrando Request", request.path)
    if (response.status == '403'):
        response.status = '403 FORBIDEN'
    if (response.status == '404'):
        response.status = '404 NOT FOUND'
    return response

@app.before_request
def before_request(): 
    
    
    g.user = current_user 

    from app import get_uri_db  
    
    #username = request.form.get('username')
    #password = request.form.get('password')    
    #print("USUARIO", username)
    #print("SENHA", password)

    
    ambiente = session.get("ambiente")
    ambiente_api = request.headers.get('X-Softlog-Resource')
    codigo_empresa = session.get("codigo_empresa")
    codigo_filial = session.get("codigo_filial")



    #print("****X-Softlog-Resource***",ambiente)
    #print(request.form.keys())
    #print("****AUTORIZACAO***", request.headers.get("Authorization"))
    if request.path[0:7] == '/files/':        
        g.user = current_user
    elif request.path.find('/login/') > -1 and request.method == 'POST':            
        if app.debug:
            pass
            #print("****ACESSANDO***",request.path, "com ", escape(current_user), "sessao")
        id_db_tny = request.form['ambiente']        
        uri = None
        if id_db_tny is not None:
            uri =  get_uri_db(id_db_tny)
        
        getattr(_app_ctx_stack.top,'uri_login',None)
        setattr(_app_ctx_stack.top,'uri_login',uri)
        g.user = current_user 
        #print(ab)

    elif ambiente is not None:        
        from app import get_uri_db   
           
        id_db_tny = ambiente.lower()

        uri = None
        if id_db_tny is not None:
            uri =  get_uri_db(id_db_tny)
                
        getattr(_app_ctx_stack.top,'uri_request',None)
        setattr(_app_ctx_stack.top,'uri_request',uri)          
        g.user = current_user 
        if app.debug:
            pass
            #print("****ACESSANDO***", request.path, "com ", escape(g.user), "sessao")

        if codigo_filial is not None and codigo_empresa is not None:                      
           
            try:                
                filial = g.current_filial
            except:  
                filial = db.session.query(Filial)\
                        .filter(Filial.codigo_empresa == codigo_empresa,\
                        Filial.codigo_filial==codigo_filial).first()
                g.current_filial = filial                          
                   
    elif ambiente_api is not None:                
        if app.debug:
            pass
            #print("****ACESSANDO***",request.path, "com ", escape(current_user), "sessao")

        from app import get_uri_db   
           
        id_db_tny = ambiente_api.lower()

        uri = None
        if id_db_tny is not None:
            uri =  get_uri_db(id_db_tny)
                
        getattr(_app_ctx_stack.top,'uri_api_softlog',None)
        setattr(_app_ctx_stack.top,'uri_api_softlog',uri)        
        g.user = current_user 
    #BaseSecurityManager.before_request()




def get_db(id_db):
    """
       Realiza uma conexao com o banco de dados, quando uma 
       requisição e feita para a aplicacao. A arquitetura utilizada 
       segue o padrao multi-tenancy. 
       Parametros: 
           id_db - O identificador do banco de dados tenancy. 
       Return: 
           Um objeto de conexão do tipo psycopg2.connection
    """  
    #Conexão ao banco de dados principal da arquitetura multi-tenancy
    #O objetivo é pegar o DSN do banco de dados tenancy.
    

    #Verifica se a conexão ao banco tenancy existe
    db_name = '_database_' + str(id_db)
    db = getattr(_app_ctx_stack.top,db_name,None)
    if db is not None:
        return db 

    #Se não existe conexão principal faz conexão 
    dbm = getattr(_app_ctx_stack.top,'_database_main',None)        
    if dbm is None:
        dbm = psycopg2.connect(app.config.get('DSN_MAIN'))       
        c = dbm.cursor()
        c.execute("SET application_name = 'Api Softlog Principal'") 
        c.close()
        _app_ctx_stack.top._database_main = dbm
            
    #Obtem o dsn do banco destino
    if str(type(id_db)) == "<class 'str'>":
        cmd = "SELECT f_get_dsn_tenancy('%s') as dsn " % id_db            
    else:
        cmd = "SELECT f_get_dsn_tenancy(%i) as dsn " % id_db

    cursor = dbm.cursor(cursor_factory=DictCursor)
    cursor.execute(cmd)
    resultado = cursor.fetchone()
    cursor.close()
        
    id_db_session = getattr(_app_ctx_stack.top,'id_db',None)
    setattr(_app_ctx_stack.top,'id_db',id_db)
        
    #Conexão ao banco de dados tenancy 
    db = psycopg2.connect(resultado['dsn'])
    c = db.cursor()
    c.execute("SET application_name = 'Api Softlog Principal'") 
    c.close()

    setattr(_app_ctx_stack.top,db_name,db)
   # print('Conexao estabelecida com ',resultado['dsn'])
    #print(db.status)
        
    return db


@app.teardown_appcontext
def close_connection(exception):
    pass
    #id_db = getattr(_app_ctx_stack.top,'id_db',None)    
    #dbm = getattr(_app_ctx_stack.top,'_database_main',None)    
    #print(dbm.dsn,' fechada')
    #if dbm is not None: dbm.close()
        
    #db_name = '_database_' + str(id_db)
    #db = getattr(_app_ctx_stack.top,db_name,None)
    #print(db.dsn, ' fechada')
    #print('Antes de fechar',db.closed)
    #if db is not None: db.close()    
    #print('Depois de fechar',db.closed)

 

def get_uri_db(id_db):
    """
       Retorna a URI de um Banco de Dados pelo id_db
    """     

    #Conexão ao banco de dados principal da arquitetura multi-tenancy
    #O objetivo é pegar o DSN do banco de dados tenancy.
    id_db_aux = id_db
    if id_db_aux not in ["softrans_sb","softlog"]:
        id_db_aux = "softlog_" + id_db


    cmd = "SELECT * FROM string_conexoes WHERE trim(banco_dados) = '%s'" % id_db_aux
    
    dbm = psycopg2.connect(app.config.get('DSN_MAIN'))
    cursor = dbm.cursor(cursor_factory=DictCursor)        
    cursor.execute(cmd)
    resultado = cursor.fetchone()
    cursor.close()
    
    #print(ab)

    if resultado is None:
        return None

    uri = 'postgresql://%s:%s@%s:%s/%s' % (resultado['usuario'],
                                           resultado['senha'],
                                           resultado['host'],
                                           resultado['port'],
                                           str(resultado['banco_dados'].strip())
    )
    
    return  uri

def query_db(id_db, query, args={}, one=False):
    #Tratando conexao com banco fora do padrão do framework
    #id_db_aux
    id_db_aux = id_db
    if id_db == "softlog_sb":
        id_db_aux = "softrans_sb"

    if id_db == "softlog_jetlog_teste":
        id_db_aux == "jetlog_teste"

    if id_db == "softlog_softlog":
        id_db_aux = "softlog"
    
    try:
        db = get_db(id_db_aux)
        cur = db.cursor(cursor_factory=DictCursor)    
        psycopg2.extras.register_default_json(loads=None)
        cur.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
    except:
        print(traceback.format_exc())
        return None

def query_db_2(id_db, query, args={}, one=False):
    #Tratando conexao com banco fora do padrão do framework
    #id_db_aux
    id_db_aux = id_db
    if id_db == "softlog_sb":
        id_db_aux = "softrans_sb"

    if id_db == "softlog_jetlog_teste":
        id_db_aux == "jetlog_teste"

    if id_db == "softlog_softlog":
        id_db_aux = "softlog"
    
    try:
        db = get_db(id_db_aux)
        cur = db.cursor(cursor_factory=DictCursor)    
        psycopg2.extras.register_default_json(loads=lambda x: x)
        cur.execute(query, args)
        psycopg2.extras.register_default_json(loads=None)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
    except:
        traceback.format_exc()
        return None

def query_db_cursor(id_db, reffunc, cursor, args, one=False):
    db = get_db(id_db)    
    parametros = [cursor] + args
    cur = conn.cursor(cursor)
    cur.callproc(reffunc, parametros)

    cur2 = db.cursor(cursor_factory=DictCursor)
    return cur2 

def execute_db(id_db, query):
    try:
        db = get_db(id_db)
        cur = db.cursor()
        cur.execute(query)
        cur.close()        
        return True 
    except:
        return False

app.jinja_env.globals.update(_=lazy_gettext)
@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/websurge-allow.txt')
def static_from_root():
    return ''



#Serve imagens do sistema de logistica softlog
from .api.logistica.documentos import Imagens
@app.route('/api/softlog/imagem/<int:codigo_acesso>/<imagem>')
def get_imagem(codigo_acesso,imagem):
    r = Imagens.getImagem(codigo_acesso,imagem)

    #print(codigo_acesso)
    #print(imagem)
    if r is None:
        return ''
    else:       

        from base64 import b64decode
        
        r2 = b64decode(r)

        response = make_response(r2)
        response.headers.set('Content-Type', 'image/jpeg')
        
        #response.headers.set(
        #    'Content-Disposition', filename='%s' % imagem
        #)
        
        return response

@app.route('/api/softlog/resize_imagem/<int:codigo_acesso>/<imagem>')
def resize_imagem(codigo_acesso,imagem):
    r = Imagens.getImagem(codigo_acesso,imagem)

    print(codigo_acesso)
    print(imagem)
    if r is None:
        return ''
    else:       

        from base64 import b64decode
        
        r2 = b64decode(r)

        response = make_response(r2)
        response.headers.set('Content-Type', 'image/jpeg')
        
        #response.headers.set(
        #    'Content-Disposition', filename='%s' % imagem
        #)
        
        return response

@app.route('/politica_privacidade')
def get_politica_privacidade():
    return render_template("/politica_publicidade.html")

##app.register_blueprint(charts,url_prefix='/v1')

#from app.api.nfe import views_nfe

from app.api.integracao_parceiros.views import logistica
app.register_blueprint(logistica,url_prefix='/api/logistica')

from app.api.logistica.views import softlog
app.register_blueprint(softlog,url_prefix='/api/softlog')

#Adiciona um blueprint para arquivos staticos
from app.files import static
app.register_blueprint(static,url_prefix='/files')

#Adiciona as views para o portal
from app.frontend.portal import views

#Adiciona um blueprint para o dashboard
from app.frontend.dashboards_v1 import views

#from app.frontend import views
from app.frontend.integracao_parceiros import views 

#Importa visões da api_cobranca
from app.api_cobranca import views

#Importa visoes da api tms 
from app.api.tms import views

#Importa visoes do modulo security
from app.security import views

#View do portal de consulta
from app.frontend.portal_consulta import views

from app.frontend.cadastros import views_cadastros

from app.frontend.treinamento import base_views

#Importa visoes base
from app.base import index_view
from app.base import main_view
from app.base import views
from app.frontend.treinamento import views

from app.frontend.portal.consulta_base_sefaz import views_consulta_base_sefaz
#import app.baseviews

from app.frontend.treinamento import treinamento_wtf
from app.frontend.treinamento import treinamento_jinja
#result = add_together.delay(10,20)
#result.wait()
