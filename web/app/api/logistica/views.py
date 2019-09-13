# -*- coding: latin-1 -*-
#!/usr/bin/env python
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from flask_restful import Api, Resource, reqparse, marshal, abort
from psycopg2.extras import DictCursor
from app import query_db, get_db 
from app.api.model import filial_schema
from app.util import calcula_hash


from app.api.logistica.documentos import Usuarios, Romaneios, Imagens, Trackings
from app.api.logistica.model.ocorrencias import Ocorrencias
from app.api.logistica.model.notas_fiscais import NotasFiscaisModel
from app.api.logistica.model.veiculos import VeiculosModel
from app.api.logistica.model.motoristas import MotoristaModel
from app.api.logistica.model.protocolos import ProtocolosModel
from app.api.logistica.model.romaneios_app import RomaneiosAppModel
from app.api.logistica.model.regiao_cidades import RegiaoCidadesModel
from app.api.logistica.model.vuupt import VuuptModel

#from app import get_db, close_conection 

from marshmallow import ValidationError

softlog = Blueprint('softlog',__name__)

api = Api(softlog)


class Hello(Resource):

    def get(self):                    
        """Retorna Hello World"""
       
        return "Hello World" 

class Usuario(Resource):

    def get(self, codigo_acesso, login):                    
        """Retorna Dados do Usuario"""       
        #parser = reqparse.RequestParser()
        #parser.add_argument('codigo_acesso',type=int,help='Codigo de acesso obrigatório')
        #parser.add_argument('login',type=str,help='Login do usuário obrigatório')

        #args = parser.parse_args()
        
        r = Usuarios.get_user(login,codigo_acesso)

        if r is None:
            abort(404, message="Usuário {} não existe".format(login))
        else:
            return r, 200

class Usuario2(Resource):
    def get(self, codigo_acesso, cpf):
        r = Usuarios.get_user_fornecedor(cpf,codigo_acesso)

        if r is None:
            abort(404, message="Usuário {} não existe".format(cpf))
        else:
            return r, 200

class Protocolo(Resource):

    def get(self,codigo_acesso,data_expedicao,id_nf_protocolo):
        """Retorna lista de protocolos"""

        o = ProtocolosModel()

        r = o.get_protocolo(data_expedicao,id_nf_protocolo,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de protocolos")
        else:
            return r, 200


class Protocolo2(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('conferencias',type=str,help='O parâmetro conferências é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        conferencias = args.get('conferencias')
        #print(args.get('conferencias'))

        o = ProtocolosModel()
        r = o.setConferenciaProtocolo(codigo_acesso,conferencias)

        if r is None:
            abort(404, message="Não há documentos disponíveis.")

        return {"resultado":"Ok"}


class NotasFiscais(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

        parser.add_argument('tipo_busca',
                                type=int,
                                required=True, 
                                help='O parâmetro tipo_busca é inválido.')

        parser.add_argument('id_protocolo',
                                type=int,
                                help='O parâmetro id_protocolo é inválido.')

        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        id_protocolo = args.get('id_protocolo')
        tipo_busca = args.get('tipo_busca')
        #print(args.get('conferencias'))

        o = NotasFiscaisModel()
        if tipo_busca == 1:
            r = o.get_nota_fiscal_by_protocolo(id_protocolo,codigo_acesso)
        else:
            abort(404,'Tipo de Busca inexistente.')

        if r is None:
            abort(404, message="Não há documentos disponíveis.")
    
        return r,200

class Veiculos(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = VeiculosModel()
        r = o.get_veiculos(codigo_acesso)

        if r is None:
            abort(404, message="Não há veiculos registrados.")
    
        return r,200

class RegiaoCidades(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = RegiaoCidadesModel()
        r = o.get(codigo_acesso)

        if r is None:
            abort(404, message="Não há cidades com regiao na base de dados.")

        resposta = json.loads(r)

        h = calcula_hash(r)
        d = {
                    'data':resposta,
                    'ETag':h
            }

        h1 = request.headers.get('ETag')
        print(h1)
        if (h==h1):
            d = {
                'data':{'cidades':[], 'regioes':[]},
                'ETag':h
            }
                 
        return d,200
  
class Motoristas(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = MotoristaModel()
        r = o.get_motoristas(codigo_acesso)

        if r is None:
            abort(404, message="Não há motoristas registrados.")
    
        return r,200

class RomaneiosApp(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('romaneios',type=str,help='O parâmetro romaneios é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        romaneios = args.get('romaneios')
        #print(args.get('conferencias'))

        o = RomaneiosAppModel()
        r = o.set(codigo_acesso,romaneios)
        
        if r is None:
            abort(404, message="Nao foi possivel gravar documentos")
        else:
            return {"resultado":"Ok"}, 200


class Romaneio(Resource):

    def get(self,codigo_acesso,data,cpf_motorista):
        """Retorna lista de protocolos"""      
                
        r = Romaneios.get_romaneios2(cpf_motorista,data,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de romaneios")
        else:
            return r, 200

class Romaneio2(Resource):

    def get(self,codigo_acesso,data,cpf_motorista):
        """Retorna lista de protocolos"""      
                
        r = Romaneios.get_romaneios2(cpf_motorista,data,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de romaneios")
        else:
            return r, 200


class Ocorrencia(Resource):

    def get(self,codigo_acesso):
        """Retorna lista de ocorrências"""      
                
        r = Ocorrencias.getOcorrencias(codigo_acesso)

        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return r, 200


class Ocorrencias2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('ocorrencias',type=str,help='O parâmetro ocorrencias é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        ocorrencias = args.get('ocorrencias')
        #print(args.get('conferencias'))

        r = Ocorrencias.setOcorrencias(codigo_acesso,ocorrencias)
        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return {"resultado":"Ok"}, 200
        

class Imagem(Resource):
        
    def get(self,codigo_acesso,imagem):
        
        r = Imagens.getImagem(codigo_acesso,imagem)

        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return r, 200

class Imagem2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('imagens',type=str,help='O parâmetro imagens é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        imagens = args.get('imagens')
        #print(args.get('conferencias'))

        r = Imagens.setImagens(codigo_acesso,imagens)

        if r is None:
            abort(404, message="Ocorreu um erro ao persistir informacoes")

        return {"resultado":"Ok"}

class Tracking(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('tracking',type=str,help='O parâmetro tracking é inválido.')

        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        tracking = args.get('tracking')
        #print(args.get('conferencias'))

        r = Trackings.setTracking(codigo_acesso,tracking)

        if r is None:
            abort(404, message="Ocorreu um erro ao persistir informacoes")
        
        return {"resultado":"Ok"}

class VuuptOcorrencia(Resource):
    def post(self):
        
        # data in string format and you have to parse into dictionary
        data = request.data.decode()
        #dataDict = json.loads(data)
        print(data)
        
        
        VuuptModel.set_vuupt_ocorrencias(self,53, data)
        return {"resultado":"Ok"}

api.add_resource(Hello,'/hello')
api.add_resource(Usuario,'/usuario/<int:codigo_acesso>/<login>')
api.add_resource(Usuario2,'/usuario2/<int:codigo_acesso>/<cpf>')
api.add_resource(Protocolo,'/protocolo/<int:codigo_acesso>/<data_expedicao>/<int:id_nf_protocolo>')
api.add_resource(Protocolo2,'/protocolo')
##api.add_resource(NotasFiscais,'/notasromaneio/<int:codigo_acesso>/<int:id_protocolo>')
api.add_resource(NotasFiscais,'/notasromaneio')
api.add_resource(Veiculos,'/veiculos')
api.add_resource(RegiaoCidades,'/regiao_cidades')
api.add_resource(Motoristas,'/motoristas')
api.add_resource(RomaneiosApp,'/romaneiosapp')
api.add_resource(Romaneio,'/romaneio/<int:codigo_acesso>/<data>/<cpf_motorista>')
api.add_resource(Romaneio2,'/romaneio2/<int:codigo_acesso>/<data>/<cpf_motorista>')
api.add_resource(Ocorrencia,'/ocorrencia/<int:codigo_acesso>')
api.add_resource(Ocorrencias2,'/ocorrencia')
api.add_resource(Imagem2,'/imagem')
api.add_resource(Tracking,'/tracking')
api.add_resource(VuuptOcorrencia,'/vuupt/ocorrencias')
