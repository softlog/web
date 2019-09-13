from app import app, db, auth
from flask import g
from app.models.users_api_softlog import UserApiSoftlog as User
from app.models.softlog_notfis import SoftlogNotfis
from app.models.scr_ocorrencia_edi import ScrOcorrenciaEdi
from app.models.scr_doc_integracao import ScrDocIntegracao
from app.schemas.scr_doc_integracao_schema import ScrDocIntegracaoSchema
from app.schemas.softlog_notfis_schema import SoftlogNotfisSchema
from app.schemas.scr_ocorrencia_edi_schema import ScrOcorrenciaEdiSchema
from sqlalchemy.orm.exc import NoResultFound

from flask import Flask, abort, request, jsonify, g, url_for
from app.flask_rest_jsonapi_custom import Api, ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound, AccessDenied 
from flask_rest_jsonapi import JsonApiException

class AccessDeniedDetail(JsonApiException):
    """Throw this error when requested resource owner doesn't match the user of the ticket"""

    title = 'Access denied'
    status = 403

##Rotina para autenticacao de apis via token
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = db.session.query(User).filter(User.username==username_or_token).first()
        if not user or not user.verify_password(password):
            return False

    g.user = user
    return True

@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.form.get('username')
    password = request.form.get('password')    
    #print("USUARIO", username)
    #print("SENHA", password)
    if username is None or password is None:
        abort(400)    # missing arguments
    
    #if User.query.filter_by(username=username).first() is not None:
    if db.session.query(User).filter(User.username==username).first() is not None:
        abort(400)    # existing user

    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()    
    return (jsonify({'username': user.username}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})


@app.route('/api/users/<int:id>')
def get_user(id):
    print(ab)
    #print(dir(db.session.query))
    user = db.session.query(User).get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})

class ScrDocIntegracaoList(ResourceList):
    
    schema = ScrDocIntegracaoSchema

    methods = ['GET','POST']
    data_layer = {'session':db.session,
                  'model':ScrDocIntegracao
                 }

    decorators = (auth.login_required,)     



class ScrDocIntegracaoDetail(ResourceDetail):
    
    methods = ['GET','POST']
    schema = ScrDocIntegracaoSchema
    decorators = (auth.login_required,)    

    data_layer = {'session': db.session,
                  'model': ScrDocIntegracao
                  }


class SoftlogNotfisList(ResourceList):
    #disable_permission = True

    schema = SoftlogNotfisSchema
    methods = ['GET','POST']
    decorators = (auth.login_required,)    

    def query(self, view_kwargs):
        query_ = self.session.query(SoftlogNotfis).filter_by(user_api_id=g.user.id)        
        return query_


    def before_create_object(self, data, view_kwargs):
        if data.get('user_api_id') is None:
            data['user_api_id'] = str(g.user.id)
        print(data)       

    data_layer = {'session':db.session,
                  'model':SoftlogNotfis,
                  'methods':{
                      'query':query,
                      'before_create_object':before_create_object
                      }
                 }


class SoftlogNotfisDetail(ResourceDetail):
    
    methods = ['GET']
    schema = SoftlogNotfisSchema
    decorators = (auth.login_required, )    

    def before_get_object(self, view_kwargs):
        
        if view_kwargs.get('id') is not None:
            try:
                doc = self.session.query(SoftlogNotfis).filter_by(id=view_kwargs['id']).one()
                #print(a)
            except NoResultFound:
                pass
            else:
                user = g.user                
                if doc.user_api_id != user.id:
                    raise AccessDenied("Access Denied")
    

    
    data_layer = {'session': db.session,
                  'model': SoftlogNotfis,
                  'methods':{ 'before_get_object':before_get_object
                      }
                  }


class ScrOcorrenciaEdiList(ResourceList):
    
    schema = ScrOcorrenciaEdiSchema

    methods = ['GET']
    data_layer = {'session':db.session,
                  'model':ScrOcorrenciaEdi
                 }

    decorators = (auth.login_required,)     



class ScrOcorrenciaEdiDetail(ResourceDetail):
    
    methods = ['GET']
    schema = ScrOcorrenciaEdiSchema
    decorators = (auth.login_required,)    
    
    data_layer = {'session': db.session,
                  'model': ScrOcorrenciaEdi
                  }


def permission_manager(view, view_args, view_kwargs, *args, **kwargs):
    """The function use to check permissions

    :param callable view: the view
    :param list view_args: view args
    :param dict view_kwargs: view kwargs
    :param list args: decorator args
    :param dict kwargs: decorator kwargs"""

    user = g.user
    ##print(a)
    ##raise AccessDenied("Acesso Negado")
    #print("Estou aparecendo aqui")



api = Api(app)

#api.oauth_manager(auth.login_required)
api.route(ScrDocIntegracaoList, 'scr_doc_integracao_list', '/api/softlog/tms/scr_doc_integracao')
api.route(ScrDocIntegracaoDetail, 'scr_doc_integracao_detail', '/api/softlog/tms/scr_doc_integracao/<int:id>')
api.route(SoftlogNotfisList, 'softlog_notfis_list', '/api/softlog/tms/softlog_notfis')
api.route(SoftlogNotfisDetail, 'softlog_notfis_detail', '/api/softlog/tms/softlog_notfis/<int:id>')
api.route(ScrOcorrenciaEdiList, 'scr_ocorrencia_edi_list', '/api/softlog/tms/scr_ocorrencia_edi')
api.route(ScrOcorrenciaEdiDetail, 'scr_ocorrencia_edi_detail', '/api/softlog/tms/scr_ocorrencia_edi/<int:id>')
api.permission_manager(permission_manager)
