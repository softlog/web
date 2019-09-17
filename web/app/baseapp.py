from app.menu import Menu
from app.views import IndexView, UtilView
from app.security.sqla.manager import SecurityManager
from app.filters import TemplateFilters
from app.sqla.interface import SQLAInterface
from app.security.sqla.models import StringConexoes
from flask import session, Blueprint, url_for
from app.models.gerais import Filial

class AppBuilder(object):
    """
        Classe principal do Builder de Aplicação. Responsável por 
        registrar as views, inicializar base de permissões.
    """
    baseviews = []
    security_manager_class = None
    # Flask app
    app = None
    # Database Session
    session = None
    # Security Manager Class
    sm = None
    # Babel Manager Class
    bm = None
    # dict with addon name has key and intantiated class has value
    addon_managers = None
    # temporary list that hold addon_managers config key
    _addon_managers = None

    baseviews = []
    menu = None
    endpoint = None
    route_base = None
    indexview = None
    template_folder = None
    static_folder = None
    static_url_path = None

    template_filters = None

    model_string_conexoes = None

    string_conexoes = None
    
    uris = None
    
    def __init__(self, app, session):

        self.menu = Menu()        
        self.app = app
        self.session = session
        self.base_template = "frontend/base_onepage.html"
        self.template_folder = "templates"
        self.static_folder = "files/static"
        self.security_manager_class = SecurityManager
        self.sm = self.security_manager_class(self)    
        self.indexview = IndexView
        self._add_admin_views()
        #self._add_addon_views()
        self._add_menu_permissions()
        self._add_global_filters()      
        self.model_string_conexoes = SQLAInterface(StringConexoes,session)
        #session.close()
        
        #self._add_uris()

        if not self.app:
            for baseview in self.baseviews:
                # instantiate the views and add session
                self._check_and_init(baseview)
                # Register the views has blueprints
                self.register_blueprint(baseview)
                # Add missing permissions where needed
                self._add_permission(baseview)
    
    def _check_and_init(self, baseview):
        # If class if not instantiated, instantiate it
        # and add db session from security models.
        if hasattr(baseview, 'datamodel'):
            if baseview.datamodel.session is None:
                baseview.datamodel.session = self.session
        if hasattr(baseview, '__call__'):
            baseview = baseview()
        return baseview

    def add_view(self, baseview, name, href="", icon="",
                 label="", category="",
                 category_icon="", category_label=""):
        """
        Add your views associated with menus using this method.

        :param baseview:
            A BaseView type class instantiated or not.
            This method will instantiate the class for you if needed.
        :param name:
            The string name that identifies the menu.
        :param href:
            Override the generated href for the menu.
            You can use an url string or an endpoint name
            if non provided default_view from view will be set as href.
        :param icon:
            Font-Awesome icon name, optional.
        :param label:
            The label that will be displayed on the menu,
            if absent param name will be used
        :param category:
            The menu category where the menu will be included,
            if non provided the view will be acessible as a top menu.
        :param category_icon:
            Font-Awesome icon name for the category, optional.
        :param category_label:
            The label that will be displayed on the menu,
            if absent param name will be used

        Examples::

            appbuilder = AppBuilder(app, db)
            # Register a view, rendering a top menu without icon.
            appbuilder.add_view(MyModelView(), "My View")
            # or not instantiated
            appbuilder.add_view(MyModelView, "My View")
            # Register a view, a submenu "Other View" from "Other" with a phone icon.
            appbuilder.add_view(MyOtherModelView, "Other View", icon='fa-phone', category="Others")
            # Register a view, with category icon and translation.
            appbuilder.add_view(YetOtherModelView(), "Other View", icon='fa-phone',
                            label=_('Other View'), category="Others", category_icon='fa-envelop',
                            category_label=_('Other View'))
            # Add a link
            appbuilder.add_link("google", href="www.google.com", icon = "fa-google-plus")
        """
        baseview = self._check_and_init(baseview)
        #log.info(LOGMSG_INF_FAB_ADD_VIEW.format(baseview.__class__.__name__, name))

        if not self._view_exists(baseview):
            baseview.appbuilder = self
            self.baseviews.append(baseview)
            #self._process_inner_views()
            if self.app:
                self.register_blueprint(baseview)
                self._add_permission(baseview)
        self.add_link(name=name, href=href, icon=icon, label=label,
                      category=category, category_icon=category_icon,
                      category_label=category_label, baseview=baseview)
        return baseview

    def add_link(self, name, href, icon="", label="",
                 category="", category_icon="",
                 category_label="", baseview=None):
        """
            Add your own links to menu using this method

            :param name:
                The string name that identifies the menu.
            :param href:
                Override the generated href for the menu.
                You can use an url string or an endpoint name
            :param icon:
                Font-Awesome icon name, optional.
            :param label:
                The label that will be displayed on the menu,
                if absent param name will be used
            :param category:
                The menu category where the menu will be included,
                if non provided the view will be accessible as a top menu.
            :param category_icon:
                Font-Awesome icon name for the category, optional.
            :param category_label:
                The label that will be displayed on the menu,
                if absent param name will be used

        """
        self.menu.add_link(name=name, href=href, icon=icon, label=label,
                           category=category, category_icon=category_icon,
                           category_label=category_label, baseview=baseview)
        if self.app:            
            self._add_permissions_menu(name)
            if category:
                self._add_permissions_menu(category)

    def add_view_no_menu(self, baseview, endpoint=None, static_folder=None):
        """
            Add your views without creating a menu.

            :param baseview:
                A BaseView type class instantiated.

        """
        baseview = self._check_and_init(baseview)
        #log.info(LOGMSG_INF_FAB_ADD_VIEW.format(baseview.__class__.__name__, ""))

        if not self._view_exists(baseview):
            baseview.appbuilder = self
            self.baseviews.append(baseview)
            #self._process_inner_views()
            if self.app:
                self.register_blueprint(baseview,
                     endpoint=endpoint, static_folder=static_folder)
                #self._add_permission(baseview)
        #else:
            #log.warning(LOGMSG_WAR_FAB_VIEW_EXISTS.format(baseview.__class__.__name__))
        return baseview

    def _view_exists(self, view):
        for baseview in self.baseviews:
            if baseview.__class__ == view.__class__:
                return True
        return False


    def register_blueprint(self, baseview, endpoint=None, static_folder=None):
        self.get_app.register_blueprint(baseview.create_blueprint(self, endpoint=endpoint, static_folder=static_folder))
    
    def _add_uris(self):
        qt, string_conexoes = self.model_string_conexoes.query()
    
        uris = {}
        for s in string_conexoes:
            uri = 'postgresql://%s:%s@%s:%s/%s' % (s.usuario.strip(),
                                           s.senha.strip(),
                                           s.host.strip(),
                                           str(s.port),
                                           s.banco_dados.strip()
                                           )

            uris[str(s.id_string_conexao)] = uri  

    def get_uri(self, id_string_conexao):

        return self.uris.get(str(id_string_conexao))

    def _add_global_filters(self):
        self.template_filters = TemplateFilters(self.get_app, self.sm)


    @property
    def get_app(self):
        """
            Get current or configured flask app

            :return: Flask App
        """
        if self.app:
            return self.app
        else:
            return current_app

    @property
    def get_session(self):
        """
            Get the current sqlalchemy session.

            :return: SQLAlchemy Session
        """
        return self.session

    @property
    def app_name(self):
        """
            Get the App name

            :return: String with app name
        """
        return self.get_app.config['APP_NAME']

    @property
    def app_theme(self):
        """
            Get the App theme name

            :return: String app theme name
        """
        return self.get_app.config['APP_THEME']

    @property
    def app_icon(self):
        """
            Get the App icon location

            :return: String with relative app icon location
        """
        return self.get_app.config['APP_ICON']

    @property
    def languages(self):
        return self.get_app.config['LANGUAGES']

    @property
    def version(self):
        """
            Get the current F.A.B. version

            :return: String with the current F.A.B. version
        """
        return VERSION_STRING

    def _add_admin_views(self):
        """
            Registers indexview, utilview (back function), babel views and Security views.
        """
        self.indexview = self._check_and_init(self.indexview)
        self.add_view_no_menu(self.indexview)
        self.add_view_no_menu(UtilView())
        #self.bm.register_views()
        self.sm.register_views()   
    
    @property
    def get_url_for_index(self):
        return url_for('%s.%s' % (self.indexview.endpoint, self.indexview.default_view))
        
    @property
    def get_url_for_userinfo(self):
        return url_for('%s.%s' % (self.sm.user_view.endpoint, 'userinfo'))

    def _add_permission(self, baseview):
        self.sm.add_permissions_view(baseview.base_permissions, baseview.__class__.__name__)
        try:
            pass
            #self.sm.add_permissions_view(baseview.base_permissions, baseview.__class__.__name__)
        except Exception as e:
            log.error(LOGMSG_ERR_FAB_ADD_PERMISSION_VIEW.format(str(e)))


    def _add_permissions_menu(self, name):
        try:
            self.sm.add_permissions_menu(name)
        except Exception as e:
            log.error(LOGMSG_ERR_FAB_ADD_PERMISSION_MENU.format(str(e)))

    def _add_menu_permissions(self):        
        for category in self.menu.get_list():            
            self._add_permissions_menu(category.name)
            for item in category.childs:
                #dont add permission for menu separator
                if item.name != '-':
                    self._add_permissions_menu(item.name)