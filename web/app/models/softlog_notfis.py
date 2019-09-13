from sqlalchemy.sql import func
from sqlalchemy.orm import synonym
from app.sqla import Model, Base
from app.sqla.types import StrippedString
from decimal import Decimal


from app import db, app

 # db.Column(StrippedString(3))
 # db.Column(db.Numeric(15,2),server_default=)
 # db.Column(db.Integer)
 # db.Column(db.DateTime(timezone=True), server_default=func.now())

class SoftlogNotfis(db.Model):
    __tablename__ = 'softlog_notfis'

    id = db.Column(db.Integer,db.Sequence('softlog_notfis_id_seq'), primary_key=True )
    serie_doc = db.Column(StrippedString(3))
    numero_doc = db.Column(StrippedString(9))
    chave_doc = db.Column(StrippedString(44))
    data_emissao = db.Column(db.DateTime(timezone=True))
    valor = db.Column(db.Numeric(12,2),server_default="0.00")
    valor_produtos = db.Column(db.Numeric(12,2),server_default="0.00")
    peso = db.Column(db.Numeric(20,4), server_default="0.00")
    peso_liquido = db.Column(db.Numeric(20,4), server_default="0.00")
    volumes = db.Column(db.Integer, server_default="0")
    volume_cubico = db.Column(db.Numeric(16,4), server_default="0.00")
    numero_pedido = db.Column(StrippedString(30))
    natureza_carga = db.Column(StrippedString(30))
    remetente_cnpj_cpf = db.Column(StrippedString(14))
    remetente_nome = db.Column(StrippedString(50))
    remetente_inscricao_estadual = db.Column(StrippedString(18))
    remetente_endereco = db.Column(StrippedString(100))
    remetente_numero = db.Column(StrippedString(10))
    remetente_bairro = db.Column(StrippedString(30))
    remetente_cod_mun_ibge = db.Column(StrippedString(7))
    remetente_cep = db.Column(StrippedString(8))
    remetente_email = db.Column(db.Text)
    remetente_celular = db.Column(db.Text)
    destinatario_cnpj_cpf = db.Column(StrippedString(14))
    destinatario_nome = db.Column(StrippedString(50))
    destinatario_inscricao_estadual = db.Column(StrippedString(18))
    destinatario_endereco = db.Column(StrippedString(100))
    destinatario_numero = db.Column(StrippedString(10))
    destinatario_bairro = db.Column(StrippedString(30))
    destinatario_cod_mun_ibge = db.Column(StrippedString(7))
    destinatario_cep = db.Column(StrippedString(8))
    destinatario_email = db.Column(db.Text)
    destinatario_celular = db.Column(db.Text)
    destinatario_whatsapp = db.Column(db.Text)
    data_registro = db.Column(db.DateTime(timezone=True), server_default=func.now())
    placa_veiculo = db.Column(StrippedString(20))
    id_nota_fiscal_imp = db.Column(db.Integer)
    frete_cif_fob = db.Column(db.Integer, server_default='0')
    placa_veiculo = db.Column(StrippedString(10))
    rastreamento = db.Column(db.Text)
    user_api_id = db.Column(db.Integer)
