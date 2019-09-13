import datetime
from flask import g, current_app, _app_ctx_stack 
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, Text, Numeric, Float 
from sqlalchemy.orm import relationship, backref, synonym
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.ext.declarative import declared_attr
from app.sqla import Model
from flask_login import UserMixin
from app._compat import as_unicode

_dont_audit = False


class Permission(Model):
    __tablename__ = 'ab_permission'   

    id = Column(Integer, Sequence('ab_permission_id_seq'), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)    

    def __repr__(self):
        return self.name

class ViewMenu(Model):
    __tablename__ = 'ab_view_menu'
    

    id = Column(Integer, Sequence('ab_view_menu_id_seq'), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and (self.name == other.name)

    def __neq__(self, other):
        return self.name != other.name

    def __repr__(self):
        return self.name


class PermissionView(Model):
    __tablename__ = 'ab_permission_view'    


    id = Column(Integer, Sequence('ab_permission_view_id_seq'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('ab_permission.id'))
    permission = relationship("Permission", innerjoin=False, lazy='joined')
    view_menu_id = Column(Integer, ForeignKey('ab_view_menu.id'))
    view_menu = relationship("ViewMenu",innerjoin=False, lazy='joined')

    def __repr__(self):
        return str(self.view_menu) + ': ' + str(self.permission).replace('_', ' ')


assoc_permissionview_role = Table('ab_permission_view_role', Model.metadata,
                                  Column('id', Integer, Sequence('ab_permission_view_role_id_seq'), primary_key=True),
                                  Column('permission_view_id', Integer, ForeignKey('ab_permission_view.id')),
                                  Column('role_id', Integer, ForeignKey('ab_role.id'))
)


class Role(Model):
    __tablename__ = 'ab_role'

    id = Column(Integer, Sequence('ab_role_id_seq'), primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    permissions = relationship('PermissionView', secondary=assoc_permissionview_role, backref='role', innerjoin=False, lazy='joined')

    def __repr__(self):
        return self.name


assoc_user_role = Table('ab_user_role', Model.metadata,
                                  Column('id', Integer, Sequence('ab_user_role_id_seq'), primary_key=True),
                                  Column('user_id', Integer, ForeignKey('v_usuarios.id_usuario')),
                                  Column('role_id', Integer, ForeignKey('ab_role.id'))
)

#assoc_user_filial = Table('ab_user_filial', Model.metadata,
#                                  Column('id', Integer, Sequence('ab_user_filial_id_seq'), primary_key=True),
#                                  Column('user_id', Integer, ForeignKey('v_usuarios.id_usuario')),
#                                  Column('filial_id', Integer, ForeignKey('filial.id_filial'))
#)

class User(UserMixin, Model):    
    __tablename__ = 'v_usuarios'

    id_usuario = Column(Integer, Sequence('usuarios_id_usuario_seq'), primary_key=True)
    nome_usuario = Column(String(40))
    email = Column(String(50))
    senha = Column(String(30))
    login_name = Column(String(30))
    codigo_filial = Column(String(3))
    codigo_empresa = Column(String(3))
    ativo = Column(Integer())
    email = Column(String(64), unique=True, nullable=False)
    categoria = Column(Integer())
    roles = relationship('Role', secondary=assoc_user_role, backref='user', innerjoin=False, lazy='joined')
    
    
    #Compatibilizacao de esquema para o periodo de transicao,
    #ate migrar para nova estrutura de tabela de usuario
    id = Column(Integer())
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64), unique=True)
    password = Column(String(256))
    active = Column(Boolean)    
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=True)
    changed_on = Column(DateTime, default=datetime.datetime.now, nullable=True)
    created_by_fk = Column(Integer)
    changed_by_fk = Column(Integer)    

    def check_password(self, password):
        return password.strip() == self.senha.strip()
        uri = getattr(_app_ctx_stack.top,'uri_login',None)
        current_app.config['SQLALCHEMY_DATABASE_URI_' + (user.id_user_db_tny).upper()] = uri

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception as e:
            return None

    #def is_authenticated(self):
    #    return True
       


    #def is_active(self):
    #    return self.active

    #def is_anonymous(self):
    #    return False

    def get_id(self):
        return as_unicode(self.id_usuario)

    ##def get_id_tny(self):
    ##    return as_unicode(self.id_user_db_tny)

    #def get_full_name(self):
    #   return u'{0} {1}'.format(self.first_name, self.last_name)
   
    
    def __repr__(self):
        return self.nome_usuario


class RegisterUser(Model):
    __tablename__ = 'ab_register_user'
    id = Column(Integer, Sequence('ab_register_user_id_seq'), primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256))
    email = Column(String(64), nullable=False)
    registration_date = Column(DateTime, default=datetime.datetime.now, nullable=True)
    registration_hash = Column(String(256))

# TODO Criar Classe para String de Conexoes

class StringConexoes(Model):
    __tablename__ = 'string_conexoes'
    __bind_key__  = 'pg_db_main'

    id_string_conexao = Column(Integer,Sequence('string_conexoes_id_string_conexao_seq'),primary_key=True)
    banco_dados = Column(String(50))
    usuario = Column(Text)
    senha = Column(Text)
    cliente_ativo = (Integer)
    port = Column(Text)
    host = Column(Text)
    softlog_web = Column(Integer)
    softlog_integracao = Column(Integer)

    def db_uri_pg(self):
        """
            Retorna URI para acesso a DATABASE Postgresql
        """
        uri = 'postgresql://%s:%s@%s:%s/%s' % (self.usuario,
                                               self.senha,
                                               self.host,
                                               self.port,
                                               str(self.banco_dados).strip())
        return uri.strip()


#class Edi_parceiros(Model):
#    __tablename__ = 'edi_parceiros'
#    __bind_key__  = 'pg_db_main'

#    id = Column(Integer,Sequence('edi_parceiros_id_seq'), primary_key=True)
#    id_bd = Column(Integer, ForeignKey('string_conexoes.id_string_conexao'))
#    cnpj_cpf = Column(String(14))
