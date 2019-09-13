# -*- coding: latin-1 -*-
#!/usr/bin/env python
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from flask_restful import Api, Resource, reqparse, marshal
from psycopg2.extras import DictCursor
from app import query_db, get_db 

from marshmallow import ValidationError

fila_softlog = Blueprint('fila_softlog',__name__)

api = Api(fila_softlog)


class StatusFilas(Resource):
    
    def get(self):
        """Rotina que consulta se há documentos disponíveis nos parceiros"""
        #print("PESQUISANDO MOVIMENTOS: ")
        parser = reqparse.RequestParser()
        parser.add_argument('id_db',type=int,help='O parâmetro Id_db inválido.')
        parser.add_argument('data',type=str,help='O parâmetro Data é inválido.')
        parser.add_argument('cnpj',type=str,help='O parâmetro CNPJ é inválido.')
        parser.add_argument('acesso',type=str,help='O parâmetro Acesso é inválido.')

        args = parser.parse_args()               
        
        response = movimentos
        return response




api.add_resource(StatusFilas,'/status')

