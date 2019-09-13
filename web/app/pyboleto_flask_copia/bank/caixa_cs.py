# -*- coding: utf-8 -*-
from app.pyboleto_flask.data import BoletoData, CustomProperty

class BoletoCaixaCs(BoletoData):
    '''
        Gera Dados necessários para criação de boleto para o banco Caixa
        Economica Federal - Carteira CS
    '''

    conta_cedente = CustomProperty('conta_cedente', 19)
    '''
        Este numero tem o inicio fixo
    '''
    nosso_numero = CustomProperty('nosso_numero', 8)

    def __init__(self):
        super(BoletoCaixaCs, self).__init__()

        self.codigo_banco = "104"
        self.local_pagamento = "Preferencialmente nas Casas Lotéricas e \
Agências da Caixa"
        self.logo_image = "logo_bancocaixa.jpg"

    @property
    def dv_nosso_numero(self):
        resto2 = self.modulo11('9' + self.nosso_numero.split('-')[0], 9, 1)
        digito = 11 - resto2
        if digito == 10 or digito == 11:
            dv = 0
        else:
            dv = digito
        return dv

    @property
    def campo_livre(self):
        content = '8'  \
                  + self.nosso_numero.strip()   \
                  + self.agencia_cedente.strip() \
                  + self.conta_cedente[7:10] \
                  + self.conta_cedente[11:19]        
        return content

    def format_nosso_numero(self):
        return '8' + self.nosso_numero + '-' + str(self.dv_nosso_numero)

    @property
    def agencia_conta_cedente(self):
        resultado = self.conta_cedente[2:]
        return resultado
                             