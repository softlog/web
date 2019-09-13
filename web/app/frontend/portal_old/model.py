import json
import traceback
from app import query_db, execute_db, app

class Rastreamento(object):
 
    def get_01(self, id_db, id_doc):
        
        dados = {"id_doc":id_doc}

        sql_str = """
        WITH situacao AS (
	        WITH temp AS (
		        SELECT row_to_json(row,true) as situacoes FROM (
			        SELECT 				
				        evento,
				        unidade,
				        to_char(data,'DD/MM/YYYY HH24:MI') as data,
				        detalhes,
				        usuario,
				        id
			        FROM 
				        f_situacao_nota_fiscal_imp(%(id_doc)i,0)
		        ) row
	        )
	        SELECT array_agg(temp.situacoes) as situacoes FROM temp
        ) 
        , geral AS (
	        SELECT 		
		        nf.serie_nota_fiscal,
		        nf.numero_nota_fiscal,
		        nf.chave_nfe,
		        r.nome_cliente as remetente_nome,
		        d.nome_cliente as destinatario_nome,
		        trim(c.nome_cidade) || '-' || (c.uf) as destino,
                img.url_imagem,
                trim(filial.razao_social) as transportadora
	        FROM
		        scr_notas_fiscais_imp nf
		        LEFT JOIN cliente r
			        ON r.codigo_cliente = nf.remetente_id
		        LEFT JOIN cliente d
			        ON d.codigo_cliente = nf.destinatario_id
		        LEFT JOIN cidades c
			        ON nf.calculado_ate_id_cidade = c.id_cidade
                LEFT JOIN edi_ocorrencias_entrega img
				    ON img.id_nota_fiscal_imp = nf.id_nota_fiscal_imp
                LEFT JOIN filial
				    ON filial.codigo_filial = nf.filial_emitente 
					    AND filial.codigo_empresa = nf.empresa_emitente
	        WHERE 	
		        nf.id_nota_fiscal_imp = %(id_doc)i 
        )
        SELECT row_to_json(row, true) as dados FROM (
	        SELECT 
		        serie_nota_fiscal,
		        numero_nota_fiscal,
		        chave_nfe,
		        remetente_nome,
		        destinatario_nome,
		        destino,
                url_imagem as imagem,
                transportadora,
		        situacao.situacoes as situacoes
	        FROM 
		        geral,
		        situacao
        ) row
        """ % dados
         
        try:
            r = query_db(id_db,sql_str,None,True)
            #app.logger.info(sql_str)
        except:            
            r = None
            #app.logger.error(traceback.format_exc())             

        if r is None:
            return None

        return r[0]

    def get_02(self, id_db, chave_doc):
        
        sql_chave = """SELECT 
                            id_nota_fiscal_imp, 
                            chave,
                            ident_sistema                            
                        FROM scr_notas_fiscais_imp nf
                            LEFT JOIN scr_nfe_rastreamentos r
                                ON r.chave = nf.chave_nfe
                        WHERE chave_nfe = '%s'
                        ORDER BY nf.data_registro
                    """ % chave_doc


        try:
            r = query_db(id_db,sql_chave,None,True)
        except:            
            r = None
            #app.logger.error(traceback.format_exc())             
        
        if r is not None:
            if r['chave'] is None:
                #print(a)
                return self.get_01(id_db,r['id_nota_fiscal_imp'])
                
            if r['ident_sistema'] == 0:
                return self.get_01(id_db,r['id_nota_fiscal_imp'])

        dados = {"id_doc":chave_doc}

        

        sql_str = """
        WITH situacao AS (
	        WITH temp AS (
		        SELECT row_to_json(row,true) as situacoes, form FROM (
			        SELECT 				
				        evento,
				        unidade,
				        to_char(data,'DD/MM/YYYY HH24:MI') as data,
				        detalhes,
				        usuario,
                        form,
				        id
			        FROM 
				        --f_situacao_nota_fiscal_imp('%(id_doc)s')
				        f_situacao_nota_fiscal_imp('%(id_doc)s')
		        ) row
	        )
	        SELECT array_agg(temp.situacoes) as situacoes, max(form) as imagem FROM temp
        )
        ,geral AS (
		SELECT
			COALESCE(trim(nf.remetente_nome),trim(cliente.nome_cliente)) as remetente_nome,
			COALESCE(trim(nf.destinatario_nome), 'A CONFIRMAR') as destinatario_nome,
			trim(f.razao_social) as transportadora_nome,
			remetente_id,
			destinatario_id,
			chave as chave_nfe,
			substr(chave,26,9) as numero_nota_fiscal,
			substr(chave,23,3) as serie_nota_fiscal,
			CASE WHEN cidades.id_cidade IS NOT NULL THEN 
				(initcap(lower(trim(cidades.nome_cidade))) || '-' || cidades.uf)
			ELSE 
				'A CONFIRMAR'
			END as destino,
            trim(filial.razao_social) as transportadora
		FROM
			scr_nfe_rastreamentos rast
			LEFT JOIN v_mgr_notas_fiscais nf
				ON nf.chave_nfe = rast.chave
			LEFT JOIN cliente
				ON cliente.cnpj_cpf = substr(chave,7,14)
			LEFT JOIN filial f
				ON f.codigo_filial = COALESCE(nf.empresa_emitente,'001')
					AND f.codigo_empresa = COALESCE(nf.empresa_emitente,'001')
			LEFT JOIN cidades
				ON f.id_cidade = cidades.id_cidade
            LEFT JOIN filial
				    ON filial.codigo_filial = nf.filial_emitente 
					    AND filial.codigo_empresa = nf.empresa_emitente
		WHERE 
			chave = '%(id_doc)s'
        )
        SELECT row_to_json(row, true) as dados FROM (
	        SELECT 
		        serie_nota_fiscal,
		        numero_nota_fiscal,
		        chave_nfe,
		        remetente_nome,
		        destinatario_nome,
		        destino,
		        situacao.situacoes as situacoes,
                situacao.imagem,
                transportadora
	        FROM 
		        geral,
		        situacao
        ) row
        """ % dados
         
        try:
            r = query_db(id_db,sql_str,None,True)
            app.logger.info(sql_str)
        except:            
            r = None
            app.logger.error(traceback.format_exc())             

        if r is None:
            return None

        return r[0]        
        #return dados