from app import query_db, execute_db

class NotasFiscaisModel(object):
    """description of class"""


    def get_nota_fiscal_by_protocolo(self, p_id_protocolo, id_acesso):

        str_sql = """WITH p AS (
	        SELECT 
	            id_nf_protocolo,
	            data_protocolo,
	            data_conferencia,
	            usuario_protocolo,
	            usuario_conferencia,
	            status
	        FROM 
	            scr_nf_protocolo 
	        WHERE
		        --id_nf_protocolo = 104050
                id_nf_protocolo = %i
        )
        , p_notas_fiscais AS (
	        SELECT 
                nf.id_nota_fiscal_imp,
		        p.id_nf_protocolo,				
                nf.id_ocorrencia,
		        nf.chave_nfe,
		        nf.numero_nota_fiscal,
		        nf.serie_nota_fiscal,
		        nf.remetente_id,
		        nf.destinatario_id,
		        nf.data_expedicao,
		        nf.data_emissao,
		        trim(d.nome_cliente) as destinatario_nome,
		        trim(d.cnpj_cpf) as destinatario_cnpj,				
                        trim(d.endereco) as endereco,
                        trim(d.numero) as numero,
                        trim(d.bairro) as bairro,
                        trim(d.cep) as cep,
                        trim(d.ddd) as ddd,
                        trim(d.telefone) as telefone,
                        d.id_cidade		
	        FROM
		        p
		        LEFT JOIN scr_nf_protocolo_nf nfp
			        ON nfp.id_nf_protocolo = p.id_nf_protocolo
		        LEFT JOIN scr_notas_fiscais_imp nf
			        ON nfp.id_nota_fiscal_imp = nf.id_nota_fiscal_imp
		        LEFT JOIN cliente r
			        ON r.codigo_cliente = nf.remetente_id
		        LEFT JOIN cliente d
			        ON d.codigo_cliente = nf.destinatario_id
	        WHERE 
		        1=1
		        --AND nf.id_romaneio IS NULL
        )
        , destinatarios AS (
            WITH temp AS (
	            SELECT row_to_json(row, true) as destinatarios FROM (
		            SELECT
			            destinatario_id,
			            destinatario_nome,
			            destinatario_cnpj,
			            endereco,
			            numero,
			            bairro,
			            cep,
			            ddd,
			            telefone,
			            id_cidade
		            FROM
			            p_notas_fiscais
		            WHERE 
			            destinatario_id IS NOT NULL
		            GROUP BY 
			            destinatario_id,
			            destinatario_nome,
			            destinatario_cnpj,
			            endereco,
			            numero,
			            bairro,
			            cep,
			            ddd,
			            telefone,
			            id_cidade
			    
	            ) as row
            ) 
            SELECT array_agg(destinatarios) as destinatarios FROM temp		
        )
        , notas_fiscais AS (
	        WITH temp AS (
	            SELECT row_to_json(row, true) as notas_fiscais FROM (
		        SELECT 
			        id_nf_protocolo,
                    id_nota_fiscal_imp,
			        chave_nfe,
			        numero_nota_fiscal,
			        serie_nota_fiscal,
			        data_emissao,
			        data_expedicao,
			        remetente_id,
			        destinatario_id,
                    id_ocorrencia
		        FROM
			        p_notas_fiscais
		        ) row
	        )
	        SELECT array_agg(notas_fiscais) as notas_fiscais FROM temp
        )
        , cidades AS (
	        WITH temp AS (
		        SELECT row_to_json(row,true) as cidades FROM (
			        SELECT 
				        id_cidade,
				        trim(nome_cidade) as nome_cidade,
				        uf,
				        trim(cod_ibge) as cod_ibge,
				        COALESCE(lat,0.0) as latitude,
				        COALESCE(lng,0.0) as longitude
			        FROM 
				        cidades
			        WHERE
				        EXISTS (SELECT 1
					        FROM p_notas_fiscais
					        WHERE p_notas_fiscais.id_cidade = cidades.id_cidade)
		        ) row
	        )
	        SELECT array_agg(cidades) as cidades FROM temp
        )
        SELECT row_to_json(row,true) as dados FROM (
	        SELECT 
		        destinatarios.destinatarios,
		        cidades.cidades,
		        notas_fiscais.notas_fiscais
	        FROM 
		        destinatarios,
		        cidades,
		        notas_fiscais
        ) row""" % (p_id_protocolo)

        r = query_db(id_acesso,str_sql,None,True)

        ##print(str_sql)

        try:
            if r[0] is None:
                return None
        except:
            return None

        return r[0]