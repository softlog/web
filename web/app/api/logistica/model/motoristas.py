from app import query_db, execute_db


class MotoristaModel(object):

    def get_motoristas(self,id_acesso):
        str_sql = """WITH motoristas AS (
	WITH temp AS (
		SELECT row_to_json(row, true) as motorista
		FROM (		
			SELECT 
				trim(fornecedores.cnpj_cpf) as cnpj_cpf, 
				fornecedores.id_fornecedor, 
				trim(fornecedores.nome_razao) as nome_motorista, 
				trim(fornecedores.iest) as inscricao_estadual, 
				0::integer as id_endereco,
				trim(fornecedores.endereco) as endereco, 
				trim(fornecedores.numero) as numero, 
				trim(fornecedores.bairro) as bairro, 
				trim(fornecedores.cep) as cep, 
				trim(nome_cidade) as cidade,
				trim(cidades.uf) as estado, 
				trim(cidades.codigo_pais) as codigo_pais,
				trim(fornecedores.ddd) as ddd, 
				trim(fornecedores.telefone1) as telefone, 
				fornecedores.id_cidade		
			FROM 
				fornecedores
				LEFT JOIN cidades ON cidades.id_cidade =  fornecedores.id_cidade
			WHERE
				tipo_motorista = 1
			ORDER BY 
				fornecedores.nome_razao
		) row
	) 
	SELECT array_agg(temp.motorista) as motoristas FROM temp
)
, cidades AS (
	WITH temp AS (
		SELECT row_to_json(row, true) as cidade
		FROM (		
			SELECT 
				cidades.id_cidade,						   
				trim(cidades.nome_cidade) as nome_cidade,
				cidades.uf,
				trim(cidades.cod_ibge) as cod_ibge,
				cidades.lat as latitude,
				cidades.lng as longitude
			FROM 
				fornecedores
				LEFT JOIN cidades ON cidades.id_cidade =  fornecedores.id_cidade
			WHERE
				tipo_motorista = 1
			GROUP BY 
				cidades.id_cidade
			ORDER BY 
				id_cidade
		) row
	) 
	SELECT array_agg(temp.cidade) as cidades FROM temp	
)
SELECT row_to_json(row,true) as dados FROM (
	SELECT 
		motoristas.motoristas,
		cidades.cidades
	FROm 
		motoristas,
		cidades
) row
	"""
        r = query_db(id_acesso,str_sql,None,True)

        ##print(str_sql)

        try:
            if r[0] is None:
                return None
        except:
            return None

        return r[0]