from app.schemas.fields import StringTrim
from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import validate, ValidationError

class SoftlogNotfisSchema(Schema):
    class Meta:
        type_ = 'softlog_notfis'
        self_view = 'softlog_notfis_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'softlog_notfis_list'

    id = fields.Integer(as_string=True, dump_only=True)
    
    serie_doc = StringTrim(required=True, validate=validate.Length(max=3))    
    numero_doc = StringTrim(required=True, validate=validate.Length(max=9))    
    chave_doc = StringTrim(validate=validate.Length(max=44))    
    data_emissao = fields.DateTime(required=True)
    valor = fields.Decimal(required=True, places=2, as_string=True)
    valor_produtos = fields.Decimal(places=2, as_string=True)
    peso = fields.Decimal(required=True, places=4, as_string=True)
    peso_liquido = fields.Decimal(places=4, as_string=True)
    volumes = fields.Integer(as_string=True, dump_only=True)
    volume_cubico = fields.Decimal(places=4, as_string=True)
    numero_pedido = StringTrim(validate=validate.Length(max=30))    
    natureza_carga = StringTrim(validate=validate.Length(max=30))    
    remetente_cnpj_cpf = StringTrim(required=True,validate=validate.Length(max=14))    
    remetente_nome = StringTrim(required=True,validate=validate.Length(max=50))    
    remetente_inscricao_estadual = StringTrim(validate=validate.Length(max=18))    
    remetente_endereco = StringTrim(required=True,validate=validate.Length(max=100))    
    remetente_numero = StringTrim(validate=validate.Length(max=50))    
    remetente_bairro = StringTrim(required=True,validate=validate.Length(max=30))    
    remetente_cod_mun_ibge = StringTrim(required=True,validate=validate.Length(max=7))    
    remetente_cep = StringTrim(required=True,validate=validate.Length(max=8))    
    remetente_email = StringTrim()    
    remetente_celular = StringTrim()    
    destinatario_nome = StringTrim(required=True,validate=validate.Length(max=50))  
    destinatario_cnpj_cpf = StringTrim(required=True,validate=validate.Length(max=14))    
    destinatario_inscricao_estadual = StringTrim(validate=validate.Length(max=18))    
    destinatario_endereco = StringTrim(required=True,validate=validate.Length(max=100))    
    destinatario_numero = StringTrim(validate=validate.Length(max=10))    
    destinatario_bairro = StringTrim(required=True,validate=validate.Length(max=30))    
    destinatario_cod_mun_ibge = StringTrim(required=True,validate=validate.Length(max=7))    
    destinatario_cep = StringTrim(required=True,validate=validate.Length(max=8))    
    destinatario_email = StringTrim()    
    destinatario_celular = StringTrim()    
    destinatario_whatsapp = StringTrim()
    data_registro = fields.DateTime()
    placa_veiculo = StringTrim(validate=validate.Length(max=8)) 
    frete_cif_fob = fields.Integer(as_string=True, dump_only=True)
    unidade = StringTrim(validate=validate.Length(max=10)) 
    rastreamento = StringTrim()
    user_api_id = fields.Integer(as_string=True,load_only=True)