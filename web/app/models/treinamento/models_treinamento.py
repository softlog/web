import datetime
from flask import g, current_app
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, Text, Numeric, Float, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from app.sqla import Model
from app._compat import as_unicode

#Classes para manipular Modelo de Dados
from app import db
from app.sqla.interface import SQLAInterface
from app.sqla.models.filters import BaseFilterConverter
from app.sqla.models.filters import Filters
from app.sqla.filters import *
from app import query_db, execute_db
from app.models.gerais import Cidades


class Clientes(Model):
    __tablename__ = 'cliente'

    codigo_cliente = Column(Integer,Sequence('cliente_codigo_cliente_seq'), primary_key=True)
    nome_cliente = Column(String(40))
    cnpj_cpf =  Column(String(18))
    id_cidade = Column(Integer(), ForeignKey('cidades.id_cidade'))
    cidade = relationship("Cidades2")
    #notas_fiscais = relationship("NotasFiscais", back_populates="remetente")

    def __repr__(self):
        return self.nome_cliente

class Cidades2(Cidades):
    pass


class NotasFiscais(Model):
    __tablename__ = 'scr_notas_fiscais_imp'

    id_nota_fiscal_imp = Column(Integer,Sequence('scr_notas_fiscais_imp_id_nota_fiscal_imp_seq'), primary_key=True)
    chave_nfe = Column(String(44))
    numero_nota_fiscal = Column(String(9))
    serie_nota_fiscal = Column(String(3))
    data_emissao = Column(DateTime())
    remetente_id = Column(Integer, ForeignKey('cliente.codigo_cliente'))
    destinatario_id = Column(Integer, ForeignKey('cliente.codigo_cliente'))
    remetente = relationship("Clientes", foreign_keys=[remetente_id] )
    destinatario = relationship("Clientes", foreign_keys=[destinatario_id] )
    frete_cif_fob = Column(Integer)
    valor = Column(Numeric(12,2))
    consignatario_id = Column(Integer, ForeignKey('cliente.codigo_cliente'))
    consignatario = relationship("Clientes",foreign_keys=[consignatario_id])
    calculado_de_id_cidade = Column(Integer,ForeignKey("cidades.id_cidade"))
    origem = relationship("Cidades",foreign_keys=[calculado_de_id_cidade])
    calculado_ate_id_cidade = Column(Integer,ForeignKey("cidades.id_cidade"))
    destino = relationship("Cidades",foreign_keys=[calculado_ate_id_cidade])
    redespachador_id = Column(Integer)
    id_motorista = Column(Integer)

    def __repr__(self):

        if self.chave_nfe:
            return self.chave_nfe
        else:
            return ""

    def frete_cif_fob_desc(self):

        if self.frete_cif_fob == 1:
            return "CIF"
        else:
            return "FOB"


class Regiao(Model):
    __tablename__ = "regiao"

    id_regiao = Column(Integer(),Sequence('regiao_id_regiao_seq'),primary_key=True )
    descricao = Column(String(35))
    id_cidade_polo = Column(Integer(), ForeignKey("cidades.id_cidade"))
    cidade = relationship(Cidades)

    def __repr__(self):
        return self.descricao or ""

if __name__ == '__main__':

    model_nf = SQLAInterface(NotasFiscais,db.session)

    nf = model_nf.get(477224)

    model_regiao = SQLAInterface(Regiao, db.session)

    qt, regioes = model_regiao.query()

    for regiao in regioes:
        #regiao.descricao = regiao.descricao.upper()
        #model_regiao.edit(regiao)
        print(regiao.descricao)




