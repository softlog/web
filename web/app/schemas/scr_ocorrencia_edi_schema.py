from app.schemas.fields  import StringTrim
from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class ScrOcorrenciaEdiSchema(Schema):
    class Meta:
        type_ = 'scr_ocorrencia_edi'
        self_view = 'scr_ocorrencia_edi_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'scr_ocorrencia_edi_list'

    id = fields.Integer(as_string=True, dump_only=True)
    codigo_edi = fields.Integer(required=True, as_string=True)
    ocorrencia = StringTrim(required=True)


