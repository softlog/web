from app import query_db, execute_db
import json
import traceback
from app import util


class Usuarios(object):

    def get_user(user, id_acesso):
        """Retorna dados do usuario em formato Json"""
        
        sql = """SELECT row_to_json(row) as resultado FROM 
	            (SELECT 
		            id_usuario,
		            trim(nome_usuario) as nome_usuario,
		            trim(email) as email,
		            trim(senha) as senha,
		            trim(login_name) as login_name
	            FROM 
		            usuarios
	            WHERE 
		            usuarios.login_name = '%s'
	            ) row""" % (user)

        r = query_db(id_acesso,sql,None,True)

        if r is None:
            return None

        return r['resultado']

    def get_user_fornecedor(cpf,id_acesso):
        sql = """SELECT row_to_json(row) as resultado FROM 
            (SELECT 
	            id_fornecedor as id_usuario,
	            trim(nome_razao) as nome_usuario,
	            trim(email) as email,
	            '123456' senha,
	            trim(cnpj_cpf) as cnpj_cpf,
	            trim(nome_razao) as login_name
            FROM 
	            fornecedores
            WHERE 
	            fornecedores.cnpj_cpf = '%s'
            ) row""" % cpf

        r = query_db(id_acesso,sql,None,True)

        if r is None:
            return None

        return r['resultado']


class Protocolos(object):

    def get_protocolo(data_expedicao,ultimo_id, id_acesso):
        """Retorna dados do usuario em formato Json"""
        if ultimo_id == 0:
            arg_ultimo_id = "NULL"
        else:
            arg_ultimo_id = str(ultimo_id)

        sql = """WITH p AS (
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
		            CAST(data_protocolo - INTERVAL'8 hours' as date) = '%s'
                    AND CASE WHEN %s IS NULL THEN true ELSE id_nf_protocolo > %s END                                
            )
	        , p_remetentes AS (
		        SELECT 
			        p.id_nf_protocolo,
			        nf.remetente_id,
			        trim(r.nome_cliente) as remetente_nome,
			        trim(r.cnpj_cpf) as remetente_cnpj,
			        COUNT(*) as qt_nf,
			        SUM(volume_presumido::integer) as qtd_volumes
		        FROM
			        p
			        LEFT JOIN scr_nf_protocolo_nf nfp
				        ON nfp.id_nf_protocolo = p.id_nf_protocolo
			        LEFT JOIN scr_notas_fiscais_imp nf
				        ON nfp.id_nota_fiscal_imp = nf.id_nota_fiscal_imp
			        LEFT JOIN cliente r
				        ON r.codigo_cliente = nf.remetente_id		
		        GROUP BY 
			        p.id_nf_protocolo,
			        nf.remetente_id,
			        r.nome_cliente,
			        r.cnpj_cpf
		
	        )
	        , p_setor AS (
	            SELECT 		    
			        t.id_nf_protocolo_setor,
			        t.id_nf_protocolo,
			        t.id_setor,
			        t.qtd_volumes,
			        t.qtd_conferencia, 
			        t.id_usuario_conferencia,
			        to_char(t.data_conferencia,'YYYY-MM-DD HH24:MI:SS') as data_conferencia,
			        t.qtd_notas,
		            u1.nome_usuario usuario_protocolo
	            FROM
		            p
		            LEFT JOIN scr_nf_protocolo_setor t
			            ON t.id_nf_protocolo = p.id_nf_protocolo
		            LEFT JOIN usuarios u1 
			            ON u1.id_usuario = usuario_protocolo	
	        )
	        , remetentes AS (
	            WITH temp AS (
		            SELECT row_to_json(row) as remetentes FROM (
			            SELECT
				            remetente_id,
				            remetente_nome,
				            remetente_cnpj
			            FROM
				            p_remetentes
		                    WHERE 
				            remetente_id IS NOT NULL
			            GROUP BY 
				            remetente_id,
				            remetente_nome,
				            remetente_cnpj		
		            ) as row
	            ) 
	            SELECT array_agg(remetentes) as remetentes FROM temp		
	        )
	        , setores AS (
	            WITH temp AS (

		            SELECT row_to_json(row) as setores FROM (
			            SELECT
				            id_regiao,
				            descricao
			            FROM
				            p_setor
				            LEFT JOIN regiao
					            ON regiao.id_regiao = p_setor.id_setor
			            GROUP BY 
				            id_regiao
		
		            ) as row
	            ) 
	            SELECT array_agg(setores) as setores FROM temp
	        )
	        , usuarios AS (
	            WITH temp AS (

		            SELECT row_to_json(row) as usuarios FROM (
			            SELECT
				            id_usuario,
				            nome_usuario
			            FROM
				            p
				            LEFT JOIN usuarios
					            ON usuarios.id_usuario = p.usuario_conferencia
		        WHERE
		            p.usuario_conferencia IS NOT NULL
			            GROUP BY 
				            id_usuario,
		            nome_usuario
		        UNION 
			            SELECT
				            id_usuario,
				            nome_usuario
			            FROM
				            p
				            LEFT JOIN usuarios
					            ON usuarios.id_usuario = p.usuario_protocolo
		        WHERE 
		            p.usuario_protocolo IS NOT NULL
			            GROUP BY 
				            id_usuario,
		            nome_usuario
		            ) as row
	            ) 
	            SELECT array_agg(usuarios) as usuarios FROM temp
	        ) 
	        , bloco_remetentes AS (
	            WITH temp AS (
		            SELECT 
			        row_to_json(row) as itens, id_nf_protocolo FROM (
			            SELECT 
				            id_nf_protocolo,
				            remetente_id,
				            qt_nf,
				            qtd_volumes
			            FROM 
				            p_remetentes
			            WHERE 
				            remetente_id IS NOT NULL
			            ORDER BY 
				            p_remetentes.remetente_nome
		            ) row
		        )
	            SELECT array_agg(itens) as remetentes, id_nf_protocolo 
	            FROM temp
	            GROUP BY id_nf_protocolo
	        )
	        , bloco_p_setor AS (
	            WITH temp AS (
		            SELECT 	row_to_json(row) as itens, id_nf_protocolo FROM (
			            SELECT 
				            p_setor.*,
				            bloco_remetentes.remetentes
			            FROM 
				            p_setor
				            LEFT JOIN bloco_remetentes 
					        ON bloco_remetentes.id_nf_protocolo = p_setor.id_nf_protocolo
		                    WHERE 
				           bloco_remetentes.id_nf_protocolo IS NOT NULL
			            ORDER BY 
				            p_setor.id_nf_protocolo_setor
		            ) row
	            ) 
	            SELECT array_agg(itens) as itens, id_nf_protocolo 
	            FROM temp
	            GROUP BY id_nf_protocolo
	        )
	        , protocolos AS (
	            WITH temp AS (
		            SELECT row_to_json(row) as protocolos FROM (
			            SELECT 
				            p.id_nf_protocolo,
				            to_char(p.data_protocolo,'YYYY-MM-DD HH24:MI:SS') as data_protocolo,
				            to_char(p.data_conferencia,'YYYY-MM-DD HH24:MI:SS') as data_conferencia,
				            p.usuario_protocolo,
				            p.usuario_conferencia,
				            p.status,
		            to_char(p.data_protocolo-INTERVAL'8 hours','YYYY-MM-DD') as data_expedicao,
				            bloco_p_setor.itens as protocolo_setores
			            FROM 
				            p
				            LEFT JOIN bloco_p_setor
					            ON bloco_p_setor.id_nf_protocolo = p.id_nf_protocolo
		                    WHERE 
				        bloco_p_setor.id_nf_protocolo IS NOT NULL
		            ) row
		
	            )
	            SELECT array_agg(protocolos) as protocolos
	            FROM temp

	        )
	        SELECT row_to_json(row) as dados FROM (
		            SELECT
			        protocolos.protocolos,
			        setores.setores,
			        usuarios.usuarios,
			        remetentes.remetentes
		            FROM
			            protocolos,setores, usuarios, remetentes
	        ) row
            """ % (data_expedicao,arg_ultimo_id, arg_ultimo_id)

        

        r = query_db(id_acesso,sql,None,True)

        if r[0]['protocolos'] is None:
            return None

        return r[0]

    def setConferenciaProtocolo(codigo_acesso, conferencias):

       # print(conferencias);
       
        dados = json.loads(conferencias)
        if len(dados) == 0:
            return None

        comandos = []
        for protocolo in dados:
            
            observacao = protocolo.get("observacao")

            if observacao is None:
                #print("Obversavao vazia")
                observacao = "NULL"
            else:
                observacao = "'" + observacao + "'"
                #print("Observacao ",observacao)

            sql_protocolo = """UPDATE scr_nf_protocolo SET 
                                data_conferencia = '%s',
                                usuario_conferencia = %i,
                                status = 1,
                                observacao = %s
                         WHERE 
                                id_nf_protocolo = %i
                        """ % (protocolo['data_conferencia'],
                               protocolo['id_usuario_conferencia'],                               
                               observacao,
                               protocolo['id_protocolo_nf']
                               )


            comandos.append(sql_protocolo)
            for setor in protocolo['setores']:
                sql_setores = """UPDATE scr_nf_protocolo_setor SET
                                    data_conferencia = '%s',
                                    id_usuario_conferencia = %i,
                                    qtd_conferencia = %i
                                WHERE id_nf_protocolo = %i AND
                                    id_setor = %i
                        """ % (protocolo['data_conferencia'],
                               protocolo['id_usuario_conferencia'],
                               setor['qtd_conferencia'],
                               protocolo['id_protocolo_nf'],
                               setor['id_regiao'])
                comandos.append(sql_setores)

        sql = ';'.join(comandos)
        print(sql)
        try:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
        except:
            return None
        
        return comandos


class Romaneios(object):
    
    def get_romaneios(cpf_motorista, data, id_acesso):



        str_sql = """WITH rom AS (
		                SELECT 
			                r.id_romaneio,
			                r.numero_romaneio,
			                to_char(r.data_romaneio,'YYYY-MM-DD HH24:MI:SS') as data_romaneio,
                            CAST(r.data_romaneio - INTERVAL'11 hours' as date) as data_expedicao,
			                to_char(r.data_saida,'YYYY-MM-DD HH24:MI:SS') as data_saida,
			                to_char(r.data_chegada, 'YYYY-MM-DD HH24:MI:SS') as data_chegada,
			                r.placa_veiculo,
			                r.id_motorista,
			                mot.cnpj_cpf as motorista_cpf,
			                mot.id_cidade as motorista_id_cidade,
			                r.id_transportador_redespacho,
			                red.cnpj_cpf as redespachador_cpf,
			                red.id_cidade as redespacho_id_cidade,
			                r.id_origem
                            
		                FROM 
			                scr_romaneios r
			                LEFT JOIN fornecedores mot
				                ON mot.id_fornecedor = r.id_motorista
			                LEFT JOIN fornecedores red
				                ON red.id_fornecedor = r.id_transportador_redespacho
		                WHERE
                            CASE WHEN current_database() IN ('softlog_medilog','softlog_medilog2') THEN 
                                    CAST(data_romaneio - INTERVAL'11 hours' as date) = '%s'
                                ELSE 
                                    CAST(data_romaneio - INTERVAL'4 hours' as date) = '%s'
                            END
			                AND mot.cnpj_cpf = '%s'
                            AND emitido = 1
	                )
	                , documentos AS (
		                SELECT 
			                rnf.id_romaneio_nf as numero_parada,
			                nf.id_nota_fiscal_imp,
			                rnf.id_romaneio,	
			                trim(to_char(nf.data_emissao,'YYYY-MM-DD')) as data_emissao,
			                trim(to_char(nf.data_expedicao,'YYYY-MM-DD')) as data_expedicao,
			                trim(nf.serie_nota_fiscal) as serie,
			                trim(nf.numero_nota_fiscal) as numero_nota_fiscal,
			                nf.chave_nfe,
			                nf.valor,					
			                nf.peso_presumido as peso,
			                nf.peso_liquido,
                            nf.id_ocorrencia,
                            to_char(nf.data_ocorrencia,'YYYY-MM-DD HH24:MI:SS') as data_ocorrencia,
			                nf.volume_presumido as volume,
			                rem.codigo_cliente as remetente_id,
			                rem.cnpj_cpf::bigint as remetente_cnpj,
			                rem.id_cidade as remetente_id_cidade,
			                dest.codigo_cliente as destinatario_id,
			                dest.cnpj_cpf::bigint as destinatario_cnpj,
			                dest.id_cidade as destinatario_id_cidade,
                            null::integer as id_conhecimento_notas_fiscais,
                            nf.id_conhecimento
		                FROM
			                rom r
			                LEFT JOIN scr_romaneio_nf rnf
				                ON r.id_romaneio = rnf.id_romaneio
			                LEFT JOIN scr_notas_fiscais_imp nf
				                ON nf.id_nota_fiscal_imp = rnf.id_nota_fiscal_imp
			                LEFT JOIN cliente rem
				                ON rem.codigo_cliente = nf.remetente_id
			                LEFT JOIN cliente dest 
				                ON dest.codigo_cliente = nf.destinatario_id
			                LEFT JOIN cidades cd
				                ON cd.id_cidade = dest.id_cidade
			                LEFT JOIN rom
				                ON rnf.id_romaneio = rom.id_romaneio		
                      	WHERE 
                    		nf.id_nota_fiscal_imp IS NOT NULL
                        UNION 				
				SELECT 
					ce.id_conhecimento_entrega as numero_parada,
			                nf.id_nota_fiscal_imp,			                
			                r.id_romaneio,
			                trim(to_char(nf.data_nota_fiscal,'YYYY-MM-DD')) as data_emissao,
			                trim(to_char(nf.data_nota_fiscal,'YYYY-MM-DD')) as data_expedicao,
			                trim(nf.serie_nota_fiscal) as serie,
			                trim(nf.numero_nota_fiscal) as numero_nota_fiscal,
			                nf.chave_nfe,
			                nf.valor,					
			                nf.peso as peso,
			                nf.peso_liquido,
					nf.id_ocorrencia,
					to_char(f_data_entrega(nf.data_ocorrencia, nf.hora_ocorrencia),'YYYY-MM-DD HH24:MI:SS') as data_ocorrencia,
			                nf.qtd_volumes as volume,
			                rem.codigo_cliente as remetente_id,
			                rem.cnpj_cpf::bigint as remetente_cnpj,
			                rem.id_cidade as remetente_id_cidade,
			                dest.codigo_cliente as destinatario_id,
			                dest.cnpj_cpf::bigint as destinatario_cnpj,
			                dest.id_cidade as destinatario_id_cidade,
			                nf.id_conhecimento_notas_fiscais,
                            nf.id_conhecimento
		                FROM
			                rom r			                
			                LEFT JOIN scr_conhecimento_entrega ce
						ON ce.id_romaneios = r.id_romaneio
			                LEFT JOIN scr_conhecimento c
						ON c.id_conhecimento = ce.id_conhecimento
					LEFT JOIN scr_conhecimento_notas_fiscais nf
						ON c.id_conhecimento = nf.id_conhecimento					
			                LEFT JOIN cliente rem
				                ON rem.codigo_cliente = c.remetente_id
			                LEFT JOIN cliente dest 
				                ON dest.codigo_cliente = c.destinatario_id
			                LEFT JOIN cidades cd
				                ON cd.id_cidade = dest.id_cidade			                
				WHERE 
					nf.id_conhecimento_notas_fiscais IS NOT NULL)                    
	                 
                    , qt_docs as (SELECT count(*) as qt FROM documentos)
                    , cidades2 AS (
		                SELECT 
			                id_cidade,
			                nome_cidade,
			                uf,
                            cod_ibge
		                FROM
			                documentos
			                LEFT JOIN cidades
				                ON cidades.id_cidade = remetente_id_cidade
		                UNION 
		                SELECT 
			                id_cidade,
			                nome_cidade,
			                uf,
                            cod_ibge
		                FROM
			                documentos
			                LEFT JOIN cidades
				                ON cidades.id_cidade = destinatario_id_cidade
		                UNION 
		                SELECT 
			                id_cidade,
			                nome_cidade,
			                uf,
                            cod_ibge
		                FROM 
			                rom
			                LEFT JOIN cidades
				                ON cidades.id_cidade = rom.motorista_id_cidade
		                UNION 
		                SELECT
			                id_cidade,
			                nome_cidade,
			                uf,
                            cod_ibge
		                FROM 
			                rom 
			                LEFT JOIN cidades
				                ON cidades.id_cidade = rom.redespacho_id_cidade
		                WHERE
			                cidades.id_cidade IS NOT NULL 
	                )
	                , pessoas_1 AS (
		                WITH t AS (
			                SELECT 
				                trim(nome_cliente) as nome,
				                trim(cnpj_cpf) as cnpj_cpf,
                                CASE WHEN end_complemento IS NOT NULL THEN 
				                        trim(endereco) || ', ' || trim(end_complemento) 
                                    ELSE 
                                        trim(endereco)
                                END as endereco,
				                trim(numero) as numero,
				                trim(cliente.bairro) as bairro,
				                id_cidade, 
				                cliente.cep,
				                (cliente.ddd || ' ' || telefone) as telefone,
                                latitude,
                                longitude
			                FROM
				                documentos
				                LEFT JOIN cliente 
					                ON cliente.codigo_cliente = documentos.remetente_id
				
			                UNION
			                SELECT 
				                trim(nome_cliente) as nome,
				                trim(cnpj_cpf) as cnpj_cpf,
				                CASE WHEN end_complemento IS NOT NULL THEN 
				                        trim(endereco) || ', ' || trim(end_complemento) 
                                    ELSE 
                                        trim(endereco)
                                END as endereco,
				                trim(numero) as numero,
				                trim(cliente.bairro) as bairro,
				                id_cidade,
				                cliente.cep,
				                (cliente.ddd || ' ' || telefone) as telefone,
                                latitude,
                                longitude

			                FROM
				                documentos
				                LEFT JOIN cliente 
					                ON cliente.codigo_cliente = documentos.destinatario_id
			                UNION 
			                SELECT 
				                trim(nome_razao) as nome,
				                trim(cnpj_cpf) as cnpj_cpf,
				                trim(endereco) as endereco,
				                trim(numero) as numero,
				                trim(fornecedores.bairro) as bairro,
				                id_cidade,
				                fornecedores.cep,
				                (fornecedores.ddd || ' ' || telefone1) as telefone,
                                null::double precision as latitude,
                                null::double precision as longitude
			                FROM
				                rom
				                LEFT JOIN fornecedores
					                ON fornecedores.id_fornecedor = rom.id_motorista
			                UNION 
			                SELECT 
				                trim(nome_razao) as nome,
				                trim(cnpj_cpf) as cnpj_cpf,
				                trim(endereco) as endereco,
				                trim(numero) as numero,
				                trim(fornecedores.bairro) as bairro,
				                id_cidade,
				                fornecedores.cep,
				                (fornecedores.ddd || ' ' || telefone1) as telefone,
                                null::double precision as latitude,
                                null::double precision as longitude
			                FROM
				                rom
				                LEFT JOIN fornecedores
					                ON fornecedores.id_fornecedor = rom.id_transportador_redespacho
			                WHERE
				                fornecedores.id_fornecedor IS NOT NULL
		                )
		                SELECT 
			                trim(t.nome) as nome,
			                t.cnpj_cpf,
			                t.endereco,
			                t.numero,
			                t.bairro,
			                t.id_cidade,
			                t.cep,
			                t.telefone,
                            t.latitude,
                            t.longitude
		                FROM 
			                t					
	                )
	                , cep1 as (
		                SELECT 
			                pessoas_1.cep,
			                cep.latitude,
			                cep.longitude
		                FROM 
			                pessoas_1
			                LEFT JOIN cep
				                ON cep.cep = pessoas_1.cep
		                GROUP BY
			                1,2,3
	                )
	                , pessoas_2 as (
		                SELECT 
			                p.nome,
			                p.cnpj_cpf,
			                p.endereco,
			                p.numero,
			                p.bairro,
			                p.id_cidade,
			                p.cep,
			                p.telefone,
			                COALESCE(p.longitude::text, cep1.longitude::text) as longitude,
			                COALESCE(p.latitude::text, cep1.latitude::text) as latitude,
                            CASE WHEN p.latitude IS NULL THEN 1 ELSE 0 END::integer as verificar
		                FROM 
			                pessoas_1 p
			                LEFT JOIN cep1 
				                ON cep1.cep = p.cep	
	                )
	                , veiculos_1 AS (
		                SELECT 
			                placa_veiculo as placa_veiculo,
			                placa_veiculo as descricao
		                FROM 
			                rom
		                GROUP BY 
			                rom.placa_veiculo
	                )
	                , pessoas AS (
		                WITH temp AS (
			                SELECT (row_to_json(row,true))::json as json FROM (
				                SELECT 
					                *
				                FROM
					                pessoas_2				
			                ) row
		                )
		                SELECT array_agg(json) as pessoas FROM temp 
	                )
	                , veiculos AS (
		                WITH temp AS (
			                SELECT (row_to_json(row,true))::json as json FROM (
				                SELECT 
					                *
				                FROM
					                veiculos_1		
			                ) row
		                )
		                SELECT array_agg(json) as veiculo FROM temp 
	                )
	                , cidades AS (
		                WITH temp AS (
			                SELECT (row_to_json(row,true))::json as json FROM (
				                SELECT 
					                id_cidade, 
                                    trim(nome_cidade) as nome_cidade,
                                    uf,
                                    cod_ibge
				                FROM
					                cidades2
			                ) row
		                )
		                SELECT array_agg(json) as cidades FROM temp 
	                )		
	                , docs AS (		
		                WITH temp AS (
			                SELECT (row_to_json(row,true))::json as json, id_romaneio FROM (
				                SELECT 
					                *
				                FROM
					                documentos
				                ORDER BY
					                id_romaneio, numero_nota_fiscal
			                ) row
		                )
		                SELECT id_romaneio, array_agg(json) as lista_docs FROM temp GROUP BY id_romaneio
	                )	
	                , romaneios AS (
		                WITH temp AS (
				                SELECT (row_to_json(row,true))::json as json FROM (
					                SELECT 
						                rom.*,
						                docs.lista_docs as documentos
					                FROM 
						                rom
						                LEFT JOIN docs
							                ON docs.id_romaneio = rom.id_romaneio
                                    ORDER BY rom.id_romaneio
				                ) row
			                )
			                SELECT array_agg(json) as romaneio FROM temp 
	                )
	                SELECT row_to_json(row, true) as json 
	                FROM 
	                (
		                SELECT 
			                romaneios.romaneio as romaneios,
			                pessoas.pessoas,
			                cidades.cidades,
			                veiculos.veiculo
		                FROM 
			                romaneios,
			                pessoas,
			                cidades,
			                veiculos,
                            qt_docs
                        WHERE 
                            qt_docs.qt > 0
	                ) row;""" % (data, data, cpf_motorista)


        r = query_db(id_acesso,str_sql,None,True)

        #print(str_sql)

        if r is None:
            return None        
        try:
            if r[0]['romaneios'] is None:
                return None
        except:
            return None

        cidades = {}
        for c in r[0]['cidades']:
            cidades[str(c['id_cidade'])] = c['nome_cidade'] + ', ' + c['uf']

        for p in r[0]['pessoas']:
            if p['verificar'] == 1:
                #Chama rotina que tenta encontrar coordenadas
                location = util.get_location(p['endereco'], p['bairro'],cidades[str(p['id_cidade'])],p['cep'],p['nome'])
                print(location)
                if location is not None:
                    p['longitude'] = location[0]
                    p['latitude'] = location[1]
                    p['geolocation'] = True

                    str_update = """"UPDATE cliente 
                        SET longitude = '%s', latitude = '%s' 
                        WHERE cnpj_cpf = '%s' AND latitude IS NULL""" % (location[0],location[1],p['cnpj_cpf'])
                    
                    execute_db(id_acesso,str_update)


        return r[0]

class Ocorrencias(object):


    def getOcorrencias(id_acesso):

        str_sql = """WITH t AS (
	                    WITH temp AS (
		                    SELECT row_to_json(row) as dados FROM (
			                    SELECT 
				                    codigo_edi as id_ocorrencia,
				                    trim(ocorrencia) as ocorrencia,
                                    pendencia
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


class Imagens(object):

    def getImagem(codigo_acesso, imagem):

        sql_img = """
            SELECT 
                arquivo 
            FROM
                scr_imagens_base64
            WHERE 
                nome_imagem = '%s'
            """ % imagem

        r = query_db(codigo_acesso,sql_img,None,True)

        return r[0]



    def setImagens(codigo_acesso, imagens):
        # print(conferencias);       
        #print(imagens);
        dados = json.loads(imagens)
        if len(dados) == 0:
            return None

        comandos = []
        
        for i in dados:
            sql_img = """INSERT INTO scr_imagens_base64 (
                   nome_imagem,
                   id_documento_app,
                   arquivo 
            ) VALUES (
                '%(nome_arquivo)s',
                %(ocorrencia_documento_id)i,
                '%(arquivo)s'
            )
            """ % i

            comandos.append(sql_img)

        sql = ';'.join(comandos)        
        try:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
        except:    
            
            print(traceback.format_exc())        
            return None
        
        return None