from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, Text, Numeric, Float 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from app.sqla import Model

class Banco(Model):
    __tablename__ = 'banco'
    nome_banco = Column(String(40))
    id_banco = Column(Integer,Sequence('banco_id_banco_seq'), primary_key=True)
    numero_banco = Column(String(3))

    def __repr__(self):
        return self.nome_banco.strip() + " - " + self.numero_banco