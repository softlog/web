from app import query_db, execute_db
import json

class ProtocolosModel(object):

    def get_protocolo(self,data_expedicao,ultimo_id, id_acesso):

        """Retorna dados do usuario em formato Json"""

        if id_acesso > 9999:
            tem_filial = '1'
            codigo_filial = str(id_acesso)[-3:]
        else:
            tem_filial = '0'
            codigo_filial = ''
            
        

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
                    AND CASE WHEN 1 = %s THEN 
                                scr_nf_protocolo.codigo_empresa = '001' AND
                                scr_nf_protocolo.codigo_filial = '%s'
                             ELSE
                                1=1
                    END
                        
            )
	        , p_remetentes AS (
		        SELECT 
			        p.id_nf_protocolo,
			        nf.remetente_id,
			        trim(r.nome_cliente) as remetente_nome,
			        trim(r.cnpj_cpf) as remetente_cnpj,
                    trim(r.endereco) as endereco,
                    trim(r.numero) as numero,
                    trim(r.bairro) as bairro,
                    trim(r.cep) as cep,
                    trim(r.ddd) as ddd,
                    trim(r.telefone) as telefone,
                    r.id_cidade,
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
                    r.codigo_cliente
		
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
				            remetente_cnpj,
                            endereco,
                            numero,
                            bairro,
                            cep,
                            ddd,
                            telefone,
                            id_cidade
			            FROM
				            p_remetentes
		                    WHERE 
				            remetente_id IS NOT NULL
			            GROUP BY 
				            remetente_id,
				            remetente_nome,
				            remetente_cnpj,
                            endereco,
                            numero,
                            bairro,
                            cep,
                            ddd,
                            telefone,
                            id_cidade
		            ) as row
	            ) 
	            SELECT array_agg(remetentes) as remetentes FROM temp		
	        )
	        , setores AS (
	            WITH temp AS (
		            SELECT row_to_json(row) as setores FROM (
			            SELECT
				            id_regiao,
				            descricao,
                            id_cidade_polo,
                            id_regiao_agrupadora
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
            , regioes AS (
                WITH temp AS (
		            SELECT row_to_json(row) as regioes FROM (
			            SELECT
				            regiao.id_regiao,
				            regiao.descricao,
                            regiao.id_cidade_polo,
                            regiao.id_regiao_agrupadora
			            FROM
				            p_setor
				            LEFT JOIN regiao setor
					            ON setor.id_regiao = p_setor.id_setor
                            LEFT JOIN regiao 
                                ON regiao.id_regiao = setor.id_regiao_agrupadora
                        WHERE 
                            setor.id_regiao_agrupadora IS NOT NULL
			            GROUP BY 
				            regiao.id_regiao
		            ) as row
	            ) 
	            SELECT array_agg(regioes) as regioes FROM temp   
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
				            COALESCE(cidades.lat,0.00) as latitude,
				            COALESCE(cidades.lng,0.00) as longitude
			            FROM 
				            p_remetentes
				            LEFT JOIN cidades ON cidades.id_cidade =  p_remetentes.id_cidade
                        WHERE cidades.id_cidade IS NOT NULL
			            GROUP BY 
				            cidades.id_cidade 
                        UNION 
                        SELECT 
				            cidades.id_cidade,						   
				            trim(cidades.nome_cidade) as nome_cidade,
				            cidades.uf,
				            trim(cidades.cod_ibge) as cod_ibge,
				            COALESCE(cidades.lat,0.00) as latitude,
				            COALESCE(cidades.lng,0.00) as longitude
			            FROM 
				            p_setor
                            LEFT JOIN regiao 
                                ON regiao.id_regiao = p_setor.id_setor
				            LEFT JOIN cidades 
                                ON cidades.id_cidade =  regiao.id_cidade_polo
                        WHERE cidades.id_cidade IS NOT NULL
			            GROUP BY 
				            cidades.id_cidade 
                        UNION 
                        SELECT 
				            cidades.id_cidade,						   
				            trim(cidades.nome_cidade) as nome_cidade,
				            cidades.uf,
				            trim(cidades.cod_ibge) as cod_ibge,
				            COALESCE(cidades.lat,0.00) as latitude,
				            COALESCE(cidades.lng,0.00) as longitude
			            FROM 
				            p_setor
                            LEFT JOIN regiao setor
                                ON setor.id_regiao = p_setor.id_setor
                            LEFT JOIN regiao
                                ON regiao.id_regiao = setor.id_regiao_agrupadora
				            LEFT JOIN cidades 
                                ON cidades.id_cidade =  regiao.id_cidade_polo
                        WHERE
                            setor.id_regiao_agrupadora IS NOT NULL  
                            AND cidades.id_cidade IS NOT NULL
			            GROUP BY 
				            cidades.id_cidade 

			            ORDER BY 
				            id_cidade
		            ) row
	            ) 
	            SELECT array_agg(temp.cidade) as cidades FROM temp	
            )
	        , usuarios AS (
	            WITH temp AS (
		            SELECT row_to_json(row) as usuarios FROM (
			            SELECT
				            id_usuario,
				            trim(nome_usuario) as nome_usuario,
                            trim(senha) as senha
			            FROM
				            usuarios					            
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
                        regioes.regioes,
                        cidades.cidades,
			            usuarios.usuarios,
			            remetentes.remetentes
		            FROM
			            protocolos,
                        setores, 
                        regioes, 
                        cidades,
                        usuarios, 
                        remetentes
	        ) row
            """ % (data_expedicao,
                   arg_ultimo_id, 
                   arg_ultimo_id, 
                   tem_filial,
                   codigo_filial
                   )        

        r = query_db(id_acesso,sql,None,True)

        if r[0]['protocolos'] is None:
            return None

        return r[0]

    def setConferenciaProtocolo(self,codigo_acesso, conferencias):

        #print(conferencias);
        #return None
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

            if protocolo.get('notas_fiscais') is not None:
                
                for nf in protocolo['notas_fiscais']:
                    obs_nf = nf.get('observacao')

                    if obs_nf is None:
                        continue

                    sql_nf = """UPDATE scr_notas_fiscais_imp SET 
                                    id_ocorrencia = %i,
                                    obs_ocorrencia = '%s',
                                    data_ocorrencia = '%s'
                                WHERE id_nota_fiscal_imp = %i
                             """ % (nf['id_ocorrencia'], obs_nf, protocolo['data_conferencia'], nf['id_nota_fiscal_imp'])
                    comandos.append(sql_nf)

                    anexos = nf.get('anexos')

                    if anexos is None:
                        continue

                    for anexo in anexos:
                        sql_anexo = """
                        INSERT INTO scr_notas_fiscais_imp_anexos (
                            id_nota_fiscal_imp,
                            tipo_anexo,
                            data_anexo,
                            usuario_anexo,
                            descricao_anexo,
                            conteudo_anexo,
                            nome_anexo
                        ) VALUES (
                            %i,
                            1,
                            '%s',
                            '%s',
                            'CONFERENCIA VOLUMES',
                            '%s',
                            '%s'
                        )""" % (
                            nf['id_nota_fiscal_imp'],
                            protocolo['data_conferencia'],
                            protocolo['usuario_conferencia'],
                            anexo['arquivo'],
                            anexo['nome_arquivo']
                        )
                        comandos.append(sql_anexo)

        sql = ';'.join(comandos)
        print(sql)
        try:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
        except:
            return None
        
        return comandos
