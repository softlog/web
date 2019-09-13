import datetime
import logging
import copy
from werkzeug.security import generate_password_hash
from wtforms import validators, PasswordField
from wtforms.validators import EqualTo

from flask_login import current_user, login_user, logout_user, login_required
from flask import flash, redirect, session, url_for, request, g, make_response, jsonify, abort, session
from flask import render_template, _app_ctx_stack, escape
from app.idioma import lazy_gettext


from app.views import ModelView, SimpleFormView, expose, expose_api, ModelSoftlogView
from app.baseviews import BaseView
from app.charts.views import DirectByChartView
from app.fieldwidgets import BS3PasswordFieldWidget
from app.actions import action
from app._compat import as_unicode
from .forms import LoginForm_db, LoginForm_oid, ResetPasswordForm, UserInfoEdit, LoginForm_dbTny
from .decorators import has_access
from app.widgets import ListLinkWidget, ListWidget

log = logging.getLogger(__name__)


class TipoPermissoes(ModelSoftlogView):
    route_base = '/permissions'
    base_permissions = ['Listar']
    list_widget = ListWidget
    start_empty = False
    base_order = ('name','asc')

    list_title = lazy_gettext('List Base Permissions')
    show_title = lazy_gettext('Show Base Permission')
    add_title = lazy_gettext('Add Base Permission')
    edit_title = lazy_gettext('Edit Base Permission')

    label_columns = {'name': lazy_gettext('Name')}


class Menus(ModelSoftlogView):
    route_base = '/viewmenus'
    base_permissions = ['Listar']
    list_widget = ListWidget
    base_order = ('name','asc')
    start_empty = False

    list_title = lazy_gettext('List View Menus')
    show_title = lazy_gettext('Show View Menu')
    add_title = lazy_gettext('Add View Menu')
    edit_title = lazy_gettext('Edit View Menu')

    label_columns = {'name': lazy_gettext('Name')}


class Permissoes(ModelSoftlogView):
    route_base = '/permissionviews'
    base_permissions = ['Listar']
    list_widget = ListWidget
    start_empty = False
    
    list_title = lazy_gettext('List Permissions on Views/Menus')
    show_title = lazy_gettext('Show Permission on Views/Menus')
    add_title = lazy_gettext('Add Permission on Views/Menus')
    edit_title = lazy_gettext('Edit Permission on Views/Menus')

    label_columns = {'permission': lazy_gettext('Permission'), 'view_menu': lazy_gettext('View/Menu')}
    list_columns = ['permission', 'view_menu']
    

class RedefinirMinhaSenha(SimpleFormView):
    """
        View for resetting own user password
    """
    route_base = '/resetmypassword'    

    form = ResetPasswordForm
    form_title = lazy_gettext('Reset Password Form')
    redirect_url = '/'
    message = lazy_gettext('Password Changed')

    def form_post(self, form):
        self.appbuilder.sm.reset_password(g.user.id, form.password.data)
        flash(as_unicode(self.message), 'info')


class RedefinirSenha(SimpleFormView):
    """
        View for reseting all users password
    """
    route_base = '/resetpassword'
    form = ResetPasswordForm
    form_title = lazy_gettext('Reset Password Form')
    redirect_url = '/'
    message = lazy_gettext('Password Changed')

    def form_post(self, form):
        pk = request.args.get('pk')
        self.appbuilder.sm.reset_password(pk, form.password.data)
        flash(as_unicode(self.message), 'info')


class UsuarioInformacoes(SimpleFormView):
    form = UserInfoEdit
    form_title = lazy_gettext('Edit User Information')
    redirect_url = '/'
    message = lazy_gettext('User information changed')
    

    def form_get(self, form):
        item = self.appbuilder.sm.get_user_by_id(g.user.id)
        # fills the form generic solution
        for key, value in  form.data.items():
            form_field = getattr(form, key)
            form_field.data = getattr(item, key)

    def form_post(self, form):
        form = self.form.refresh(request.form)
        item = self.appbuilder.sm.get_user_by_id(g.user.id)
        form.populate_obj(item)
        self.appbuilder.sm.update_user(item)
        flash(as_unicode(self.message), 'info')


class UserModelView(ModelSoftlogView):
    route_base = '/users'
    list_widget = ListWidget
    start_empty = False

    list_title = lazy_gettext('List Users')
    show_title = lazy_gettext('Show User')
    add_title = lazy_gettext('Add User')
    edit_title = lazy_gettext('Edit User')    
    base_order      = ("first_name","asc")

    label_columns = {'get_full_name': lazy_gettext('Full Name'),
                     'first_name': lazy_gettext('First Name'),
                     'last_name': lazy_gettext('Last Name'),
                     'username': lazy_gettext('User Name'),
                     'password': lazy_gettext('Password'),
                     'active': lazy_gettext('Is Active?'),
                     'email': lazy_gettext('EMail'),
                     'roles': lazy_gettext('Role'),
                     'last_login': lazy_gettext('Last login'),
                     'login_count': lazy_gettext('Login count'),
                     'fail_login_count': lazy_gettext('Failed login count'),
                     'created_on': lazy_gettext('Created on'),
                     'created_by': lazy_gettext('Created by'),
                     'changed_on': lazy_gettext('Changed on'),
                     'changed_by': lazy_gettext('Changed by')}

    description_columns = {'first_name': lazy_gettext('Write the user first name or names'),
                           'last_name': lazy_gettext('Write the user last name'),
                           'username': lazy_gettext(
                               'Username valid for authentication on DB or LDAP, unused for OID auth'),
                           'password': lazy_gettext(
                               'Please use a good password policy, this application does not check this for you'),
                           'active': lazy_gettext('It\'s not a good policy to remove a user, just make it inactive'),
                           'email': lazy_gettext('The user\'s email, this will also be used for OID auth'),
                           'roles': lazy_gettext(
                               'The user role on the application, this will associate with a list of permissions'),
                           'conf_password': lazy_gettext('Please rewrite the user\'s password to confirm')}

    list_columns = ['nome_usuario', 'last_name', 'username', 'email', 'active', 'roles']

    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles','login_count']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    search_exclude_columns = ['password']

    add_columns = ['nome_usuario', 'last_name', 'username', 'active', 'email', 'roles']
    edit_columns = ['nome_usuario', 'last_name', 'username', 'active', 'email', 'roles']
    user_info_title = lazy_gettext("Your user information")


    @expose('/userinfo/')
    @has_access
    def userinfo(self):
        item = self.datamodel.get(g.user.id, self._base_filters)
        widgets = self._get_show_widget(g.user.id, item, show_fieldsets=self.user_show_fieldsets)
        self.update_redirect()
        return self.render_template(self.show_template,
                               title=self.user_info_title,
                               widgets=widgets,
                               appbuilder=self.appbuilder)

    @action('userinfoedit', lazy_gettext("Edit User"), "", "fa-edit", multiple=False)
    def userinfoedit(self, item):
        return redirect(url_for(self.appbuilder.sm.userinfoeditview.__name__ + '.this_form_get'))

class UserOIDModelView(UserModelView):
    """
        View that add OID specifics to User view.
        Override to implement your own custom view.
        Then override useroidmodelview property on SecurityManager
    """
    pass


class UserLDAPModelView(UserModelView):
    """
        View that add LDAP specifics to User view.
        Override to implement your own custom view.
        Then override userldapmodelview property on SecurityManager
    """
    pass


class UserOAuthModelView(UserModelView):
    """
        View that add OAUTH specifics to User view.
        Override to implement your own custom view.
        Then override userldapmodelview property on SecurityManager
    """
    pass


class UserRemoteUserModelView(UserModelView):
    """
        View that add REMOTE_USER specifics to User view.
        Override to implement your own custom view.
        Then override userldapmodelview property on SecurityManager
    """
    pass


class Usuarios(UserModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """
    add_form_extra_fields = {'password': PasswordField(lazy_gettext('Password'),
                                                       description=lazy_gettext(
                                                           'Please use a good password policy, this application does not check this for you'),
                                                       validators=[validators.DataRequired()],
                                                       widget=BS3PasswordFieldWidget()),
                             'conf_password': PasswordField(lazy_gettext('Confirm Password'),
                                                            description=lazy_gettext(
                                                                'Please rewrite the user\'s password to confirm'),
                                                            validators=[EqualTo('password', message=lazy_gettext(
                                                                'Passwords must match'))],
                                                            widget=BS3PasswordFieldWidget())}

    add_columns = ['nome_usuario', 'last_name', 'username', 'active', 'email', 'roles','password', 'conf_password']

    @expose('/show/<pk>', methods=['GET'])
    @has_access
    def show(self, pk):
        actions = {}
        actions['resetpasswords'] = self.actions.get('resetpasswords')
        item = self.datamodel.get(pk, self._base_filters)
        if not item:
            abort(404)
        widgets = self._get_show_widget(pk, item, actions=actions)
        self.update_redirect()
        return self.render_template(self.show_template,
                               pk=pk,
                               title=self.show_title,
                               widgets=widgets,
                               appbuilder=self.appbuilder,
                               related_views=self._related_views)


    @expose('/userinfo/')
    @has_access
    def userinfo(self):
        actions = {}
        actions['resetmypassword'] = self.actions.get('resetmypassword')
        actions['userinfoedit'] = self.actions.get('userinfoedit')

        item = self.datamodel.get(g.user.id, self._base_filters)
        widgets = self._get_show_widget(g.user.id, item, actions=actions, show_fieldsets=self.user_show_fieldsets)
        self.update_redirect()
        return self.render_template(self.show_template,
                               title=self.user_info_title,
                               widgets=widgets,
                               appbuilder=self.appbuilder,
        )

    @action('resetmypassword', lazy_gettext("Reset my password"), "", "fa-lock", multiple=False)
    def resetmypassword(self, item):
        return redirect(url_for(self.appbuilder.sm.resetmypasswordview.__name__ + '.this_form_get'))

    @action('resetpasswords', lazy_gettext("Reset Password"), "", "fa-lock", multiple=False)
    def resetpasswords(self, item):
        return redirect(url_for(self.appbuilder.sm.resetpasswordview.__name__ + '.this_form_get', pk=item.id))

    def pre_update(self, item):
        item.changed_on = datetime.datetime.now()
        item.changed_by_fk = g.user.id

    def pre_add(self, item):
        item.password = generate_password_hash(item.password)


class UsuarioEstatisticas(DirectByChartView):
    chart_title = lazy_gettext('User Statistics')
    label_columns = {'username': lazy_gettext('User Name'),
                     'login_count': lazy_gettext('Login count'),
                     'fail_login_count': lazy_gettext('Failed login count')
    }

    search_columns = UserModelView.search_columns

    definitions = [
        {
            'label': 'Login Count',
            'group': 'username',
            'series': ['login_count']
        },
        {
            'label': 'Failed Login Count',
            'group': 'username',
            'series': ['fail_login_count']
        }

    ]


class GruposUsuario(ModelSoftlogView):
    route_base = '/roles'
    list_widget = ListWidget
    base_order = ('name','asc')
    start_empty = False

    list_title = lazy_gettext('List Roles')
    show_title = lazy_gettext('Show Role')
    add_title = lazy_gettext('Add Role')
    edit_title = lazy_gettext('Edit Role')

    label_columns = {'name': lazy_gettext('Name'), 'permissions': lazy_gettext('Permissions')}
    list_columns = ['name', 'permissions']
    order_columns = ['name']
    
    @action("Clonar Grupo", lazy_gettext('Copy Role'), lazy_gettext('Copy the selected roles?'), icon='fa-copy', single=False)
    def copy_role(self, items):
        self.update_redirect()
        for item in items:
            new_role = item.__class__()
            new_role.name = item.name
            new_role.permissions = item.permissions
            new_role.name = new_role.name + ' copiar'
            self.datamodel.add(new_role)
        return redirect(self.get_redirect())


class RegistroUsuario(ModelSoftlogView):
    route_base = '/registeruser'
    list_widget = ListWidget
    base_order = ('username','asc')

    base_permissions = ['Listar', 'Visualizar', 'Excluir']
    list_title = lazy_gettext('List of Registration Requests')
    show_title = lazy_gettext('Show Registration')
    list_columns = ['username','registration_date','email']
    show_exclude_columns = ['password']
    search_exclude_columns = ['password']

class AuthView(BaseView):
    route_base = ''
    login_template = ''

    invalid_login_message = lazy_gettext('Invalid login. Please try again.')

    title = lazy_gettext('Sign In')

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        pass

    @expose('/logout/')
    def logout(self):
        logout_user()
        return redirect(self.appbuilder.get_url_for_index)

    @expose('/relogin/',methods=['GET', 'POST'])
    def relogin(self):
        pass

class Autenticacao(AuthView):
    login_template = 'appbuilder/general/security/login_db.html'

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        if g.user is not None and g.user.is_authenticated():
            return redirect('/')
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_db(form.username.data, form.password.data)
            if not user:
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect(self.appbuilder.get_url_for_login)
            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)
        return self.render_template(self.login_template,
                               title=self.title,
                               form=form,
                               appbuilder=self.appbuilder)


class AuthLDAPView(AuthView):
    login_template = 'appbuilder/general/security/login_ldap.html'

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        if g.user is not None and g.user.is_authenticated():
            return redirect(self.appbuilder.get_url_for_index)
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_ldap(form.username.data, form.password.data)
            if not user:
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect(self.appbuilder.get_url_for_login)
            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)
        return self.render_template(self.login_template,
                               title=self.title,
                               form=form,
                               appbuilder=self.appbuilder)

    """
        For Future Use, API Auth, must check howto keep REST stateless
    """
    
    """
    @expose_api(name='auth',url='/api/auth')
    def auth(self):
        if g.user is not None and g.user.is_authenticated():
            http_return_code = 401
            response = make_response(jsonify({'message': 'Login Failed already authenticated',
                                              'severity': 'critical'}), http_return_code)
        username = str(request.args.get('username'))
        password = str(request.args.get('password'))
        user = self.appbuilder.sm.auth_user_ldap(username, password)
        if not user:
            http_return_code = 401
            response = make_response(jsonify({'message': 'Login Failed',
                                              'severity': 'critical'}), http_return_code)            
        else:
            login_user(user, remember=False)
            http_return_code = 201
            response = make_response(jsonify({'message': 'Login Success',
                                              'severity': 'info'}), http_return_code)            
        
        return response     
    """

class AuthOIDView(AuthView):
    login_template = 'appbuilder/general/security/login_oid.html'
    oid_ask_for = ['email']
    oid_ask_for_optional = []

    def __init__(self):
        super(AuthOIDView, self).__init__()

    @expose('/login/', methods=['GET', 'POST'])
    def login(self, flag=True):
        @self.appbuilder.sm.oid.loginhandler
        def login_handler(self):
            if g.user is not None and g.user.is_authenticated():
                return redirect(self.appbuilder.get_url_for_index)
            form = LoginForm_oid()
            if form.validate_on_submit():
                session['remember_me'] = form.remember_me.data
                return self.appbuilder.sm.oid.try_login(form.openid.data, ask_for=self.oid_ask_for,
                                                        ask_for_optional=self.oid_ask_for_optional)
            return self.render_template(self.login_template,
                                   title=self.title,
                                   form=form,
                                   providers=self.appbuilder.sm.openid_providers,
                                   appbuilder=self.appbuilder
            )

        @self.appbuilder.sm.oid.after_login
        def after_login(resp):
            if resp.email is None or resp.email == "":
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect('login')
            user = self.appbuilder.sm.auth_user_oid(resp.email)
            if user is None:
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect('login')
            remember_me = False
            if 'remember_me' in session:
                remember_me = session['remember_me']
                session.pop('remember_me', None)

            login_user(user, remember=remember_me)
            return redirect(self.appbuilder.get_url_for_index)

        return login_handler(self)


class AuthOAuthView(AuthView):
    login_template = 'appbuilder/general/security/login_oauth.html'
    
    
    @expose('/login/')
    @expose('/login/<provider>')
    @expose('/login/<provider>/<register>')
    def login(self, provider=None, register=None):
        log.debug('Provider: {0}'.format(provider))
        if g.user is not None and g.user.is_authenticated():
            log.debug("Already authenticated {0}".format(g.user))
            return redirect(self.appbuilder.get_url_for_index)
        if provider is None:
            return self.render_template(self.login_template,
                               providers = self.appbuilder.sm.oauth_providers,
                               title=self.title,
                               appbuilder=self.appbuilder)
        else:
            log.debug("Going to call authorize for: {0}".format(provider))
            try:
                if register:
                    log.debug('Login to Register')
                    session['register'] = True
                return self.appbuilder.sm.oauth_remotes[provider].authorize(callback=url_for('.oauth_authorized',provider=provider, _external=True))
            except Exception as e:
                log.error("Error on OAuth authorize: {0}".format(e))
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect(self.appbuilder.get_url_for_index)
            
    @expose('/oauth-authorized/<provider>')
    def oauth_authorized(self, provider):
        log.debug("Authorized init")
        resp = self.appbuilder.sm.oauth_remotes[provider].authorized_response()
        if resp is None:
            flash(u'You denied the request to sign in.', 'warning')
            return redirect('login')
        log.debug('OAUTH Authorized resp: {0}'.format(resp))
        # Retrieves specific user info from the provider
        try:
            self.appbuilder.sm.set_oauth_session(provider, resp)
            userinfo = self.appbuilder.sm.oauth_user_info(provider)
            log.debug("User info retrieved from {0}: {1}".format(provider, userinfo))
        except Exception as e:
            log.error("Error returning OAuth user info: {0}".format(e))
        # Is this Authorization to register a new user ?
        if session.pop('register', None):
            return redirect(self.appbuilder.sm.registeruseroauthview.get_default_url(**userinfo))
        user = self.appbuilder.sm.auth_user_oauth(userinfo)
        if user is None:
            flash(as_unicode(self.invalid_login_message), 'warning')
            return redirect('login')
        else:
            login_user(user)
            return redirect(self.appbuilder.get_url_for_index)
        
        
class AuthRemoteUserView(AuthView):
    login_template = ''

    @expose('/login/')
    def login(self):
        username = request.environ.get('REMOTE_USER')
        if g.user is not None and g.user.is_authenticated():
            return redirect(self.appbuilder.get_url_for_index)
        if username:
            user = self.appbuilder.sm.auth_user_remote_user(username)
            if user is None:
                flash(as_unicode(self.invalid_login_message), 'warning')
            else:
                login_user(user)
        else:
            flash(as_unicode(self.invalid_login_message), 'warning')
        return redirect(self.appbuilder.get_url_for_index)

class StringConexoesView(ModelSoftlogView):
    route_base = '/databases_tenancy'
    base_permissions = ['Listar','Visualizar']
    list_columns = ['banco_dados','host','port']

    list_title = lazy_gettext('List Base Permissions')
    show_title = lazy_gettext('Show Base Permission')
    add_title = lazy_gettext('Add Base Permission')
    edit_title = lazy_gettext('Edit Base Permission')

    label_columns = {'id_string_conexao': lazy_gettext('Id'),
                     'banco_dados': lazy_gettext('DataBase'),
                     'usuario': lazy_gettext('User'),
                     'senha': lazy_gettext('Password'),
                     'port': lazy_gettext('Port'),
                     'host': lazy_gettext('Host')
                     }


class AuthDBTnyView(AuthView):
    # TODO Criar Rotina que faz autenticacao direta sem formulario    
    login_template = 'appbuilder/general/security/login_db_tny.html'
    @expose('/login/', methods=['GET', 'POST'])
    def login(self):     
        
        try:
            if g.user is not None:          
                if g.user.is_authenticated(): 
                    return redirect('/')
        except:
            pass
            #logout_user()       

        form = LoginForm_dbTny()
        #print('Realizando Login')
        if form.validate_on_submit():
            user = form.username.data
            password = form.password.data
            ambiente = form.ambiente.data
            cod_empresa = form.empresa.data
            cod_filial = form.filial.data
            if not (user and password and ambiente):
                flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect('/')

            auth = self.appbuilder.sm.auth_user_db_tny(user, password, ambiente, cod_empresa, cod_filial)            
            #session['uri'] = getattr(_app_ctx_stack.top,'uri',None)
            user = auth[0]
            filial = auth[1]
            if not user:
                flash(as_unicode(self.invalid_login_message), 'warning')
                #return redirect(self.appbuilder.get_url_for_login)
                if g.user is not None and g.user.is_authenticated():     
                    logout_user()            
            
            login_user(user, remember=False, filial=filial)
            return redirect(self.appbuilder.get_url_for_index)
        
        return self.render_template(self.login_template,
                        title=self.title,
                        form=form,
                        appbuilder=self.appbuilder) 

    @expose('/relogin/<codigo_empresa>/<codigo_filial>/', methods=['GET', 'POST'])
    def relogin(self,codigo_empresa,codigo_filial):                        
        #Verifica se o usuário já está logado
        if g.user is None or not g.user.is_authenticated():            
            #logout_user()        
            return redirect('/')
        
        if request.method == 'GET':            
            #Captura os valores de parametros
             
            if not (codigo_empresa and codigo_filial):
                #flash(as_unicode(self.invalid_login_message), 'warning')
                return redirect('/')

            user = g.user
            filial = self.appbuilder.sm.find_filial(codigo_empresa, codigo_filial)

            if filial is None:
                #TODO: Criar uma mensagem para dizer que filial já esta logada
                return redirect('/')

            if filial == g.filial:
                #TODO: Criar uma mensagem para dizer que filial já esta logada
                return redirect('/')            
            
            login_user(user, remember=False, filial=filial)
        
        return redirect(self.appbuilder.get_url_for_index)




class CidadeView(ModelSoftlogView):
    route_base = '/cidade'
    list_widget = ListLinkWidget

    #base_permissions = ['can_add', 'can_show']
    list_columns    = ['nome_cidade', 'uf']    
    label_columns   = {'nome_cidade':'Cidade','uf':'UF'}  
    base_order      = ("nome_cidade","asc")
    
    
    columns = ['nome_cidade','uf']
    add_columns = edit_columns = view_columns = columns
    
        
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'


class FilialView(ModelSoftlogView):    
    route_base = '/filial'
    list_widget = ListLinkWidget
    base_order = ('razao_social','asc')

    list_columns = ['codigo_empresa',
                    'codigo_filial',
                    'cnpj',
                    'razao_social',
                    'nome_descritivo',
                    'cidade']

    label_columns = {'codigo_empresa':'Empresa',
                     'codigo_filial':'Filial',
                     'cnpj':'Cnpj',
                     'razao_social':'Razao Social',
                     'nome_descritivo':'Nome Descritivo'}

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

    validators_columns = {}


class EmpresaView(ModelSoftlogView):
    route_base = '/empresa'
    list_widget = ListLinkWidget
    base_order = ('razao_social','asc')

    list_columns = ['codigo_empresa',                    
                    'cnpj',
                    'razao_social',
                    'nome_fantasia']

    label_columns = {'codigo_empresa':'Empresa',
                     'codigo_filial':'Filial',
                     'cnpj':'Cnpj',
                     'razao_social':'Razao Social',
                     'nome_fantasia':'Fantasia'}

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'