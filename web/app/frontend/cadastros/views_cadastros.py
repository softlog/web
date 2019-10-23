##Classes para implementação de Views
from app.baseviews import expose, BaseView
from app.views import ModelSoftlogView
from app.security.decorators import has_access, permission_name, has_access_api
from app import appbuilder
from app.sqla.interface import SQLAInterface

## Modelos de Dados
from app.models.gerais import Filial, BancosModel

##View Cadastro Banco
class Bancos(ModelSoftlogView):

    datamodel = SQLAInterface(BancosModel)
    start_empty = False

    #Colunas que vão aparecer na listagem
    list_columns = ['nome_banco','numero_banco']

    #Colunas que vão aparecer nas telas de Inserção, Edição e Visualização
    add_columns = ['nome_banco','numero_banco']
    edit_columns = show_columns = add_columns 

    #Títulos das colunas (Captions)
    label_columns = {'nome_banco':'Banco'}

    #Determina o Order By (Está em conflito com a classe do datagrid js)
    order_columns = ['nome_banco']

    #Colunas disponíveis para filtros na listagem
    search_columns = ['nome_banco','numero_banco']

    search_columns







appbuilder.add_view(Bancos, "Bancos", icon="fa-group", label='Bancos',
                     category="Cadastros", category_icon="fa-cogs")
