import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey,Date, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.builder import Model

class Usuarios(Model):
    __tablename__ = 'usuarios'
    nome_usuario = Column(String(40))
    email = Column(String(50))
    senha = Column(String(30))
    login_name = Column(String(30))
    codigo_filial = Column(String(3))
    codigo_empresa = Column(String(3))
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__
