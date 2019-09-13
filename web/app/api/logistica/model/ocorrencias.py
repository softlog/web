from app import query_db, execute_db
import json
import traceback


class Ocorrencias(object):

    def getOcorrencias(id_acesso):

        str_sql = """WITH t AS (
	                    WITH temp AS (
		                    SELECT row_to_json(row) as dados FROM (
			                    SELECT 
				                    codigo_edi as id_ocorrencia,
				                    trim(ocorrencia) as ocorrencia,
                                    pendencia, 
                                    aplicativo_mobile,
                                    aplicativo_sconferencia
			                    FROM 
				                    scr_ocorrencia_edi 
			                    WHERE 
				                    ocorrencia_coleta = 0 
			                    ORDER BY codigo_edi
		                    ) row		
	                    )
	                    SELECT 
		                    array_agg(temp.dados) as ocorrencias
	                    FROM 
		                    temp
                    )
                    SELECT row_to_json(t) FROM t
            """

        r = query_db(id_acesso,str_sql,None,True)

        return r[0]

    def setOcorrencias(codigo_acesso, ocorrencias):
       # print(conferencias);
       
        dados = json.loads(ocorrencias)
        if len(dados) == 0:
            return None

        comandos = []
        
        for o in dados:
            d = {
                    'id': o['id'],                    
                    'id_ocorrencia': o['id_ocorrencia'],
                    'data_registro': o['data_registro'],
                    'data_ocorrencia': o['data_ocorrencia'] + " " + o['hora_ocorrencia'] + ':00',
                    'nome_recebedor': 'NAO INFORMADO' if o.get('nome_recebedor') == '' else o.get('nome_recebedor'),
                    'documento_recebedor': 'NAO INFORMADO' if o.get('documento_recebedor') == '' else o.get('documento_recebedor'),
                    'observacao': "NULL" if o.get('observacao') is None else "'" + o.get('observacao') + "'",
                    'latitude': "NULL" if o.get('latitude') is None else "'"  + o.get('latitude') + "'",
                    'longitude': "NULL" if o.get('longitude') is None else "'" + o.get('longitude') + "'",
                    'chave_nfe': o['chave_nfe'],
                    'numero_nota_fiscal': o['numero_nota_fiscal'],
                    'serie_nota_fiscal': o['serie_nota_fiscal'],
                    'remetente_cnpj': o['remetente_cnpj'],
                    'id_nota_fiscal_imp': "NULL" if o.get('id_nota_fiscal_imp') is None else str(o.get('id_nota_fiscal_imp')),
                    'id_romaneio': "NULL" if o.get('id_romaneio') is None else o.get('id_romaneio'),
                    'url_imagem': "NULL" if o.get('url_imagem') is None else "'" + o.get('url_imagem') + "'",
                    'id_conhecimento_notas_fiscais': "NULL" if o.get('id_conhecimento_notas_fiscais') is None else str(o.get('id_conhecimento_notas_fiscais')),
                    'id_conhecimento': "NULL" if o.get('id_conhecimento') is None else str(o.get('id_conhecimento'))
               }
        
            print(d)    
            sql_ocorrencia = """INSERT INTO edi_ocorrencias_entrega (
                    servico_integracao,
                    numero_nfe,
                    serie_nfe,
                    cnpj_emitente,                    
                    chave_nfe,
                    numero_ocorrencia,
                    data_ocorrencia,
                    recebedor,
                    doc_recebedor,
                    id_nota_fiscal_imp,
                    id_romaneio,
                    id_ocorrencia_app,
                    latitude,
                    longitude,
                    observacao,
                    url_imagem,
                    id_conhecimento,
                    id_conhecimento_notas_fiscais
                ) VALUES (         
                    2,
                    '%(numero_nota_fiscal)s',
                    '%(serie_nota_fiscal)s',
                    '%(remetente_cnpj)s',
                    '%(chave_nfe)s',
                    %(id_ocorrencia)i,
                    '%(data_ocorrencia)s',
                    '%(nome_recebedor)s',
                    '%(documento_recebedor)s',
                    %(id_nota_fiscal_imp)s,
                    %(id_romaneio)i,
                    %(id)i,
                    %(latitude)s,
                    %(longitude)s,
                    %(observacao)s,
                    %(url_imagem)s,
                    %(id_conhecimento)s,
                    %(id_conhecimento_notas_fiscais)s
                )""" % (d)

            comandos.append(sql_ocorrencia)

        sql = ';'.join(comandos)        
        try:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
        except:    
            
            print(traceback.format_exc())        
            return None
        
        return comandos

