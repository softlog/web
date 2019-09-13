# -*- coding: latin-1 -*-
#!/usr/bin/env python
from flask_restful import Resource, fields, marshal

qry_cte = """
    	    SELECT
                nf.id_nota_fiscal_redespachador as id_nota_fiscal_imp,
                COALESCE(c.chave_cte,'') as chave_cte
            FROM
                scr_notas_fiscais_imp nf
                LEFT JOIN scr_conhecimento c
                    ON c.id_conhecimento = nf.id_conhecimento
                LEFT JOIN scr_romaneios r
			        ON nf.id_romaneio = r.id_romaneio
	        	LEFT JOIN fornecedores f
			        ON f.id_fornecedor = r.id_transportador_redespacho
            WHERE
                nf.id_nota_fiscal_redespachador IN (%s)
                AND f.cnpj_cpf = '%s'
            """

qry_db ="""
    SELECT
    	p.cnpj_cpf,
    	p.id_bd,
        trim(p.razao_social) as razao_social,
    	f_get_dsn_tenancy(p.id_bd) as dsn
    FROM
    	edi_parceiros p
    	LEFT JOIN string_conexoes c
    		ON c.id_string_conexao = p.id_bd
    WHERE cnpj_cpf IN (%s);
"""

qry_qt_docs = """SELECT         
	    1::integer as tp_romaneio,
        count(*) qt,
        string_agg(nf.id_nota_fiscal_imp::text,',') as lst_notas
    FROM
		scr_romaneios r
		RIGHT JOIN scr_notas_fiscais_imp nf
			ON nf.id_romaneio = r.id_romaneio
		LEFT JOIN fornecedores red
			ON red.id_fornecedor = r.id_transportador_redespacho
		WHERE
			r.data_romaneio::date = '%(data)s'
			AND red.cnpj_cpf = '%(cnpj)s'
			AND r.emitido = 1  
            AND nf.id_nota_fiscal_redespachador IS NULL 
            AND nf.id_nota_fiscal_imp IS NOT NULL     
    HAVING count(*) > 0
    UNION 
    SELECT         
	    2::integer as tp_romaneio,
        count(*) qt,
        string_agg(nf.id_conhecimento_notas_fiscais::text,',') as lst_notas
    FROM
		scr_romaneios r
		LEFT JOIN scr_conhecimento_entrega e
			ON e.id_romaneios = r.id_romaneio
		LEFT JOIN scr_conhecimento_notas_fiscais nf
			ON nf.id_conhecimento = e.id_conhecimento
		LEFT JOIN fornecedores red
			ON red.id_fornecedor = r.id_transportador_redespacho
		WHERE
			r.data_romaneio::date = '%(data)s'
			AND red.cnpj_cpf = '%(cnpj)s'
			AND r.emitido = 1  
            AND nf.id_nota_fiscal_redespachador IS NULL
     """

qry_lst_participantes = """
    WITH t as  (
        SELECT         
            nf.remetente_id as codigo_cliente                    
	    FROM
		    scr_romaneios r
		    LEFT JOIN scr_notas_fiscais_imp nf
			    ON nf.id_romaneio = r.id_romaneio
		    LEFT JOIN fornecedores red
			    ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1    
            AND nf.id_nota_fiscal_redespachador IS NULL
        UNION 
        SELECT         
            nf.destinatario_id as codigo_cliente                    
	    FROM
		    scr_romaneios r
		    LEFT JOIN scr_notas_fiscais_imp nf
			    ON nf.id_romaneio = r.id_romaneio
		    LEFT JOIN fornecedores red
			    ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1    
            AND nf.id_nota_fiscal_redespachador IS NULL
        UNION 
        SELECT         
            nf.consignatario_id as codigo_cliente                    
	    FROM
		    scr_romaneios r
		    LEFT JOIN scr_notas_fiscais_imp nf
			    ON nf.id_romaneio = r.id_romaneio
		    LEFT JOIN fornecedores red
			    ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1 
            AND nf.id_nota_fiscal_redespachador IS NULL
    )
    SELECT    
        string_agg(codigo_cliente::text,',') as lst_clientes
    FROM
        t
"""

qry_lst_participantes_2 = """
 WITH t as  (
        SELECT         
            c.remetente_id as codigo_cliente                    
	    FROM 	scr_romaneios r
			LEFT JOIN scr_conhecimento_entrega e
				ON e.id_romaneios = r.id_romaneio
			LEFT JOIN scr_conhecimento_notas_fiscais nf
				ON nf.id_conhecimento = e.id_conhecimento	
			LEFT JOIN scr_conhecimento c 	
				ON c.id_conhecimento = e.id_conhecimento
			LEFT JOIN fornecedores red
				ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1
            AND nf.id_nota_fiscal_redespachador IS NULL
        UNION 
        SELECT         
            c.destinatario_id as codigo_cliente                    
	    FROM 	scr_romaneios r
			LEFT JOIN scr_conhecimento_entrega e
				ON e.id_romaneios = r.id_romaneio
			LEFT JOIN scr_conhecimento_notas_fiscais nf
				ON nf.id_conhecimento = e.id_conhecimento	
			LEFT JOIN scr_conhecimento c 	
				ON c.id_conhecimento = e.id_conhecimento
			LEFT JOIN fornecedores red
				ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1
            AND nf.id_nota_fiscal_redespachador IS NULL
        UNION 
        SELECT         
            c.consig_red_id as codigo_cliente                    
	    FROM 	scr_romaneios r
			LEFT JOIN scr_conhecimento_entrega e
				ON e.id_romaneios = r.id_romaneio
			LEFT JOIN scr_conhecimento_notas_fiscais nf
				ON nf.id_conhecimento = e.id_conhecimento	
			LEFT JOIN scr_conhecimento c 	
				ON c.id_conhecimento = e.id_conhecimento
			LEFT JOIN fornecedores red
				ON red.id_fornecedor = r.id_transportador_redespacho
 	    WHERE
		    r.data_romaneio::date = '%(data)s'
		    AND red.cnpj_cpf = '%(cnpj)s'
		    AND r.emitido = 1
            AND nf.id_nota_fiscal_redespachador IS NULL
    )
    SELECT    
        string_agg(codigo_cliente::text,',') as lst_clientes
    FROM
        t   
"""

qry_participantes = """
SELECT row_to_json(row) FROM (
		SELECT
			trim(c.cnpj_cpf) as part_cnpj_cpf,
			trim(c.nome_cliente) as part_nome,
			trim(c.inscricao_estadual) as part_ie,
			trim(c.endereco) as part_logradouro,
			trim(c.numero) as part_numero,
			trim(c.bairro) as part_bairro,
			trim(cid.cod_ibge) as part_cod_mun,
			trim(cid.nome_cidade) as part_cidade,
			trim(cid.uf) as part_uf,
			trim(c.cep) as part_cep,
			trim(c.telefone) as part_fone,
			trim(c.email) as part_email,
			c.percentual_devolucao,
			c.percentual_reentrega,
			c.frequencia_faturamento,
			c.prazo_pagamento,	
			c.frete as frete_padrao,
			c.formas_pgto as forma_pagamento,
			c.imposto_por_conta as imposto_cliente	
		FROM
			cliente c
			LEFT JOIN cidades cid
				ON cid.id_cidade = c.id_cidade
		WHERE
			codigo_cliente IN (%(lst_clientes)s)
		GROUP BY 
			c.codigo_cliente,
			cid.id_cidade
			
) row
"""

qry_nf = """
	SELECT row_to_json(row) as nfes FROM (
			SELECT 
                id_nota_fiscal_imp::text as id_nota_fiscal_imp,
				trim(nf.chave_nfe) as nfe_chave_nfe,
				CASE WHEN nf.frete_cif_fob = 1 THEN '0' ELSE '1' END::text as nfe_modo_frete,
				trim(rem.cnpj_cpf) as nfe_emit_cnpj_cpf,
				trim(o.cod_ibge) as nfe_emit_cod_mun,
				trim(dest.cnpj_cpf) as nfe_dest_cnpj_cpf,
				--nf.calculado_ate_id_cidade as cidade_destino,
				trim(d.cod_ibge) as nfe_dest_cod_mun,
				nf.data_emissao::date::text as nfe_data_emissao,
				nf.numero_nota_fiscal as nfe_numero_doc,
				'55'::text as nfe_modelo,
				nf.serie_nota_fiscal as nfe_serie,
				nf.placa_veiculo as nfe_placa_veiculo,
				nf.placa_carreta1 as nfe_placa_reboque1,
				nf.placa_carreta2 as nfe_placa_reboque2,
				nf.valor::text as nfe_valor,
				nf.valor_base_calculo::text as nfe_valor_bc,
				nf.valor_icms_nf::text as nfe_valor_icms,
				nf.valor_base_calculo_icms_st::text as nfe_valor_bc_st,
				nf.valor_icms_nf_st::text as nfe_valor_icms_st,
				trim(nf.especie_mercadoria) as nfe_especie_mercadoria,
				trim('UN'::text) as nfe_unidade,
				trim(nf.cfop_pred_nf) as nfe_cfop_predominante,
				''::text as nfe_informacoes,
				nf.consumidor_final::text as nfe_ind_final,
				trim(dest.inscricao_estadual) as nfe_ie_dest,
				'1'::text as nfe_tp_nf,
				nf.peso::text as nfe_peso_presumido,
				nf.peso_liquido::text as nfe_peso_liquido,
				nf.qtd_volumes::text as nfe_volume_presumido,
				nf.peso::text as nfe_peso_presumido,
				nf.qtd_volumes::text as nfe_volume_produtos,
                nf.valor_total_produtos::text as nfe_valor_produtos,
				nf.peso::text as nfe_peso_produtos,
				NULL::text as nfe_num_cte,
				NULL::text as nfe_chave_cte,
				NULL::text as nfe_frete_origem,
                filial.cnpj as nfe_pagador_cnpj_cpf,
				r.emitido,
				r.id_romaneio as nfe_id_romaneio_parceiro,
				nf.id_nota_fiscal_imp as nfe_id_nota_fiscal_parceiro,
                trim(df.cod_ibge) as nfe_pagador_cod_mun,
                c.chave_cte 
				--c.redespachador_id::text as redespachador_id	
			FROM		
				scr_romaneios r		
				LEFT JOIN scr_notas_fiscais_imp nf
					ON r.id_romaneio = nf.id_romaneio		
				LEFT JOIN cliente rem
					ON rem.codigo_cliente = nf.remetente_id
				LEFT JOIN cliente dest
					ON dest.codigo_cliente = nf.destinatario_id
				LEFT JOIN fornecedores red
					ON red.id_fornecedor = r.id_transportador_redespacho
				LEFT JOIN cidades o 
					ON o.id_cidade = calculado_de_id_cidade
				LEFT JOIN cidades d
					ON d.id_cidade = calculado_ate_id_cidade
                LEFT JOIN filial
                    ON nf.filial_emitente = filial.codigo_filial 
                        AND nf.empresa_emitente = filial.codigo_empresa
				LEFT JOIN cidades df
					ON df.id_cidade = filial.id_cidade
                LEFT JOIN scr_conhecimento c
                    ON c.id_conhecimento = nf.id_conhecimento
			WHERE
				nf.id_nota_fiscal_imp IN (%s)				                
		) row
"""

qry_nf2 = """
		SELECT row_to_json(row) as nfes FROM (
			SELECT 
				id_conhecimento_notas_fiscais::text as id_nota_fiscal_imp,
				trim(nf.chave_nfe) as nfe_chave_nfe,
				CASE WHEN c.frete_cif_fob = 1 THEN '0' ELSE '1' END::text as nfe_modo_frete,
				trim(rem.cnpj_cpf) as nfe_emit_cnpj_cpf,
				trim(o.cod_ibge) as nfe_emit_cod_mun,
				trim(dest.cnpj_cpf) as nfe_dest_cnpj_cpf,
				--nf.calculado_ate_id_cidade as cidade_destino,
				trim(d.cod_ibge) as nfe_dest_cod_mun,
				nf.data_nota_fiscal::date::text as nfe_data_emissao,
				nf.numero_nota_fiscal as nfe_numero_doc,
				'55'::text as nfe_modelo,
				nf.serie_nota_fiscal as nfe_serie,
				c.placa_veiculo as nfe_placa_veiculo,
				c.placa_reboque1 as nfe_placa_reboque1,
				c.placa_reboque2 as nfe_placa_reboque2,
				nf.valor::text as nfe_valor,
				nf.valor_base_calculo::text as nfe_valor_bc,
				nf.valor_icms_nf::text as nfe_valor_icms,
				nf.valor_base_calculo_icms_st::text as nfe_valor_bc_st,
				nf.valor_icms_nf_st::text as nfe_valor_icms_st,
				trim(nf.especie_mercadoria) as nfe_especie_mercadoria,
				trim('UN'::text) as nfe_unidade,
				trim(nf.cfop_pred_nf) as nfe_cfop_predominante,
				''::text as nfe_informacoes,
				'0'::text as nfe_ind_final,
				trim(dest.inscricao_estadual) as nfe_ie_dest,
				'1'::text as nfe_tp_nf,
				nf.peso::text as nfe_peso_presumido,
				nf.peso_liquido::text as nfe_peso_liquido,
				nf.qtd_volumes::text as nfe_volume_presumido,
				nf.peso::text as nfe_peso_presumido,
				nf.qtd_volumes::text as nfe_volume_produtos,
				nf.valor_total_produtos::text as nfe_valor_produtos,
				nf.peso::text as nfe_peso_produtos,
				NULL::text as nfe_num_cte,
				NULL::text as nfe_chave_cte,
				NULL::text as nfe_frete_origem,
				filial.cnpj as nfe_pagador_cnpj_cpf,
				r.emitido,
				r.id_romaneio as nfe_id_romaneio_parceiro,
				nf.id_conhecimento_notas_fiscais as nfe_id_nota_fiscal_parceiro,
				trim(df.cod_ibge) as nfe_pagador_cod_mun
				--c.redespachador_id::text as redespachador_id	
			FROM		
				scr_romaneios r		
				LEFT JOIN scr_conhecimento_entrega e
					ON r.id_romaneio = e.id_romaneios
				LEFT JOIN scr_conhecimento_notas_fiscais nf
					ON nf.id_conhecimento = e.id_conhecimento
				LEFT JOIN scr_conhecimento c
					ON c.id_conhecimento = nf.id_conhecimento
				LEFT JOIN cliente rem
					ON rem.codigo_cliente = c.remetente_id
				LEFT JOIN cliente dest
					ON dest.codigo_cliente = c.destinatario_id
				LEFT JOIN fornecedores red
					ON red.id_fornecedor = r.id_transportador_redespacho
				LEFT JOIN cidades o 
					ON o.id_cidade = c.calculado_de_id_cidade
				LEFT JOIN cidades d
					ON d.id_cidade = c.calculado_ate_id_cidade
				LEFT JOIN filial
				    ON c.filial_emitente = filial.codigo_filial 
					AND c.empresa_emitente = filial.codigo_empresa
				LEFT JOIN cidades df
					ON df.id_cidade = filial.id_cidade
			WHERE
				nf.id_conhecimento_notas_fiscais IN (%s)				                
		) row
"""

qry_upd_baixa_nfe = """
  UPDATE scr_notas_fiscais_imp
  SET
    id_ocorrencia = %(id_ocorrencia)i,
    canhoto = %(id_canhonto)i,
    entrega_realizada = %(entrega_realizada)i,
    data_ocorrencia = '%(data_ocorrencia)s',
    nome_recebedor = '%(nome_recebedor)s',
    cpf_recebedor = '%(doc_recebedor)s'
   WHERE id_nota_fiscal_imp = %(id_nota_fiscal)i
  RETURNING numero_nota_fiscal
"""