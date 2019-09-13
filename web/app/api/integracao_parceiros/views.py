# -*- coding: latin-1 -*-
#!/usr/bin/env python
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from flask_restful import Api, Resource, reqparse, marshal
from psycopg2.extras import DictCursor
from app import query_db, get_db 
from app.api.model import filial_schema


from app.api.integracao_parceiros.documentos import Documentos

#from app import get_db, close_conection 

from marshmallow import ValidationError

logistica = Blueprint('logistica',__name__)

api = Api(logistica)

class Set_edi_parceiros(Resource):
    
    def post(self):
        #Consulta todos banco de dados
        qry_db = """
            SELECT 
                id_string_conexao, 
                usuario,
                senha,
                port,
                host, 
                banco_dados
            FROM 
                string_conexoes 
            WHERE 
                softlog_integracao = 1
        """
        dbs = query_db(1,qry_db)
               
        lista_filial = []
        for db in dbs:
            qry_filial = """
                SELECT cnpj, trim(razao_social) as razao_social FROM filial 
            """
            filiais = query_db(db['id_string_conexao'],qry_filial)
            for f in filiais:
                lista_filial.append(f)
                qry_parceiro = """
                                    SELECT 
                                        id 
                                    FROM 
                                        edi_parceiros 
                                    WHERE 
                                        cnpj_cpf = '%s'
                                        AND id_bd = %i
                              """ % (f['cnpj'],db['id_string_conexao'])

                parceiro = query_db(1,qry_parceiro)                
                if len(parceiro) == 0:
                    #print('Cadastrando parceiro!')
                    upd_parceiro = """
                        INSERT INTO edi_parceiros (id_bd, cnpj_cpf, razao_social)
                        VALUES (%i,'%s','%s')
                    """ % (db['id_string_conexao'],f['cnpj'],f['razao_social'])

                    db_main = get_db(1)
                    cur = db_main.cursor()                    
                    cur.execute(upd_parceiro)
                    cur.close()
                    db_main.commit()
        
        return lista_filial

class Documentos_disponiveis(Resource):
    
    def get(self):
        """Rotina que consulta se ha documentos disponiveis nos parceiros"""
        #print("PESQUISANDO MOVIMENTOS: ")
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O parametro Id_db invalido.')
        parser.add_argument('data',type=str,help='O parametro Data e invalido.')
        parser.add_argument('cnpj',type=str,help='O parametro CNPJ e invalido.')
        parser.add_argument('acesso',type=str,help='O parametro Acesso e invalido.')

        args = parser.parse_args()
        
        

        id_db = int(args['id_db'])
        data = args['data']
        cnpj = args['cnpj']
        acesso = args['acesso']
                
        movimentos = Documentos.get_docs_disponiveis(id_db,cnpj,data,acesso)

        
        #print("MOVIMENTOS: ", movimentos)
        response = movimentos
        return response

    def post(self):
        """Comentario"""
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O parametro Id_db invalido.')
        parser.add_argument('lst_notas',type=str,help='O parametro Notas e invalido.')
        parser.add_argument('tp_romaneio',type=int,help='O parametro tp_romaneio e invalido.')

        args = parser.parse_args()
        
        id_db = int(args['id_db'])
        lst_notas = args['lst_notas']        
        tp_romaneio = int(args['tp_romaneio'])
        
        try:
            nfes = Documentos.get_json_notas(id_db,lst_notas,tp_romaneio)
        except Exception as e:
            nfes = None 
        
                
        return nfes


    def put(self):
        """Comentario"""
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O parametro Id_db invalido.')
        parser.add_argument('dados',type=str,help='O parametro Dados e invalido.')
        parser.add_argument('empresa',type=str,help='O parametro Empresa e invalido.')
        parser.add_argument('filial',type=str,help='O parametro Filial e invalido.')
        parser.add_argument('id_usuario',type=str,help='O parametro Id Usuario e invalido.')
        parser.add_argument('id_db_origem',type=int,help='O parametro Id_db_origem e invalido.')
        parser.add_argument('tp_romaneio',type=int,help='O parametro tp_romaneio e invalido.')
        
        args = parser.parse_args()
        
        id_db = int(args['id_db'])
        dados = args['dados']        
        empresa = args['empresa']
        filial = args['filial']
        id_usuario = args['id_usuario']
        id_db_origem = args['id_db_origem']
        tp_romaneio = int(args['tp_romaneio'])
        
        try:
            resultado = Documentos.insere_nf(id_db,dados,id_usuario,empresa,filial,id_db_origem,tp_romaneio)
        except Exception as e:
            resultado = None
                
        return resultado 



class ClientesResource(Resource):
    
    def post(self):
        """Comentario"""
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O par�metro Id_db inv�lido.')
        parser.add_argument('lst_clientes',type=str,help='O par�metro Data � inv�lido.')
        parser.add_argument('tp_romaneio',type=int,help='O par�metro tp_romaneio � inv�lido.')
        
        args = parser.parse_args()
        
        id_db = int(args['id_db'])
        lst_clientes = args['lst_clientes']        
        tp_romaneio = args['tp_romaneio']
        
        try: 
            clientes = Documentos.get_json_clientes(id_db,lst_clientes)
        except Exception as e:
            #print('Ocorreu um erro: ', str(e.args))
            clientes = None
                
        return clientes 

    def put(self):
        """Comentario"""
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O par�metro Id_db inv�lido.')
        parser.add_argument('dados',type=str,help='O par�metro Dados � inv�lido.')
        parser.add_argument('tp_romaneio',type=int,help='O par�metro tp_romaneio � inv�lido.')
        
        args = parser.parse_args()
        
        id_db = int(args['id_db'])
        dados = args['dados']        
        
        try:
            resultado = Documentos.insere_clientes(id_db,dados)
        except Exception as e:
            resultado = None  
        return resultado 

class ChaveCte(Resource):


    def post(self):
            
        """Rotina que consulta se h� conhecimentos emitidos no parceiro"""
        parser = reqparse.RequestParser()                
        parser.add_argument('redespachador_cnpj',type=str,help='O par�metro redespachador_cnpj � inv�lido.')
        parser.add_argument('parceiro_cnpj',type=str,help='O par�metro parceiro_cnpj � inv�lido.')
        parser.add_argument('lst_id_nfs',type=str,help='O par�metro lst_id_nfs � inv�lido.')
        
        args = parser.parse_args()
                
        try:            
            resultado = Documentos.get_chaves_cte(args['lst_id_nfs'], args['parceiro_cnpj'], args['redespachador_cnpj'])
        except Exception as e:            
            resultado = ''
                    
        return resultado 


class BaixaEntregaNfe(Resource):

    def post(self):                    
        """Rotina que consulta se h� conhecimentos emitidos no parceiro"""
        parser = reqparse.RequestParser()                
        parser.add_argument('cnpj_transportadora',type=str,help='O parametro redespachador_cnpj e invalido.')
        parser.add_argument('id_nota_fiscal',type=int,help='O parametro id_nota_fiscal e invalido.')
        parser.add_argument('tp_doc',type=int,help='O parametro tp_doc e invalido.')
        parser.add_argument('id_ocorrencia',type=int,help='O parametro id_ocorrencia e invalido.')
        parser.add_argument('canhoto',type=int,help='O parametro canhoto e invalido.')
        parser.add_argument('entrega_realizada',type=int,help='O parametro entrega_realizada e invalido.')
        parser.add_argument('data_ocorrencia',type=str,help='O parametro data_ocorrencia e invalido.')
        parser.add_argument('nome_recebedor',type=str,help='O parametro nome_recebedor e invalido.')
        parser.add_argument('doc_recebedor',type=str,help='O parametro doc_recebedor e invalido.')        
        
        args = parser.parse_args()
        
        Documentos.set_baixa_entrega_nfe(args)

        return "Realizando Baixa de Entregas" 



api.add_resource(Set_edi_parceiros,'/set_edi_parceiros')
api.add_resource(Documentos_disponiveis,'/documentos_disponiveis')
api.add_resource(ChaveCte,'/chave_cte')
api.add_resource(ClientesResource,'/clientes')
api.add_resource(BaixaEntregaNfe,'/baixa_entrega_nfe')

