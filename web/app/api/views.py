# -*- coding: latin-1 -*-
#!/usr/bin/env python
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from flask_restful import Api, Resource, reqparse, marshal
from psycopg2.extras import DictCursor
from app import query_db
from app.api.model import filial_schema


#from app import get_db, close_conection 

from marshmallow import ValidationError

logistica = Blueprint('logistica',__name__)

api = Api(logistica)

class Empresas(Resource):

    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O parâmetro Id_db inválido.')
        parser.add_argument('token',type=str,help='O parâmetro Token inválido.')
        parser.add_argument('dados',type=str,help='O parâmetro Dados inválido.')

        args = parser.parse_args()
        
        id_db = args['id_db']
        
        dados = json.loads(args['dados'])
        
        #db = get_db(args['id_db'])
        filial = query_db(args['id_db'],'SELECT row_to_json(filial) as json FROM filial  WHERE codigo_filial = %(filial)s AND codigo_empresa = %(empresa)s',dados,True)

        empresa = query_db(args['id_db'],'SELECT * FROM empresa')

        #print(str(db.status))               
        return filial['json']
        return marshal(filial,filial_schema),200

        #dsn ='dbname=softlog user=softlog port=5435 password=paulino host=localhost'
        #conn = psycopg2.connect(dsn)
        #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        #cursor.execute("SELECT row_to_json(filial,true)::text as dados FROM filial")
        #r = cursor.fetchone()        
        #resp = make_response(r['dados'])
        #cursor.close()
        #conn.close()
        #return resp 


class dashEmissoes(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        #parser.add_argument('alias_db',type=str,help='O parâmetro Id_db inválido.')

        #args = parser.parse_args()
        
        #alias_db = args['alias_db']
        
        #dados = json.loads(args['dados'])
        
        #db = get_db(args['id_db'])
        #resultado = query_db(args['alias_db'],'SELECT * FROM f_get_dash_emissoes();')

        records = [
            { 'titulo': 'Total de Emissões', 'valor': 70, 'serie': "34, 42, 12, 67, 32, 23, 56,34, 42, 12, 67, 32, 23, 56,34, 42, 12, 67, 32, 23, 56" },
            { 'titulo': 'Total de CTe', 'valor': 35, 'serie': "34, 42, 12, 67, 32, 23, 56,34, 42, 12, 67, 32, 23, 56,34, 42, 12, 67, 32, 23" },
            { 'titulo': 'Total de Minutas', 'valor': 35, 'serie': "34, 42, 12, 67, 32, 23, 56,34, 42, 12, 67, 32, 23, 56,23, 56,34, 42, 12, 67, 32, 23," },
            { 'titulo': 'Total de Minutas', 'valor': 100, 'serie': "34, 42, 12, 67, 32, 23, 56,34, 42, 12,23, 56,34, 42, 12, 67, 32, 23, 67, 32, 23, 56, 32, 23, 67, 32, 23, 56" }
        ]       
       
        resultado = {'records':records}
        #print(str(db.status))  
        return resultado
 
    

api.add_resource(dashEmissoes,'/dashemissoes.json')


