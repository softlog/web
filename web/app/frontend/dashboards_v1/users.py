"""
    Classe que implementa o callback do modulo Flask-Login
    Autor: Paulo Sergio Alves
"""

from flask_login import UserMixin
from app import query_db

class User(UserMixin):
    password = None
    email = None
    id_usuario = None
    nome_usuario = None
    
    def __init__(self, id):
        self.id = id        

        cmd = """SELECT 
                id_usuario,
                trim(nome_usuario) as nome_usuario,
                trim(email) as email,     
                trim(login_name) as login,
                senha
           FROM 
                usuarios
           WHERE 
                login_name = '%s' 
        """ % self.id.split(':')[0]

        r = query_db('softlog_' + id.split(':')[1], cmd, None, True)

        if r is not None:
            self.password     = r['senha']
            self.email        = r['email']
            self.id_usuario   = r['id_usuario']
            self.nome_usuario = r['nome_usuario']

    #def __repr__(self):
    #    return "%d/%s/%s" % (self.id, self.name, self.password)


