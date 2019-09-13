from app import query_db, execute_db


class VeiculosModel(object):

    def get_veiculos(self,id_acesso):

        str_sql = """WITH veiculos AS (
	WITH temp AS (
		SELECT row_to_json(row,true) as veiculos FROM (
			SELECT 
				trim(placa_veiculo) as placa_veiculo, 
				(COALESCE(trim(nome_marca),'') || ' - ' || COALESCE(trim(descricao_modelo),'')) as descricao 				
			FROM 
				v_veiculos
			ORDER BY 
				placa_veiculo
		) row
	) 
	SELECT array_agg(veiculos) as veiculos FROM temp
)
SELECT row_to_json(v) as veiculos FROM veiculos v"""

        r = query_db(id_acesso,str_sql,None,True)

        ##print(str_sql)

        try:
            if r[0] is None:
                return None
        except:
            return None

        return r[0]