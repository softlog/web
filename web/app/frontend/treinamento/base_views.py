from app.baseviews import expose, BaseView
from app.views import ModelSoftlogView
from app.security.decorators import has_access, permission_name, has_access_api
from app import appbuilder
from app.models.gerais import Filial
from app.sqla.interface import SQLAInterface

class OlaBaseView(BaseView):


    @expose("ola_baseview")
    @has_access
    @permission_name("acesso_ola_baseview")
    def ola(self):
        return "Ola Base View"


class Filial(ModelSoftlogView):
    datamodel = SQLAInterface(Filial)

    list_columns = ['razao_social', 'cnpj', 'codigo_filial', 'codigo_empresa']

    add_columns = ['razao_social', 'cnpj', 'codigo_filial', 'codigo_empresa']

    show_columns = edit_columns = add_columns
    
    #start_empty = False



appbuilder.add_view(OlaBaseView, "Ola BaseView", href="/olabaseview/ola_baseview", icon="fa-group", label='Ola Base View',
                     category="Treinamento", category_icon="fa-cogs")

appbuilder.add_view(Filial,"Filial",category="Cadastros")

