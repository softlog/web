# -*- coding: latin-1 -*-
#!/usr/bin/env python

from app import pyboleto_flask
from app.pyboleto_flask.bank.bradesco import BoletoBradesco
from app.pyboleto_flask.bank.caixa_sig14 import BoletoCaixaSig14
from app.pyboleto_flask.bank.caixa_cs import BoletoCaixaCs
from app.pyboleto_flask.bank.itau_109 import BoletoItau109
from app.pyboleto_flask.bank.bancodobrasil import BoletoBB
from app.pyboleto_flask.bank.sicoob import BoletoSicoob

from app.pyboleto_flask.pdf import BoletoPDF
from io import BytesIO
from flask_restful import Api, Resource, reqparse, marshal
from decimal import Decimal
from datetime import date
from flask import render_template

import datetime
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from psycopg2.extras import DictCursor
from app import query_db, execute_db
from app import app
from app.util import format_value 

from flask import make_response
from reportlab.pdfgen import canvas


#from app import get_db, close_conection 

@app.route('/cobranca/itau') 
def itau():
    listaDadosBradesco = []
    for i in range(2):
        d = BoletoBradesco(carteira='09')
        d.carteira = '09'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'SEVEN TRANSPORTE, LOGISTICA E DISTRIBUICAO'
        d.cedente_documento = "04.377.377/0001-15"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '2344-2'
        d.conta_cedente = '0006777-6'

        d.data_vencimento = datetime.date(2016, 9, 18)
        d.data_documento = datetime.date(2010, 9, 5)
        d.data_processamento = datetime.date(2010, 9, 5)

        d.instrucoes = [
            "Ap�s o Vencimento Cobrar Multa de R$7,84 e Juros de RS0,65 ao Dia",
            "ENVIAR PARA CARTORIO NO 5o. DIA APOS O VENCIMENTO",
            ]
        d.demonstrativo = [
            "- Servi�o Transporte R$ 392,13",
            "- Total R$ 392,13",
            ]
        d.valor_documento = 392.13
        d.especie_documento = "DS"             
        
        d.nosso_numero = "5446"
        d.numero_documento = "0010036740"
        d.sacado = [
            "TECNOMONT MONTAGENS INDUSTRIAIS LTDA",
            "AVENIDA CAIAPO, 1749",
            "SANTA GENOVEVA   GOIANIA   GO   74672400"
            ]
        listaDadosBradesco.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBradesco)):
        boleto.drawBoleto(
            listaDadosBradesco[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename=boleto_bradesco.pdf"
    response.mimetype = 'application/pdf'
    return response            

@app.route('/cobranca/bradesco') 
def bradesco():
    listaDadosBradesco = []
    for i in range(2):
        d = BoletoBradesco(carteira='09')
        d.carteira = '09'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'SEVEN TRANSPORTE, LOGISTICA E DISTRIBUICAO'
        d.cedente_documento = "04.377.377/0001-15"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '2344-2'
        d.conta_cedente = '0006777-6'

        d.data_vencimento = datetime.date(2016, 9, 18)
        d.data_documento = datetime.date(2010, 9, 5)
        d.data_processamento = datetime.date(2010, 9, 5)

        d.instrucoes = [
            "Ap�s o Vencimento Cobrar Multa de R$7,84 e Juros de RS0,65 ao Dia",
            "ENVIAR PARA CARTORIO NO 5o. DIA APOS O VENCIMENTO",
            ]
        d.demonstrativo = [
            "- Servi�o Transporte R$ 392,13",
            "- Total R$ 392,13",
            ]
        d.valor_documento = 392.13
        d.especie_documento = "DS"             
        
        d.nosso_numero = "5446"
        d.numero_documento = "0010036740"
        d.sacado = [
            "TECNOMONT MONTAGENS INDUSTRIAIS LTDA",
            "AVENIDA CAIAPO, 1749",
            "SANTA GENOVEVA   GOIANIA   GO   74672400"
            ]
        listaDadosBradesco.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBradesco)):
        boleto.drawBoleto(
            listaDadosBradesco[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename=boleto_bradesco.pdf"
    response.mimetype = 'application/pdf'
    return response            

@app.route('/cobranca/caixa') 
def print_caixa():
    listaDadosCaixa = []
    for i in range(2):
        d = BoletoCaixaSigcb()
        d.carteira = 'RG'  # Contrato firmado com o Banco Bradesco
        d.cedente = 'Empresa ACME LTDA'
        d.cedente_documento = "102.323.777-01"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '1565'
        d.conta_cedente = '414-3'

        d.data_vencimento = datetime.date(2010, 3, 27)
        d.data_documento = datetime.date(2010, 2, 12)
        d.data_processamento = datetime.date(2010, 2, 12)

        d.instrucoes = [
            "- Linha 1",
            "- Sr Caixa, cobrar multa de 2% apos o vencimento",
            "- Receber ate 10 dias apos o vencimento",
            ]
        d.demonstrativo = [
            "- Servico Teste R$ 5,00",
            "- Total R$ 5,00",
            ]
        d.valor_documento = 255.00

        d.nosso_numero = "8019525086"
        d.numero_documento = "8019525086"
        d.sacado = [
            "Cliente Teste %d" % (i + 1),
            "Rua Desconhecida, 00/0000 - Nao Sei - Cidade - Cep. 00000-000",
            ""
            ]
        listaDadosCaixa.append(d)

    # Caixa Formato normal - uma pagina por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosCaixa)):
        boleto.drawBoleto(listaDadosCaixa[i])
        boleto.nextPage()    
    boleto.save()
    
    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename=boleto_cef.pdf"
    response.mimetype = 'application/pdf'
    return response               

    # Caixa Formato normal - uma pagina por folha A4
    boleto = BoletoPDF('boleto-caixa-formato-normal-teste.pdf')
    for i in range(len(listaDadosCaixa)):
        boleto.drawBoleto(listaDadosCaixa[i])
        boleto.nextPage()
    boleto.save()


@app.route('/cobranca/bb') 
def bb():
    listaDadosBB = []
    for i in range(2):
        d = BoletoBB(7,2)
        d.carteira = '17'  
        d.cedente = 'SEVEN TRANSPORTE, LOGISTICA E DISTRIBUICAO'
        d.cedente_documento = "04.377.377/0001-15"
        d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
        d.agencia_cedente = '3689'
        d.conta_cedente = '43871'

        d.data_vencimento = datetime.date(2018, 1, 24)
        d.data_documento = datetime.date(2018, 1, 16)
        d.data_processamento = datetime.date(2018, 1, 16)

        d.instrucoes = [
            "Ap�s o Vencimento Cobrar Multa de R$7,84 e Juros de RS0,65 ao Dia",
            "ENVIAR PARA CARTORIO NO 5o. DIA APOS O VENCIMENTO",
            ]
        d.demonstrativo = [
            "- Servi�o Transporte R$ 392,13",
            "- Total R$ 392,13",
            ]
        d.valor_documento = '5762,48'
        d.especie_documento = "DS"                     
        
        d.convenio = '3066623'
        d.nosso_numero = "159"
        d.numero_documento = "0010041694"
        d.sacado = [
            "TECNOMONT MONTAGENS INDUSTRIAIS LTDA",
            "AVENIDA CAIAPO, 1749",
            "SANTA GENOVEVA   GOIANIA   GO   74672400"
            ]
        listaDadosBB.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBB)):
        boleto.drawBoleto(
            listaDadosBB[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename=boleto_bradesco.pdf"
    response.mimetype = 'application/pdf'
    return response         

@app.route('/cobranca/boleto_atualizado') 
def boleto_atualizado():

    parser = reqparse.RequestParser()
    parser.add_argument('id_db',type=int,help='Par�metro Id_db inv�lido.')
    parser.add_argument('id_remessa',type=int,help='Par�metro id_remessa inv�lido.')
    parser.add_argument('id_fatura',type=int,help='Par�metro id_boleto inv�lido.')    
    parser.add_argument('data_boleto',type=str,help='Par�metro data_boleto inv�lido.')    
    parser.add_argument('e',type=str,help='Par�metro e inv�lido.')


    args = parser.parse_args()
    id_db = args['id_db']
    id_remessa = args['id_remessa']
    id_boleto = args['id_fatura'] 
    data_boleto = args['data_boleto']
    e = args['e']

    link = """http://api.softlog.eti.br/cobranca/boleto_atualizado_v1?id_db=%i&id_remessa=%i&id_fatura=%i&e=%s&data_boleto=%s""" % \
            (id_db,id_remessa,id_boleto,e,data_boleto)

 #   link = """http://localhost:5000/cobranca/boleto_atualizado_v1?id_db=%i&id_remessa=%i&id_fatura=%i&e=%s&data_boleto=%s""" % \
 #           (id_db,id_remessa,id_boleto,e,data_boleto)
  
    return render_template("api_cobranca/baixa_boleto.html",link=link)

@app.route('/cobranca/boleto') 
def boleto():

    parser = reqparse.RequestParser()
    parser.add_argument('id_db',type=int,help='Par�metro Id_db inv�lido.')
    parser.add_argument('id_remessa',type=int,help='Par�metro id_remessa inv�lido.')
    parser.add_argument('id_fatura',type=int,help='Par�metro id_boleto inv�lido.')    
    parser.add_argument('e',type=str,help='Par�metro e inv�lido.')


    args = parser.parse_args()
    id_db = args['id_db']
    id_remessa = args['id_remessa']
    id_boleto = args['id_fatura'] 
    e = args['e']

    link = """http://api.softlog.eti.br/cobranca/boleto_v1?id_db=%i&id_remessa=%i&id_fatura=%i&e=%s&data_boleto=NULL""" % \
            (id_db,id_remessa,id_boleto,e)

    #link = """http://localhost:5000/cobranca/boleto_v1?id_db=%i&id_remessa=%i&id_fatura=%i&e=%s&data_boleto=NULL""" % \
    #        (id_db,id_remessa,id_boleto,e)

    
    
    return render_template("api_cobranca/baixa_boleto.html",link=link)


@app.route('/cobranca/boleto_atualizado_v1') 
@app.route('/cobranca/boleto_v1') 
def boleto_v1():    
    parser = reqparse.RequestParser()
    parser.add_argument('id_db',type=int,help='Parametro Id_db invalido.')
    parser.add_argument('id_remessa',type=int,help='Parametro id_remessa invalido.')
    parser.add_argument('id_fatura',type=int,help='Parametro id_boleto invalido.')
    parser.add_argument('e',type=str,help='Parametro e invalido.')
    parser.add_argument('data_boleto',type=str,help='Parametro e invalido.')

    args = parser.parse_args()
        
    id_db = args['id_db']
    id_remessa = args['id_remessa']
    id_boleto = args['id_fatura']
    e = args['e']
    data_boleto = args['data_boleto']


    if id_boleto == 0:
        campo_ref = 'id_remessa'
        id_ref = id_remessa
    else:
        campo_ref = 'id_faturamento'
        id_ref = id_boleto

    boleto_atualizado = 0
    if request.path == '/cobranca/boleto_atualizado_v1':
        boleto_atualizado = 1

    
    if data_boleto != 'NULL':
        data_boleto = "'" + data_boleto + "'"

    dados = {    
        'data_boleto':data_boleto, 
        'boleto_atualizado':boleto_atualizado, 
        'campo_ref':campo_ref,
        'id_ref':id_ref, 
        'id_remessa':id_remessa
    }

    qry_rem = """
            SELECT 
			        id_remessa, 
			        numero_remessa, 
			        numero_convenio, 
			        cod_empresa, 
			        cod_filial, 
			        id_carteira, 
			        id_carteira_agregada, 
			        proximo_nosso_numero_agregado, 
			        numero_remessa_agregado, 
			        trim(codigo_carteira) as codigo_carteira, 
			        trim(numero_conta) as numero_conta, 
			        trim(numero_agencia) as numero_agencia, 
			        trim(numero_banco) as numero_banco, 
			        data_hora_geracao, 
			        valor_remessa, 
			        banco_emite_boleto, 
			        nosso_numero_inicial, 
			        gerar_novo_numero, 
			        protestar, 
			        protestar_apos_dias, 
			        juros_perc, 
			        multa_perc, 
			        observacao, 
			        arquivo, 
			        acrescimo, 
			        tipo_duplicata, 
			        layout_remessa, 
			        layout_retorno, 
			        local_pagamento, 
			        left(trim(instrucoes),90) as instrucoes, 
			        cnpj_sacador, 
			        sacador,
			        trim(initcap(filial.razao_social)) as razao_social,
                    cnpj_cpf(filial.cnpj) as cnpj,
                    trim(initcap(filial.endereco)) as endereco, 
                    trim(filial.numero) as numero, 
                    trim(initcap(filial.bairro)) as bairro,                    
                    filial.id_cidade, 
                    trim(initcap(cidades.nome_cidade)) as nome_cidade,
                    trim(cidades.uf) as uf,
                    trim(filial.cep) as cep,
                    trim(v_remessa.codigo_cedente) as codigo_cedente
		        FROM 
			        v_remessa 
			        LEFT JOIN filial
				        ON v_remessa.cod_filial = filial.codigo_filial
				        AND v_remessa.cod_empresa = filial.codigo_empresa
                    LEFT JOIN cidades
                        ON cidades.id_cidade = filial.id_cidade
		        WHERE
			        id_remessa = %i""" % (id_remessa)
    
                        
    qry_fatura = """
        WITH t AS (
          SELECT 
            %(boleto_atualizado)i::integer as ba,
            %(data_boleto)s::date as data_atualizada
        ),
        t1 AS (
            SELECT 			
	            f.id_faturamento, 
	            scr_faturamento_remessas.id_remessa, 
	            f.numero_fatura, 
	            trim(f.numero_boleto) as numero_boleto, 
	            trim(initcap(f.fatura_nome)) as fatura_nome, 
	            cnpj_cpf(f.fatura_cnpj) as fatura_cnpj, 
	            CASE WHEN char_length(trim(f.fatura_cnpj)) = 14 THEN 
		            '02'
	            ELSE
		            '01'
	            END::text as tipo_cliente,
	            trim(initcap(f.fatura_endereco)) as fatura_endereco, 
	            trim(f.fatura_numero) as fatura_numero, 
	            trim(initcap(f.fatura_bairro)) as fatura_bairro, 
	            trim(initcap(f.fatura_cidade)) as fatura_cidade, 
	            trim(f.fatura_uf) as fatura_uf, 
	            trim(f.fatura_cep) as fatura_cep, 
	            f.fatura_ie, 
	            f.valor_total_ctrc, 
	            f.valor_total_servicos, 
	            CASE 	WHEN f.valor_adicional IS NOT NULL 
		            THEN (f.valor_fatura + f.valor_adicional) 
		            ELSE f.valor_fatura 
	            END as valor_fatura, 
	            (f.valor_total) as valor_total, 
	            (f.perc_desconto) as perc_desconto, 
	            (f.desconto) as desconto, 
	            f.prazo_desconto, 
	            (f.perc_juros) as perc_juros,
	            CASE 	WHEN f.perc_juros > 0 THEN 
			            ' E JUROS DE R$' ||
			            replace(
				            (
				            (
				              ((f.valor_fatura + COALESCE(f.valor_adicional,0,00)) 
					         * f.perc_juros
				               )/100
				            )/30)::numeric(12,2)::text,
				            '.',',')
			            || ' AO DIA' 
		            ELSE 
			            ''
	            END::text as msg_juros,
	            (
	               (
		            (
		              ((f.valor_fatura + COALESCE(f.valor_adicional,0,00)) 
			         * f.perc_juros
		               )/100
		            )/30
		        )
	            )::numeric(12,2) as valor_juros,
	            CASE 	WHEN f.perc_multa > 0 THEN 
			            'APOS O VENCIMENTO COBRAR MULTA DE R$' ||
			            replace(
				            (						
				              ((f.valor_fatura + COALESCE(f.valor_adicional,0,00)) 
					         * f.perc_multa
				               )/100
				            )::numeric(12,2)::text,
				            '.',',')					
		            ELSE 
			            ''
	            END::text as msg_multa,			  
	            CASE 	WHEN f.perc_multa > 0 THEN 
				            (						
				              ((f.valor_fatura + COALESCE(f.valor_adicional,0,00)) 
					         * f.perc_multa
				               )/100
				            )::numeric(12,2)				            			
		            ELSE 
			            0.00
	            END as valor_multa,			  
	            f.juros, 
	            f.perc_multa, 		
	            f.multa, 
	            COALESCE(f.abatimento,0.00) as abatimento, 
	            f.valor_inss, 
	            f.tarifa, 
	            COALESCE(t.data_atualizada,f.data_vencimento) as data_vencimento,
	            f.data_processamento,			
	            to_char(f.data_lim_desconto,'DD/MM/YYYY') as data_lim_desconto, 
	            f.protesto, 
	            scr_faturamento_remessas.tipo_acao_cobranca, 
	            scr_faturamento_remessas.gerar_nosso_numero, 
	            scr_faturamento_remessas.status_geracao, 
	            scr_faturamento_remessas.id_remessa_fatura, 
	            f.prazo_protesto, 
	            fp.valor_fatura as valor_fatura_principal, 
	            CASE 	WHEN f.num_parcela IS NULL 
			            OR f.tipo_fatura <> 3 THEN 'Única' 
		            WHEN f.num_parcela = 0 THEN 'Entrada' 
		            WHEN f.num_parcela > 0 THEN lpad(f.num_parcela::text,2,'0') || '-' || lpad(f.qtd_parcelas::text,2,'0') 
	            END::text as parcelas,			 
	            to_char(dia_util(t.data_atualizada, 
		            COALESCE(cart.id_cidade::integer,fil.id_cidade::integer)),'DD/MM/YYYY'
	            ) as dt_vencto_atu,			
	            dias_atraso(
		            COALESCE(acordo.previsao_pagto,f.data_vencimento),
		            t.data_atualizada,
		            COALESCE(cart.id_cidade::integer,fil.id_cidade::integer)
	            ) as dias_atraso,
	            t.ba
            FROM	
	            t,		
	            scr_faturamento_remessas 				
	            LEFT JOIN scr_faturamento f
		            ON scr_faturamento_remessas.id_faturamento = f.id_faturamento 
	            LEFT JOIN scr_faturamento fp 
		            ON fp.id_faturamento = f.id_faturamento_principal
	            LEFT JOIN v_carteira cart 
		            ON cart.id_carteira = f.id_cobrador
	            LEFT JOIN filial fil 
		            ON fil.codigo_empresa = f.codigo_empresa 
			            AND f.codigo_filial = fil.codigo_filial
	            LEFT JOIN v_scr_faturamento_dt_acordo acordo 
		            ON acordo.id_faturamento = f.id_faturamento
            WHERE        
	        scr_faturamento_remessas.%(campo_ref)s = %(id_ref)i            
        )
        SELECT  *, 
	        CASE WHEN ba = 1 THEN 
	            valor_fatura +
	            (valor_juros * dias_atraso) + 
	            valor_multa
	        ELSE
	            valor_fatura
	        END::numeric(12,2) as valor_boleto,
	        data_vencimento as vencimento_boleto
        FROM t1 
        WHERE id_remessa = %(id_remessa)i
        ORDER BY numero_fatura 
        """ % dados
        ##(boleto_atualizado, campo_ref,id_ref, id_remessa)
    
    #print(qry_fatura)
    
    remessa = query_db(id_db,qry_rem,{},True)
    
    faturas = query_db(id_db,qry_fatura)
   
    #print("DIAS ATRASO",faturas[0]['dias_atraso'])
    #print("Valor Multa",faturas[0]['valor_multa'])
    #print("VALOR JUROS",faturas[0]['valor_juros'])
    #print("VALOR BOLETO",faturas[0]['valor_boleto'])
    #if faturas[0]['dias_atraso'] > 0:        
    #    return render_template("api_cobranca/baixa_boleto.html")
    
    response = get_boleto(faturas,remessa)
    
    
    if response is not None and e != 'None':        
        cmd_log = """INSERT INTO scr_faturamento_log_atividades(
					id_faturamento,					
					atividade_executada,					 
					usuario 
					)
				VALUES (%i,
					LEFT('ACESSO BOLETO (%s)',100),'sistema')
              """  % (id_boleto,e)
        rl = execute_db(id_db,'begin')        
        rl = execute_db(id_db,cmd_log)        
        rl = execute_db(id_db,'commit')        

    response.headers['Content-Disposition'] = "attachment; filename=boleto.pdf"
    response.mimetype = 'application/pdf'
    
    return response            


def get_boleto(faturas, remessa):
    
    if remessa['numero_banco'] == '341':
        return get_boleto_itau_109(faturas,remessa)
    if remessa['numero_banco'] == '237':
        return get_boleto_bradesco(faturas,remessa)
    if remessa['codigo_carteira'].strip() == 'SIG14':
        return get_boleto_caixa_sig14(faturas, remessa)
    if remessa['codigo_carteira'].strip() == 'CS':
        return get_boleto_caixa_cs(faturas, remessa)
    if remessa['numero_banco'].strip() == '001':
        return get_boleto_bb(faturas, remessa)
    if remessa['numero_banco'].strip() == '756':
        return get_boleto_sicob(faturas, remessa)


    return None 

def get_boleto_itau_109(faturas,remessa):
    listaDados = [] 
    for fatura in faturas:
        d = BoletoItau109()
        d.carteira = '109'  # Contrato firmado com o Banco Bradesco
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s-%(bairro)s-%(nome_cidade)s-%(uf)s-CEP:%(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia']
        #d.conta_cedente = remessa['numero_conta']
        conta_cedente = remessa['numero_conta'].split('-')[0]
        
        d.conta_cedente = conta_cedente

        d.data_vencimento = fatura['vencimento_boleto']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ %s" % (format_value(fatura['abatimento'])))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % ("{0:0.2f}".format(fatura['valor_fatura'])),
            "- Encargos: RS %s " % ("{0:0.2f}".format(fatura['valor_boleto']-fatura['valor_fatura'])),
            "- Total R$ %s " % ("{0:0.2f}".format(fatura['valor_boleto']))
            ]
                

                
        d.valor_documento = format_value(fatura['valor_boleto'])
        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto']
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        listaDados.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDados)):
        boleto.drawBoleto(
            listaDados[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)

def get_boleto_caixa(faturas,remessa):
    listaDados = [] 
    for fatura in faturas:
        d = BoletoCaixaSigcb()
        d.carteira = 'RG'  # Contrato firmado com o Banco Bradesco
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s-%(bairro)s-%(nome_cidade)s-%(uf)s-CEP:%(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia']
        #d.conta_cedente = remessa['numero_conta']
        d.conta_cedente = remessa['codigo_cedente'].strip()

        d.data_vencimento = fatura['vencimento_boleto']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ %s" % (format_value(fatura['abatimento'])))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % (format_value(fatura['valor_fatura'])),
            "- Total R$ %s " % (format_value(fatura['valor_fatura']))
            ]

                
        d.valor_documento = format_value(fatura['valor_boleto'])
        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto']
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        listaDados.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDados)):
        boleto.drawBoleto(
            listaDados[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)


def get_boleto_caixa_sig14(faturas,remessa):
    listaDados = []
    for fatura in faturas:
        d = BoletoCaixaSig14()
        d.carteira = 'RG'  # Contrato firmado com o Banco Bradesco
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s - %(bairro)s - %(nome_cidade)s-%(uf)s - CEP: %(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia']
        #d.conta_cedente = remessa['numero_conta']
        d.conta_cedente = remessa['codigo_cedente']

        d.data_vencimento = fatura['vencimento_boleto']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ %s" % (format_value(fatura['abatimento'])))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % (format_value(fatura['valor_fatura'])),
            "- Total R$ %s " % (format_value(fatura['valor_fatura']))
            ]

                
        d.valor_documento = "{0:0.2f}".format(fatura['valor_boleto'])

        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto']
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        listaDados.append(d)
         
    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDados)):
        boleto.drawBoleto(
            listaDados[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)

def get_boleto_caixa_cs(faturas,remessa):
    listaDados = []
    for fatura in faturas:
        d = BoletoCaixaCs()
        d.carteira = 'CS'  # Contrato firmado com o Banco Bradesco
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s - %(bairro)s - %(nome_cidade)s-%(uf)s - CEP: %(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia']
        #d.conta_cedente = remessa['numero_conta']
        d.conta_cedente = remessa['codigo_cedente']

        d.data_vencimento = fatura['vencimento_boleto']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ %s" % (format_value(fatura['abatimento'])))

        d.demonstrativo = []
        d.demonstrativo.append("- Serviço Transporte: RS %s " % (format_value(fatura['valor_fatura'])))

        if fatura['valor_juros'] * fatura['dias_atraso'] > 0 and fatura['ba'] == 1:
            d.demonstrativo.append("- Juros: RS %s " % (format_value(fatura['valor_juros'] * dias_atraso)))
        if fatura['dias_atraso'] > 0 and fatura['ba'] == 1:
            d.demonstrativo.append("- Multa: RS %s " % (format_value(fatura['valor_multa'])))
                
        d.valor_documento = "{0:0.2f}".format(fatura['valor_boleto'])

        d.especie_documento = "RC"             
        
        d.nosso_numero = fatura['numero_boleto']
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        listaDados.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO()
    boleto = BoletoPDF(output)
    for i in range(len(listaDados)):
        boleto.drawBoleto(
            listaDados[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)

def get_boleto_bradesco(faturas,remessa):
    listaDadosBradesco = []
    
    for fatura in faturas:
        d = BoletoBradesco(carteira=remessa['codigo_carteira'])
        d.carteira = remessa['codigo_carteira']  # Contrato firmado com o Banco Bradesco
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s - %(bairro)s - %(nome_cidade)s-%(uf)s - CEP: %(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia']
        d.conta_cedente = remessa['numero_conta']

        d.data_vencimento = fatura['data_vencimento']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ {0:0.2f}".format(fatura['abatimento']))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % ("{0:0.2f}".format(fatura['valor_fatura'])),
            "- Encargos: RS %s " % ("{0:0.2f}".format(fatura['valor_boleto']-fatura['valor_fatura'])),
            "- Total R$ %s " % ("{0:0.2f}".format(fatura['valor_boleto']))
            ]
                
        d.valor_documento = "{0:0.2f}".format(fatura['valor_boleto'])
        
        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto']
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        listaDadosBradesco.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO() 
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBradesco)):
        boleto.drawBoleto(
            listaDadosBradesco[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)


def get_boleto_bb(faturas,remessa):
    listaDadosBB = []
    
    for fatura in faturas:
        d = BoletoBB(7,2)
        d.carteira = remessa['codigo_carteira'][0:2]  # Contrato firmado com o Banco Brasil
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s - %(bairro)s - %(nome_cidade)s-%(uf)s - CEP: %(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia'].split('-')[0]
        d.conta_cedente = remessa['numero_conta'].split('-')[0]
        
        d.convenio = remessa['codigo_cedente']        

        d.data_vencimento = fatura['data_vencimento']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ {0:0.2f}".format(fatura['abatimento']))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % ("{0:0.2f}".format(fatura['valor_fatura'])),
            "- Encargos: RS %s " % ("{0:0.2f}".format(fatura['valor_boleto']-fatura['valor_fatura'])),
            "- Total R$ %s " % ("{0:0.2f}".format(fatura['valor_boleto']))
            ]

                
        #d.valor_documento = "{0:0.2f}".format(fatura['valor_fatura'])
        

        d.valor_documento = str(fatura['valor_boleto']).replace('.',',')
        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto'].lstrip('0')
        d.numero_documento = fatura['numero_fatura'][3:]
        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        
        listaDadosBB.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO() 
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBB)):
        boleto.drawBoleto(
            listaDadosBB[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)


def get_boleto_sicob(faturas,remessa):
    listaDadosBB = []
    
    for fatura in faturas:
        d = BoletoSicoob()
        ##d.carteira = remessa['codigo_carteira'][0:2]  
        d.carteira = '1'
        d.cedente = remessa['razao_social'].strip()
        d.cedente_documento = remessa['cnpj'].strip()

        d.cedente_endereco = "%(endereco)s - %(bairro)s - %(nome_cidade)s-%(uf)s - CEP: %(cep)s" % (remessa)
        d.agencia_cedente = remessa['numero_agencia'].split('-')[0]
        d.conta_cedente = remessa['numero_conta'].split('-')[0]
        
        d.convenio = remessa['codigo_cedente']        
        d.codigo_beneficiario = remessa['codigo_cedente'][-7:]        

        d.data_vencimento = fatura['data_vencimento']
        d.data_documento = fatura['data_processamento']
        d.data_processamento = fatura['data_processamento']

        #"{0:0.2f}".format(Decimal('119.41'))

        d.instrucoes = [
            "%(msg_multa)s%(msg_juros)s" % (fatura),
            remessa['instrucoes']
            ]
        if fatura['abatimento'] > 0:
            d.instrucoes.append("Conceder abatimento de R$ {0:0.2f}".format(fatura['abatimento']))

        d.demonstrativo = [
            "- Serviço Transporte: RS %s " % ("{0:0.2f}".format(fatura['valor_fatura'])),
            "- Encargos: RS %s " % ("{0:0.2f}".format(fatura['valor_boleto']-fatura['valor_fatura'])),
            "- Total R$ %s " % ("{0:0.2f}".format(fatura['valor_boleto']))
            ]

                
        #d.valor_documento = "{0:0.2f}".format(fatura['valor_fatura'])
        

        d.valor_documento = str(fatura['valor_boleto']).replace('.',',')
        d.especie_documento = "DS"             
        
        d.nosso_numero = fatura['numero_boleto'][-7:]
        d.numero_documento = fatura['numero_fatura'][3:]

        d.sacado = [
            fatura['fatura_nome'] + ' - ' + fatura['fatura_cnpj'],
            "%(fatura_endereco)s - %(fatura_bairro)s" % (fatura),
            "%(fatura_cidade)s-%(fatura_uf)s - CEP: %(fatura_cep)s" %(fatura)
            ]
        
        listaDadosBB.append(d)

    # Bradesco Formato carne - duas paginas por folha A4
    output = BytesIO() 
    boleto = BoletoPDF(output)
    for i in range(len(listaDadosBB)):
        boleto.drawBoleto(
            listaDadosBB[i]
        )
        boleto.nextPage()    
    boleto.save()
                      
    pdf_out = output.getvalue()
    output.close()
    
    return make_response(pdf_out)

