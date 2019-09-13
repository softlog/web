from app import query_db_2, execute_db
import json
import psycopg2




class RegiaoCidadesModel(object):

    def get(self,id_acesso):

        str_sql = """
            WITH t AS (
                SELECT array_agg(row_to_json(row(id_cidade,nome_cidade,uf,cod_ibge,latitude,longitude,id_regiao)::t_api_regiao_cidades)) as cidades FROM (
	                SELECT 
		                c.id_cidade,
		                trim(c.nome_cidade) as nome_cidade,
		                c.uf,
		                trim(c.cod_ibge) as cod_ibge,
		                c.lat as latitude,
		                c.lng as longitude,
		                rc.id_regiao 
	                FROM 
		                regiao_cidades rc
		                LEFT JOIN cidades c
			                ON rc.id_cidade = c.id_cidade
                ORDER BY 
	            rc.id_cidade
                ) row
            )
            ,regioes AS (
                            WITH temp AS (
		                        SELECT row_to_json(row) as regioes FROM (
			                        SELECT
				                    regiao.id_regiao,
				                    regiao.descricao,
					            regiao.id_cidade_polo,
					            regiao.id_regiao_agrupadora
			                        FROM
				                    regiao
				                ORDER BY 
					            descricao
		                        ) as row
	                        ) 
	                        SELECT array_agg(regioes) as regioes FROM temp   
            )	
            SELECT row_to_json(row,true) as dados FROM (
	            SELECT 
		            regioes.regioes,
		            t.cidades
	            FROm
		            t,regioes
            ) row"""

        
        r = query_db_2(id_acesso,str_sql,None,True)
        
        ##print(str_sql)

        try:
            if r[0] is None:
                return None
        except:
            return None        

        return r[0]