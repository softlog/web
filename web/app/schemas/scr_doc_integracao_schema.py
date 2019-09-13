from app.schemas.fields import StringTrim

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class ScrDocIntegracaoSchema(Schema):
    class Meta:
        type_ = 'scr_doc_integracao'
        self_view = 'scr_doc_integracao_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'scr_doc_integracao_list'

    id = fields.Integer(as_string=True, dump_only=True)
    documento = StringTrim(required=True)    
    tipo_doc = fields.Integer(required=True, as_string=True)
    codigo_empresa = StringTrim()
    codigo_filial = StringTrim()
    data_recebimento = fields.DateTime()
    chave_doc = StringTrim()
    id_uid_imap = fields.Integer()

