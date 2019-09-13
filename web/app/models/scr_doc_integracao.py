from sqlalchemy.sql import func
from sqlalchemy.orm import synonym
from app.sqla import Model, Base

from app import db, app


class ScrDocIntegracao(db.Model):
    __tablename__ = 'scr_doc_integracao'
    
    id_doc_integracao = db.Column(db.Integer,db.Sequence('scr_doc_integracao_id_doc_integracao_seq'), primary_key=True )
    id = synonym('id_doc_integracao')
    doc_xml = db.Column(db.Text, index=True) 
    documento = synonym('doc_xml')
    tipo_doc = db.Column(db.Integer)
    codigo_empresa = db.Column(db.String(3))
    codigo_filial = db.Column(db.String(3))
    data_recebimento = db.Column(db.DateTime(timezone=True), server_default=func.now())
    chave_doc = db.Column(db.String(44))
    id_uid_imap = db.Column(db.Integer)




