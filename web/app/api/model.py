# -*- coding: latin-1 -*-
#!/usr/bin/env python

from flask_restful import Resource, fields, marshal

filial_schema = {
    'codigo_filial': fields.String,
    'razao_social': fields.String,
    'nome_descritivo':fields.String,
    'email_principal':fields.String
}