import datetime
from flask import g, current_app 
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Sequence, Text, Numeric, Float, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declared_attr
from app.sqla import Model
from app._compat import as_unicode



_dont_audit = False

class ClientesBaseSefaz(Model):
    __tablename__ = 'v_base_sefaz_transporte'

    id = Column(Integer,primary_key=True)    
    cnpj = Column(String(14))
    razao_social = Column(String(200))
    nome_fantasia = Column(String(200))
    situacao = Column(String(2))
    endereco = Column(String(100))
    numero = Column(String(30))    
    bairro = Column(String(100))
    uf = Column(String(2))
    codigo_municipio = Column(String(4),  ForeignKey('cidades_serpro.codigo_serpro'))
    nome_cidade = Column(String(100))
    #cidade = relationship("CidadesSerpro", foreign_keys=[codigo_municipio] )
    cep = Column(String(8))
    telefones = Column(String(200))
    email = Column(Text())
    cnae = Column(String(10))
    inicio_atividade = Column(Date())

class CidadesSerpro(Model):
    __tablename__ = 'cidades_serpro'

    id = Column(Integer,primary_key=True)
    codigo_serpro = Column(String(4))
    nome_cidade = Column(String(100))
    uf = Column(String(2))
    
    def __repr__(self):
        return self.nome_cidade


class Cidades(Model):
    __tablename__ = 'cidades'

    id_cidade = Column(Integer,Sequence('cidades_id_cidade_seq'), primary_key=True)
    sigla_cidade = Column(String(3))
    nome_cidade = Column(String(50))
    uf = Column(String(2))
    id_regiao = Column(Numeric(5,0))
    praca_especial = Column(Numeric(1,0))
    data_alteracao = Column(DateTime)
    filial_cidade = Column(String(3))
    cod_ibge = Column(String(7))
    codigo_pais = Column(String(5))
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    zoom = Column(Integer)
    ddd_padrao = Column(String(2))
    id_aeroporto_padrao = Column(Integer)
    id_agente_redespacho_padrao = Column(Integer)
    id_cidade_retirada = Column(Integer)
    ent_seg = Column(Integer)
    ent_ter = Column(Integer)
    ent_qua = Column(Integer)
    ent_qui = Column(Integer)
    ent_sex = Column(Integer)
    ent_sab = Column(Integer)
    ent_dom = Column(Integer)    

    def __repr__(self):
        return self.nome_cidade.strip() + '-' + self.uf


class Empresa(Model):
    __tablename__ = 'empresa'

    id_empresa = Column(Integer,primary_key=True)
    codigo_empresa = Column(String(3))
    cnpj = Column(String(14))
    razao_social = Column(String(50))
    nome_fantasia = Column(String(50))
    inscricao_estadual = Column(String(15))
    #id_cidade = Column(Integer, ForeignKey('cidades.id_cidade'))
    #cidade     = relationship("Cidade")

    def __repr__(self):
        return self.razao_social



class Filial(Model):
    __tablename__ = 'filial'

    id_filial = Column(Integer,primary_key=True)
    codigo_filial = Column(String(3))
    codigo_empresa = Column(String(3))
    cnpj = Column(String(14))
    razao_social = Column(String(50))
    codigo_filial = Column(String(50))
    endereco = Column(String(50))
    numero = Column(String(10))
    bairro = Column(String(30))
    cep = Column(String(8))
    estado = Column(String(2))
    ddd = Column(String(2))
    telefone = Column(String(8))
    fax = Column(String(8))
    email_principal = Column(String(50))
    nome_descritivo = Column(String(50))
    id_cidade = Column(Integer, ForeignKey('cidades.id_cidade'))
    sigla = Column(String(4))
    cidades = relationship("Cidades")
    ativa = Column(Integer)

    def get_endereco_completo(self):
        return self.endereco.strip().title() + ', ' + \
                self.numero.strip() + ', ' + \
                self.bairro.strip().title() + ', ' + \
                self.cidades.nome_cidade.strip().title() + '-' + \
                self.cidades.uf + ' - ' + \
                self.cep 

    def __repr__(self):
        return self.codigo_empresa + '-' + self.codigo_filial + ' ' + self.razao_social



class Cliente(Model):
    __tablename__ = 'cliente'

    codigo_cliente = Column(Integer,Sequence('cliente_codigo_cliente_seq'), primary_key=True)
    cnpj_cpf = Column(String(18))
    nome_cliente = Column(String(50))
    nome_fantasia = Column(String(50))
    inscricao_estadual = Column(String(18))
    ddd = Column(String(2))
    telefone = Column(String(8))
    fax = Column(String(8))
    cnpj_cpf_responsavel = Column(String(18))
    classe_cliente = Column(String(1))
    tipo_frete = Column(String(1))
    tabela_padrao = Column(String(13))
    devolver_canhoto = Column(Integer)
    frequencia_faturamento = Column(String(1))
    prazo_pagamento = Column(Numeric(2,0))
    desconto_fatura_percentual = Column(Numeric(5,2))
    desconto_fatura_dias = Column(Numeric(2,0))
    percentual_devolucao = Column(Numeric(5,1))
    percentual_reentrega = Column(Numeric(5,1))
    filial_responsavel = Column(String(3))
    filial_cadastro = Column(String(3))
    codigo_vendedor = Column(String(3))
    desc_frete_minimo = Column(Numeric(5,1))
    desc_limite_peso = Column(Numeric(5,1))
    desc_frete_peso = Column(Numeric(5,1))
    desc_frete_valor = Column(Numeric(5,1))
    desc_sec_cat = Column(Numeric(5,1))
    desc_pedagio = Column(Numeric(5,1))
    desc_itr = Column(Numeric(5,1))
    desc_ademe = Column(Numeric(5,1))
    desc_despacho = Column(Numeric(5,1))
    desc_outros = Column(Numeric(5,1))
    desc_suframa = Column(Numeric(5,1))
    desc_taxa_estadual = Column(Numeric(5,1))
    ddd_cliente = Column(String(2))
    id_empresa = Column(String(2))
    contato = Column(String(25))
    fone_contato = Column(String(8))
    email = Column(String(100))
    site = Column(String(100))
    classificacao_fiscal = Column(String(15))
    natureza_da_carga = Column(String(40))
    usuario_cadastro = Column(String(30))
    usuario_alteracao = Column(String(30))
    usuario_aprovacao = Column(String(30))
    dt_alteracao = Column(DateTime)
    codigo_filial = Column(String(3))
    formas_pgto = Column(String(8))
    frete = Column(String(15))
    dev_canhoto = Column(Integer)
    limite_peso = Column(Numeric(8,3))
    fat_canhoto = Column(Integer)
    fat_pfilial = Column(Integer)
    suframa = Column(String(15))
    responsavel_seguro = Column(Numeric(1,0))
    forma_pagto = Column(String(15))
    tipo_cliente = Column(Numeric(2,0))
    dt_cadastro = Column(DateTime)
    endereco = Column(String(100))
    numero = Column(String(6))
    cep = Column(String(8))
    bairro = Column(String(30))
    id_cidade = Column(Integer, ForeignKey('cidades.id_cidade'))
    ramo_atividade = Column(String(40))
    nextel_id = Column(String(12))
    telefone_voip = Column(String(15))
    lat = Column(Float)
    lng = Column(Float)
    nivel_zoom = Column(Integer)
    desc_gris = Column(Numeric(5,1))
    dia_fatura1 = Column(Integer)
    dia_fatura2 = Column(Integer)
    dia_fatura3 = Column(Integer)
    dia_fatura4 = Column(Integer)
    dia_fatura5 = Column(Integer)
    dia_semana1 = Column(Integer)
    dia_semana2 = Column(Integer)
    dia_semana3 = Column(Integer)
    protestar = Column(Integer)
    codigo_cobrador = Column(Integer)
    devedor = Column(Integer)
    versao_edi = Column(String(15))
    imposto_por_conta = Column(Integer)
    admite_outra_tabela = Column(Integer)
    tabela_aereo = Column(String(13))
    tabela_transferencia = Column(String(13))
    desc_taxa_rodoviario = Column(Numeric(8,2))
    desc_reentrega_aereo = Column(Numeric(8,2))
    desc_taxa_dce = Column(Numeric(8,2))
    desc_taxa_veiculo_exclusivo = Column(Numeric(8,2))
    desc_taxa_outros = Column(Numeric(8,2))
    desc_taxa_coleta = Column(Numeric(8,2))
    desc_taxa_entrega = Column(Numeric(8,2))
    desc_taxa_redespacho = Column(Numeric(8,2))
    desc_taxa_expresso = Column(Numeric(8,2))
    desc_taxa_emergencia = Column(Numeric(8,2))
    desc_taxa_manuseio = Column(Numeric(8,2))
    desc_taxa_escolta = Column(Numeric(8,2))
    desc_frete_valor_aereo = Column(Numeric(8,2))
    id_vendedor = Column(Integer)
    frequencia_especial = Column(String(1))
    limite_ctrc_fatura = Column(Integer)
    limite_valor_fatura = Column(Numeric(10,2))
    exige_agrupar_notas = Column(Integer)
    pc_contabil = Column(String(10))
    exige_observacao = Column(Integer)
    texto_observacao = Column(Text)
    substituto_tributario = Column(Integer)
    cobrar_tx_coleta = Column(Integer)
    cobrar_tx_entrega = Column(Integer)
    cobrar_tx_dce = Column(Integer)
    end_complemento = Column(String(100))
    regime_especial_mg = Column(Integer)
    utiliza_cod_interno_frete = Column(Integer)
    idestrangeiro = Column(String(20))
    fob_dirigido = Column(Integer)
    volume_no_item_nota = Column(Integer)
    repasse_credito_presumido = Column(Integer)
    nr_apolice = Column(String(20))
    base_dados_softlog = Column(Text)
    optante_simples = Column(Integer)
    id_bairro = Column(Integer)
    cnpj_cod_interno_frete = Column(String(14))
    tipo_contribuinte = Column(String(1))
    cli_id_motorista = Column(Integer)
    cli_placa_veiculo = Column(String(8))
    tipo_parceiro = Column(Integer)
    movimentacao = Column(String(1))
    empresa_responsavel = Column(String(3))
    id_seguradora = Column(Integer)
    xml_ok = Column(Integer)
    tipo_data = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    enderecos = relationship("ClienteEnderecos", back_populates="cliente")
    cidade = relationship("Cidades")

    def __repr__(self):
        return self.nome_cliente

class ClienteEnderecos(Model):
    __tablename__ = 'cliente_enderecos'
    id_endereco = Column(Integer,Sequence('cliente_enderecos_id_endereco_seq'), primary_key=True)
    codigo_cliente = Column(Integer, ForeignKey("cliente.codigo_cliente"))
    cliente = relationship("Cliente", back_populates="enderecos", foreign_keys=[codigo_cliente] )
    logradouro = Column(String(100))
    numero = Column(String(10))
    bairro = Column(String(30))
    estado = Column(String(2))
    cep = Column(String(8))
    ddd = Column(String(2))
    telefone = Column(String(8))
    id_temp = Column(String(10))
    id_cidade = Column(Integer,ForeignKey('cidades.id_cidade'))
    cidade = relationship("Cidades")
    lat = Column(Float)
    lng = Column(Float)
    nivel_zoom = Column(Integer)
    end_complemento = Column(String(100))
    id_bairro = Column(Integer)

    def __repr__(self):
        return self.__tablename__
