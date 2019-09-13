from app import query_db
from flask import g, session 
import trace
import traceback

class BaseManager(object):
    """Classe abstrata para Manager"""

    def __init__(self):
        self.id_db = None
        self.empresa = None
        self.filial = None
        self.user = None 
        self.reg_empresa = None
        self.reg_filial  = None        

    def load_user_dashboard(self,token):
        pass

class Manager(BaseManager):
    """Classe responsavel por rotinas de controle dos dashboards"""

    def __init__(self, user, empresa, filial):        
        self.dashboards = []
        self.empresa = empresa
        self.filial = filial 
        self.current_dashboard = None        
        self.menu = None        

        
        try:
            #self.id_db = 'softlog_' + g.user.id.split(':')[1]
            self.id_db = 'softlog_' + session.get('ambiente')
            self.user = user
            self.load_empresas(session.get('ambiente'))
            self.load_filiais(session.get('ambiente'))
            self.load_menu_dashboard()
        except Exception as e:
            print(traceback.format_exc())
            pass

    def load_user(self,login_user, password, ambient):
        
        #Verifica se Ambiente é válido
        cmd = "SELECT string_to_array(string_agg(replace(banco_dados,'softrans_sb','softlog_sb'),','),',') FROM string_conexoes"
            
        ambients = query_db(1,cmd,None,True)        
        
        if ('softlog_' + ambient) not in ambients[0]:
            return None
                 
        #Verifica usuario
        cmd = """SELECT 
                id_usuario,
                trim(nome_usuario) as nome_usuario,
                trim(email) as email, 
                id_usuario as id_usuario,
                trim(login_name) as login,
                senha
           FROM 
                usuarios
           WHERE 
                id_usario = '%i' 
        """ % current_user.id_usuario       


        user = query_db('softlog_' + ambient, cmd, None, True)
        if user is None:
            self.user = None        
            return None

        if user['senha'] != password:
            return None
        else:
            return user

    def get_data_dashboard(self, id_dash, empresa, filial, data_ref=None):
        """Retorna as configuracoes de um dashboard"""

        if data_ref:
            p_var_aux = "'" + data_ref + "'"
        else:
            p_var_aux = 'NULL'

        if filial is not None and empresa is not None:
            cmd = """
                        SELECT f_dashboard_view(%i, '%s', '%s',%s) as dados
                """ % (id_dash,empresa,filial, p_var_aux)

        elif empresa is not None:
            cmd = """
                        SELECT f_dashboard_view(%i, '%s',NULL,%s) as dados
                """ % (id_dash,empresa,p_var_aux)
        else:
            cmd = """
                        SELECT f_dashboard_view(%i, NULL,NULL,%s) as dados
                """ % (id_dash,p_var_aux)

        print(cmd)

        r = query_db(self.id_db, cmd, None, True)
                
        return r['dados']
    
    def load_menu_dashboard(self):
        """Busca e monta um menu com os dashboards disponiveis
            para o usuario.
        """
        

        cmd = """
                WITH t AS (
	                SELECT DISTINCT
		                d.id,
		                trim(d.nome_dashboard) as nome_dashboard,
		                trim(COALESCE(d.subtitulo,'')) as subtitulo,
		                trim(d.grupo) as grupo
	                FROM
		                bi_dashboards d
		                LEFT JOIN bi_dashboards_usuarios du
			                ON du.id_dashboard = d.id
	                WHERE 
		                du.id_usuario = %s	
		
                )
                , t1 AS (
	                SELECT grupo FROM t ORDER BY grupo LIMIT 1
                ) 
                , t2 AS (
	                WITH temp AS (
		                SELECT row_to_json(row) as j, grupo FROM (
			                SELECT 
				                id as id_item,
				                nome_dashboard as item,
				                grupo		
			                FROM 
				                t							
			                ) row
		                ORDER BY grupo, item
	                )
                SELECT json_agg(j) as sub_item, grupo FROM temp GROUP BY grupo
                )
                , t3 AS ( 
	                WITH temp AS (
		                SELECT  row_to_json(row) as menu FROM (
			                SELECT 
				                t2.sub_item,
				                t2.grupo,
    			                CASE 
					                WHEN t2.grupo = t1.grupo 
					                THEN 1 
					                ELSE 0 
				                END::integer as ativo
			                FROM 
				                t2, t1
			                ORDER BY 
				                t2.grupo
			                ) row 
		                ORDER BY grupo
	                )
                SELECT json_agg(menu) as menu FROM temp 
                )
                SELECT menu FROM t3 
        """ % self.user.id_usuario

        
        r = query_db(self.id_db, cmd, None, True)

        #Monta uma lista de id de dashboards

        for grupo in r['menu']:
            for i in grupo['sub_item']:
                self.dashboards.append(i['id_item'])

        self.menu = r['menu']
        session['menu'] = r['menu']
        
        return self.menu
    
    def load_empresa(self,empresa,ambient):
        
        cmd = "SELECT * FROM empresa WHERE codigo_empresa = '%s'" % (empresa)
        r   = query_db('softlog_' + ambient, cmd, None, True)
        self.reg_empresa = r
        return r

    def load_filial(self,empresa,filial,ambient):                
        cmd = "SELECT * FROM filial WHERE codigo_empresa = '%s' AND codigo_filial = '%s'" % (empresa, filial)
        r   = query_db('softlog_' + ambient, cmd, None, True)
        self.reg_filial = r
        return r
        
    def load_empresas(self,ambient):
        
        cmd = "SELECT * FROM empresa ORDER BY codigo_empresa"
        r   = query_db('softlog_' + ambient,cmd, None,False)
        self.empresas = r        
        return r

    def load_filiais(self,ambient): 
        if self.empresa is None:
            cmd = "SELECT * FROM filial ORDER BY codigo_empresa, codigo_filial"
        else:
            cmd = "SELECT * FROM filial WHERE codigo_empresa = '%s' ORDER BY codigo_empresa, codigo_filial" % self.empresa
        r   = query_db('softlog_' +ambient,cmd,None,False)
        self.filiais = r
        return r
            