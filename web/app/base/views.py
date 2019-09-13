from flask import render_template, session, escape, g, redirect, _app_ctx_stack, request, flash
from flask_login import login_required, current_user
from app import app
from app import db
from app import widgets
from app.baseviews import BaseView, expose
from app.views import SimpleFormView, UtilView
from app.views import ModelView
from app.sqla.interface import SQLAInterface
from app.idioma import lazy_gettext as _
from app.models.bancos import Banco
from app.models.gerais import Filial, Cidades
from app.models.treinamento.models_treinamento import NotasFiscais
from app.security.sqla.models import User

from app import appbuilder

from app.sqla.models.filters import BaseFilterConverter
from app.sqla.models.filters import Filters
from app.sqla.filters import *

from app.base.forms import FormSearchCidades



@app.route('/material/')
def material():
    #users = db.session.query(User).all()
    
    return render_template('frontend/material/base.html')


@app.route('/semantic/')
def semantic():
    #users = db.session.query(User).all()
    menu = ["Nav","Animated Icon", "Box", "Cards"]
    return render_template('frontend/admin_semantic/sample.html', menu=menu)



@app.route('/')
@login_required
def root2():      

    if g.user is None:
        return redirect('/login/')
        #return 'Logged in as %s user %s' % (escape(session),"Sem Usuario")
    
    filial =  db.session.query(Filial).filter(Filial.codigo_empresa=='001').first()

    #return 'Logged in as %s user %s with Filial %s' % (escape(session),escape(g.user), escape(filial))
    return render_template('frontend/base_softlog.html')


@app.route('/user_list/')
def user_list():
    print(getattr(_app_ctx_stack.top,'uri_request',None))
    users = db.session.query(User).all()

    return render_template('security/user_list.html', dados=users)



@app.route('/edit/')
def edit():
    #users = db.session.query(User).all()

    return render_template('frontend/general/model/edit.html')

@app.route('/list/')
def list():

    #users = db.session.query(User).all()
    return render_template('frontend/general/model/list.html', title="Lista Template")

class UserView(BaseView):
   
    
    title="Um teste"

    @expose('/teste/<string:param1>')
    def method1(self, param1):
        # do something with param1
        # and return it
        return self.render_template("contact.html",appbuilder=appbuilder)





from .forms import MyForm

class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(self.message, 'info')


class UsuariosView(ModelView):
    datamodel = SQLAInterface(User)

    list_columns = ['nome_usuario', 'email', 'login_name', 'id_usuario']    
        
class NotasFiscaisView(ModelView):
    datamodel = SQLAInterface(NotasFiscais)

    list_columns = ['chave_nfe', 'numero_nota_fiscal', 'data_emissao', 'valor', 'remetente.nome_cliente']


class BancosView(ModelView):
    datamodel = SQLAInterface(Banco)

    show_column = list_columns = ['id_banco', 'nome_banco', 'numero_banco']
    add_columns = edit_columns = ['nome_banco', 'numero_banco']

        
appbuilder.add_view_no_menu(UtilView)

appbuilder.add_view_no_menu(UserView)

##appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
##                     category="My Forms", category_icon="fa-cogs")

##appbuilder.add_view(UsuariosView, "Usuários", icon="fa-group", label=_('Usuários'),
                     ##category="Geral", category_icon="fa-cogs")

##appbuilder.add_view(NotasFiscaisView, "Notas Fiscais", icon="fa-group", label="Notas Fiscais",
##                     category="Geral", category_icon="fa-cogs")

##appbuilder.add_view(BancosView, "Bancos", icon="fa-group", label="Bancos",
##                     category="Geral", category_icon="fa-cogs")