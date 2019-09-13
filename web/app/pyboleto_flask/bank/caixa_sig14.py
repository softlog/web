# -*- coding: utf-8 -*-
## from pyboleto.data import BoletoData, CustomProperty
from app.pyboleto_flask.data import BoletoData, CustomProperty


class BoletoCaixaSig14(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal

    '''

    conta_cedente = CustomProperty('conta_cedente', 6)
    '''
        Este numero tem o inicio fixo
        Carteira SR: 80, 81 ou 82
        Carteira CR: 90 (Confirmar com gerente qual usar)

    '''
    nosso_numero = CustomProperty('nosso_numero', 15)

    def __init__(self):
        super(BoletoCaixaSig14, self).__init__()

        self.codigo_banco = "104"
        self.local_pagamento = "Preferencialmente nas Casas Lotéricas e \
Agências da Caixa"
        self.logo_image = "logo_bancocaixa.jpg"

    @property
    def dv_agencia_conta_cedente(self):
        conta_cedente = "%s" % (self.conta_cedente)
        dv = self.modulo11(conta_cedente)
        return dv

    @property
    def agencia_conta_cedente(self):
        resultado = "%s/%s-%s" % (self.agencia_cedente, self.conta_cedente,
                             self.dv_agencia_conta_cedente)        
        return resultado

    @property
    def dv_nosso_numero(self):
        resto2 =  self.modulo11('14' + self.nosso_numero, 9, 1)        
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):  # 24 digits
        nosso_numero = '14' + self.nosso_numero
        content = "%6s%1s%3s%1s%3s%1s%9s" % (
            self.conta_cedente.split('-')[0],
            self.modulo11(self.conta_cedente.split('-')[0]),
            nosso_numero[2:5],
            nosso_numero[0:1],
            nosso_numero[5:8],
            nosso_numero[1:2],
            nosso_numero[8:17]
        )
        dv_content = self.modulo11(content)

        return "%24s%1s" % (content, dv_content)

    def format_nosso_numero(self):
        return "14%s-%s" % (self.nosso_numero,str(self.dv_nosso_numero))
        #return self.nosso_numero + '-' + str(self.dv_nosso_numero)
