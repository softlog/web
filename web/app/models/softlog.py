import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey,Date, Text, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.builder import Model


class Ab_Filial_Role(Model):
    __tablename__ = 'ab_filial_role'
    id = Column(Integer,Sequence('ab_filial_role_id_seq'), primary_key=True)
    id_filial = Column(Integer)
    role_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_Permission(Model):
    __tablename__ = 'ab_permission'
    id = Column(Integer,Sequence('ab_permission_id_seq'), primary_key=True)
    name = Column(String(100))
    alias = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Ab_Permission_View(Model):
    __tablename__ = 'ab_permission_view'
    id = Column(Integer,Sequence('ab_permission_view_id_seq'), primary_key=True)
    permission_id = Column(Integer)
    view_menu_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_Permission_View_Role(Model):
    __tablename__ = 'ab_permission_view_role'
    id = Column(Integer,Sequence('ab_permission_view_role_id_seq'), primary_key=True)
    permission_view_id = Column(Integer)
    role_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_Register_User(Model):
    __tablename__ = 'ab_register_user'
    id = Column(Integer,Sequence('ab_register_user_id_seq'), primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64))
    password = Column(String(256))
    email = Column(String(64))
    registration_date = Column(DateTime)
    registration_hash = Column(String(256))

    def __repr__(self):
        return self.__tablename__



class Ab_Role(Model):
    __tablename__ = 'ab_role'
    id = Column(Integer,Sequence('ab_role_id_seq'), primary_key=True)
    name = Column(String(64))

    def __repr__(self):
        return self.__tablename__



class Ab_User(Model):
    __tablename__ = 'ab_user'
    id = Column(Integer,Sequence('ab_user_id_seq'), primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(64))
    password = Column(String(256))
    email = Column(String(64))
    last_login = Column(DateTime)
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime)
    changed_on = Column(DateTime)
    id_user_db_tny = Column(text)
    changed_by_fk = Column(Integer)
    created_by_fk = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_User_Filial(Model):
    __tablename__ = 'ab_user_filial'
    id = Column(Integer,Sequence('ab_user_filial_id_seq'), primary_key=True)
    user_id = Column(Integer)
    filial_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_User_Role(Model):
    __tablename__ = 'ab_user_role'
    id = Column(Integer,Sequence('ab_user_role_id_seq'), primary_key=True)
    user_id = Column(Integer)
    role_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ab_View_Menu(Model):
    __tablename__ = 'ab_view_menu'
    id = Column(Integer,Sequence('ab_view_menu_id_seq'), primary_key=True)
    name = Column(String(100))
    alias = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Adm_Integracao(Model):
    __tablename__ = 'adm_integracao'
    id_integracao = Column(Integer,Sequence('adm_integracao_id_integracao_seq'), primary_key=True)
    id_relacao = Column(Integer)
    id_banco_dados = Column(Integer)
    vl_chave_primaria = Column(Integer)
    vl_chave_secundaria = Column(text)
    data_insercao = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Adm_Relacoes(Model):
    __tablename__ = 'adm_relacoes'
    id_relacao = Column(Integer,Sequence('adm_relacoes_id_relacao_seq'), primary_key=True)
    relacao = Column(text)
    nome_chave_primaria = Column(text)
    tipo_chave_primaria = Column(text)
    sequencia_chave_primaria = Column(text)
    nome_chave_secundaria = Column(text)
    tipo_chave_secundaria = Column(text)

    def __repr__(self):
        return self.__tablename__



class Aer_Tbl_Servicos_Cia_Aerea(Model):
    __tablename__ = 'aer_tbl_servicos_cia_aerea'
    id_servico_cia_aerea = Column(Integer,Sequence('aer_tbl_servicos_cia_aerea_id_servico_cia_aerea_seq'), primary_key=True)
    id_cia_aerea = Column(Integer)
    descricao_servico = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Almoxarifado(Model):
    __tablename__ = 'almoxarifado'
    id_almoxarifado = Column(Integer,Sequence('almoxarifado_id_almoxarifado_seq'), primary_key=True)
    cod_almoxarifado = Column(String(10))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    descricao_almoxarifado = Column(String(50))
    combustivel = Column(Integer)
    publico = Column(Integer)
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Anexos(Model):
    __tablename__ = 'anexos'
    id_anexo = Column(Integer,Sequence('anexos_id_anexo_seq'), primary_key=True)
    id_externo = Column(Integer)
    id_tabela = Column(Integer)
    tipo_anexo = Column(Integer)
    data_anexo = Column(Date)
    usuario_anexo = Column(String(30))
    descricao_anexo = Column(String(100))
    conteudo_anexo = Column(text)
    nome_anexo = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Backup_Visoes(Model):
    __tablename__ = 'backup_visoes'
    id_backup_visao = Column(Integer,Sequence('backup_visoes_id_backup_visao_seq'), primary_key=True)
    nome_relacao = Column(text)
    visao = Column(text)
    level = Column(Integer)
    definicao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Banco(Model):
    __tablename__ = 'banco'
    nome_banco = Column(String(40))
    id_banco = Column(Integer,Sequence('banco_id_banco_seq'), primary_key=True)
    numero_banco = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Colunas(Model):
    __tablename__ = 'bi_cubo_colunas'
    id_cubo_coluna = Column(Integer,Sequence('bi_cubo_colunas_id_cubo_coluna_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    coluna_identificador = Column(String(50))
    coluna_sql = Column(text)

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Condicoes(Model):
    __tablename__ = 'bi_cubo_condicoes'
    id_cubo_condicao = Column(Integer,Sequence('bi_cubo_condicoes_id_cubo_condicao_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    condicao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Dimensoes(Model):
    __tablename__ = 'bi_cubo_dimensoes'
    id_cubo_dimensao = Column(Integer,Sequence('bi_cubo_dimensoes_id_cubo_dimensao_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    coluna_identificador = Column(String(50))
    dimensao_identificador = Column(String(50))
    titulo = Column(text)
    tipo_dimensao = Column(Integer)
    sql_text = Column(text)
    keyfield = Column(String(50))
    lookupfield = Column(String(50))
    parentfield = Column(String(50))
    dimensao_toolbar = Column(Integer)
    sorting = Column(Integer)
    wrapto = Column(Integer)
    forecastingenabled = Column(Integer)
    forecastingmethod = Column(Integer)
    precedingname = Column(String(50))
    consequentname = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Dimensoes_User(Model):
    __tablename__ = 'bi_cubo_dimensoes_user'
    id_cubo_dimensao_user = Column(Integer,Sequence('bi_cubo_dimensoes_user_id_cubo_dimensao_user_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    id_cubo_dimensao = Column(Integer)
    id_usuario = Column(Integer)
    ativo = Column(Integer)
    titulo = Column(text)
    dimensao_toolbar = Column(Integer)
    sorting = Column(Integer)
    forecastingenabled = Column(Integer)
    forecastingmethod = Column(Integer)
    precedingname = Column(String(50))
    consequentname = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Medidas(Model):
    __tablename__ = 'bi_cubo_medidas'
    id_cubo_medida = Column(Integer,Sequence('bi_cubo_medidas_id_cubo_medida_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    coluna_identificador = Column(String(50))
    medida_identificador = Column(String(50))
    titulo = Column(text)
    tipo_calculo = Column(Integer)
    tipo_data = Column(Integer)
    formato_string = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_Medidas_User(Model):
    __tablename__ = 'bi_cubo_medidas_user'
    id_cubo_medida_user = Column(Integer,Sequence('bi_cubo_medidas_user_id_cubo_medida_user_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    id_cubo_medida = Column(Integer)
    id_usuario = Column(Integer)
    ativo = Column(Integer)
    titulo = Column(text)
    tipo_calculo = Column(Integer)
    tipo_data = Column(Integer)
    formato_string = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Bi_Cubo_User(Model):
    __tablename__ = 'bi_cubo_user'
    id_cubo_user = Column(Integer,Sequence('bi_cubo_user_id_cubo_user_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    id_usuario = Column(Integer)
    data_inicial = Column(Date)
    data_final = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Bi_Cubos(Model):
    __tablename__ = 'bi_cubos'
    id_cubo = Column(Integer,Sequence('bi_cubos_id_cubo_seq'), primary_key=True)
    cubo_identificador = Column(String(50))
    cubo_nome = Column(String(50))
    cubo_descricao = Column(String(200))
    cubo_from = Column(text)
    cubo_where = Column(text)
    cubo_group_by = Column(text)
    cubo_order_by = Column(text)
    campo_data = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Bi_Dashboards(Model):
    __tablename__ = 'bi_dashboards'
    id = Column(Integer,Sequence('bi_dashboards_id_seq'), primary_key=True)
    codigo_dashboard = Column(text)
    nome_dashboard = Column(text)
    subtitulo = Column(text)
    grupo = Column(text)

    def __repr__(self):
        return self.__tablename__



class Bi_Dashboards_Itens(Model):
    __tablename__ = 'bi_dashboards_itens'
    id = Column(Integer,Sequence('bi_dashboards_itens_id_seq'), primary_key=True)
    id_dashboard = Column(Integer)
    code_item = Column(text)
    row = Column(Integer)
    col = Column(Integer)
    name = Column(String(30))
    type_widget = Column(String(20))
    xs = Column(Integer)
    sm = Column(Integer)
    md = Column(Integer)
    lg = Column(Integer)
    btn_close = Column(Integer)
    btn_colapse = Column(Integer)
    btn_setting = Column(Integer)
    class_row = Column(text)
    id_row = Column(text)
    style_row = Column(text)
    skip_row = Column(text)
    scale_values = Column(String(1))
    datasource = Column(text)
    function_conf = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Bi_Dashboards_Usuarios(Model):
    __tablename__ = 'bi_dashboards_usuarios'
    id = Column(Integer,Sequence('bi_dashboards_usuarios_id_seq'), primary_key=True)
    id_usuario = Column(Integer)
    id_dashboard = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Captcha_Creditos(Model):
    __tablename__ = 'captcha_creditos'
    id_captcha_credito = Column(Integer,Sequence('captcha_creditos_id_captcha_credito_seq'), primary_key=True)
    data_credito = Column(Date)
    qtd_creditos = Column(Integer)
    valor_credito = Column(Numeric(12,2))
    origem_compra = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Captcha_Log(Model):
    __tablename__ = 'captcha_log'
    id_transacao = Column(Integer,Sequence('captcha_log_id_transacao_seq'), primary_key=True)
    banco_dados = Column(String(50))
    login_name = Column(String(50))
    data_transacao = Column(DateTime)
    imagem_captcha = Column(text)
    chave_nfe = Column(String(44))
    sincronizado = Column(Integer)
    origem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Carteira(Model):
    __tablename__ = 'carteira'
    id_carteira = Column(Integer,Sequence('carteira_id_carteira_seq'), primary_key=True)
    id_conta_corrente = Column(Integer)
    codigo_carteira = Column(String(20))
    nome_carteira = Column(String(50))
    numero_agencia_f = Column(String(8))
    conta_corrente_f = Column(String(16))
    codigo_cedente = Column(String(20))
    caption_outro_dado_configuracao_1 = Column(String(50))
    outro_dado_configuracao_1 = Column(String(20))
    caption_outro_dado_configuracao_2 = Column(String(50))
    outro_dado_configuracao_2 = Column(String(20))
    arquivo_configuracao = Column(String(255))
    nosso_numero_inicial = Column(String(20))
    nosso_numero_final = Column(String(20))
    proximo_nosso_numero = Column(String(20))
    numero_convenio_lider = Column(String(12))
    numero_convenio = Column(String(12))
    numero_remessa = Column(Integer)
    valor_limite_acrescimo = Column(Numeric(12,2))
    juros_perc = Column(Numeric(5,2))
    multa_perc = Column(Numeric(5,2))
    dias_prazo_execucao = Column(Integer)
    dias_antes_desconto = Column(Integer)
    desconto_perc = Column(Numeric(5,2))
    acrescimo = Column(Numeric(12,2))
    tipo_duplicata = Column(String(20))
    local_pagamento = Column(text)
    instrucoes = Column(text)
    cnpj_sacador = Column(String(14))
    sacador = Column(String(50))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    layout_remessa = Column(String(30))
    layout_retorno = Column(String(30))
    arquivo = Column(text)
    id_carteira_agregada = Column(Integer)
    chave1 = Column(String(60))
    chave2 = Column(String(60))
    nro_conta_cobrebem = Column(String(15))
    registrada = Column(Integer)
    lanca_baixa_financeiro = Column(Integer)
    altura_boleto = Column(Integer)
    forma_cadastramento = Column(Integer)
    instrucao3 = Column(text)
    dias_prazo_devolucao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cep(Model):
    __tablename__ = 'cep'
    id_cep = Column(Integer,Sequence('cep_id_cep_seq'), primary_key=True)
    cep = Column(String(8))
    logradouro = Column(String(150))
    endereco_complemento = Column(String(72))
    bairro = Column(String(72))
    cidade = Column(String(72))
    uf = Column(String(2))
    cod_ibge = Column(String(7))
    longitude = Column(Float)
    latitude = Column(Float)
    ddd = Column(String(2))
    id_bd_fornecedor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cfop(Model):
    __tablename__ = 'cfop'
    id_cfop = Column(Integer,Sequence('cfop_id_cfop_seq'), primary_key=True)
    codigo_cfop = Column(String(4))
    descricao_cfop = Column(String(250))
    classificacao_fiscal = Column(String(15))
    codigo_totvs = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Chat_Mensagens(Model):
    __tablename__ = 'chat_mensagens'
    id_mensagem = Column(Integer,Sequence('chat_mensagens_id_mensagem_seq'), primary_key=True)
    data_mensagem = Column(DateTime)
    login_chat = Column(String(30))
    conteudo_mensagem = Column(text)
    estado = Column(Integer)
    mensagem_de = Column(String(30))
    mensagem_para = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Chat_Usuarios(Model):
    __tablename__ = 'chat_usuarios'
    id_usuario_chat = Column(Integer,Sequence('chat_usuarios_id_usuario_chat_seq'), primary_key=True)
    login_chat = Column(String(30))
    situacao = Column(Integer)
    ultima_conexao = Column(DateTime)
    ultima_desconexao = Column(DateTime)
    ultima_leitura = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Cidades(Model):
    __tablename__ = 'cidades'
    sigla_cidade = Column(String(3))
    nome_cidade = Column(String(50))
    uf = Column(String(2))
    id_regiao = Column(Numeric(5,0))
    praca_especial = Column(Numeric(1,0))
    data_alteracao = Column(DateTime)
    id_cidade = Column(Integer,Sequence('cidades_id_cidade_seq'), primary_key=True)
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
        return self.__tablename__



class Cidades_De_Para(Model):
    __tablename__ = 'cidades_de_para'
    id_cidades_de_para = Column(Integer,Sequence('cidades_de_para_id_cidades_de_para_seq'), primary_key=True)
    id_cidade_origem = Column(Integer)
    id_cidade_destino = Column(Integer)
    distancia = Column(Numeric(12,1))
    tempo_rodoviario = Column(Integer)
    tempo_aereo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cidades_New(Model):
    __tablename__ = 'cidades_new'
    sigla_cidade = Column(String(3))
    nome_cidade = Column(String(50))
    uf = Column(String(2))
    id_regiao = Column(Numeric(5,0))
    praca_especial = Column(Numeric(1,0))
    data_alteracao = Column(DateTime)
    id_cidade = Column(Integer,Sequence('cidades_new_id_cidade_seq'), primary_key=True)
    filial_cidade = Column(String(3))
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cidades_Serpro(Model):
    __tablename__ = 'cidades_serpro'
    id = Column(Integer,Sequence('cidades_serpro_id_seq'), primary_key=True)
    codigo_serpro = Column(String(4))
    digito_serpro = Column(String(1))
    id_cidade = Column(Integer)
    nome_cidade = Column(text)
    uf = Column(text)
    orgao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Cli_Emp_Planocontas(Model):
    __tablename__ = 'cli_emp_planocontas'
    id_cli_emp_planocontas = Column(Integer,Sequence('cli_emp_planocontas_id_cli_emp_planocontas_seq'), primary_key=True)
    codigo_cliente = Column(Integer)
    codigo_empresa = Column(String(3))
    plano_contas = Column(String(10))

    def __repr__(self):
        return self.__tablename__



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
    id_cidade = Column(Numeric(5,0))
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
    texto_observacao = Column(text)
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
    base_dados_softlog = Column(text)
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

    def __repr__(self):
        return self.__tablename__



class Cliente_Enderecos(Model):
    __tablename__ = 'cliente_enderecos'
    cnpj_cpf = Column(String(18))
    logradouro = Column(String(100))
    numero = Column(String(10))
    bairro = Column(String(30))
    estado = Column(String(2))
    cep = Column(String(8))
    ddd = Column(String(2))
    telefone = Column(String(8))
    id_temp = Column(String(10))
    id_cidade = Column(Numeric(5,0))
    lat = Column(Float)
    lng = Column(Float)
    nivel_zoom = Column(Integer)
    end_complemento = Column(String(100))
    id_bairro = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cliente_Origem_Destino(Model):
    __tablename__ = 'cliente_origem_destino'
    id_cliente_origem_destino = Column(Integer,Sequence('cliente_origem_destino_id_cliente_origem_destino_seq'), primary_key=True)
    codigo_cliente = Column(Integer)
    id_cidade_origem = Column(Integer)
    id_cidade_destino = Column(Integer)
    percentual_tabela = Column(Numeric(6,2))
    id_inclusao = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Cliente_Parametros(Model):
    __tablename__ = 'cliente_parametros'
    id_cliente_parametro = Column(Integer,Sequence('cliente_parametros_id_cliente_parametro_seq'), primary_key=True)
    codigo_cliente = Column(Integer)
    id_tipo_parametro = Column(Integer)
    valor_parametro = Column(text)
    tipo_dado_parametro = Column(String(1))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Cliente_Prospect(Model):
    __tablename__ = 'cliente_prospect'
    id_cliente = Column(Integer,Sequence('cliente_prospect_id_cliente_seq'), primary_key=True)
    cnpj_cpf = Column(String(18))
    nome_cliente = Column(String(100))
    nome_fantasia = Column(String(100))
    inscricao_estadual = Column(String(18))
    endereco = Column(String(200))
    numero = Column(String(6))
    cep = Column(String(8))
    bairro = Column(String(50))
    id_cidade = Column(Numeric(5,0))
    ramo_atividade = Column(String(40))
    ddd = Column(String(2))
    telefone = Column(text)
    produtos_servicos_atuais = Column(text)
    id_usuario = Column(Integer)
    data_acomp_usuario = Column(Date)
    observacoes = Column(text)
    data_ultima_atualizacao = Column(Date)
    data_inclusao = Column(DateTime)
    email = Column(text)
    site = Column(text)

    def __repr__(self):
        return self.__tablename__



class Cliente_Prospect_Acompanhamento(Model):
    __tablename__ = 'cliente_prospect_acompanhamento'
    id_acompahamento_prospect = Column(Integer,Sequence('cliente_prospect_acompanhamento_id_acompahamento_prospect_seq'), primary_key=True)
    id_cliente = Column(Integer)
    pessoa_contactada = Column(String(50))
    data_contato = Column(DateTime)
    id_funcionario = Column(Integer)
    assunto_trato = Column(text)
    reacao_prospect = Column(text)
    status_contato = Column(Integer)
    data_proximo_contato = Column(DateTime)
    motivo_proximo_contato = Column(text)

    def __repr__(self):
        return self.__tablename__



class Cliente_Prospect_Contatos(Model):
    __tablename__ = 'cliente_prospect_contatos'
    id_prospect_contatos = Column(Integer,Sequence('cliente_prospect_contatos_id_prospect_contatos_seq'), primary_key=True)
    id_cliente = Column(Integer)
    id_tipo_contato = Column(Integer)
    informacao_contato = Column(text)
    nome_contato = Column(String(100))
    cargo_funcao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Cliente_Prospect_Tmp(Model):
    __tablename__ = 'cliente_prospect_tmp'
    nome = Column(String)
    empresa = Column(String)
    email_1 = Column(text)
    email_2 = Column(text)
    ddd = Column(text)
    telefone = Column(text)
    telefone_1 = Column(text)
    telefone_2 = Column(text)
    telefone_2_s = Column(text)
    telefone_3 = Column(text)
    telefone_3_s = Column(text)
    endereco = Column(String)
    bairro = Column(String)
    cep = Column(text)
    id_cidade = Column(Integer)
    cidade = Column(text)
    cnpj = Column(text)
    observacao = Column(String)

    def __repr__(self):
        return self.__tablename__



class Cliente_Regiao_Origem_Destino(Model):
    __tablename__ = 'cliente_regiao_origem_destino'
    id_cliente_regiao_origem_destino = Column(Integer,Sequence('cliente_regiao_origem_destino_id_cliente_regiao_origem_destino_seq'), primary_key=True)
    codigo_cliente = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    percentual_tabela = Column(Numeric(6,2))
    id_inclusao = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Cliente_Servicos_Contratados(Model):
    __tablename__ = 'cliente_servicos_contratados'
    id_servicos_cliente = Column(Integer,Sequence('cliente_servicos_contratados_id_servicos_cliente_seq'), primary_key=True)
    id_servico = Column(Integer)
    descricao_servico = Column(String(50))
    situacao = Column(Integer)
    data_ativacao = Column(Date)
    data_desativacao = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Cliente_Sr(Model):
    __tablename__ = 'cliente_sr'
    id_sr = Column(Integer,Sequence('cliente_sr_id_sr_seq'), primary_key=True)
    id_cliente = Column(Integer)
    opcao_pagamento = Column(String(1))
    mes_ultimafatura = Column(String(2))
    ano_ultimafatura = Column(String(4))
    proxima_fatura = Column(String(7))
    meio_cobranca = Column(Integer)
    situacao = Column(Integer)
    arquivo_boleto = Column(String(30))
    requer_nf = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Cliente_Sr_Itens(Model):
    __tablename__ = 'cliente_sr_itens'
    id_sr_item = Column(Integer,Sequence('cliente_sr_itens_id_sr_item_seq'), primary_key=True)
    id_sr = Column(Integer)
    id_servico = Column(Integer)
    descricao_servico = Column(String(50))
    valor_servico = Column(Numeric(12,2))
    situacao = Column(Integer)
    data_ativacao = Column(Date)
    data_desativacao = Column(Date)
    reajuste = Column(String(5))
    perc_reajuste = Column(Numeric(5,2))

    def __repr__(self):
        return self.__tablename__



class Cliente_Tipo_Endereco(Model):
    __tablename__ = 'cliente_tipo_endereco'
    descricao_tipo_endereco = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Cliente_Tipo_Parametros(Model):
    __tablename__ = 'cliente_tipo_parametros'
    id_tipo_parametro = Column(Integer,Sequence('cliente_tipo_parametros_id_tipo_parametro_seq'), primary_key=True)
    nome_parametro = Column(String(30))
    descricao_parametro = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Clientes_Base_Sefaz(Model):
    __tablename__ = 'clientes_base_sefaz'
    id = Column(Integer,Sequence('clientes_base_sefaz_id_seq'), primary_key=True)
    cnpj = Column(String(14))
    razao_social = Column(text)
    nome_fantasia = Column(text)
    situacao = Column(text)
    endereco = Column(text)
    numero = Column(text)
    bairro = Column(text)
    codigo_municipio = Column(text)
    uf = Column(text)
    cep = Column(text)
    ie = Column(text)
    telefones = Column(text)
    email = Column(text)
    cnae = Column(text)
    inicio_atividade = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Col_Coletas(Model):
    __tablename__ = 'col_coletas'
    filial_coleta = Column(String(3))
    data_solicitacao = Column(Date)
    hora_solicitacao = Column(String(5))
    data_coleta = Column(Date)
    hora_coleta = Column(String(5))
    remetente_nome = Column(String(100))
    remetente_cnpj = Column(String(18))
    remetente_inscricao = Column(String(15))
    remetente_endereco = Column(String(100))
    remetente_cidade = Column(String(30))
    remetente_bairro = Column(String(30))
    remetente_cep = Column(String(8))
    remetente_uf = Column(String(2))
    remetente_ddd = Column(String(2))
    remetente_telefone = Column(String(12))
    destinatario_nome = Column(String(100))
    destinatario_cnpj = Column(String(18))
    destinatario_endereco = Column(String(100))
    destinatario_inscricao = Column(String(15))
    destinatario_bairro = Column(String(30))
    destinatario_cep = Column(String(8))
    destinatario_cidade = Column(String(30))
    destinatario_uf = Column(String(2))
    pessoa_contato = Column(String(40))
    telefone_contato = Column(String(12))
    placa_veiculo = Column(String(8))
    placa_carreta = Column(String(8))
    prioridade = Column(Numeric(1,0))
    observacoes = Column(text)
    emitido = Column(Numeric(1,0))
    baixa = Column(Numeric(1,0))
    cancelado = Column(Numeric(1,0))
    formcole = Column(Numeric(6,0))
    id_temp = Column(String(10))
    id_end_remetente = Column(Numeric(6,0))
    id_end_destinatario = Column(Numeric(6,0))
    tipo_frete = Column(Numeric(1,0))
    remetente_numero = Column(String(10))
    destinatario_numero = Column(String(10))
    destinatario_ddd = Column(String(2))
    destinatario_telefone = Column(String(8))
    id_coleta = Column(Integer,Sequence('col_coletas_id_coleta_seq'), primary_key=True)
    id_coleta_filial = Column(String(13))
    data_alteracao = Column(Date)
    hora_alteracao = Column(String(5))
    numero_romaneio = Column(String(13))
    usuario_inclusao = Column(String(30))
    usuario_alteracao = Column(String(30))
    usuario_emissao = Column(String(30))
    usuario_execucao = Column(String(30))
    usuario_baixa = Column(String(30))
    usuario_cancelamento = Column(String(30))
    id_motorista = Column(Numeric(6,0))
    serie_form = Column(String(10))
    cod_empresa = Column(String(3))
    ocorrencia = Column(String(12))
    descricao_ocorrencia = Column(String(60))
    data_cancelamento = Column(Date)
    remetente_lat = Column(Float)
    remetente_lng = Column(Float)
    destinatario_lat = Column(Float)
    destinatario_lng = Column(Float)
    id_consignatario = Column(Integer)
    consignatario_cnpj = Column(String(14))
    consignatario_nome = Column(String(100))
    consignatario_endereco = Column(String(100))
    consignatario_numero = Column(String(10))
    consignatario_bairro = Column(String(30))
    consignatario_cidade = Column(String(30))
    consignatario_uf = Column(String(2))
    consignatario_cep = Column(String(8))
    consignatario_inscricao = Column(String(15))
    consignatario_ddd = Column(String(2))
    consignatario_telefone = Column(String(12))
    consignatario_lat = Column(Float)
    consignatario_lng = Column(Float)
    id_redespachador = Column(Integer)
    redespachador_cnpj = Column(String(14))
    redespachador_nome = Column(String(100))
    redespachador_endereco = Column(String(100))
    redespachador_numero = Column(String(10))
    redespachador_bairro = Column(String(30))
    redespachador_cidade = Column(String(30))
    redespachador_uf = Column(String(2))
    redespachador_cep = Column(String(8))
    redespachador_inscricao = Column(String(15))
    redespachador_ddd = Column(String(2))
    redespachador_telefone = Column(String(12))
    redespachador_lat = Column(Float)
    redespachador_lng = Column(Float)
    id_end_consignatario = Column(Integer)
    id_end_redespachador = Column(Integer)
    tipo_coleta = Column(Integer)
    id_remetente = Column(Integer)
    id_destinatario = Column(Integer)
    nome_expedidor = Column(String(40))
    doc_expedidor = Column(String(20))
    conteudo_html = Column(text)
    conteudo_html_peq = Column(text)
    id_ocorrencia_edi = Column(Integer)
    versao_edi = Column(String(15))
    tem_alarme = Column(Integer)
    alarme_prazo = Column(String(5))
    id_regiao = Column(Integer)
    id_cidade_polo = Column(Integer)
    protocolo_cliente = Column(String(15))
    placas_engates = Column(String(60))
    odometro_inicial = Column(Numeric(10,1))
    odometro_final = Column(Numeric(10,1))
    horimetro_inicial = Column(Numeric(9,2))
    horimetro_final = Column(Numeric(9,2))
    col_pedido = Column(String(20))
    col_recebedor = Column(String(20))

    def __repr__(self):
        return self.__tablename__



class Col_Coletas_Itens(Model):
    __tablename__ = 'col_coletas_itens'
    id_coleta_filial = Column(String(13))
    marca = Column(String(30))
    quantidade = Column(Numeric(8,2))
    descricao = Column(String(50))
    peso = Column(Numeric(9,3))
    data_nf = Column(Date)
    numero_nf = Column(String(10))
    id_temp = Column(String(10))
    data_alteracao = Column(Date)
    hora_alteracao = Column(String(5))
    vol_m3 = Column(Numeric(7,3))
    valor_nota_fiscal = Column(Numeric(12,2))
    id_coleta = Column(Integer)
    id_natureza_carga = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)
    coleta_total = Column(Integer)
    id_ocorrencia_motivo = Column(Integer)
    vol_col = Column(Integer)
    vol_rec = Column(Integer)
    serie_nota_fiscal = Column(String(3))
    protocolo_cliente = Column(String(15))
    pedido_cliente = Column(String(15))

    def __repr__(self):
        return self.__tablename__



class Col_Coletas_Nf_Imp(Model):
    __tablename__ = 'col_coletas_nf_imp'
    id_coleta_nf_imp = Column(Integer,Sequence('col_coletas_nf_imp_id_coleta_nf_imp_seq'), primary_key=True)
    id_coleta = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)
    data_inclusao = Column(Date)
    data_emissao = Column(Date)
    vol_col = Column(Integer)
    vol_rec = Column(Integer)
    rem_id = Column(Integer)
    rem_cnpj = Column(String(18))
    rem_nome = Column(String(50))
    rem_cid = Column(String(50))
    rem_uf = Column(String(2))
    dest_id = Column(Integer)
    dest_cnpj = Column(String(18))
    dest_nome = Column(String(50))
    dest_cid = Column(String(50))
    dest_uf = Column(String(2))
    valor_nf = Column(Numeric(10,2))
    numero_nota_fiscal = Column(String(9))
    serie_nota_fiscal = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Col_Coletas_Romaneio(Model):
    __tablename__ = 'col_coletas_romaneio'
    id_coletas_romaneio = Column(Integer,Sequence('col_coletas_romaneio_id_coletas_romaneio_seq'), primary_key=True)
    id_coleta = Column(Integer)
    id_romaneios = Column(Integer)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    id_ocorrencia = Column(Integer)
    data_ocorrencia = Column(DateTime)
    coleta_realizada = Column(Integer)
    obs_ocorrencia = Column(String(200))
    vol_col = Column(Integer)
    vol_rec = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Col_Coletas_Romaneio_Tmp(Model):
    __tablename__ = 'col_coletas_romaneio_tmp'
    id_coletas_romaneio = Column(Integer)
    id_coleta = Column(Integer)
    id_romaneios = Column(Integer)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    id_ocorrencia = Column(Integer)
    data_ocorrencia = Column(DateTime)
    coleta_realizada = Column(Integer)
    obs_ocorrencia = Column(String(200))

    def __repr__(self):
        return self.__tablename__



class Col_Formularios_Cancelados(Model):
    __tablename__ = 'col_formularios_cancelados'
    id_col_formularios_cancelados = Column(Integer,Sequence('col_formularios_cancelados_id_col_formularios_cancelados_seq'), primary_key=True)
    serie_formulario = Column(String(10))
    numero_formulario = Column(Numeric(6,0))
    motivo_cancelamento = Column(text)
    usuario_cancelamento = Column(String(30))
    data_cancelamento = Column(DateTime)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Col_Log_Atividades(Model):
    __tablename__ = 'col_log_atividades'
    id_log_atividade = Column(Integer,Sequence('col_log_atividades_id_log_atividade_seq'), primary_key=True)
    id_coleta_filial = Column(String(13))
    data_hora = Column(DateTime)
    atividade_executada = Column(String(50))
    usuario = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Col_Ocorrencia_Coleta(Model):
    __tablename__ = 'col_ocorrencia_coleta'
    id_ocorrencia_coleta = Column(Integer,Sequence('col_ocorrencia_coleta_id_ocorrencia_coleta_seq'), primary_key=True)
    codigo_ocorrencia = Column(Integer)
    ocorrencia = Column(String(150))
    tipo_edi = Column(String(10))
    pendencia = Column(Integer)
    gera_acerto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Col_Parametros(Model):
    __tablename__ = 'col_parametros'
    serie_padrao = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Com_Acomp_Compra(Model):
    __tablename__ = 'com_acomp_compra'
    id_seq_acomp_compra = Column(Numeric(7,0))

    def __repr__(self):
        return self.__tablename__



class Com_Compras(Model):
    __tablename__ = 'com_compras'
    id_compra = Column(Integer,Sequence('com_compras_id_compra_seq'), primary_key=True)
    numero_compra = Column(String(13))
    id_centro_custo = Column(Integer)
    status = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    cnpj_fornecedor = Column(String(14))
    tipo_documento = Column(String(2))
    numero_pedido_compra = Column(String(13))
    modelo_doc_fiscal = Column(String(2))
    serie_doc = Column(String(3))
    numero_documento = Column(String(9))
    chave_nfe = Column(String(44))
    data_emissao = Column(Date)
    data_entrada = Column(Date)
    data_cancelamento = Column(Date)
    motivo_cancelamento = Column(String(50))
    tipo_pagamento = Column(String(1))
    vl_desconto = Column(Numeric(10,2))
    vl_abatimento_nt = Column(Numeric(10,2))
    vl_mercadoria = Column(Numeric(10,2))
    tipo_frete = Column(String(1))
    vl_frete = Column(Numeric(10,2))
    vl_seguro = Column(Numeric(10,2))
    vl_outras_despesas = Column(Numeric(10,2))
    vl_base_calculo = Column(Numeric(10,2))
    vl_icms = Column(Numeric(10,2))
    vl_base_calculo_st = Column(Numeric(10,2))
    vl_icms_st = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    vl_pis = Column(Numeric(10,2))
    vl_confins = Column(Numeric(10,2))
    vl_pis_st = Column(Numeric(10,2))
    vl_cofins_st = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    observacao = Column(String(250))
    sub_serie = Column(String(5))
    data_registro = Column(DateTime)
    valor_centro_custo_pred = Column(Numeric(12,2))
    status_financeiro = Column(Integer)
    cod_consumo_energia = Column(String(2))
    cod_consumo_agua = Column(String(2))
    tp_ligacao = Column(String(1))
    cod_grupo_tensao = Column(String(2))
    tp_assinante = Column(String(1))
    vl_serv_nt = Column(Numeric(12,2))
    vl_terc = Column(Numeric(12,2))
    vl_servico = Column(Numeric(12,2))
    vl_iss = Column(Numeric(12,2))
    vl_bc_pis = Column(Numeric(12,2))
    vl_bc_cofins = Column(Numeric(12,2))
    vl_pis_ret = Column(Numeric(12,2))
    vl_cofins_ret = Column(Numeric(12,2))
    placa_veiculo = Column(String(8))
    historico = Column(String(100))
    aguardando_boleto = Column(Integer)
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))
    id_condicao_pagamento = Column(Integer)
    id_forma_pagamento = Column(Integer)
    id_departamento = Column(Integer)
    destino_lancamento = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Centro_Custos(Model):
    __tablename__ = 'com_compras_centro_custos'
    id_compras_centro_custo = Column(Integer,Sequence('com_compras_centro_custos_id_compras_centro_custo_seq'), primary_key=True)
    id_compra = Column(Integer)
    codigo_centro_custo = Column(Integer)
    valor_por_centro_custo = Column(Numeric(12,3))
    placa_veiculo = Column(String(8))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Cotacao(Model):
    __tablename__ = 'com_compras_cotacao'
    id_cotacao = Column(Integer,Sequence('com_compras_cotacao_id_cotacao_seq'), primary_key=True)
    numero_cotacao = Column(String(13))
    numero_solicitacao = Column(String(13))
    data_hora_emissao = Column(DateTime)
    id_cotador = Column(Integer)
    id_fornecedor1 = Column(Integer)
    id_fornecedor2 = Column(Integer)
    id_fornecedor3 = Column(Integer)
    id_fornecedor4 = Column(Integer)
    id_fornecedor5 = Column(Integer)
    observacao = Column(String(250))
    id_aprovador = Column(Integer)
    data_hora_aprovacao = Column(DateTime)
    situacao = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    data_entrega1 = Column(Date)
    data_entrega2 = Column(Date)
    data_entrega3 = Column(Date)
    data_entrega4 = Column(Date)
    data_entrega5 = Column(Date)
    condicao_pgto1 = Column(Integer)
    condicao_pgto2 = Column(Integer)
    condicao_pgto3 = Column(Integer)
    condicao_pgto4 = Column(Integer)
    condicao_pgto5 = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Faturas(Model):
    __tablename__ = 'com_compras_faturas'
    id = Column(Integer,Sequence('com_compras_faturas_id_seq'), primary_key=True)
    id_compra = Column(Integer)
    numero = Column(String(15))
    data_vencimento = Column(Date)
    valor = Column(Numeric(10,2))
    id_conta_pagar = Column(Integer)
    flg_lancamento_contas_pagar = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Itens(Model):
    __tablename__ = 'com_compras_itens'
    id_compra_item = Column(Integer,Sequence('com_compras_itens_id_compra_item_seq'), primary_key=True)
    id_compra = Column(Integer)
    codigo_produto = Column(String(8))
    descricao_complementar = Column(String(50))
    quantidade = Column(Numeric(10,5))
    unidade = Column(String(6))
    vl_item = Column(Numeric(10,4))
    vl_desconto = Column(Numeric(10,2))
    movimentacao_fisica = Column(Integer)
    cst_icms = Column(String(3))
    cfop = Column(String(4))
    cod_natureza = Column(String(10))
    vl_base_icms = Column(Numeric(10,2))
    aliquota_icms = Column(Numeric(10,2))
    valor_icms = Column(Numeric(10,2))
    valor_base_icms_st = Column(Numeric(10,2))
    aliquota_icms_st = Column(Numeric(10,2))
    valor_icms_st = Column(Numeric(10,2))
    cst_ipi = Column(String(2))
    cod_enq = Column(String(3))
    vl_base_ipi = Column(Numeric(10,2))
    aliquota_ipi = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    cst_pis = Column(String(2))
    vl_base_pis = Column(Numeric(10,2))
    aliquota_pis_perc = Column(Numeric(10,2))
    quantidade_base_pis = Column(Numeric(10,3))
    vl_aliquota_pis = Column(Numeric(10,4))
    valor_pis = Column(Numeric(10,2))
    cst_cofins = Column(String(2))
    valor_base_cofins = Column(Numeric(10,2))
    aliquota_cofins_perc = Column(Numeric(10,2))
    quantidade_base_cofins = Column(Numeric(10,3))
    vl_aliquota_cofins = Column(Numeric(10,4))
    vl_cofins = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    observacao = Column(String(250))
    id_produto = Column(Integer)
    vl_frete = Column(Numeric(10,2))
    lote_numero = Column(String(20))
    lote_data_fabricacao = Column(Date)
    lote_data_validade = Column(Date)
    id_almoxarifado = Column(Integer)
    nat_bc_cred = Column(String(2))
    ind_orig_cred = Column(Integer)
    totvs_idnat = Column(String(15))
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))
    totvs_conta_cotabil = Column(String(55))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Log_Atividades(Model):
    __tablename__ = 'com_compras_log_atividades'
    id_compra_log_atividade = Column(Integer,Sequence('com_compras_log_atividades_id_compra_log_atividade_seq'), primary_key=True)
    id_compra = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(String(50))
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Pedido(Model):
    __tablename__ = 'com_compras_pedido'
    id_pedido_compra = Column(Integer,Sequence('com_compras_pedido_id_pedido_compra_seq'), primary_key=True)
    numero_pedido = Column(String(13))
    numero_cotacao = Column(String(13))
    cnpj_cpf_fornecedor = Column(String(14))
    data_hora_emissao = Column(DateTime)
    condicao_pgto = Column(Integer)
    especie_pgto = Column(Integer)
    vl_pedido = Column(Numeric(12,2))
    vl_desconto = Column(Numeric(10,2))
    vl_acrecimo = Column(Numeric(10,2))
    data_entrega = Column(Date)
    situacao = Column(Integer)
    observacao = Column(String(250))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Pedido_Itens(Model):
    __tablename__ = 'com_compras_pedido_itens'
    id_pedido_compra_item = Column(Integer,Sequence('com_compras_pedido_itens_id_pedido_compra_item_seq'), primary_key=True)
    id_pedido_compra = Column(Integer)
    id_produto = Column(Integer)
    id_almoxarifado = Column(Integer)
    quantidade = Column(Numeric(12,3))
    valor = Column(Numeric(12,2))
    vl_desconto = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Sol_Cot_Itens(Model):
    __tablename__ = 'com_compras_sol_cot_itens'
    id_item = Column(Integer,Sequence('com_compras_sol_cot_itens_id_item_seq'), primary_key=True)
    id_solicitacao = Column(Integer)
    id_cotacao = Column(Integer)
    id_produto = Column(Integer)
    quantidade_solicitada = Column(Numeric(12,3))
    quantidade_cotada = Column(Numeric(12,3))
    data_necessidade = Column(Date)
    id_almoxarifado = Column(Integer)
    valor_fornecedor1 = Column(Numeric(12,2))
    pedir_fornecedor1 = Column(Integer)
    valor_fornecedor2 = Column(Numeric(12,2))
    pedir_fornecedor2 = Column(Integer)
    valor_fornecedor3 = Column(Numeric(12,2))
    pedir_fornecedor3 = Column(Integer)
    valor_fornecedor4 = Column(Numeric(12,2))
    pedir_fornecedor4 = Column(Integer)
    valor_fornecedor5 = Column(Numeric(12,2))
    pedir_fornecedor5 = Column(Integer)
    flag_aprovado = Column(Integer)
    motivo_nao_aprovado = Column(String(200))
    tipo_servico = Column(Integer)
    item_origem = Column(Integer)
    qtd_aprovada = Column(Numeric(12,3))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Solicitacao(Model):
    __tablename__ = 'com_compras_solicitacao'
    id_solicitacao = Column(Integer,Sequence('com_compras_solicitacao_id_solicitacao_seq'), primary_key=True)
    numero_solicitacao = Column(String(13))
    data_hora_emissao = Column(DateTime)
    id_solicitante = Column(Integer)
    id_departamento = Column(Integer)
    id_aprovador = Column(Integer)
    data_hora_aprovacao = Column(DateTime)
    situacao = Column(Integer)
    observacao = Column(String(250))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    placa_veic_os = Column(String(8))
    id_os_solic = Column(Integer)
    id_req_solic = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Sugestao_Cfop_Cst(Model):
    __tablename__ = 'com_compras_sugestao_cfop_cst'
    id = Column(Integer,Sequence('com_compras_sugestao_cfop_cst_id_seq'), primary_key=True)
    fk_codigo_cfop = Column(String(4))
    tipo_item = Column(String(2))
    cst_icms = Column(String(3))
    cst_pis = Column(String(2))
    cst_cofins = Column(String(2))

    def __repr__(self):
        return self.__tablename__



class Com_Compras_Temp(Model):
    __tablename__ = 'com_compras_temp'
    id = Column(Integer,Sequence('com_compras_temp_id_seq'), primary_key=True)
    id_compra = Column(Integer)
    numero_compra = Column(String(13))
    id_centro_custo = Column(Integer)
    status = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    cnpj_fornecedor = Column(String(14))
    tipo_documento = Column(String(1))
    numero_pedido_compra = Column(String(13))
    modelo_doc_fiscal = Column(String(2))
    serie_doc = Column(String(3))
    numero_documento = Column(String(9))
    chave_nfe = Column(String(44))
    data_emissao = Column(Date)
    data_entrada = Column(Date)
    data_cancelamento = Column(Date)
    motivo_cancelamento = Column(String(50))
    tipo_pagamento = Column(String(1))
    vl_desconto = Column(Numeric(10,2))
    vl_abatimento_nt = Column(Numeric(10,2))
    vl_mercadoria = Column(Numeric(10,2))
    vl_frete = Column(Numeric(10,2))
    vl_seguro = Column(Numeric(10,2))
    vl_outras_despesas = Column(Numeric(10,2))
    vl_base_calculo = Column(Numeric(10,2))
    vl_icms = Column(Numeric(10,2))
    vl_base_calculo_st = Column(Numeric(10,2))
    vl_icms_st = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    vl_pis = Column(Numeric(10,2))
    vl_confins = Column(Numeric(10,2))
    vl_pis_st = Column(Numeric(10,2))
    vl_cofins_st = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    observacao = Column(String(250))
    sub_serie = Column(String(5))
    tipo_frete = Column(String(1))
    cnpj_cpf_transportador = Column(String(14))
    ie_transportador = Column(String(14))
    placa_veiculo = Column(String(10))
    placa_veiculo_uf = Column(String(2))
    quantidade_volumes = Column(Integer)
    especie = Column(String(40))
    peso_liquido = Column(Numeric(10,4))
    peso_bruto = Column(Numeric(10,4))
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Com_Condicoes_Pgto(Model):
    __tablename__ = 'com_condicoes_pgto'
    id_condicao_pgto = Column(Integer,Sequence('com_condicoes_pgto_id_condicao_pgto_seq'), primary_key=True)
    descricao_condicao = Column(String(60))
    flag_compra = Column(Integer)
    flag_venda = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Condicoes_Pgto_Parcelas(Model):
    __tablename__ = 'com_condicoes_pgto_parcelas'
    id_condicao_pgto_parcela = Column(Integer,Sequence('com_condicoes_pgto_parcelas_id_condicao_pgto_parcela_seq'), primary_key=True)
    id_condicao_pgto = Column(Integer)
    parcela = Column(Integer)
    percentual = Column(Numeric(5,2))
    prazo_pgto_dias = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Fabricante_Produto(Model):
    __tablename__ = 'com_fabricante_produto'
    id_fabricante = Column(Integer,Sequence('com_fabricante_produto_id_fabricante_seq'), primary_key=True)
    codigo_fabricante = Column(Integer)
    fabricante = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Com_Faturas_Temp(Model):
    __tablename__ = 'com_faturas_temp'
    id = Column(Integer,Sequence('com_faturas_temp_id_seq'), primary_key=True)
    id_compra = Column(Integer)
    numero = Column(String(15))
    data_vencimento = Column(Date)
    valor = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Com_Fornecedor_Temp(Model):
    __tablename__ = 'com_fornecedor_temp'
    id = Column(Integer,Sequence('com_fornecedor_temp_id_seq'), primary_key=True)
    id_compra = Column(Integer)
    tipo = Column(Integer)
    nome_razao = Column(String(50))
    fantasia = Column(String(40))
    cnpj_cpf = Column(String(14))
    iest = Column(String(15))
    endereco = Column(String(50))
    numero = Column(String(10))
    cep = Column(String(8))
    bairro = Column(String(30))
    cod_ibge = Column(String(7))
    nome_cidade = Column(String(50))
    estado = Column(String(2))
    ddd = Column(String(2))
    telefone = Column(String(8))
    cod_pais = Column(String(4))
    id_cidade = Column(Integer)
    id_fornecedor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Nf(Model):
    __tablename__ = 'com_nf'
    id_nf = Column(Integer,Sequence('com_nf_id_nf_seq'), primary_key=True)
    entrada_saida = Column(String(1))
    id_natureza_operacao = Column(String(4))
    id_tipo_emissao = Column(Integer)
    id_tipo_ambiente = Column(Integer)
    id_transportador = Column(Integer)
    id_finalidade_emissao = Column(Integer)
    consumidor = Column(Integer)
    numero_nota_fiscal = Column(String(13))
    id_centro_custo = Column(Integer)
    id_plano_contas = Column(Integer)
    status = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    cnpj_cpf_cliente = Column(String(14))
    cnpj_fornecedor = Column(String(14))
    numero_pedido_saida = Column(String(13))
    modelo_doc_fiscal = Column(String(2))
    serie_doc = Column(String(3))
    sub_serie = Column(String(5))
    numero_documento = Column(String(9))
    chave_eletronica = Column(String(44))
    data_emissao = Column(DateTime)
    data_saida_entrada = Column(DateTime)
    data_cancelamento = Column(DateTime)
    motivo_cancelamento = Column(String(250))
    tipo_pagamento = Column(String(1))
    vl_desconto = Column(Numeric(10,2))
    vl_abatimento_nt = Column(Numeric(10,2))
    vl_mercadoria = Column(Numeric(10,2))
    tipo_frete = Column(String(1))
    vl_frete = Column(Numeric(10,2))
    vl_seguro = Column(Numeric(10,2))
    vl_outras_despesas = Column(Numeric(10,2))
    vl_base_calculo = Column(Numeric(10,2))
    vl_icms = Column(Numeric(10,2))
    vl_base_calculo_st = Column(Numeric(10,2))
    vl_icms_st = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    vl_pis = Column(Numeric(10,2))
    vl_cofins = Column(Numeric(10,2))
    vl_pis_st = Column(Numeric(10,2))
    vl_cofins_st = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    observacao = Column(text)
    data_registro = Column(DateTime)
    valor_centro_custo_pred = Column(Numeric(12,2))
    status_financeiro = Column(Integer)
    ind_emit = Column(String(1))
    id_nf_referenciada = Column(Integer)
    cstat = Column(Integer)
    xmotivo = Column(text)
    prot_autorizacao_nfe = Column(String(15))
    usuario_cancelamento = Column(Integer)
    xml_proc_cancelamento = Column(text)
    protocolo_cancelamento = Column(String(15))
    data_autorizacao = Column(DateTime)
    numero_lote = Column(Integer)
    xml_nfe_original = Column(text)
    xml_nfe_com_assinatura = Column(text)
    xml_proc_nfe = Column(text)
    xml_retorno = Column(text)
    numero_recibo = Column(String(30))
    nro_fatura = Column(String(13))
    placa_veiculo = Column(String(8))
    nro_correcoes = Column(Integer)
    indfinal = Column(Integer)
    indpres = Column(Integer)
    iss_dcompet = Column(Date)
    trans_peso_bruto = Column(Numeric(12,3))
    trans_peso_liquido = Column(Numeric(12,3))
    trans_qtd_volumes = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Nf_Itens(Model):
    __tablename__ = 'com_nf_itens'
    id_nf_item = Column(Integer,Sequence('com_nf_itens_id_nf_item_seq'), primary_key=True)
    id_nf = Column(Integer)
    id_produto = Column(Integer)
    descricao_complementar = Column(String(50))
    quantidade = Column(Numeric(10,6))
    unidade = Column(String(6))
    vl_item = Column(Numeric(10,4))
    vl_desconto = Column(Numeric(10,2))
    movimentacao_fisica = Column(Integer)
    cst_icms = Column(String(3))
    cfop = Column(String(4))
    cod_natureza = Column(String(10))
    vl_base_icms = Column(Numeric(10,2))
    aliquota_icms = Column(Numeric(10,2))
    valor_icms = Column(Numeric(10,2))
    valor_base_icms_st = Column(Numeric(10,2))
    aliquota_icms_st = Column(Numeric(10,2))
    valor_icms_st = Column(Numeric(10,2))
    cst_ipi = Column(String(2))
    cod_enq = Column(String(3))
    vl_base_ipi = Column(Numeric(10,2))
    aliquota_ipi = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    cst_pis = Column(String(2))
    vl_base_pis = Column(Numeric(10,2))
    aliquota_pis_perc = Column(Numeric(10,2))
    quantidade_base_pis = Column(Numeric(10,3))
    vl_aliquota_pis = Column(Numeric(10,4))
    valor_pis = Column(Numeric(10,2))
    cst_cofins = Column(String(2))
    valor_base_cofins = Column(Numeric(10,2))
    aliquota_cofins_perc = Column(Numeric(10,2))
    quantidade_base_cofins = Column(Numeric(10,3))
    vl_aliquota_cofins = Column(Numeric(10,4))
    vl_cofins = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    vl_frete = Column(Numeric(10,2))
    comb_cprodanp = Column(String(9))
    comb_codif = Column(String(21))
    comb_qtemp = Column(Numeric(16,2))
    comb_ufcons = Column(String(2))
    comb_qbcprod = Column(Numeric(15,4))
    comb_valiqprod = Column(Numeric(15,4))
    comb_vcide = Column(Numeric(15,2))
    observacao = Column(String(250))
    issqn_valor_bc = Column(Numeric(10,2))
    issqn_aliquota = Column(Numeric(5,2))
    comb_pmixcn = Column(Numeric(6,4))
    pdevol = Column(Numeric(5,2))
    vipidevol = Column(Numeric(12,2))
    vtottrib = Column(Numeric(12,2))
    issqn_vdeducao = Column(Numeric(12,2))
    issqn_voutro = Column(Numeric(12,2))
    issqn_vdescincond = Column(Numeric(12,2))
    issqn_vdesccond = Column(Numeric(12,2))
    issqn_vissret = Column(Numeric(12,2))
    issqn_indiss = Column(Integer)
    issqn_cservico = Column(String(20))
    issqn_cmun = Column(String(7))
    issqn_cpais = Column(String(7))
    issqn_nprocesso = Column(String(30))
    issqn_indincentivo = Column(Integer)
    id_almoxarifado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Nf_Itens_Medicamentos(Model):
    __tablename__ = 'com_nf_itens_medicamentos'
    id_lote_medicamento = Column(Integer,Sequence('com_nf_itens_medicamentos_id_lote_medicamento_seq'), primary_key=True)
    id_nf_item = Column(Integer)
    id_produto = Column(Integer)
    lote_numero = Column(String(20))
    lote_quantidade = Column(Numeric(11,3))
    lote_data_fabricacao = Column(Date)
    lote_data_validade = Column(Date)
    lote_vpmc = Column(Numeric(15,2))

    def __repr__(self):
        return self.__tablename__



class Com_Nf_Ref(Model):
    __tablename__ = 'com_nf_ref'
    id_nf_ref = Column(Integer,Sequence('com_nf_ref_id_nf_ref_seq'), primary_key=True)
    id_nf = Column(Integer)
    refnfe = Column(String(44))

    def __repr__(self):
        return self.__tablename__



class Com_Nfe_Lote(Model):
    __tablename__ = 'com_nfe_lote'
    id_lote = Column(Integer,Sequence('com_nfe_lote_id_lote_seq'), primary_key=True)
    numero_lote = Column(Integer)
    data_hora_geracao = Column(DateTime)
    data_hora_trasmissao = Column(DateTime)
    data_hora_cancelamento = Column(DateTime)
    data_hora_correcao = Column(DateTime)
    numero_recibo_1 = Column(String(30))
    numero_recibo_2 = Column(String(30))
    numero_recibo_3 = Column(String(30))
    numero_recibo_4 = Column(String(30))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    recebeu_retorno = Column(Integer)
    cstat = Column(String(3))
    xmotivo = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Com_Nfe_Lote_Itens(Model):
    __tablename__ = 'com_nfe_lote_itens'
    id_lote_itens = Column(Integer,Sequence('com_nfe_lote_itens_id_lote_itens_seq'), primary_key=True)
    numero_lote = Column(Integer)
    id_nf = Column(Integer)
    xml_nfe_original = Column(text)
    xml_nfe_com_assinatura = Column(text)
    xml_retorno = Column(text)
    numero_recibo = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Com_Nfe_Parametros(Model):
    __tablename__ = 'com_nfe_parametros'
    id_nfe_parametro = Column(Integer,Sequence('com_nfe_parametros_id_nfe_parametro_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    certificado = Column(text)
    nfe_versao = Column(String(4))
    sigla_ws = Column(String(4))
    sigla_uf = Column(String(2))
    nfe_modelo = Column(String(3))
    nfe_serie = Column(String(3))
    nfe_ambiente = Column(Integer)
    nfe_proxy = Column(String(50))
    nfe_usuario_proxy = Column(String(30))
    nfe_senha_proxy = Column(String(15))
    nfe_licenca = Column(text)
    nfe_tipo_emissao = Column(Integer)
    cert_data_inicio = Column(DateTime)
    cert_data_final = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Com_Op_Estoque(Model):
    __tablename__ = 'com_op_estoque'
    id_operacao = Column(Integer,Sequence('com_op_estoque_id_operacao_seq'), primary_key=True)
    descricao_operacao = Column(String(20))
    credito_debito = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Pedido(Model):
    __tablename__ = 'com_pedido'
    id_pedido = Column(Integer,Sequence('com_pedido_id_pedido_seq'), primary_key=True)
    nro_pedido = Column(String(13))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    data_pedido = Column(Date)
    cnpj_cpf_cliente = Column(String(14))
    id_vendedor = Column(Integer)
    valor_pedido = Column(Numeric(12,2))
    vl_desconto = Column(Numeric(10,2))
    vl_acrecimo = Column(Numeric(10,2))
    obs_pedido = Column(text)
    id_transportador = Column(Integer)
    tipo_pagto = Column(Integer)
    faturado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Pedido_Itens(Model):
    __tablename__ = 'com_pedido_itens'
    id_pedido_itens = Column(Integer,Sequence('com_pedido_itens_id_pedido_itens_seq'), primary_key=True)
    id_pedido = Column(Integer)
    id_produto = Column(Integer)
    quantidade = Column(Numeric(12,3))
    valor = Column(Numeric(12,2))
    vl_desconto = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos(Model):
    __tablename__ = 'com_produtos'
    id_produto = Column(Integer,Sequence('com_produtos_id_produto_seq'), primary_key=True)
    codigo_produto = Column(String(8))
    descr_item = Column(String(150))
    cod_barra = Column(String(128))
    id_unidade = Column(Integer)
    tipo_item = Column(String(2))
    codigo_mercosul = Column(String(8))
    codigo_ex = Column(String(3))
    codigo_genero = Column(String(2))
    codigo_servico = Column(String(4))
    tipo_tributacao = Column(Integer)
    cst_icms = Column(String(3))
    cfop = Column(String(4))
    aliquota_icms = Column(Numeric(6,2))
    aliquota_icms_st = Column(Numeric(6,2))
    reducao_icms = Column(Numeric(6,2))
    cst_ipi = Column(String(2))
    aliquota_ipi = Column(Numeric(6,2))
    cst_pis = Column(String(2))
    aliquota_pis = Column(Numeric(9,4))
    base_pis = Column(Numeric(6,2))
    aliquota_pis_st = Column(Numeric(6,2))
    base_pis_st = Column(Numeric(6,2))
    cst_confins = Column(String(2))
    aliquota_confins = Column(Numeric(9,4))
    base_confins = Column(Numeric(6,2))
    aliquota_confins_st = Column(Numeric(6,2))
    base_confins_st = Column(Numeric(6,2))
    informacao_compl = Column(String(200))
    data_cadastro = Column(DateTime)
    usuario_cadastro = Column(String(30))
    data_alteracao = Column(DateTime)
    usuario_alteracao = Column(String(30))
    referencia = Column(String(30))
    empresa = Column(String(3))
    filial = Column(String(3))
    codigo_fabricante = Column(Integer)
    natureza_tributacao = Column(Integer)
    id_old = Column(Integer)
    flg_vasilhame = Column(Integer)
    id_vasilhame = Column(Integer)
    flg_mov_estoque = Column(Integer)
    id_grupo = Column(Integer)
    id_classif_fiscal = Column(Integer)
    id_classif_tribut = Column(Integer)
    tamanho = Column(String(50))
    cor = Column(String(20))
    peso_liquido = Column(Numeric(12,4))
    peso_bruto = Column(Numeric(12,4))
    valor_custo = Column(Numeric(12,2))
    valor_venda = Column(Numeric(12,2))
    qtd_estoque = Column(Numeric(12,4))
    qtd_est_min = Column(Numeric(12,4))
    cod_barra_atacado = Column(String(128))
    id_unidade_atacado = Column(Integer)
    valor_venda_atacado = Column(Numeric(12,2))
    fator_baixa_atacado = Column(Numeric(12,4))
    ativo_inativo = Column(Integer)
    imagem_prod = Column(String(100))
    comb_cprodanp = Column(String(9))
    detespecifico = Column(Integer)
    issqn_aliquota = Column(Numeric(5,2))
    issqn_clistserv = Column(Integer)
    issqn_csittrib = Column(String(5))
    totvs_idprd = Column(String(15))
    totvs_idnat = Column(String(15))
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))
    totvs_conta_cotabil = Column(String(55))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Cores(Model):
    __tablename__ = 'com_produtos_cores'
    id_cor = Column(Integer,Sequence('com_produtos_cores_id_cor_seq'), primary_key=True)
    cor = Column(String(150))
    rgb = Column(String(12))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_De_Para(Model):
    __tablename__ = 'com_produtos_de_para'
    id_produto_de_para = Column(Integer,Sequence('com_produtos_de_para_id_produto_de_para_seq'), primary_key=True)
    id_produto = Column(Integer)
    data_inicial = Column(Date)
    data_final = Column(Date)
    de_descricao = Column(String(50))
    para_descricao = Column(String(50))
    de_codigo = Column(String(8))
    para_codigo = Column(String(8))
    informado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Empresa_Fornecedor(Model):
    __tablename__ = 'com_produtos_empresa_fornecedor'
    id = Column(Integer,Sequence('com_produtos_empresa_fornecedor_id_seq'), primary_key=True)
    fk_id_fornecedor = Column(Integer)
    codigo_produto_fornecedor = Column(String(30))
    fk_codigo_produto = Column(String(8))
    fk_id_produto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Grupos(Model):
    __tablename__ = 'com_produtos_grupos'
    id_grupo = Column(Integer,Sequence('com_produtos_grupos_id_grupo_seq'), primary_key=True)
    descr_grupo = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Lotes(Model):
    __tablename__ = 'com_produtos_lotes'
    id_produtos_lotes = Column(Integer,Sequence('com_produtos_lotes_id_produtos_lotes_seq'), primary_key=True)
    cnpj_fornecedor = Column(String(14))
    id_produto = Column(Integer)
    lote_numero = Column(String(20))
    lote_data_fabricacao = Column(Date)
    lote_data_validade = Column(Date)
    lote_quantidade = Column(Numeric(11,3))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Sugestao_Cfop_Cst(Model):
    __tablename__ = 'com_produtos_sugestao_cfop_cst'
    id = Column(Integer,Sequence('com_produtos_sugestao_cfop_cst_id_seq'), primary_key=True)
    fk_com_produtos_empresa_fornecedor_id = Column(Integer)
    cfop_fornecedor = Column(String(4))
    cfop_entrada = Column(String(4))
    cst_icms = Column(String(4))
    cst_pis = Column(String(2))
    cst_cofins = Column(String(2))

    def __repr__(self):
        return self.__tablename__



class Com_Produtos_Temp(Model):
    __tablename__ = 'com_produtos_temp'
    id = Column(Integer,Sequence('com_produtos_temp_id_seq'), primary_key=True)
    cod_prod_for = Column(String(20))
    ncm = Column(String(8))
    codigo_produto = Column(String(8))
    descricao = Column(String(150))
    id_unidade = Column(Integer)
    tipo_item = Column(String(2))
    cst_icms = Column(String(3))
    cfop = Column(String(4))
    cfop_for = Column(String(4))
    aliquota_icms = Column(Numeric(10,2))
    cst_ipi = Column(String(2))
    aliquota_ipi = Column(Numeric(10,2))
    cst_pis = Column(String(2))
    aliquota_pis = Column(Numeric(10,2))
    cst_cofins = Column(String(2))
    aliquota_cofins = Column(Numeric(10,2))
    numero_item = Column(Numeric(3,0))
    quantidade = Column(Numeric(10,5))
    unidade = Column(String(6))
    vl_item = Column(Numeric(10,4))
    vl_desconto = Column(Numeric(10,2))
    movimentacao_fisica = Column(Integer)
    vl_base_icms = Column(Numeric(10,2))
    valor_icms = Column(Numeric(10,2))
    valor_base_icms_st = Column(Numeric(10,2))
    aliquota_icms_st = Column(Numeric(10,2))
    valor_icms_st = Column(Numeric(10,2))
    vl_base_ipi = Column(Numeric(10,2))
    vl_ipi = Column(Numeric(10,2))
    vl_base_pis = Column(Numeric(10,2))
    quantidade_base_pis = Column(Numeric(10,3))
    vl_aliquota_pis = Column(Numeric(10,4))
    valor_pis = Column(Numeric(10,2))
    valor_base_cofins = Column(Numeric(10,2))
    quantidade_base_cofins = Column(Numeric(10,3))
    vl_aliquota_cofins = Column(Numeric(10,4))
    vl_cofins = Column(Numeric(10,2))
    vl_total = Column(Numeric(10,2))
    vl_frete = Column(Numeric(10,2))
    observacao = Column(String(250))
    id_produto = Column(Integer)
    parametrizado = Column(Integer)
    cadastrado = Column(Integer)
    id_temp = Column(Integer)
    usuario_cadastro = Column(String(30))
    empresa = Column(String(3))
    id_fornecedor = Column(Integer)
    id_almoxarifado = Column(Integer)
    totvs_idnat = Column(String(15))
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))
    totvs_conta_cotabil = Column(String(55))

    def __repr__(self):
        return self.__tablename__



class Com_Requisicao(Model):
    __tablename__ = 'com_requisicao'
    id_requisicao = Column(Integer,Sequence('com_requisicao_id_requisicao_seq'), primary_key=True)
    numero_requisicao = Column(String(13))
    data_hora_emissao = Column(DateTime)
    id_requisitante = Column(Integer)
    id_departamento = Column(Integer)
    id_aprovador = Column(Integer)
    data_hora_aprovacao = Column(DateTime)
    situacao = Column(Integer)
    observacao = Column(String(250))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Com_Requisicao_Itens(Model):
    __tablename__ = 'com_requisicao_itens'
    id_item_req = Column(Integer,Sequence('com_requisicao_itens_id_item_req_seq'), primary_key=True)
    id_requisicao = Column(Integer)
    id_produto = Column(Integer)
    quantidade_requisitada = Column(Numeric(12,3))
    data_necessidade = Column(Date)
    id_almoxarifado = Column(Integer)
    valor_produto = Column(Numeric(12,2))
    status = Column(Integer)
    flag_aprovado = Column(Integer)
    motivo_nao_aprovado = Column(String(200))
    id_estoquista = Column(Integer)
    qtd_entregue = Column(Numeric(12,3))
    qtd_pendente = Column(Numeric(12,3))
    qtd_gerar = Column(Numeric(12,3))
    item_obs = Column(String(50))
    qtd_aprovada = Column(Numeric(12,3))

    def __repr__(self):
        return self.__tablename__



class Com_Solicitacao_Produtos_Estoquista(Model):
    __tablename__ = 'com_solicitacao_produtos_estoquista'
    id_solicitacao = Column(Numeric(7,0))
    numero_solicitacao = Column(Numeric(6,0))
    data_solicitacao = Column(Date)
    hora_solicitacao = Column(String(5))
    cod_filial = Column(String(3))
    almoxarifado = Column(String(10))
    id_usuario = Column(Integer)
    cod_empresa = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Com_Solicitacao_Produtos_Estoquista_Itens(Model):
    __tablename__ = 'com_solicitacao_produtos_estoquista_itens'
    id_solicitacao = Column(Numeric(7,0))
    id_produto = Column(Integer)
    qtde_pedida = Column(Numeric(7,3))
    qtde_atendida = Column(Numeric(7,3))
    justificativa = Column(String(50))
    autorizado_cotacao = Column(Numeric(1,0))
    id_item_solicitacao_usuario = Column(Integer)
    id_usuario = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Com_Solicitacao_Produtos_Usuario(Model):
    __tablename__ = 'com_solicitacao_produtos_usuario'
    data_solicitacao = Column(Date)
    hora_solicitacao = Column(String(5))
    cod_filial = Column(String(3))
    status = Column(String(1))
    id_usuario = Column(Integer)
    cod_empresa = Column(String(3))
    numero_solicitacao = Column(String(13))
    id_solicitacao = Column(Integer,Sequence('com_solicitacao_produtos_usuario_id_solicitacao_seq'), primary_key=True)

    def __repr__(self):
        return self.__tablename__



class Com_Solicitacao_Produtos_Usuario_Itens(Model):
    __tablename__ = 'com_solicitacao_produtos_usuario_itens'
    id_produto = Column(Integer)
    qtde_pedida = Column(Numeric(7,3))
    qtde_atendida = Column(Numeric(7,3))
    justificativa = Column(String(50))
    numero_solicitacao = Column(String(13))
    id_item_solicitacao = Column(Integer,Sequence('com_solicitacao_produtos_usuario_itens_id_item_solicitacao_seq'), primary_key=True)
    status = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Conf_Cursoradapter(Model):
    __tablename__ = 'conf_cursoradapter'
    id = Column(Integer,Sequence('conf_cursoradapter_id_seq'), primary_key=True)
    id_formulario = Column(Integer)
    nome_cursoradapter = Column(text)
    ativo = Column(Integer)
    select_cmd = Column(text)
    cursor_schema = Column(text)
    update_name_list = Column(text)
    updatable_field_list = Column(text)

    def __repr__(self):
        return self.__tablename__



class Conf_Formulario(Model):
    __tablename__ = 'conf_formulario'
    id_formulario = Column(Integer,Sequence('conf_formulario_id_formulario_seq'), primary_key=True)
    nome_formulario = Column(text)
    obsservacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Contador_Formularios(Model):
    __tablename__ = 'contador_formularios'
    id_formulario = Column(Integer,Sequence('contador_formularios_id_formulario_seq'), primary_key=True)
    codigo_filial = Column(String(3))
    tipo_formulario = Column(String(20))
    serie = Column(String(10))
    numero_atual = Column(Integer)
    numero_final_serie = Column(Integer)
    avisar_restando = Column(Integer)
    codigo_empresa = Column(String(3))
    data_validade = Column(Date)
    aviso_formulario = Column(text)
    email_aviso = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Contato_Site(Model):
    __tablename__ = 'contato_site'
    id_contato = Column(Integer,Sequence('contato_site_id_contato_seq'), primary_key=True)
    nome_contato = Column(String(100))
    email_contato = Column(String(100))
    telefone_contato = Column(String(50))
    whatsapp = Column(String(50))
    empresa = Column(String(100))
    comentario = Column(text)
    origem_contato = Column(String(50))
    data_cadastro = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Acoes(Model):
    __tablename__ = 'crm_acoes'
    id_acao = Column(Integer,Sequence('crm_acoes_id_acao_seq'), primary_key=True)
    nome_acao = Column(String(50))
    horas_previstas = Column(Numeric(10,1))
    obs_acao = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Avisos(Model):
    __tablename__ = 'crm_avisos'
    id_aviso = Column(Integer,Sequence('crm_avisos_id_aviso_seq'), primary_key=True)
    dt_emissao = Column(Date)
    corpo_aviso = Column(text)
    status_aviso = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Calendario_Compromissos(Model):
    __tablename__ = 'crm_calendario_compromissos'
    id_calendario = Column(Integer,Sequence('crm_calendario_compromissos_id_calendario_seq'), primary_key=True)
    titulo_compromisso = Column(String(100))
    data_inicio = Column(Date)
    data_final = Column(Date)
    recorrente = Column(String(1))
    periodicidade_recorrente = Column(String(1))
    id_usuario = Column(Integer)
    id_cliente = Column(Integer)
    id_lancamento_externo = Column(Integer)
    origem_lancamento = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Crm_Cargos(Model):
    __tablename__ = 'crm_cargos'
    id_cargo = Column(Integer,Sequence('crm_cargos_id_cargo_seq'), primary_key=True)
    nome_cargo = Column(String(50))
    obs_cargo = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Comp_Cont(Model):
    __tablename__ = 'crm_comp_cont'
    id_comp_cont = Column(Integer,Sequence('crm_comp_cont_id_comp_cont_seq'), primary_key=True)
    id_compromisso = Column(Integer)
    id_contato = Column(Integer)
    id_cargo = Column(Integer)
    dt_prev_de = Column(Date)
    dt_prev_ate = Column(Date)
    dt_real_de = Column(Date)
    dt_real_ate = Column(Date)
    flg_email_enviar = Column(Integer)
    flg_email_recebido = Column(Integer)
    status_comp_cont = Column(Integer)
    obs_comp_cont = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Comp_Cont_Acao(Model):
    __tablename__ = 'crm_comp_cont_acao'
    id_comp_cont_acao = Column(Integer,Sequence('crm_comp_cont_acao_id_comp_cont_acao_seq'), primary_key=True)
    id_comp_cont = Column(Integer)
    id_acao = Column(Integer)
    dt_acao = Column(Date)
    horas_previstas = Column(Numeric(10,1))
    horas_realizadas = Column(Numeric(10,1))
    status_acao = Column(Integer)
    obs_comp_cont_acao = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Compromissos(Model):
    __tablename__ = 'crm_compromissos'
    id_compromisso = Column(Integer,Sequence('crm_compromissos_id_compromisso_seq'), primary_key=True)
    nm_compromisso = Column(String(50))
    id_processo = Column(Integer)
    ordem_comp = Column(Integer)
    dt_prev_de = Column(Date)
    dt_prev_ate = Column(Date)
    dt_real_de = Column(Date)
    dt_real_ate = Column(Date)
    status_compromisso = Column(Integer)
    obs_compromisso = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Compromissos_Fotos(Model):
    __tablename__ = 'crm_compromissos_fotos'
    id_compromisso_foto = Column(Integer,Sequence('crm_compromissos_fotos_id_compromisso_foto_seq'), primary_key=True)
    id_compromisso = Column(Integer)
    nome_arquivo = Column(String(120))
    data_upload = Column(Date)
    caminho_arquivo = Column(String(150))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Cont_Relacoes(Model):
    __tablename__ = 'crm_cont_relacoes'
    id_cont_relacao = Column(Integer,Sequence('crm_cont_relacoes_id_cont_relacao_seq'), primary_key=True)
    id_contato = Column(Integer)
    id_estrangeiro = Column(Integer)
    flg_estrangeiro = Column(String(1))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Contatos(Model):
    __tablename__ = 'crm_contatos'
    id_contato = Column(Integer,Sequence('crm_contatos_id_contato_seq'), primary_key=True)
    nome_razao = Column(String(50))
    id_cargo = Column(Integer)
    id_tipo_endereco = Column(Integer)
    endereco = Column(String(50))
    numero = Column(String(10))
    complemento = Column(String(50))
    bairro = Column(String(30))
    id_cidade = Column(Numeric(5,0))
    cep = Column(String(8))
    nacionalidade = Column(String(30))
    naturalidade = Column(String(25))
    cnpj_cpf = Column(String(18))
    identidade = Column(String(20))
    nascimento = Column(Date)
    sexo = Column(String(9))
    estado_civil = Column(String(10))
    grau_instrucao = Column(String(23))
    obs_contato = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Contatos_Detalhes(Model):
    __tablename__ = 'crm_contatos_detalhes'
    id_contato_detalhe = Column(Integer,Sequence('crm_contatos_detalhes_id_contato_detalhe_seq'), primary_key=True)
    id_contato = Column(Integer)
    tp_detalhe = Column(String(20))
    detalhe = Column(String(150))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Contatos_Fotos(Model):
    __tablename__ = 'crm_contatos_fotos'
    id_contato_foto = Column(Integer,Sequence('crm_contatos_fotos_id_contato_foto_seq'), primary_key=True)
    id_contato = Column(Integer)
    contato_foto = Column(text)

    def __repr__(self):
        return self.__tablename__



class Crm_Contr_Cont(Model):
    __tablename__ = 'crm_contr_cont'
    id_contr_cont = Column(Integer,Sequence('crm_contr_cont_id_contr_cont_seq'), primary_key=True)
    id_contrato = Column(Integer)
    id_contato = Column(Integer)
    id_cargo = Column(Integer)
    flg_email_enviar = Column(Integer)
    flg_email_recebido = Column(Integer)
    status_contr_cont = Column(Integer)
    obs_contr_cont = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Contratos(Model):
    __tablename__ = 'crm_contratos'
    id_contrato = Column(Integer,Sequence('crm_contratos_id_contrato_seq'), primary_key=True)
    nr_contrato = Column(String(13))
    nm_contrato = Column(String(50))
    empresa = Column(String(3))
    filial = Column(String(3))
    cnpj_for = Column(String(18))
    cnpj_cli = Column(String(18))
    dt_prev_de = Column(Date)
    dt_prev_ate = Column(Date)
    dt_real_de = Column(Date)
    dt_real_ate = Column(Date)
    id_tp_doc = Column(Integer)
    id_tp_contrato = Column(Integer)
    nr_doc_origem = Column(Integer)
    serie_doc_origem = Column(String(5))
    dt_entrada_doc_origem = Column(Date)
    dt_emissao_doc_origem = Column(Date)
    flg_comp_cp = Column(Integer)
    flg_comp_cr = Column(Integer)
    valor_total_contrato = Column(Numeric(15,2))
    qtd_parc_doc_origem = Column(Numeric(4,0))
    fatura_min = Column(Integer)
    km_min = Column(Numeric(8,0))
    hr_min = Column(Numeric(8,0))
    status_doc_origem = Column(Integer)
    obs_contrato = Column(text)
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Processos(Model):
    __tablename__ = 'crm_processos'
    id_processo = Column(Integer,Sequence('crm_processos_id_processo_seq'), primary_key=True)
    nr_processo = Column(String(13))
    nm_processo = Column(String(50))
    dt_registro = Column(Date)
    status_processo = Column(Integer)
    obs_processo = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Tipos_Contrato(Model):
    __tablename__ = 'crm_tipos_contrato'
    id_tp_contrato = Column(Integer,Sequence('crm_tipos_contrato_id_tp_contrato_seq'), primary_key=True)
    tp_contrato = Column(String(50))
    obs_tpcontrato = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Crm_Tipos_Documento(Model):
    __tablename__ = 'crm_tipos_documento'
    id_tp_doc = Column(Integer,Sequence('crm_tipos_documento_id_tp_doc_seq'), primary_key=True)
    tp_doc = Column(String(50))
    obs_tpdoc = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Cubo_Pivot_Conf(Model):
    __tablename__ = 'cubo_pivot_conf'
    id_cube_pivot_conf = Column(Integer)
    codigo = Column(String(4))
    descricao = Column(String(50))
    configuracao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Debug(Model):
    __tablename__ = 'debug'
    id_debug = Column(Integer,Sequence('debug_id_debug_seq'), primary_key=True)
    descricao = Column(String(50))
    valor = Column(text)
    data_hora = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Departamentos(Model):
    __tablename__ = 'departamentos'
    id_departamento = Column(Integer,Sequence('departamentos_id_departamento_seq'), primary_key=True)
    descricao_departamento = Column(String(60))

    def __repr__(self):
        return self.__tablename__



class Departamentos_Funcionarios(Model):
    __tablename__ = 'departamentos_funcionarios'
    id_depto_funcionario = Column(Integer,Sequence('departamentos_funcionarios_id_depto_funcionario_seq'), primary_key=True)
    id_departamento = Column(Integer)
    id_funcionario = Column(Integer)
    id_usuario = Column(Integer)
    flag_aprovador = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Conhecimentos_Cobranca(Model):
    __tablename__ = 'edi_conhecimentos_cobranca'
    id_conhecimento_cobranca = Column(Integer,Sequence('edi_conhecimentos_cobranca_id_conhecimento_cobranca_seq'), primary_key=True)
    id_documento_cobranca = Column(Integer)
    serie_conhecimento = Column(String(5))
    numero_conhecimento = Column(String(12))
    linha = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Conhecimentos_Embarcados(Model):
    __tablename__ = 'edi_conhecimentos_embarcados'
    id_conhecimento_embarcado = Column(Integer,Sequence('edi_conhecimentos_embarcados_id_conhecimento_embarcado_seq'), primary_key=True)
    serie_conhecimento = Column(String(5))
    numero_conhecimento = Column(String(12))
    data_emissao = Column(Date)
    condicao_frete = Column(String(1))
    peso_transportado = Column(Numeric(13,2))
    valor_frete = Column(Numeric(13,2))
    base_calculo_icms = Column(Numeric(13,2))
    aliquota_icms = Column(Numeric(13,2))
    valor_icms = Column(Numeric(13,2))
    frete_peso = Column(Numeric(13,2))
    frete_valor = Column(Numeric(13,2))
    sec_cat = Column(Numeric(13,2))
    itr = Column(Numeric(13,2))
    despacho = Column(Numeric(13,2))
    pedagio = Column(Numeric(13,2))
    valor_ademe = Column(Numeric(13,2))
    substituicao_tributaria = Column(Integer)
    cnpj_emitente = Column(String(14))
    cnpj_remetente = Column(String(14))
    acao_documento = Column(String(1))
    tipo_transporte = Column(String(1))
    cfop = Column(String(5))
    tipo_meio_transporte = Column(String(5))
    total_outras_despesas = Column(Numeric(13,2))
    valor_iss = Column(Numeric(13,2))
    serie_conhecimento_origem = Column(String(5))
    numero_conhecimento_origem = Column(String(12))
    id_edi_intercambio = Column(Integer)
    id_conhecimentos_embarcados = Column(Integer)
    linha = Column(Integer)
    pendencias = Column(Integer)
    importado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Conhecimentos_Nf(Model):
    __tablename__ = 'edi_conhecimentos_nf'
    id_conhecimento_nf = Column(Integer,Sequence('edi_conhecimentos_nf_id_conhecimento_nf_seq'), primary_key=True)
    id_conhecimento_embarcado = Column(Integer)
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(9))
    importado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Consignatario(Model):
    __tablename__ = 'edi_consignatario'
    id_consignatario = Column(Integer,Sequence('edi_consignatario_id_consignatario_seq'), primary_key=True)
    razao_social = Column(String(40))
    cnpj_cpf = Column(String(14))
    tipo_particpante = Column(Integer)
    endereco = Column(String(40))
    bairro = Column(String(20))
    cidade = Column(String(35))
    cep = Column(String(9))
    uf = Column(String(2))
    data_embarque = Column(Date)
    inscricao_estadual = Column(String(15))
    codigo_municipio = Column(String(9))
    contato = Column(String(35))
    linha = Column(Integer)
    pendencia = Column(Integer)
    id_edi_nota_fiscal = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Destinatario(Model):
    __tablename__ = 'edi_destinatario'
    id_destinatario = Column(Integer,Sequence('edi_destinatario_id_destinatario_seq'), primary_key=True)
    razao_social = Column(String(40))
    cnpj_cpf = Column(String(14))
    tipo_particpante = Column(Integer)
    endereco = Column(String(40))
    bairro = Column(String(20))
    cidade = Column(String(35))
    cep = Column(String(9))
    uf = Column(String(2))
    data_embarque = Column(Date)
    inscricao_estadual = Column(String(15))
    codigo_municipio = Column(String(9))
    contato = Column(String(35))
    linha = Column(Integer)
    pendencia = Column(Integer)
    id_remetente = Column(Integer)
    id_edi_intercambio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Documentos_Cobranca(Model):
    __tablename__ = 'edi_documentos_cobranca'
    id_documento_cobranca = Column(Integer,Sequence('edi_documentos_cobranca_id_documento_cobranca_seq'), primary_key=True)
    tipo_documento = Column(Integer)
    serie_documento = Column(String(3))
    numero_documento = Column(String(10))
    data_emissao = Column(Date)
    data_vencimento = Column(Date)
    valor_documento = Column(Numeric(13,2))
    tipo_cobranca = Column(String(3))
    valor_icms = Column(Numeric(13,2))
    valor_juros_mora = Column(Numeric(13,2))
    data_limite_desconto = Column(Date)
    valor_desconto = Column(Numeric(13,2))
    nome_banco = Column(String(35))
    numero_agencia = Column(String(4))
    digito_agencia = Column(String(1))
    numero_conta_corrente = Column(String(10))
    digito_conta_corrente = Column(String(1))
    acao_documento = Column(String(1))
    id_edi_intercambio = Column(Integer)
    linha = Column(Integer)
    pendencias = Column(Integer)
    importado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Intercambio(Model):
    __tablename__ = 'edi_intercambio'
    id_edi_intercambio = Column(Integer,Sequence('edi_intercambio_id_edi_intercambio_seq'), primary_key=True)
    remetente = Column(String(35))
    destinatario = Column(String(35))
    arquivo_recebido = Column(text)
    data_intercambio = Column(Date)
    cnpj_transportadora = Column(String(18))
    data_processamento = Column(DateTime)
    status = Column(Integer)
    ident_documento = Column(String(3))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    mensagem = Column(text)
    total_documentos_importados = Column(Integer)
    total_documentos_nao_importados = Column(Integer)
    cnpj_embarcadora = Column(String(14))

    def __repr__(self):
        return self.__tablename__



class Edi_Log_Documento(Model):
    __tablename__ = 'edi_log_documento'
    id_log_documento = Column(Integer,Sequence('edi_log_documento_id_log_documento_seq'), primary_key=True)
    descricao = Column(String(50))
    id_edi_intercambio = Column(Integer)
    mensagem = Column(text)
    linha = Column(Integer)
    coluna = Column(Integer)
    registro = Column(String(3))
    conteudo = Column(text)
    qt_erros = Column(Integer)
    tipo_log = Column(Integer)
    id_edi_ocorrencia_entrega = Column(Integer)
    id_conhecimento_embarcado = Column(Integer)
    id_documento_cobranca = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Notas_Fiscais(Model):
    __tablename__ = 'edi_notas_fiscais'
    id_edi_nota_fiscal = Column(Integer,Sequence('edi_notas_fiscais_id_edi_nota_fiscal_seq'), primary_key=True)
    nr_romaneio = Column(String(15))
    codigo_rota = Column(String(7))
    meio_transporte = Column(Integer)
    tipo_transporte_carga = Column(Integer)
    tipo_carga = Column(Integer)
    condicao_frete = Column(String(1))
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(9))
    data_emissao = Column(Date)
    natureza_carga = Column(String(15))
    especie_carga = Column(String(15))
    qtd_volumes = Column(Numeric(13,2))
    valor_total_nota = Column(Numeric(12,2))
    peso = Column(Numeric(13,2))
    peso_cubado = Column(Numeric(13,6))
    tipo_icms = Column(String(1))
    seguro_efetuado = Column(String(1))
    valor_seguro = Column(Numeric(13,2))
    valor_cobrado = Column(Numeric(13,2))
    placa_veiculo = Column(String(7))
    carga_rapida = Column(String(1))
    frete_peso = Column(Numeric(13,2))
    frete_valor = Column(Numeric(13,2))
    total_frete = Column(Numeric(13,2))
    acao_documento = Column(String(1))
    valor_icms = Column(Numeric(13,2))
    valor_icms_retito = Column(Numeric(13,2))
    tem_bonificacao = Column(String(1))
    cfop = Column(String(4))
    tipo_periodo_entrega = Column(Integer)
    data_inicial = Column(Date)
    hora_inicial = Column(String(4))
    data_final = Column(Date)
    hora_final = Column(String(4))
    local_desembarque = Column(String(15))
    frete_diferenciado = Column(String(1))
    tabela_frete = Column(String(10))
    tipo_veiculo_transporte = Column(String(5))
    filial_contratante = Column(String(10))
    serie_conhecimento_origem = Column(String(5))
    numero_conhecimento_origem = Column(String(12))
    id_destinatario = Column(Integer)
    id_consignatario = Column(Integer)
    id_redespachador = Column(Integer)
    id_pagador = Column(Integer)
    linha = Column(Integer)
    pendencia = Column(Integer)
    chave_nfe = Column(String(45))
    peso_4 = Column(Numeric(10,4))
    cnpj_remetente = Column(String(14))
    valor_total_produtos = Column(Numeric(12,2))
    peso_liquido = Column(Numeric(10,4))
    valor_operacao = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Edi_Notas_Fiscais_Cobranca(Model):
    __tablename__ = 'edi_notas_fiscais_cobranca'
    id_nota_fiscal_cobranca = Column(Integer,Sequence('edi_notas_fiscais_cobranca_id_nota_fiscal_cobranca_seq'), primary_key=True)
    id_conhecimento_cobranca = Column(Integer)
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(9))
    data_emissao = Column(Date)
    total_peso = Column(Numeric(13,2))
    valor_total_produtos = Column(Numeric(13,2))
    linha = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Ocorrencia_Entrega(Model):
    __tablename__ = 'edi_ocorrencia_entrega'
    id_edi_ocorrencia_entrega = Column(Integer,Sequence('edi_ocorrencia_entrega_id_edi_ocorrencia_entrega_seq'), primary_key=True)
    id_edi_intercambio = Column(Integer)
    cnpj_emissora_nota_fiscal = Column(String(14))
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(9))
    codigo_ocorrencia = Column(Integer)
    data_ocorrencia = Column(Date)
    horario_ocorrencia = Column(String(4))
    codigo_obs_ocorrencia = Column(Integer)
    observacao = Column(text)
    linha = Column(Integer)
    pendencias = Column(Integer)
    importado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Ocorrencias_Comprovei(Model):
    __tablename__ = 'edi_ocorrencias_comprovei'
    id = Column(Integer,Sequence('edi_ocorrencias_comprovei_id_seq'), primary_key=True)
    codigo_status = Column(Integer)
    status = Column(String(150))
    id_ocorrencia_softlog = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Ocorrencias_Entrega(Model):
    __tablename__ = 'edi_ocorrencias_entrega'
    id = Column(Integer,Sequence('edi_ocorrencias_entrega_id_seq'), primary_key=True)
    servico_integracao = Column(Integer)
    numero_nfe = Column(String(9))
    serie_nfe = Column(String(3))
    cnpj_emitente = Column(String(14))
    data_emissao = Column(DateTime)
    chave_nfe = Column(String(44))
    status = Column(String(50))
    numero_ocorrencia = Column(Integer)
    motivo_ocorrencia = Column(String(100))
    data_ocorrencia = Column(DateTime)
    url_assinatura = Column(text)
    url_imagem = Column(text)
    recebedor = Column(text)
    doc_recebedor = Column(text)
    id_nota_fiscal_imp = Column(Integer)
    data_importacao = Column(DateTime)
    numero_protocolo = Column(text)
    id_romaneio = Column(Integer)
    latitude = Column(text)
    longitude = Column(text)
    observacao = Column(text)
    id_ocorrencia_app = Column(Integer)
    id_conhecimento = Column(Integer)
    id_conhecimento_notas_fiscais = Column(Integer)
    data_check_in = Column(DateTime)
    latitude_check_in = Column(text)
    longitude_check_in = Column(text)
    id_carga_itrack = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Pagador(Model):
    __tablename__ = 'edi_pagador'
    id_pagador = Column(Integer,Sequence('edi_pagador_id_pagador_seq'), primary_key=True)
    razao_social = Column(String(40))
    cnpj_cpf = Column(String(14))
    tipo_particpante = Column(Integer)
    endereco = Column(String(40))
    bairro = Column(String(20))
    cidade = Column(String(35))
    cep = Column(String(9))
    uf = Column(String(2))
    data_embarque = Column(Date)
    inscricao_estadual = Column(String(15))
    codigo_municipio = Column(String(9))
    contato = Column(String(35))
    linha = Column(Integer)
    pendencia = Column(Integer)
    id_edi_nota_fiscal = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Parceiros(Model):
    __tablename__ = 'edi_parceiros'
    id = Column(Integer,Sequence('edi_parceiros_id_seq'), primary_key=True)
    id_bd = Column(Integer)
    cnpj_cpf = Column(String(14))
    razao_social = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Edi_Redespachador(Model):
    __tablename__ = 'edi_redespachador'
    id_redespachador = Column(Integer,Sequence('edi_redespachador_id_redespachador_seq'), primary_key=True)
    razao_social = Column(String(40))
    cnpj_cpf = Column(String(14))
    tipo_particpante = Column(Integer)
    endereco = Column(String(40))
    bairro = Column(String(20))
    cidade = Column(String(35))
    cep = Column(String(9))
    uf = Column(String(2))
    data_embarque = Column(Date)
    inscricao_estadual = Column(String(15))
    codigo_municipio = Column(String(9))
    contato = Column(String(35))
    linha = Column(Integer)
    pendencia = Column(Integer)
    id_edi_nota_fiscal = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Remetente(Model):
    __tablename__ = 'edi_remetente'
    id_remetente = Column(Integer,Sequence('edi_remetente_id_remetente_seq'), primary_key=True)
    razao_social = Column(String(40))
    cnpj_cpf = Column(String(14))
    tipo_particpante = Column(Integer)
    endereco = Column(String(40))
    bairro = Column(String(20))
    cidade = Column(String(35))
    cep = Column(String(9))
    uf = Column(String(2))
    data_embarque = Column(Date)
    inscricao_estadual = Column(String(15))
    codigo_municipio = Column(String(9))
    contato = Column(String(35))
    linha = Column(Integer)
    pendencia = Column(Integer)
    id_edi_intercambio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Sped_Docs(Model):
    __tablename__ = 'edi_sped_docs'
    id_sped_doc = Column(Integer,Sequence('edi_sped_docs_id_sped_doc_seq'), primary_key=True)
    nome_leiaute = Column(text)
    tipo_sped = Column(text)
    versao_leiaute = Column(text)
    inicio = Column(Date)
    fim = Column(Date)
    descricao_leiaute = Column(text)
    leiaute = Column(text)
    funcao_responsavel = Column(text)
    email_remetente = Column(text)

    def __repr__(self):
        return self.__tablename__



class Edi_Tms_Agenda_Envio(Model):
    __tablename__ = 'edi_tms_agenda_envio'
    id = Column(Integer,Sequence('edi_tms_agenda_envio_id_seq'), primary_key=True)
    id_banco_dados = Column(Integer)
    id_subscricao = Column(Integer)
    ultimo_processamento = Column(DateTime)
    proximo_processamento = Column(DateTime)
    tipo_evento = Column(Integer)
    periodo = Column(Integer)
    horario = Column(String(4))
    status = Column(Integer)
    observacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Edi_Tms_Docs(Model):
    __tablename__ = 'edi_tms_docs'
    id_doc = Column(Integer,Sequence('edi_tms_docs_id_doc_seq'), primary_key=True)
    nome_leiaute = Column(text)
    leiaute_padrao = Column(text)
    descricao_leiaute = Column(text)
    formato_doc = Column(text)
    tipo_doc = Column(Integer)
    funcao_responsavel = Column(text)
    email_remetente = Column(text)
    template_statico = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Edi_Tms_Embarcador_Docs(Model):
    __tablename__ = 'edi_tms_embarcador_docs'
    id_embarcador_doc = Column(Integer,Sequence('edi_tms_embarcador_docs_id_embarcador_doc_seq'), primary_key=True)
    id_embarcador = Column(Integer)
    id_doc = Column(Integer)
    email = Column(text)
    tipo_evento = Column(Integer)
    periodo = Column(Integer)
    horario = Column(String(4))
    formato_nome_arquivo = Column(text)
    tipo_host = Column(Integer)
    host = Column(String(100))
    usuario = Column(String(250))
    senha = Column(String(100))
    port = Column(Integer)
    configuracao = Column(String(200))

    def __repr__(self):
        return self.__tablename__



class Edi_Tms_Embarcadores(Model):
    __tablename__ = 'edi_tms_embarcadores'
    id_embarcador = Column(Integer,Sequence('edi_tms_embarcadores_id_embarcador_seq'), primary_key=True)
    cnpj_cliente = Column(String(14))
    cxp_remet = Column(String(35))
    cxp_dest = Column(String(35))
    serie_nf_remet = Column(String(3))
    cnpj_fornecedor = Column(String(14))
    id_servico_integracao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Efd_Bc_Credito(Model):
    __tablename__ = 'efd_bc_credito'
    id = Column(Integer,Sequence('efd_bc_credito_id_seq'), primary_key=True)
    codigo = Column(String(2))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Consumo_Agua(Model):
    __tablename__ = 'efd_consumo_agua'
    id = Column(Integer,Sequence('efd_consumo_agua_id_seq'), primary_key=True)
    codigo = Column(String(2))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Consumo_Energia(Model):
    __tablename__ = 'efd_consumo_energia'
    id = Column(Integer,Sequence('efd_consumo_energia_id_seq'), primary_key=True)
    codigo = Column(String(2))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Cst_Confins(Model):
    __tablename__ = 'efd_cst_confins'
    id_cst_confins = Column(Integer,Sequence('efd_cst_confins_id_cst_confins_seq'), primary_key=True)
    cst_confins = Column(String(2))
    descricao = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Efd_Cst_Icms(Model):
    __tablename__ = 'efd_cst_icms'
    id_cst_icms = Column(Integer,Sequence('efd_cst_icms_id_cst_icms_seq'), primary_key=True)
    cst_icms = Column(String(3))
    descricao = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Efd_Cst_Ipi(Model):
    __tablename__ = 'efd_cst_ipi'
    id_cst_ipi = Column(Integer,Sequence('efd_cst_ipi_id_cst_ipi_seq'), primary_key=True)
    cst_ipi = Column(String(2))
    descricao = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Efd_Cst_Pis(Model):
    __tablename__ = 'efd_cst_pis'
    id_cst_pis = Column(Integer,Sequence('efd_cst_pis_id_cst_pis_seq'), primary_key=True)
    cst_pis = Column(String(2))
    descricao = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Efd_Genero_Item(Model):
    __tablename__ = 'efd_genero_item'
    id_genero_item = Column(Integer,Sequence('efd_genero_item_id_genero_item_seq'), primary_key=True)
    codigo_genero = Column(String(2))
    genero = Column(String(250))

    def __repr__(self):
        return self.__tablename__



class Efd_Grupo_Tensao(Model):
    __tablename__ = 'efd_grupo_tensao'
    id = Column(Integer,Sequence('efd_grupo_tensao_id_seq'), primary_key=True)
    codigo = Column(String(2))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Mod_Doc_Fiscal(Model):
    __tablename__ = 'efd_mod_doc_fiscal'
    id_mod_doc_fiscal = Column(Integer,Sequence('efd_mod_doc_fiscal_id_mod_doc_fiscal_seq'), primary_key=True)
    codigo = Column(String(2))
    descricao = Column(String(70))
    modelo_doc_fiscal = Column(String(4))
    situacao_fiscal = Column(String(2))

    def __repr__(self):
        return self.__tablename__



class Efd_Situacao_Fiscal(Model):
    __tablename__ = 'efd_situacao_fiscal'
    id_situacao_fiscal = Column(Integer,Sequence('efd_situacao_fiscal_id_situacao_fiscal_seq'), primary_key=True)
    codigo = Column(String(2))
    situacao_fiscal = Column(String(80))

    def __repr__(self):
        return self.__tablename__



class Efd_Tipo_Item(Model):
    __tablename__ = 'efd_tipo_item'
    id_tipo_item = Column(Integer,Sequence('efd_tipo_item_id_tipo_item_seq'), primary_key=True)
    codigo_item = Column(String(2))
    item = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Efd_Tp_Assinante(Model):
    __tablename__ = 'efd_tp_assinante'
    id = Column(Integer,Sequence('efd_tp_assinante_id_seq'), primary_key=True)
    codigo = Column(String(1))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Tp_Ligacao(Model):
    __tablename__ = 'efd_tp_ligacao'
    id = Column(Integer,Sequence('efd_tp_ligacao_id_seq'), primary_key=True)
    codigo = Column(String(1))
    descricao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Efd_Unidades_Medida(Model):
    __tablename__ = 'efd_unidades_medida'
    id_unidade = Column(Integer,Sequence('efd_unidades_medida_id_unidade_seq'), primary_key=True)
    unidade = Column(String(6))
    descricao = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Email_Uid_Imap(Model):
    __tablename__ = 'email_uid_imap'
    id = Column(Integer,Sequence('email_uid_imap_id_seq'), primary_key=True)
    empresa_acesso_servico_id = Column(Integer)
    status = Column(Integer)
    data_registro = Column(DateTime)
    data_importacao = Column(DateTime)
    data_email = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Emb_Conhecimentos_Embarcados(Model):
    __tablename__ = 'emb_conhecimentos_embarcados'
    id_emb_conhecimento_embarcado = Column(Integer,Sequence('emb_conhecimentos_embarcados_id_emb_conhecimento_embarcado_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    serie_conhecimento = Column(String(5))
    numero_conhecimento = Column(String(12))
    data_emissao = Column(Date)
    condicao_frete = Column(String(1))
    peso_transportado = Column(Numeric(13,2))
    valor_frete = Column(Numeric(13,2))
    base_calculo_icms = Column(Numeric(13,2))
    aliquota_icms = Column(Numeric(13,2))
    valor_icms = Column(Numeric(13,2))
    frete_peso = Column(Numeric(13,2))
    frete_valor = Column(Numeric(13,2))
    sec_cat = Column(Numeric(13,2))
    itr = Column(Numeric(13,2))
    despacho = Column(Numeric(13,2))
    pedagio = Column(Numeric(13,2))
    valor_ademe = Column(Numeric(13,2))
    substituicao_tributaria = Column(Integer)
    cnpj_emitente = Column(String(14))
    cnpj_remetente = Column(String(14))
    acao_documento = Column(String(1))
    tipo_transporte = Column(String(1))
    cfop = Column(String(5))
    tipo_meio_transporte = Column(String(5))
    total_outras_despesas = Column(Numeric(13,2))
    valor_iss = Column(Numeric(13,2))
    serie_conhecimento_origem = Column(String(5))
    numero_conhecimento_origem = Column(String(12))
    pendencias = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Emb_Documentos_Cobranca(Model):
    __tablename__ = 'emb_documentos_cobranca'
    id_emb_documento_cobranca = Column(Integer,Sequence('emb_documentos_cobranca_id_emb_documento_cobranca_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    cnpj_transportadora = Column(String(18))
    tipo_documento = Column(Integer)
    serie_documento = Column(String(3))
    numero_documento = Column(String(10))
    data_emissao = Column(Date)
    data_vencimento = Column(Date)
    valor_documento = Column(Numeric(13,2))
    tipo_cobranca = Column(String(3))
    valor_icms = Column(Numeric(13,2))
    valor_juros_mora = Column(Numeric(13,2))
    data_limite_desconto = Column(Date)
    valor_desconto = Column(Numeric(13,2))
    nome_banco = Column(String(35))
    numero_agencia = Column(String(4))
    digito_agencia = Column(String(1))
    numero_conta_corrente = Column(String(10))
    digito_conta_corrente = Column(String(1))
    acao_documento = Column(String(1))
    pendencias = Column(Integer)
    status = Column(Integer)
    conferido = Column(Integer)
    fechada = Column(Integer)
    limite_dif_valor = Column(Numeric(12,2))
    limite_dif_perc = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Emb_Documentos_Cobranca_Itens(Model):
    __tablename__ = 'emb_documentos_cobranca_itens'
    id_documento_cobranca_itens = Column(Integer,Sequence('emb_documentos_cobranca_itens_id_documento_cobranca_itens_seq'), primary_key=True)
    cnpj_transportadora = Column(String(18))
    serie_conhecimento = Column(String(5))
    numero_conhecimento = Column(String(12))
    id_emb_documento_cobranca = Column(Integer)
    id_emb_conhecimento_embarcado = Column(Integer)
    aliquota_diferente = Column(Integer)
    valor_frete_diferente = Column(Integer)
    aprovado = Column(Integer)
    minuta_incompativel = Column(Integer)
    mensagem = Column(String(70))
    conferido = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Emb_Notas_Fiscais(Model):
    __tablename__ = 'emb_notas_fiscais'
    id_emb_nota_fiscal = Column(Integer,Sequence('emb_notas_fiscais_id_emb_nota_fiscal_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(8))
    id_conhecimento_notas_fiscais = Column(Integer)
    cnpj_emitente = Column(String(18))
    data_emissao = Column(Date)
    total_peso = Column(Numeric(13,2))
    valor_total_produtos = Column(Numeric(13,2))
    id_emb_conhecimento_embarcado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Emb_Ocorrencia_Entrega(Model):
    __tablename__ = 'emb_ocorrencia_entrega'
    id_emb_ocorrencia_entrega = Column(Integer,Sequence('emb_ocorrencia_entrega_id_emb_ocorrencia_entrega_seq'), primary_key=True)
    cnpj_emissora_nota_fiscal = Column(String(14))
    serie_nota_fiscal = Column(String(3))
    numero_nota_fiscal = Column(String(9))
    codigo_ocorrencia = Column(Integer)
    data_ocorrencia = Column(Date)
    horario_ocorrencia = Column(String(4))
    codigo_obs_ocorrencia = Column(Integer)
    observacao = Column(text)
    pendencias = Column(Integer)
    id_emb_nota_fiscal = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Embarcador_Logistica(Model):
    __tablename__ = 'embarcador_logistica'
    id_embarcador_logistica = Column(Integer,Sequence('embarcador_logistica_id_embarcador_logistica_seq'), primary_key=True)
    nome_embarcador_logistica = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Embarcadores_Edi(Model):
    __tablename__ = 'embarcadores_edi'
    id_embarcadores_edi = Column(Integer,Sequence('embarcadores_edi_id_embarcadores_edi_seq'), primary_key=True)
    cnpj_cliente = Column(String(14))
    cxp_remet = Column(String(35))
    cxp_dest = Column(String(35))
    tipo_edi = Column(String(10))
    serie_nf_remet = Column(String(3))
    ponto_decimal = Column(Integer)
    cod_transportadora = Column(String(10))
    cod_cliente_logistica = Column(String(10))
    calculo_frete = Column(Integer)
    logistica_embarcador = Column(Integer)
    arq_ocoren = Column(Integer)
    arq_conemb = Column(Integer)
    arq_doc_cob = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Empresa(Model):
    __tablename__ = 'empresa'
    id_empresa = Column(Integer,Sequence('empresa_id_empresa_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    cnpj = Column(String(14))
    razao_social = Column(String(50))
    nome_fantasia = Column(String(50))
    cidade = Column(Numeric(4,0))
    estado = Column(String(2))
    cep = Column(String(8))
    codigo_pais = Column(Numeric(3,0))
    inscricao_estadual = Column(String(15))
    rntrc = Column(String(14))
    logo_empresa = Column(String(150))
    logo_arquivo = Column(text)
    regime_tributario = Column(Integer)
    aliquota_simples = Column(Numeric(7,2))
    credito_presumido = Column(Integer)
    perfil_empresa = Column(String(1))
    aliquota_irpj = Column(Numeric(7,2))
    aliquota_ipi = Column(Numeric(7,2))
    aliquota_csll = Column(Numeric(7,2))
    aliquota_cofins = Column(Numeric(7,2))
    aliquota_pis = Column(Numeric(7,2))
    aliquota_cpp = Column(Numeric(7,2))
    data_vecto_rntrc = Column(Date)
    id_seguradora = Column(Integer)
    perfil_sistema = Column(Integer)
    cnpj_responsavel = Column(String(14))
    nro_apolice_padrao = Column(String(20))
    ativa = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Empresa_Acesso_Servicos(Model):
    __tablename__ = 'empresa_acesso_servicos'
    id = Column(Integer,Sequence('empresa_acesso_servicos_id_seq'), primary_key=True)
    id_empresa = Column(Integer)
    id_servico_integracao = Column(Integer)
    host = Column(String(200))
    usuario = Column(String(50))
    senha = Column(String(30))
    port = Column(String(8))
    codigo_acesso = Column(text)
    modal = Column(Integer)
    averba_rodo = Column(Integer)
    averba_aereo = Column(Integer)
    averba_minuta = Column(Integer)
    descricao = Column(String(15))
    averba_manifesto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Empresa_Regime_Tributario(Model):
    __tablename__ = 'empresa_regime_tributario'
    id = Column(Integer,Sequence('empresa_regime_tributario_id_seq'), primary_key=True)
    id_empresa = Column(Integer)
    regime_tributario = Column(Integer)
    inicio = Column(Date)
    cont_cod_inc_trib = Column(Integer)
    cont_ind_apro_cred = Column(Integer)
    cont_cod_tipo_cont = Column(Integer)
    cont_ind_reg_cum = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Estado(Model):
    __tablename__ = 'estado'
    id_estado = Column(String(2))
    nome_estado = Column(String(20))
    data_alteracao = Column(DateTime)
    icms_p_juridica = Column(Numeric(5,2))
    icms_p_fisica = Column(Numeric(5,2))
    base_calculo = Column(Numeric(5,2))
    icms_isento = Column(Numeric(5,2))
    cod_ibge = Column(String(2))
    aliquota_interna = Column(Numeric(5,2))
    icms_aereo = Column(Numeric(5,2))
    icms_orgao_publico = Column(Numeric(5,2))
    id_estado_pk = Column(Integer,Sequence('estado_id_estado_pk_seq'), primary_key=True)
    icms_aereo_nao_contrib = Column(Numeric(6,2))
    icms_aliquota_interna_aereo = Column(Numeric(6,2))
    icms_orgao_publico_aereo = Column(Numeric(6,2))
    isen_interno_c = Column(Integer)
    isen_interno_n = Column(Integer)
    tomador_contribuinte = Column(Integer)
    aliquota_interna_simples = Column(Numeric(5,2))
    obs_fisco_uf = Column(text)
    aliquota_fcp = Column(Numeric(5,2))
    obs_fiscal_interna = Column(text)
    obs_fiscal_inter = Column(text)

    def __repr__(self):
        return self.__tablename__



class Estado_Aliquotas(Model):
    __tablename__ = 'estado_aliquotas'
    id_estado_aliquota = Column(Integer,Sequence('estado_aliquotas_id_estado_aliquota_seq'), primary_key=True)
    id_estado_tabela_icms = Column(Integer)
    id_tipo_aliquota = Column(Integer)
    aliquota = Column(Numeric(6,2))
    base_calculo = Column(Numeric(6,2))
    observacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Estado_Aliquotas_Icms(Model):
    __tablename__ = 'estado_aliquotas_icms'
    id_estado_aliquota_pk = Column(Integer,Sequence('estado_aliquotas_icms_id_estado_aliquota_pk_seq'), primary_key=True)
    id_estado_origem = Column(Integer)
    id_estado_destino = Column(Integer)
    icms_p_juridica = Column(Numeric(6,2))
    icms_p_fisica = Column(Numeric(6,2))
    aliquota_interna = Column(Numeric(6,2))
    icms_aereo = Column(Numeric(6,2))
    icms_orgao_publico = Column(Numeric(6,2))
    base_calculo = Column(Numeric(6,2))
    icms_aereo_nao_contrib = Column(Numeric(6,2))
    icms_aliquota_interna_aereo = Column(Numeric(6,2))
    icms_orgao_publico_aereo = Column(Numeric(6,2))
    aliquota_interna_nao_contrib = Column(Numeric(6,2))

    def __repr__(self):
        return self.__tablename__



class Estado_Operacoes_Frete(Model):
    __tablename__ = 'estado_operacoes_frete'
    id_operacao_frete = Column(Integer,Sequence('estado_operacoes_frete_id_operacao_frete_seq'), primary_key=True)
    operacao = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Estado_Tabela_Icms(Model):
    __tablename__ = 'estado_tabela_icms'
    id_estado_tabela_icms = Column(Integer,Sequence('estado_tabela_icms_id_estado_tabela_icms_seq'), primary_key=True)
    id_estado_origem = Column(Integer)
    id_estado_destino = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Estado_Tipo_Aliquotas(Model):
    __tablename__ = 'estado_tipo_aliquotas'
    id_tipo_aliquota = Column(Integer,Sequence('estado_tipo_aliquotas_id_tipo_aliquota_seq'), primary_key=True)
    tipo_aliquota = Column(String(50))
    modal = Column(Integer)
    tipo_contribuinte = Column(String(1))
    ativa = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Estoque_Movimentacao(Model):
    __tablename__ = 'estoque_movimentacao'
    id_mov = Column(Integer,Sequence('estoque_movimentacao_id_mov_seq'), primary_key=True)
    id_origem = Column(Integer)
    id_produto = Column(Integer)
    data_mov = Column(DateTime)
    id_motivo = Column(String(4))
    id_operacao = Column(Integer)
    quantidade_mov = Column(Numeric(12,3))
    valor_mov = Column(Numeric(12,2))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    id_almoxarifado = Column(Integer)
    tabela_origem = Column(String(30))
    id_usuario = Column(Integer)
    data_transacao = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Estoques(Model):
    __tablename__ = 'estoques'
    id_estoque = Column(Integer,Sequence('estoques_id_estoque_seq'), primary_key=True)
    codigo_produto = Column(Numeric(6,0))
    qtd_estoque = Column(Numeric(7,3))
    id_almoxarifado = Column(Numeric(4,0))

    def __repr__(self):
        return self.__tablename__



class Fdw_Parametros_Softlog_Cep(Model):
    __tablename__ = 'fdw_parametros_softlog_cep'
    id_parametro_softlog_cep = Column(Integer,Sequence('fdw_parametros_softlog_cep_id_parametro_softlog_cep_seq'), primary_key=True)
    ativado = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    banco_dados = Column(text)
    servidor = Column(text)
    porta = Column(text)
    usuario = Column(text)
    senha = Column(text)

    def __repr__(self):
        return self.__tablename__



class Fila_Envio_Romaneios(Model):
    __tablename__ = 'fila_envio_romaneios'
    id = Column(Integer,Sequence('fila_envio_romaneios_id_seq'), primary_key=True)
    id_notificacao = Column(Integer)
    id_tipo_servico = Column(Integer)
    id_romaneio = Column(Integer)
    data_registro = Column(DateTime)
    status_envio = Column(Integer)
    data_envio = Column(DateTime)
    status_confirmacao = Column(Integer)
    data_confirmacao = Column(DateTime)
    numero_protocolo = Column(text)
    mensagem = Column(text)
    mensagem2 = Column(text)
    mensagem3 = Column(text)
    mensagem4 = Column(text)
    tentativas_envio = Column(Integer)
    cnpjs_subscritos = Column(text)

    def __repr__(self):
        return self.__tablename__



class Fila_Frete_Automatico(Model):
    __tablename__ = 'fila_frete_automatico'
    id = Column(Integer,Sequence('fila_frete_automatico_id_seq'), primary_key=True)
    id_banco_dados = Column(Integer)
    id_nfe = Column(Integer)
    chave_grupo = Column(text)
    data_registro = Column(DateTime)
    data_calculo = Column(DateTime)
    status = Column(Integer)
    pendencia_fiscal = Column(Integer)
    pendencia_rota = Column(Integer)
    frete_zerado = Column(Integer)
    id_conhecimento = Column(Integer)
    thread = Column(Integer)
    id_pesquisa = Column(Integer)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Fila_Importacao_Xml(Model):
    __tablename__ = 'fila_importacao_xml'
    id = Column(Integer,Sequence('fila_importacao_xml_id_seq'), primary_key=True)
    tipo_servico = Column(Integer)
    tipo_doc = Column(Integer)
    id_banco_dados = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    chave_doc = Column(String(44))
    status = Column(Integer)
    data_registro = Column(DateTime)
    data_processamento = Column(DateTime)
    id_usuario = Column(Integer)
    status_importacao = Column(Integer)
    data_processamento_importacao = Column(DateTime)
    id2 = Column(Integer)
    qt_tentativas = Column(Integer)
    mensagem_api = Column(text)

    def __repr__(self):
        return self.__tablename__



class Fila_Protoloco_Comprovei(Model):
    __tablename__ = 'fila_protoloco_comprovei'
    id = Column(Integer,Sequence('fila_protoloco_comprovei_id_seq'), primary_key=True)
    protocolo = Column(text)
    data_registro = Column(DateTime)
    status = Column(Integer)
    data_consulta = Column(DateTime)
    mensagem = Column(text)
    url = Column(text)

    def __repr__(self):
        return self.__tablename__



class Filial(Model):
    __tablename__ = 'filial'
    id_filial = Column(Integer,Sequence('filial_id_filial_seq'), primary_key=True)
    codigo_filial = Column(String(3))
    cnpj = Column(String(14))
    razao_social = Column(String(50))
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
    id_regiao = Column(Numeric(3,0))
    id_cidade = Column(Numeric(5,0))
    codigo_empresa = Column(String(3))
    inscricao_estadual = Column(String(15))
    pessoa_contato = Column(String(40))
    id_contador = Column(Integer)
    suframa = Column(String(9))
    inscricao_municipal = Column(String(18))
    credito_presumido = Column(Integer)
    perfil_empresa = Column(Integer)
    regime_tributario = Column(Integer)
    aliquota_simples = Column(Numeric(6,2))
    aliquota_simpes = Column(Numeric(6,2))
    tipo_unidade = Column(Integer)
    aliquota_iss = Column(Numeric(7,2))
    aliquota_icms_simples = Column(Numeric(5,2))
    flg_item_1400_sped_fiscal = Column(Integer)
    cod_item_1400_sped_fiscal = Column(Integer)
    sigla = Column(String(4))
    serie_emissao_cte = Column(String(3))
    emitir_por_outro_cnpj = Column(Integer)
    cnpj_emitente = Column(String(14))
    fuso_horario = Column(Integer)
    aliquota_irpj = Column(Numeric(7,2))
    aliquota_ipi = Column(Numeric(7,2))
    aliquota_csll = Column(Numeric(7,2))
    aliquota_cofins = Column(Numeric(7,2))
    aliquota_pis = Column(Numeric(7,2))
    aliquota_cpp = Column(Numeric(7,2))
    modulo_cte = Column(Integer)
    modulo_nfe = Column(Integer)
    modulo_nfse = Column(Integer)
    cnae_emitente = Column(String(7))
    crt_emitente = Column(String(1))
    iss_cregtrib = Column(String(1))
    perc_credito_presumido_icms = Column(Numeric(5,2))
    categoria_uso_softlog = Column(Integer)
    recolhe_difal = Column(Integer)
    aliq_inter_cif = Column(Integer)
    ativa = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Filial_Cidades(Model):
    __tablename__ = 'filial_cidades'
    id_filial_cidades = Column(Integer,Sequence('filial_cidades_id_filial_cidades_seq'), primary_key=True)
    id_filial = Column(Integer)
    id_cidade = Column(Integer)
    distancia_filial_origem = Column(Integer)
    prazo_entrega_dias = Column(Integer)
    prazo_entrega_horas = Column(Integer)
    tarifa_1 = Column(Integer)
    tarifa_2 = Column(Integer)
    tarifa_3 = Column(Integer)
    tarifa_4 = Column(Integer)
    tarifa_5 = Column(Integer)
    cobrar_pedagio = Column(Integer)
    ressalva = Column(Numeric(8,2))
    frete_minimo = Column(Numeric(8,2))

    def __repr__(self):
        return self.__tablename__



class Filial_Inscricoes_Est(Model):
    __tablename__ = 'filial_inscricoes_est'
    id_inscricao_est = Column(Integer,Sequence('filial_inscricoes_est_id_inscricao_est_seq'), primary_key=True)
    id_filial = Column(Integer)
    uf = Column(String(2))
    inscricao_estadual = Column(String(15))

    def __repr__(self):
        return self.__tablename__



class Filial_Rotas(Model):
    __tablename__ = 'filial_rotas'
    id_filial_rotas = Column(Integer,Sequence('filial_rotas_id_filial_rotas_seq'), primary_key=True)
    sigla_unidade_origem = Column(String(4))
    sigla_unidade_destino = Column(String(4))
    distancia = Column(Integer)
    dias_transferencia = Column(Integer)
    horas_previsao_chegada = Column(Integer)
    qtd_pedagios = Column(Integer)
    custo_transferencia = Column(Numeric(10,2))
    hora_limite_saida = Column(String(4))
    hora_limite_chegada = Column(String(4))

    def __repr__(self):
        return self.__tablename__



class Flag_Trigger_Tabela(Model):
    __tablename__ = 'flag_trigger_tabela'
    id_flag_trigger_tabela = Column(Integer,Sequence('flag_trigger_tabela_id_flag_trigger_tabela_seq'), primary_key=True)
    tabela = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class For_Emp_Planocontas(Model):
    __tablename__ = 'for_emp_planocontas'
    id_for_emp_planocontas = Column(Integer,Sequence('for_emp_planocontas_id_for_emp_planocontas_seq'), primary_key=True)
    id_fornecedor = Column(Integer)
    codigo_empresa = Column(String(3))
    plano_contas = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Fornecedor_Cargos(Model):
    __tablename__ = 'fornecedor_cargos'
    id_cargos = Column(Integer)
    Descricao_cargos = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Fornecedor_Departamento(Model):
    __tablename__ = 'fornecedor_departamento'
    id_departamento = Column(Numeric)
    descricao_departamento = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Fornecedor_Parametros(Model):
    __tablename__ = 'fornecedor_parametros'
    id = Column(Integer,Sequence('fornecedor_parametros_id_seq'), primary_key=True)
    id_fornecedor = Column(Integer)
    id_tipo_parametro = Column(Integer)
    valor_parametro = Column(text)
    tipo_dado_parametro = Column(String(1))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Fornecedor_Tipo_Parametros(Model):
    __tablename__ = 'fornecedor_tipo_parametros'
    id = Column(Integer,Sequence('fornecedor_tipo_parametros_id_seq'), primary_key=True)
    nome_parametro = Column(String(30))
    descricao_parametro = Column(text)

    def __repr__(self):
        return self.__tablename__



class Fornecedores(Model):
    __tablename__ = 'fornecedores'
    id_empresa = Column(String(2))
    id_filial = Column(String(3))
    cnpj_cpf = Column(String(18))
    ramo = Column(String(40))
    nome_razao = Column(String(50))
    fantasia = Column(String(40))
    endereco = Column(String(50))
    bairro = Column(String(30))
    estado = Column(String(2))
    cep = Column(String(8))
    telefone1 = Column(String(8))
    telefone2 = Column(String(8))
    fax = Column(String(8))
    contato = Column(String(30))
    ddd = Column(String(2))
    tel_contato = Column(String(8))
    iest = Column(String(15))
    nivel = Column(String(10))
    email = Column(String(50))
    site = Column(String(50))
    numero_b = Column(String(3))
    banco_b = Column(String(40))
    agencia_b = Column(String(10))
    numero_cc = Column(String(12))
    tipo_funcionario = Column(Numeric(1,0))
    tipo_cobrador = Column(Integer)
    tipo_vendedor = Column(Integer)
    tipo_motorista = Column(Integer)
    tipo_proprietario = Column(Integer)
    tipo_transportador = Column(Integer)
    tipo_fornecedor = Column(Integer)
    dt_cadastro = Column(DateTime)
    dt_alteracao = Column(DateTime)
    fone_resid = Column(String(8))
    celular = Column(String(8))
    identidade = Column(String(20))
    orgao_expedidor = Column(String(10))
    dt_expedicao = Column(Date)
    nascimento = Column(Date)
    sexo = Column(String(9))
    naturalidade = Column(String(25))
    mae = Column(String(30))
    estado_civil = Column(String(10))
    conjuge = Column(String(35))
    dependentes = Column(Numeric(2,0))
    mot_prontuario = Column(String(15))
    mot_categoria = Column(String(3))
    mot_dt_1_hab = Column(Date)
    mot_validade = Column(Date)
    mot_registro = Column(String(15))
    mot_orgao = Column(String(20))
    mot_dt_exped = Column(Date)
    mot_restringe = Column(Numeric(1,0))
    mot_motivo = Column(String(40))
    mot_cabelo = Column(String(15))
    mot_olhos = Column(String(15))
    mot_sinais = Column(String(30))
    mot_probsaude = Column(String(30))
    mot_altura = Column(Numeric(4,2))
    mot_peso = Column(Numeric(6,3))
    mot_cor = Column(String(10))
    mot_tiposangue = Column(String(5))
    mot_cargaperigosa = Column(Numeric(1,0))
    mot_obs = Column(String(40))
    func_funcao = Column(String(25))
    cob_comissao = Column(Numeric(5,2))
    ven_comissao = Column(Numeric(5,2))
    observacoes = Column(text)
    id_fornecedor = Column(Integer,Sequence('fornecedores_id_fornecedor_seq'), primary_key=True)
    hr_alteracao = Column(String(8))
    doc_rg = Column(String(12))
    doc_rg_emissor = Column(String(4))
    doc_rg_uf = Column(String(2))
    doc_rg_data_emissao = Column(Date)
    doc_pis = Column(String(14))
    data_recisao = Column(Date)
    motivo_recisao = Column(String(45))
    salario_contratual = Column(Numeric(10,2))
    id_cidade = Column(Numeric(5,0))
    fun_data_admissao = Column(Date)
    nacionalidade = Column(String(30))
    grau_instrucao = Column(String(23))
    raca = Column(String(10))
    doc_titulo_eleitor = Column(String(18))
    numero_ctps = Column(String(20))
    doc_reservista = Column(String(18))
    classificacao_fornecedor = Column(Numeric(1,0))
    numero = Column(String(10))
    mot_barba = Column(Numeric(1,0))
    usuario_cadastro = Column(String(30))
    usuario_alteracao = Column(String(30))
    ano_chegada = Column(Date)
    ddd_residencia = Column(String(2))
    ddd_celular = Column(String(2))
    skype = Column(String(30))
    mot_averbacao = Column(String)
    mot_validade_averbacao = Column(Date)
    mot_seg_data_emissao = Column(Date)
    mot_seg_validade = Column(Date)
    mot_seg_cartao = Column(String(20))
    mot_ref1_nome = Column(String(40))
    mot_ref2_nome = Column(String(40))
    mot_ref3_nome = Column(String(40))
    mot_ref1_fone = Column(String(11))
    mot_ref2_fone = Column(String(11))
    mot_ref3_fone = Column(String(11))
    tipo_agente = Column(Integer)
    tipo_contador = Column(Integer)
    conselho_regional = Column(String(15))
    numero_tabela_motorista = Column(String(13))
    inscricao_municipal = Column(String(15))
    pc_contabil = Column(String(10))
    prazo_pagamento = Column(Integer)
    frequencia_pagamento = Column(String(1))
    codigo_centro_custo = Column(Integer)
    tipo_ciaaerea = Column(Integer)
    ven_comissao_aereo = Column(Numeric(5,2))
    seg_numero_apolice = Column(String(20))
    seg_nome_corretora = Column(String(50))
    seg_data_ini_vigencia = Column(Date)
    seg_data_fim_vigencia = Column(Date)
    seg_valor_colisao = Column(Numeric(12,2))
    seg_valor_incendio = Column(Numeric(12,2))
    seg_valor_roubo = Column(Numeric(12,2))
    seg_valor_raio = Column(Numeric(12,2))
    seg_valor_explosao = Column(Numeric(12,2))
    seg_valor_outros = Column(Numeric(12,2))
    seg_valor_danos_materiais = Column(Numeric(12,2))
    seg_valor_danos_terceiros = Column(Numeric(12,2))
    seg_valor_seguro = Column(Numeric(12,2))
    tipo_seguradora = Column(Integer)
    cnpj_responsavel = Column(String(14))
    tipo_edi = Column(String(15))
    end_complemento = Column(String(100))
    tipo_usuario = Column(Integer)
    tipo_posto = Column(Integer)
    id_cid_naturalidade = Column(Integer)
    tipo_parceiro = Column(Integer)
    id_conta_ab = Column(String(20))
    for_inativo = Column(Integer)
    dt_inativo = Column(DateTime)
    id_usu_inativo = Column(Integer)
    mot_inativo = Column(text)
    tipo_pecas = Column(Integer)
    tipo_servicos = Column(Integer)
    rec_comissao = Column(Numeric(5,2))
    rec_comissao_aereo = Column(Numeric(5,2))

    def __repr__(self):
        return self.__tablename__



class Fornecedores_Contas_Correntes(Model):
    __tablename__ = 'fornecedores_contas_correntes'
    id_cc_fornecedor = Column(Integer,Sequence('fornecedores_contas_correntes_id_cc_fornecedor_seq'), primary_key=True)
    id_fornecedor = Column(Numeric(6,0))
    tipo_conta = Column(String(8))
    numero_banco = Column(String(3))
    numero_conta = Column(String(10))
    dv_conta = Column(String(2))
    numero_agencia = Column(String(10))
    dv_agencia = Column(String(2))
    nome_titular = Column(String(50))
    cpf_titular = Column(String(14))
    id_temp = Column(String(10))
    op_conta = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Fornecedores_Fotos(Model):
    __tablename__ = 'fornecedores_fotos'
    id_foto = Column(Integer,Sequence('fornecedores_fotos_id_foto_seq'), primary_key=True)
    id_fornecedor = Column(Numeric(5,0))
    foto = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab(Model):
    __tablename__ = 'frt_ab'
    id_ab = Column(Integer,Sequence('frt_ab_id_ab_seq'), primary_key=True)
    ab_empresa = Column(String(3))
    ab_filial = Column(String(3))
    ab_id_req = Column(Integer)
    ab_nr = Column(String(13))
    ab_cancelado = Column(Integer)
    ab_placa = Column(String(8))
    ab_id_combust = Column(Integer)
    ab_encheu = Column(Integer)
    ab_data = Column(DateTime)
    ab_usu = Column(Integer)
    ab_tp = Column(Integer)
    ab_km = Column(Numeric(8,0))
    ab_hr = Column(Numeric(9,2))
    ab_id_cliente = Column(Integer)
    ab_id_posto = Column(Integer)
    ab_id_bomba = Column(Integer)
    ab_id_motorista = Column(Integer)
    ab_id_nr_contrato = Column(Integer)
    ab_qtd = Column(Numeric(10,2))
    ab_vlr_unit = Column(Numeric(14,2))
    ab_vlr_acresc = Column(Numeric(14,2))
    ab_vlr_descon = Column(Numeric(14,2))
    ab_vlr_total = Column(Numeric(14,2))
    ab_nf_nr = Column(Integer)
    ab_nf_serie = Column(String(3))
    ab_nf_emissao = Column(Date)
    ab_id_pagto = Column(Integer)
    ab_vencimento = Column(Date)
    ab_dt_pagto = Column(Date)
    ab_obs = Column(text)
    atual_em = Column(DateTime)
    ab_origem = Column(Integer)
    ab_nr_autor = Column(String(13))
    ab_id_romaneio = Column(Integer)
    ab_km_anterior = Column(Numeric(8,0))
    ab_km_rodados = Column(Numeric(8,0))

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Autor(Model):
    __tablename__ = 'frt_ab_autor'
    id_autor = Column(Integer,Sequence('frt_ab_autor_id_autor_seq'), primary_key=True)
    autor_empresa = Column(String(3))
    autor_filial = Column(String(3))
    autor_origem = Column(Integer)
    autor_nr = Column(String(13))
    autor_placa = Column(String(8))
    autor_id_motorista = Column(Integer)
    autor_id_posto = Column(Integer)
    autor_id_bomba = Column(Integer)
    autor_id_combust = Column(Integer)
    autor_data = Column(DateTime)
    autor_validade = Column(Date)
    autor_usu = Column(Integer)
    autor_tp = Column(Integer)
    autor_qtd = Column(Numeric(10,2))
    autor_valor = Column(Numeric(10,2))
    autor_obs = Column(text)
    atual_em = Column(DateTime)
    autor_cod_saida = Column(Integer)
    autor_canc = Column(Integer)
    autor_canc_data = Column(DateTime)
    autor_canc_user = Column(Integer)
    autor_encheu = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Autor_Itens(Model):
    __tablename__ = 'frt_ab_autor_itens'
    id_autor_item = Column(Integer,Sequence('frt_ab_autor_itens_id_autor_item_seq'), primary_key=True)
    id_autor = Column(Integer)
    autor_canc = Column(Integer)
    autor_id_posto = Column(Integer)
    autor_id_bomba = Column(Integer)
    autor_id_combust = Column(Integer)
    autor_tp = Column(Integer)
    autor_qtd = Column(Numeric(10,3))
    autor_valor = Column(Numeric(10,3))
    autor_encheu = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Ecofrt_Servicos(Model):
    __tablename__ = 'frt_ab_ecofrt_servicos'
    id = Column(Integer,Sequence('frt_ab_ecofrt_servicos_id_seq'), primary_key=True)
    servico = Column(String(100))
    id_produto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Ecofrt_Tp_Mat(Model):
    __tablename__ = 'frt_ab_ecofrt_tp_mat'
    id = Column(Integer,Sequence('frt_ab_ecofrt_tp_mat_id_seq'), primary_key=True)
    tipo = Column(String(2))
    tipo_desc = Column(text)
    id_produto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Import(Model):
    __tablename__ = 'frt_ab_import'
    id = Column(Integer,Sequence('frt_ab_import_id_seq'), primary_key=True)
    data_ref = Column(Date)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Itens(Model):
    __tablename__ = 'frt_ab_itens'
    id_ab_item = Column(Integer,Sequence('frt_ab_itens_id_ab_item_seq'), primary_key=True)
    id_ab = Column(Integer)
    ab_cancelado = Column(Integer)
    ab_id_combust = Column(Integer)
    ab_encheu = Column(Integer)
    ab_usu = Column(Integer)
    ab_tp = Column(Integer)
    ab_id_bomba = Column(Integer)
    ab_qtd = Column(Numeric(10,3))
    ab_vlr_unit = Column(Numeric(14,3))
    ab_vlr_total = Column(Numeric(14,3))
    ab_obs = Column(text)
    atual_em = Column(DateTime)
    ab_vlr_acresc = Column(Numeric(14,2))
    ab_vlr_descon = Column(Numeric(14,2))
    ab_id_posto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Ab_Layouts(Model):
    __tablename__ = 'frt_ab_layouts'
    id = Column(Integer,Sequence('frt_ab_layouts_id_seq'), primary_key=True)
    leiaute = Column(String(20))

    def __repr__(self):
        return self.__tablename__



class Frt_Abastecimento_Autotrac(Model):
    __tablename__ = 'frt_abastecimento_autotrac'
    id_abastecimento_autotrac = Column(Integer,Sequence('frt_abastecimento_autotrac_id_abastecimento_autotrac_seq'), primary_key=True)
    id_mensagem = Column(Integer)
    id_romaneio_despesa = Column(Integer)
    placa_veiculo = Column(String(8))
    litros = Column(text)
    vl_unitario = Column(text)
    vl_despesa = Column(text)
    kilometragem = Column(text)
    data_posicao = Column(DateTime)
    data_mensagem = Column(DateTime)
    localidade = Column(String(254))
    lancamento = Column(Integer)
    id_romaneio = Column(Integer)
    vl_despesa_n = Column(Numeric(12,2))
    litros_n = Column(Integer)
    kilometragem_n = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Apuracao(Model):
    __tablename__ = 'frt_apuracao'
    id = Column(Integer,Sequence('frt_apuracao_id_seq'), primary_key=True)
    descricao = Column(text)
    custo_direto = Column(Integer)
    custo_indireto = Column(Integer)
    receita = Column(Integer)
    imposto = Column(Integer)
    id_despesa_viagem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Apuracao_Analitica_1(Model):
    __tablename__ = 'frt_apuracao_analitica_1'
    id = Column(Integer,Sequence('frt_apuracao_analitica_1_id_seq'), primary_key=True)
    data_referencia = Column(Date)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    remetente_id = Column(Integer)
    numero_nota_fiscal = Column(String(9))
    serie_nota_fiscal = Column(String(3))
    tipo_transporte = Column(Integer)
    valor_nota_fiscal = Column(Numeric(12,2))
    peso = Column(Numeric(9,2))
    tipo_apuracao = Column(Integer)
    placa_veiculo = Column(String(7))
    id_conhecimento = Column(Integer)
    id_fornecedor = Column(Integer)
    valor = Column(Numeric(12,2))
    id_despesa_romaneio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Bp(Model):
    __tablename__ = 'frt_bp'
    id_bp = Column(Integer,Sequence('frt_bp_id_bp_seq'), primary_key=True)
    bp_empresa = Column(String(3))
    bp_filial = Column(String(3))
    bp_nome = Column(String(30))
    bp_id_posto = Column(Integer)
    bp_id_combust = Column(Integer)
    bp_usu = Column(Integer)
    bp_tp = Column(Integer)
    bp_encerr = Column(Numeric(12,3))
    bp_obs = Column(text)
    atual_em = Column(DateTime)
    bp_id_tq = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Consumo(Model):
    __tablename__ = 'frt_consumo'
    id_consumo = Column(Integer,Sequence('frt_consumo_id_consumo_seq'), primary_key=True)
    id_combust = Column(Integer)
    flg_aditivo = Column(Integer)
    dh_consumo = Column(DateTime)
    id_forn = Column(Integer)
    id_bp = Column(Integer)
    id_romaneio = Column(Integer)
    cons_placa = Column(String(7))
    cons_modelo = Column(Integer)
    cons_cpt = Column(Integer)
    cd_ccusto = Column(Integer)
    id_ativ = Column(Integer)
    tq_cheio = Column(Integer)
    troca_rem = Column(Integer)
    horimetro = Column(Numeric(9,2))
    odometro = Column(Numeric(7,0))
    nr_nf = Column(String(13))
    sr_nf = Column(String(3))
    vlr_total = Column(Numeric(12,2))
    vlr_lt_comb = Column(Numeric(12,4))
    qtd_lt_comb = Column(Numeric(9,2))
    vlr_lt_lub = Column(Numeric(12,4))
    qtd_lt_lub = Column(Numeric(9,2))
    nr_abastec = Column(String(13))
    pc_mistura = Column(Numeric(6,2))
    dt_vencto = Column(Date)
    nr_titulo = Column(String(13))
    sr_titulo = Column(String(3))
    cd_empresa = Column(String(3))
    cd_filial = Column(String(3))
    flg_origem = Column(Integer)
    origem = Column(String(20))
    flg_partic = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Hist_Frota(Model):
    __tablename__ = 'frt_hist_frota'
    id_hist_frota = Column(Integer,Sequence('frt_hist_frota_id_hist_frota_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    hist_data = Column(DateTime)
    hist_obs = Column(String(20))
    numero_frota = Column(String(6))
    veiculo_proprio = Column(Integer)
    id_tipo_veiculo = Column(Integer)
    id_veiculo = Column(Integer)
    odometro = Column(Integer)
    frotista = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Log(Model):
    __tablename__ = 'frt_log'
    id_frt_log = Column(Integer,Sequence('frt_log_id_frt_log_seq'), primary_key=True)
    frt_tabela = Column(String(50))
    id_registro = Column(Integer)
    data_hora = Column(DateTime)
    atividade = Column(text)
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frt_Mnt_Os(Model):
    __tablename__ = 'frt_mnt_os'
    id_os = Column(Integer,Sequence('frt_mnt_os_id_os_seq'), primary_key=True)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    data_abertura = Column(DateTime)
    data_encerramento = Column(DateTime)
    motorista = Column(String(40))
    placa_veiculo = Column(String(8))
    valor_pecas = Column(Numeric(11,2))
    valor_servicos = Column(Numeric(11,2))
    valor_descontos = Column(Numeric(11,2))
    total_os = Column(Numeric(11,2))
    odometro = Column(Numeric(10,1))
    tanque = Column(String(8))
    garantia_pecas = Column(Numeric(3,0))
    garantia_vencimento_pecas = Column(Date)
    garantia_servicos = Column(Numeric(3,0))
    garantia_vencimento_servicos = Column(Date)
    garantia_norma = Column(String(50))
    garantia_exceto = Column(String(50))
    tp_pagamento = Column(String(15))
    status = Column(String(25))
    cnpj_cpf_cliente = Column(String(18))
    valor_servicos_terceiros = Column(Numeric(11,2))
    valor_acrescimos = Column(Numeric(11,2))
    numero_os = Column(String(13))

    def __repr__(self):
        return self.__tablename__



class Frt_Mnt_Os_Pecas(Model):
    __tablename__ = 'frt_mnt_os_pecas'
    id_os = Column(Integer)
    id_os_pecas = Column(Integer,Sequence('frt_mnt_os_pecas_id_os_pecas_seq'), primary_key=True)
    id_produto = Column(Integer)
    quantidade = Column(Numeric(5,2))
    valor_unitario = Column(Numeric(12,2))
    valor_total = Column(Numeric(12,2))
    garantia_peca = Column(Date)
    valor_custo = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Frt_Mnt_Os_Servicos(Model):
    __tablename__ = 'frt_mnt_os_servicos'
    id_os = Column(Integer)
    id_os_servicos = Column(Integer,Sequence('frt_mnt_os_servicos_id_os_servicos_seq'), primary_key=True)
    descricao = Column(text)
    solicitante = Column(String(30))
    data_solicitacao = Column(Date)
    valor_servico = Column(Numeric(12,2))
    status = Column(String(15))
    garantia_servico = Column(Date)
    id_servico = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Mod_Ativ_Con(Model):
    __tablename__ = 'frt_mod_ativ_con'
    id_mac = Column(Integer,Sequence('frt_mod_ativ_con_id_mac_seq'), primary_key=True)
    mac_mod_veic = Column(Integer)
    mac_ati_veic = Column(Integer)
    mac_combust = Column(Integer)
    mac_km_lt = Column(Numeric(12,2))
    mac_lt_hr = Column(Numeric(7,2))
    mac_aceita = Column(Numeric(7,2))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Mov_Eng_Deseng(Model):
    __tablename__ = 'frt_mov_eng_deseng'
    id_mov = Column(Integer,Sequence('frt_mov_eng_deseng_id_mov_seq'), primary_key=True)
    data_mov = Column(DateTime)
    placa_veiculo_tracao = Column(String(7))
    placa_veiculo_reboque = Column(String(7))
    flag_acao = Column(Integer)
    odometro_veic_tracao = Column(Integer)
    horimetro_veic_tracao = Column(Integer)
    data_hora = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Os(Model):
    __tablename__ = 'frt_os'
    id_os = Column(Integer,Sequence('frt_os_id_os_seq'), primary_key=True)
    os_empresa = Column(String(3))
    os_filial_resp = Column(String(3))
    os_filial_solic = Column(String(3))
    os_filial_pg = Column(String(3))
    os_id_cliente = Column(Integer)
    os_nr = Column(String(13))
    os_placa = Column(String(8))
    os_status = Column(Integer)
    os_abertura = Column(DateTime)
    os_aber_usu = Column(Integer)
    os_aber_tp = Column(Integer)
    os_aprovacao = Column(DateTime)
    os_aprov_por = Column(String(50))
    os_aprov_usu = Column(Integer)
    os_encerramento = Column(DateTime)
    os_encerram_por = Column(String(50))
    os_encerram_usu = Column(Integer)
    os_dt_chegada = Column(DateTime)
    os_km_chegada = Column(Numeric(8,0))
    os_hr_chegada = Column(Numeric(9,2))
    os_id_motorista = Column(Integer)
    os_tanque1 = Column(Integer)
    os_tanque2 = Column(Integer)
    os_tanque3 = Column(Integer)
    os_dt_saida = Column(DateTime)
    os_km_saida = Column(Numeric(8,0))
    os_hr_saida = Column(Numeric(9,2))
    os_tp = Column(Integer)
    os_id_nr_contrato = Column(Integer)
    os_vlr_pecas = Column(Numeric(14,2))
    os_vlr_servs = Column(Numeric(14,2))
    os_vlr_serv_3 = Column(Numeric(14,2))
    os_vlr_acresc = Column(Numeric(14,2))
    os_vlr_descon = Column(Numeric(14,2))
    os_vlr_total = Column(Numeric(14,2))
    os_nr_nf = Column(Integer)
    os_nr_serie = Column(String(3))
    os_nr_nf_emissao = Column(Date)
    os_id_pagto = Column(Integer)
    os_dt_pagto = Column(Date)
    os_gar_serv_dias = Column(Numeric(4,0))
    os_gar_serv_venc = Column(Date)
    os_gar_serv_exceto = Column(String(50))
    os_gar_peca_dias = Column(Numeric(4,0))
    os_gar_peca_venc = Column(Date)
    os_gar_peca_exceto = Column(String(50))
    os_obs = Column(text)
    atual_em = Column(DateTime)
    id_solicitacao = Column(Integer)
    os_tp_oficina = Column(Integer)
    os_revertida = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Os_Itens(Model):
    __tablename__ = 'frt_os_itens'
    id_os_item = Column(Integer,Sequence('frt_os_itens_id_os_item_seq'), primary_key=True)
    id_os = Column(Integer)
    item_numero = Column(Integer)
    item_origem = Column(Integer)
    item_id_origem = Column(Integer)
    item_qtd = Column(Numeric(8,2))
    item_vlr_unit = Column(Numeric(12,2))
    item_vlr_terc = Column(Numeric(12,2))
    item_vlr_desc = Column(Numeric(12,2))
    item_vlr_acre = Column(Numeric(12,2))
    item_nf_nr = Column(String(9))
    item_nf_sr = Column(String(3))
    item_nf_emissao = Column(Date)
    item_gar_dias = Column(Numeric(4,0))
    item_gar_venc = Column(Date)
    item_gar_exceto = Column(String(50))
    item_id_pagamento = Column(Integer)
    item_status = Column(Integer)
    item_obs = Column(String(150))
    atual_em = Column(DateTime)
    flag_aprovado = Column(Integer)
    id_almoxarifado = Column(Integer)
    chave_pro = Column(Integer)
    id_pmveic = Column(Integer)
    item_gar_km = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Parametros_Autotrac(Model):
    __tablename__ = 'frt_parametros_autotrac'
    id_parametro_autotrac = Column(Integer,Sequence('frt_parametros_autotrac_id_parametro_autotrac_seq'), primary_key=True)
    ativado = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    banco_dados = Column(text)
    servidor = Column(text)
    porta = Column(text)
    usuario = Column(text)
    senha = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frt_Pm(Model):
    __tablename__ = 'frt_pm'
    id_pm = Column(Integer,Sequence('frt_pm_id_pm_seq'), primary_key=True)
    pm_nome = Column(String(30))
    pm_tipo = Column(Integer)
    pm_ativo = Column(Integer)
    pm_vlr_pecas = Column(Numeric(12,2))
    pm_vlr_servs = Column(Numeric(12,2))
    pm_vlr_serv3 = Column(Numeric(12,2))
    pm_vlr_total = Column(Numeric(12,2))
    pm_obs = Column(text)
    pm_tp = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Pmit(Model):
    __tablename__ = 'frt_pmit'
    id_pmit = Column(Integer,Sequence('frt_pmit_id_pmit_seq'), primary_key=True)
    id_pm = Column(Integer)
    pmit_nr = Column(Integer)
    pmit_origem = Column(Integer)
    pmit_id_origem = Column(Integer)
    pmit_qtd = Column(Numeric(10,1))
    pmit_vlr = Column(Numeric(10,2))
    pmit_vlr3 = Column(Numeric(10,2))
    pmit_perdias = Column(Integer)
    pmit_perkm = Column(Integer)
    pmit_tp = Column(Integer)
    pmit_ativo = Column(Integer)
    pmit_obs = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Pmtv(Model):
    __tablename__ = 'frt_pmtv'
    id_pmtv = Column(Integer,Sequence('frt_pmtv_id_pmtv_seq'), primary_key=True)
    id_pm = Column(Integer)
    id_tv = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Pmtvit(Model):
    __tablename__ = 'frt_pmtvit'
    id_pmtvit = Column(Integer,Sequence('frt_pmtvit_id_pmtvit_seq'), primary_key=True)
    id_pmtv = Column(Integer)
    id_tv = Column(Integer)
    id_pmit = Column(Integer)
    pmtvit_qtd = Column(Numeric(10,1))
    pmtvit_vlr = Column(Numeric(10,2))
    pmtvit_vlr3 = Column(Numeric(10,2))
    pmtvit_perdias = Column(Integer)
    pmtvit_perkm = Column(Integer)
    pmtvit_ativo = Column(Integer)
    pmtvit_obs = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Pmveic(Model):
    __tablename__ = 'frt_pmveic'
    id_pmveic = Column(Integer,Sequence('frt_pmveic_id_pmveic_seq'), primary_key=True)
    id_pmtv = Column(Integer)
    id_pmtvit = Column(Integer)
    id_pmit = Column(Integer)
    id_veiculo = Column(Integer)
    placa_veiculo = Column(String(8))
    pmveic_qtd = Column(Numeric(10,1))
    pmveic_ult_dia = Column(Date)
    pmveic_perdias = Column(Integer)
    pmveic_proxdia = Column(Date)
    pmveic_ult_km = Column(Integer)
    pmveic_perkm = Column(Integer)
    pmveic_proxkm = Column(Integer)
    pmveic_ativo = Column(Integer)
    pmveic_obs = Column(text)
    atual_em = Column(DateTime)
    id_os_item = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Afericao(Model):
    __tablename__ = 'frt_pneu_afericao'
    id_pneu_afericao = Column(Integer,Sequence('frt_pneu_afericao_id_pneu_afericao_seq'), primary_key=True)
    id_pneu_vida = Column(Integer)
    data_afericao = Column(DateTime)
    sulco = Column(Numeric(5,2))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Chassi(Model):
    __tablename__ = 'frt_pneu_chassi'
    id_chassi = Column(Integer,Sequence('frt_pneu_chassi_id_chassi_seq'), primary_key=True)
    descricao_chassi = Column(String(50))
    tipo_eixo_a = Column(String(2))
    tipo_eixo_b = Column(String(2))
    tipo_eixo_c = Column(String(2))
    tipo_eixo_d = Column(String(2))
    tipo_eixo_e = Column(String(2))
    susp_eixo_a = Column(String(1))
    susp_eixo_b = Column(String(1))
    susp_eixo_c = Column(String(1))
    susp_eixo_d = Column(String(1))
    susp_eixo_e = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Chassi_Posicao(Model):
    __tablename__ = 'frt_pneu_chassi_posicao'
    id_chassi_posicao = Column(Integer,Sequence('frt_pneu_chassi_posicao_id_chassi_posicao_seq'), primary_key=True)
    id_chassi = Column(Integer)
    codigo_posicao = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Desenho(Model):
    __tablename__ = 'frt_pneu_desenho'
    id_pneu_desenho = Column(Integer,Sequence('frt_pneu_desenho_id_pneu_desenho_seq'), primary_key=True)
    descricao = Column(String(100))
    codigo = Column(String(10))
    imagem = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Despesas(Model):
    __tablename__ = 'frt_pneu_despesas'
    id_pneu_despesa = Column(Integer,Sequence('frt_pneu_despesas_id_pneu_despesa_seq'), primary_key=True)
    id_pneu = Column(Integer)
    id_fornecedor = Column(Integer)
    historico = Column(String(50))
    valor = Column(Numeric(12,2))
    data_despesa = Column(Date)
    id_pneu_vida = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Dimensao(Model):
    __tablename__ = 'frt_pneu_dimensao'
    id_pneu_dimensao = Column(Integer,Sequence('frt_pneu_dimensao_id_pneu_dimensao_seq'), primary_key=True)
    largura = Column(Integer)
    perfil = Column(Integer)
    diametro_aro = Column(Numeric(6,2))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Eixo_Suspenso(Model):
    __tablename__ = 'frt_pneu_eixo_suspenso'
    id_pneu_eixo_suspenso = Column(Integer,Sequence('frt_pneu_eixo_suspenso_id_pneu_eixo_suspenso_seq'), primary_key=True)
    id_pneu_viagem = Column(Integer)
    tipo_veiculo = Column(Integer)
    eixo_suspenso = Column(String(1))
    odometro_inicial = Column(Integer)
    odometro_final = Column(Integer)
    horimetro_inicial = Column(Integer)
    horimetro_final = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Manut(Model):
    __tablename__ = 'frt_pneu_manut'
    id_pneu_manut = Column(Integer,Sequence('frt_pneu_manut_id_pneu_manut_seq'), primary_key=True)
    id_oficina = Column(Integer)
    id_pneu_movimentacao = Column(Integer)
    id_pneu_afericao = Column(Integer)
    id_pneu = Column(Integer)
    id_entdesp = Column(Integer)
    valor = Column(Numeric(12,2))
    garantia = Column(String(50))
    contato = Column(String(100))
    data_envio = Column(Date)
    data_recebimento = Column(Date)
    data_previsao_entrega = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Marca(Model):
    __tablename__ = 'frt_pneu_marca'
    id_pneu_marca = Column(Integer,Sequence('frt_pneu_marca_id_pneu_marca_seq'), primary_key=True)
    marca = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Modelos(Model):
    __tablename__ = 'frt_pneu_modelos'
    id_pneu_modelo = Column(Integer,Sequence('frt_pneu_modelos_id_pneu_modelo_seq'), primary_key=True)
    modelo = Column(String(50))
    id_pneu_marca = Column(Integer)
    id_pneu_desenho = Column(Integer)
    id_pneu_dimensao = Column(Integer)
    sulco_original = Column(Numeric(3,1))
    sulco_reforma = Column(Numeric(3,1))
    indice_carga = Column(Integer)
    rodizio_km = Column(Integer)
    nr_lonas = Column(Integer)
    perimetro = Column(Numeric(3,2))
    pressao_max = Column(Integer)
    vida1_km = Column(Integer)
    vida2_km = Column(Integer)
    vida3_km = Column(Integer)
    vida4_km = Column(Integer)
    vida5_km = Column(Integer)
    vida6_km = Column(Integer)
    vida1_hr = Column(Integer)
    vida2_hr = Column(Integer)
    vida3_hr = Column(Integer)
    vida4_hr = Column(Integer)
    vida5_hr = Column(Integer)
    vida6_hr = Column(Integer)
    custo_km = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Motivo_Retirada(Model):
    __tablename__ = 'frt_pneu_motivo_retirada'
    id_pneu_motivo_retirada = Column(Integer,Sequence('frt_pneu_motivo_retirada_id_pneu_motivo_retirada_seq'), primary_key=True)
    descricao = Column(String(200))
    tipo_operacao = Column(Integer)
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Movimentacao(Model):
    __tablename__ = 'frt_pneu_movimentacao'
    id_pneu_movimentacao = Column(Integer,Sequence('frt_pneu_movimentacao_id_pneu_movimentacao_seq'), primary_key=True)
    id_pneu = Column(Integer)
    atividade_executada = Column(String(100))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    id_pneu_vida = Column(Integer)
    id_pneu_motivo_retirada = Column(Integer)
    placa_veiculo = Column(String(7))
    placa_odometro = Column(String(7))
    codigo_posicao = Column(String(3))
    id_almoxarifado = Column(Integer)
    id_pneu_afericao = Column(Integer)
    data_mov = Column(DateTime)
    status = Column(Integer)
    tipo = Column(Integer)
    pneu_hodometro = Column(Numeric(15,3))
    pneu_horas = Column(Numeric(15,3))
    id_usuario = Column(Integer)
    data_hora = Column(DateTime)
    veic_hodometro = Column(Integer)
    veic_horimetro = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Posicao(Model):
    __tablename__ = 'frt_pneu_posicao'
    codigo_posicao = Column(String(3),Sequence('frt_pneu_posicao_codigo_posicao_seq'), primary_key=True)
    descricao_posicao = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Recapagem(Model):
    __tablename__ = 'frt_pneu_recapagem'
    id_pneu_recapagem = Column(Integer,Sequence('frt_pneu_recapagem_id_pneu_recapagem_seq'), primary_key=True)
    id_recapadora = Column(Integer)
    id_pneu_movimentacao = Column(Integer)
    id_pneu_afericao = Column(Integer)
    id_pneu = Column(Integer)
    id_entdesp = Column(Integer)
    valor = Column(Numeric(12,2))
    garantia = Column(String(50))
    contato = Column(String(100))
    data_envio = Column(Date)
    data_recebimento = Column(Date)
    data_previsao_entrega = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Viagem(Model):
    __tablename__ = 'frt_pneu_viagem'
    id_pneu_viagem = Column(Integer,Sequence('frt_pneu_viagem_id_pneu_viagem_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    placa_veiculo_tracao = Column(String(7))
    placa_veiculo_reboque_1 = Column(String(7))
    placa_veiculo_reboque_2 = Column(String(7))
    data_viagem = Column(DateTime)
    km_eixo_suspenso = Column(Integer)
    odometro_inicial = Column(Integer)
    odometro_final = Column(Integer)
    horimetro_inicial = Column(Integer)
    horimetro_final = Column(Integer)
    observacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Viagem_Rodagem(Model):
    __tablename__ = 'frt_pneu_viagem_rodagem'
    id_pneu_viagem_rodagem = Column(Integer,Sequence('frt_pneu_viagem_rodagem_id_pneu_viagem_rodagem_seq'), primary_key=True)
    id_pneu_viagem = Column(Integer)
    codigo_posicao = Column(String(3))
    id_pneu_movimentacao = Column(Integer)
    placa_veiculo = Column(String(7))
    km_rodado = Column(Integer)
    hr_rodado = Column(Integer)
    eixo_suspenso = Column(Integer)
    calculado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneu_Vida(Model):
    __tablename__ = 'frt_pneu_vida'
    id_pneu_vida = Column(Integer,Sequence('frt_pneu_vida_id_pneu_vida_seq'), primary_key=True)
    id_pneu = Column(Integer)
    id_pneu_desenho = Column(Integer)
    id_pneu_recapagem = Column(Integer)
    vida = Column(Integer)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    km_hod_final = Column(Integer)
    hr_final = Column(Integer)
    vida_util_prevista_km = Column(Integer)
    vida_util_prevista_hr = Column(Integer)
    km_total = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Pneus(Model):
    __tablename__ = 'frt_pneus'
    id_pneu = Column(Integer,Sequence('frt_pneus_id_pneu_seq'), primary_key=True)
    id_pneu_modelo = Column(Integer)
    id_fornecedor = Column(Integer)
    codigo_referencia = Column(String(5))
    numero_fogo = Column(String(30))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    nro_serie = Column(String(30))
    placa_veiculo = Column(String(7))
    data_entrada = Column(Date)
    valor_compra = Column(Numeric(12,2))
    data_validade = Column(Date)
    data_garantia = Column(Date)
    km_garantia = Column(Integer)
    obs_garantia = Column(text)
    tipo_pneu = Column(Integer)
    situacao = Column(Integer)
    nr_vida = Column(Integer)
    vl_custo = Column(Numeric(12,2))
    localizacao = Column(Integer)
    destino = Column(Integer)
    dot = Column(String(20))
    qt_libras = Column(Numeric(12,3))
    hodometro = Column(Integer)
    hodometro_atual = Column(Integer)
    horimetro = Column(Integer)
    horimetro_atual = Column(Integer)
    rodizio_km = Column(Integer)
    reskm = Column(Integer)
    resdias = Column(Integer)
    revaltot = Column(Numeric(12,3))
    resvalmed = Column(Numeric(12,3))
    rescustokm = Column(Numeric(12,3))
    observacao = Column(text)
    km_total_vidas = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Req(Model):
    __tablename__ = 'frt_req'
    id_req = Column(Integer,Sequence('frt_req_id_req_seq'), primary_key=True)
    req_empresa = Column(String(3))
    req_filial = Column(String(3))
    req_nr = Column(String(13))
    req_placa = Column(String(8))
    req_id_combust = Column(Integer)
    req_data = Column(DateTime)
    req_usu = Column(Integer)
    req_tp = Column(Integer)
    req_id_cliente = Column(Integer)
    req_id_posto = Column(Integer)
    req_id_bomba = Column(Integer)
    req_id_motorista = Column(Integer)
    req_id_nr_contrato = Column(Integer)
    req_qtd_autoriz = Column(Numeric(10,2))
    req_obs = Column(text)
    atual_em = Column(DateTime)
    req_qtd_real = Column(Numeric(10,2))
    req_status = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Frt_Req_Itens(Model):
    __tablename__ = 'frt_req_itens'
    id_item = Column(Integer,Sequence('frt_req_itens_id_item_seq'), primary_key=True)
    id_req = Column(Integer)
    req_id_posto = Column(Integer)
    req_id_bomba = Column(Integer)
    req_id_combust = Column(Integer)
    req_qtd = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Frt_Tmp_Sem_Parar(Model):
    __tablename__ = 'frt_tmp_sem_parar'
    id_tmp_sem_parar = Column(Integer,Sequence('frt_tmp_sem_parar_id_tmp_sem_parar_seq'), primary_key=True)
    id_romaneio_despesa = Column(Integer)
    placa_veiculo = Column(String(8))
    data_hora = Column(DateTime)
    concessionaria = Column(String(50))
    praca = Column(String(50))
    cat = Column(Integer)
    valor = Column(Numeric(12,2))
    id_romaneio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Tq(Model):
    __tablename__ = 'frt_tq'
    id_tq = Column(Integer,Sequence('frt_tq_id_tq_seq'), primary_key=True)
    tq_empresa = Column(String(3))
    tq_filial = Column(String(3))
    tq_id_posto = Column(Integer)
    tq_id_combust = Column(Integer)
    tq_capacidade = Column(Numeric(12,3))
    tq_qtd_atu = Column(Numeric(12,3))
    tq_qtd_min = Column(Numeric(12,3))
    tq_qtd_max = Column(Numeric(12,3))
    tq_vlr_med = Column(Numeric(12,3))
    tq_tp = Column(Integer)
    tq_usu = Column(Integer)
    tq_obs = Column(text)
    atual_em = Column(DateTime)
    tq_nome = Column(String(30))
    id_almoxarifado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frt_Veic_Ativ(Model):
    __tablename__ = 'frt_veic_ativ'
    id_ativ = Column(Integer,Sequence('frt_veic_ativ_id_ativ_seq'), primary_key=True)
    ativ_cd = Column(String(3))
    ativ_dc = Column(String(50))
    ativ_tp = Column(Integer)
    ativ_obs = Column(String(50))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Veic_Km(Model):
    __tablename__ = 'frt_veic_km'
    id_veic_km = Column(Integer,Sequence('frt_veic_km_id_veic_km_seq'), primary_key=True)
    id_veiculo = Column(Integer)
    placa_veiculo = Column(String(7))
    tb_origem = Column(String(100))
    id_origem = Column(Integer)
    veic_km = Column(Numeric(10,1))
    veic_hr = Column(Numeric(10,1))
    veic_flag = Column(Integer)
    veic_dthr = Column(DateTime)
    veic_tipo = Column(Integer)
    veic_obs = Column(String(150))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Frt_Viagem_Nao_Rodado(Model):
    __tablename__ = 'frt_viagem_nao_rodado'
    id_viagem_nao_rodado = Column(Integer,Sequence('frt_viagem_nao_rodado_id_viagem_nao_rodado_seq'), primary_key=True)
    id_viagem_rodagem = Column(Integer)
    id_atividade = Column(Integer)
    placa_veiculo = Column(String(7))
    km_inicial = Column(Integer)
    km_final = Column(Integer)
    hr_inicial = Column(Integer)
    hr_final = Column(Integer)
    eixo_suspenso = Column(String(1))
    obs = Column(String(250))

    def __repr__(self):
        return self.__tablename__



class Frt_Viagem_Rodagem(Model):
    __tablename__ = 'frt_viagem_rodagem'
    id_viagem_rodagem = Column(Integer,Sequence('frt_viagem_rodagem_id_viagem_rodagem_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    placa_veiculo_tracao = Column(String(7))
    placa_veiculo_reboque_1 = Column(String(7))
    placa_veiculo_reboque_2 = Column(String(7))
    data_viagem = Column(DateTime)
    km_eixo_suspenso = Column(Integer)
    odometro_inicial = Column(Integer)
    odometro_final = Column(Integer)
    horimetro_inicial = Column(Integer)
    horimetro_final = Column(Integer)
    observacao = Column(text)
    data_chegada = Column(DateTime)
    placas_engates = Column(String(60))

    def __repr__(self):
        return self.__tablename__



class Frw_Column(Model):
    __tablename__ = 'frw_column'
    id = Column(Integer,Sequence('frw_column_id_seq'), primary_key=True)
    table_id = Column(Integer)
    column_name = Column(text)
    column_type = Column(text)
    column_default = Column(text)
    column_alias_default = Column(text)
    column_group_default = Column(text)
    column_sequence_pk = Column(text)
    column_ref_fk = Column(text)
    column_comment = Column(text)

    def __repr__(self):
        return self.__tablename__



class Frw_Relationship(Model):
    __tablename__ = 'frw_relationship'
    id = Column(Integer,Sequence('frw_relationship_id_seq'), primary_key=True)
    is_constraint = Column(Integer)
    relationship_name = Column(text)
    column_id = Column(Integer)
    column_id_foreign = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Frw_Table(Model):
    __tablename__ = 'frw_table'
    id = Column(Integer,Sequence('frw_table_id_seq'), primary_key=True)
    table_name = Column(text)
    table_alias = Column(text)
    table_column_pk = Column(text)

    def __repr__(self):
        return self.__tablename__



class Licenca(Model):
    __tablename__ = 'licenca'
    descricao_licenca = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Licenciamento(Model):
    __tablename__ = 'licenciamento'
    placa_veic = Column(String(8))
    ano_licenca = Column(String(4))
    dpvat = Column(Numeric(10,2))
    ipva = Column(Numeric(10,2))
    taxa_licenciamento = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Lista_Notas_Fiscais(Model):
    __tablename__ = 'lista_notas_fiscais'
    id_conhecimento_notas_fiscais = Column(Integer)
    numero_nota_fiscal = Column(String(6))

    def __repr__(self):
        return self.__tablename__



class Lista_Notas_Fiscais_2(Model):
    __tablename__ = 'lista_notas_fiscais_2'
    id_conhecimento_notas_fiscais = Column(Integer)
    numero_nota_fiscal = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Log_Atividades(Model):
    __tablename__ = 'log_atividades'
    id_log = Column(Integer,Sequence('log_atividades_id_log_seq'), primary_key=True)
    id_tabela = Column(Integer)
    nome_tabela = Column(String(63))
    data_hora = Column(DateTime)
    atividade_executada = Column(String(200))
    id_usuario = Column(Integer)
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Log_Retorno_Banco(Model):
    __tablename__ = 'log_retorno_banco'
    id_log_retorno_banco = Column(Integer,Sequence('log_retorno_banco_id_log_retorno_banco_seq'), primary_key=True)
    arquivo = Column(String(30))
    id_arquivo = Column(Integer)
    id_carteira = Column(Integer)
    historico = Column(String(100))
    data_hora = Column(DateTime)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    usuario = Column(String(30))
    id_conta_corrente = Column(Integer)
    arquivo_retorno = Column(text)

    def __repr__(self):
        return self.__tablename__



class Mod_Vendas(Model):
    __tablename__ = 'mod_vendas'
    id = Column(Integer,Sequence('mod_vendas_id_seq'), primary_key=True)
    produto = Column(Integer)
    preco = Column(Numeric(12,2))
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return self.__tablename__



class Modulo_Atualizacoes(Model):
    __tablename__ = 'modulo_atualizacoes'
    id_atualizacao_modulo = Column(Integer,Sequence('modulo_atualizacoes_id_atualizacao_modulo_seq'), primary_key=True)
    codigo_modulo = Column(String(10))
    versao = Column(String(10))
    numero_partes = Column(Numeric(2,0))
    url = Column(text)

    def __repr__(self):
        return self.__tablename__



class Modulo_Atualizacoes_Partes(Model):
    __tablename__ = 'modulo_atualizacoes_partes'
    id_modulo_atualizacoes_partes = Column(Integer,Sequence('modulo_atualizacoes_partes_id_modulo_atualizacoes_partes_seq'), primary_key=True)
    codigo_modulo = Column(String(10))
    versao = Column(String(10))
    numero_parte = Column(Numeric(2,0))
    conteudo_parte = Column(text)

    def __repr__(self):
        return self.__tablename__



class Modulo_Versao(Model):
    __tablename__ = 'modulo_versao'
    codigo_modulo = Column(String(10),Sequence('modulo_versao_codigo_modulo_seq'), primary_key=True)
    versao = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Modulos_Sistema(Model):
    __tablename__ = 'modulos_sistema'
    codigo_modulo = Column(String(10),Sequence('modulos_sistema_codigo_modulo_seq'), primary_key=True)
    nome_modulo = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Modulos_Sistema_Permissoes(Model):
    __tablename__ = 'modulos_sistema_permissoes'
    id_permissao = Column(Integer,Sequence('modulos_sistema_permissoes_id_permissao_seq'), primary_key=True)
    codigo_modulo = Column(String(10))
    codigo_permissao = Column(String(10))
    permissao = Column(Numeric(1,0))
    nome_processo = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Motorista(Model):
    __tablename__ = 'motorista'
    placa_veic = Column(String(8))
    id_fornecedor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Doc_Redespacho(Model):
    __tablename__ = 'msg_doc_redespacho'
    id_doc_redespacho = Column(Integer,Sequence('msg_doc_redespacho_id_doc_redespacho_seq'), primary_key=True)
    redespachador_id = Column(Integer)
    data_lote = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Msg_Doc_Vendedores(Model):
    __tablename__ = 'msg_doc_vendedores'
    id_doc_vendedores = Column(Integer,Sequence('msg_doc_vendedores_id_doc_vendedores_seq'), primary_key=True)
    remetente_id = Column(Integer)
    codigo_vendedor = Column(String(10))
    data_lote = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Msg_Edi_Lista_Chaves(Model):
    __tablename__ = 'msg_edi_lista_chaves'
    id = Column(Integer,Sequence('msg_edi_lista_chaves_id_seq'), primary_key=True)
    empresa = Column(String(3))
    filial = Column(String(3))
    id_embarcador = Column(Integer)
    id_doc = Column(Integer)
    lista_chaves = Column(text)
    serie_fatura = Column(text)
    serie_conhecimento = Column(text)
    serie_nf = Column(text)
    observacao = Column(text)
    data_ref = Column(Date)
    id_notificacao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Fila_Averb_Atm(Model):
    __tablename__ = 'msg_fila_averb_atm'
    id = Column(Integer,Sequence('msg_fila_averb_atm_id_seq'), primary_key=True)
    id_doc = Column(Integer)
    id_banco_dados = Column(Integer)
    status = Column(Integer)
    cancelado = Column(Integer)
    data_fila = Column(DateTime)
    data_processamento = Column(DateTime)
    id_averbacao = Column(Integer)
    is_manifesto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Fila_Edi(Model):
    __tablename__ = 'msg_fila_edi'
    id_fila_edi = Column(Integer,Sequence('msg_fila_edi_id_fila_edi_seq'), primary_key=True)
    id_notificacao = Column(Integer)
    id_chave_notificacao = Column(text)
    id_banco_dados = Column(Integer)
    codigo_envio = Column(Integer)
    status = Column(Integer)
    data_envio = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Msg_Fila_Envio(Model):
    __tablename__ = 'msg_fila_envio'
    id_fila_envio = Column(Integer,Sequence('msg_fila_envio_id_fila_envio_seq'), primary_key=True)
    id_notificacao = Column(Integer)
    id_chave_notificacao = Column(Integer)
    id_banco_dados = Column(Integer)
    codigo_envio = Column(Integer)
    status = Column(Integer)
    data_envio = Column(DateTime)
    data_registro = Column(DateTime)
    id_parceiro = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Fila_Totvs(Model):
    __tablename__ = 'msg_fila_totvs'
    id = Column(Integer,Sequence('msg_fila_totvs_id_seq'), primary_key=True)
    tipo_documento = Column(Integer)
    id_documento = Column(Integer)
    data_registro = Column(DateTime)
    status = Column(Integer)
    id_totvs = Column(String(3))
    numero_tentativa = Column(Integer)
    data_ultima_tentativa = Column(DateTime)
    ultima_mensagem = Column(text)
    qt_pendencias = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Msg_Fila_Totvs_Erros(Model):
    __tablename__ = 'msg_fila_totvs_erros'
    id = Column(Integer,Sequence('msg_fila_totvs_erros_id_seq'), primary_key=True)
    id_fila_totvs = Column(Integer)
    mensagem = Column(text)
    id_tentativa = Column(Integer)
    data_tentativa = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Msg_Filas(Model):
    __tablename__ = 'msg_filas'
    id = Column(Integer,Sequence('msg_filas_id_seq'), primary_key=True)
    nome_fila = Column(text)
    ultimo_sinal = Column(DateTime)
    nome_script = Column(text)
    servidor = Column(text)

    def __repr__(self):
        return self.__tablename__



class Msg_Notificacao(Model):
    __tablename__ = 'msg_notificacao'
    id_notificacao = Column(Integer,Sequence('msg_notificacao_id_notificacao_seq'), primary_key=True)
    ativo = Column(Integer)
    notificacao = Column(String(150))
    especie_notificacao = Column(Integer)
    remetente_email = Column(text)
    notifica_cliente = Column(Integer)
    notifica_usuario = Column(Integer)
    notifica_fornecedor = Column(Integer)
    origem_notificacao = Column(text)
    chave_notificacao = Column(text)
    valor_chave_notificacao = Column(Integer)
    periodicidade_dias = Column(Integer)
    telefone_contato = Column(String(12))
    ddd_contato = Column(String(6))
    id_notificacao_principal = Column(Integer)
    agrupa_raiz_cnpj = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Subscricao(Model):
    __tablename__ = 'msg_subscricao'
    id_subscricao = Column(Integer,Sequence('msg_subscricao_id_subscricao_seq'), primary_key=True)
    ativo = Column(Integer)
    id_notificacao = Column(Integer)
    codigo_cliente = Column(Integer)
    id_fornecedor = Column(Integer)
    id_usuario = Column(Integer)
    email = Column(text)
    fone = Column(text)
    ultimo_envio = Column(DateTime)
    host = Column(String(100))
    usuario = Column(String(250))
    senha = Column(String(100))
    porta = Column(Integer)
    codigo_acesso = Column(String(100))
    tipo_host = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Msg_Subscricao_Aux(Model):
    __tablename__ = 'msg_subscricao_aux'
    id_subscricao_aux = Column(Integer,Sequence('msg_subscricao_aux_id_subscricao_aux_seq'), primary_key=True)
    id_notificacao = Column(Integer)
    codigo_cliente = Column(Integer)
    codigo = Column(String(10))
    descricao = Column(String(50))
    email = Column(String(250))
    telefone = Column(String(20))
    ativo = Column(Integer)
    ultimo_envio = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Ocorrencia(Model):
    __tablename__ = 'ocorrencia'
    id_ocorrencia_entrega = Column(Numeric(2,0))
    descricao_ocorrencia = Column(String(45))
    gera_pendencia = Column(Numeric(1,0))

    def __repr__(self):
        return self.__tablename__



class Paises(Model):
    __tablename__ = 'paises'
    id_pais = Column(Integer,Sequence('paises_id_pais_seq'), primary_key=True)
    nome_pais = Column(String(50))
    codigo_ddi = Column(String(4))
    sigla = Column(String(4))
    codigo_pais = Column(String(5))

    def __repr__(self):
        return self.__tablename__



class Parametros(Model):
    __tablename__ = 'parametros'
    id_parametro = Column(Integer,Sequence('parametros_id_parametro_seq'), primary_key=True)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    codigo_modulo = Column(String(20))
    cod_parametro = Column(String(40))
    valor_parametro = Column(text)
    tipo_parametro = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Pg_Ts_Cfg(Model):
    __tablename__ = 'pg_ts_cfg'
    ts_name = Column(text,Sequence('pg_ts_cfg_ts_name_seq'), primary_key=True)
    prs_name = Column(text)
    locale = Column(text)

    def __repr__(self):
        return self.__tablename__



class Pg_Ts_Cfgmap(Model):
    __tablename__ = 'pg_ts_cfgmap'
    ts_name = Column(text,Sequence('pg_ts_cfgmap_ts_name_seq'), primary_key=True)
    tok_alias = Column(text)

    def __repr__(self):
        return self.__tablename__



class Pg_Ts_Dict(Model):
    __tablename__ = 'pg_ts_dict'
    dictinitoption = Column(text)

    def __repr__(self):
        return self.__tablename__



class Produtos(Model):
    __tablename__ = 'produtos'
    id_produto = Column(Integer,Sequence('produtos_id_produto_seq'), primary_key=True)
    descricao_produto = Column(String(50))
    unidade = Column(String(2))
    valor = Column(Numeric(8,2))
    codigo_barras = Column(String(30))
    codigo_produto = Column(Numeric(6,0))
    codigo_referencia = Column(String(20))

    def __repr__(self):
        return self.__tablename__



class Profile(Model):
    __tablename__ = 'profile'
    id_profile = Column(Integer,Sequence('profile_id_profile_seq'), primary_key=True)
    key_objeto = Column(String(30))
    id_usuario = Column(Integer)
    preconfiguracao = Column(text)
    ativado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Ramo(Model):
    __tablename__ = 'ramo'
    id_ramo = Column(Numeric(3,0),Sequence('ramo_id_ramo_seq'), primary_key=True)
    descricao_ramo_atividade = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Recado_Login(Model):
    __tablename__ = 'recado_login'
    id_mensagem = Column(Integer,Sequence('recado_login_id_mensagem_seq'), primary_key=True)
    texto_mensagem = Column(text)
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Regiao(Model):
    __tablename__ = 'regiao'
    id_regiao = Column(Integer,Sequence('regiao_id_regiao_seq'), primary_key=True)
    descricao = Column(String(35))
    id_cidade_polo = Column(Integer)
    rota_rodoviario = Column(Integer)
    rota_aereo = Column(Integer)
    tipo_composicao = Column(Integer)
    tipo_regiao = Column(Integer)
    id_regiao_agrupadora = Column(Integer)
    id_bairro_polo = Column(Integer)
    hora_inicio_viagem = Column(String(5))
    id_embarcador = Column(Integer)
    uso_operacional = Column(Integer)
    tipo_operacao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Regiao_Bairros(Model):
    __tablename__ = 'regiao_bairros'
    id_regiao_bairro = Column(Integer,Sequence('regiao_bairros_id_regiao_bairro_seq'), primary_key=True)
    id_regiao = Column(Integer)
    id_bairro = Column(Integer)
    tempo_dias = Column(Integer)
    tempo_horas = Column(Integer)
    distancia = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Regiao_Cidades(Model):
    __tablename__ = 'regiao_cidades'
    id_regiao_cidades = Column(Integer,Sequence('regiao_cidades_id_regiao_cidades_seq'), primary_key=True)
    id_regiao = Column(Integer)
    id_cidade = Column(Integer)
    distancia_cidade_polo = Column(Integer)
    tempo_dias = Column(Integer)
    tempo_horas = Column(Integer)
    cidade_satelite = Column(Integer)
    interior_redespacho = Column(Integer)
    capital = Column(Integer)
    percurso_fluvial = Column(Integer)
    destinatario_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Regiao_Remetentes(Model):
    __tablename__ = 'regiao_remetentes'
    id = Column(Integer,Sequence('regiao_remetentes_id_seq'), primary_key=True)
    id_regiao = Column(Integer)
    remetente_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Remessa(Model):
    __tablename__ = 'remessa'
    id_remessa = Column(Integer,Sequence('remessa_id_remessa_seq'), primary_key=True)
    numero_remessa = Column(Integer)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    id_carteira = Column(Integer)
    data_hora_geracao = Column(DateTime)
    valor_remessa = Column(Numeric(12,2))
    sacador_avalista = Column(String(50))
    cnpj_cpf_sacador = Column(String(14))
    banco_emite_boleto = Column(Integer)
    nosso_numero_inicial = Column(Integer)
    gerar_novo_numero = Column(Integer)
    protestar = Column(Integer)
    protestar_apos_dias = Column(Integer)
    juros_perc = Column(Numeric(5,2))
    multa_perc = Column(Numeric(5,2))
    observacao = Column(String(250))
    arquivo = Column(String(50))
    usuario_inclusao = Column(String(30))
    usuario_alteracao = Column(String(30))
    qtde_faturas = Column(Integer)
    data_hora_inclusao = Column(DateTime)
    data_hora_alteracao = Column(DateTime)
    tipo_acao_cobranca = Column(String(2))

    def __repr__(self):
        return self.__tablename__



class Remessa_Faturas(Model):
    __tablename__ = 'remessa_faturas'
    id_remessa_fatura = Column(Integer,Sequence('remessa_faturas_id_remessa_fatura_seq'), primary_key=True)
    id_remessa = Column(Integer)
    id_faturamento = Column(Integer)
    tipo_acao_cobranca = Column(String(2))
    desc_acao_cobranca = Column(String(50))
    nosso_numero = Column(String(16))
    gerar_nosso_numero = Column(Integer)
    status_geracao = Column(Integer)
    contador_nosso_numero = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Sca_Abastecimento(Model):
    __tablename__ = 'sca_abastecimento'
    id_abastecimento = Column(Integer,Sequence('sca_abastecimento_id_abastecimento_seq'), primary_key=True)
    id_abastecimento_filial = Column(String(13))
    placa_veiculo = Column(String(8))
    numero_requisicao = Column(String(13))
    id_fornecedor = Column(Numeric(6,0))
    data_hora = Column(DateTime)
    numero_documento = Column(String(10))
    qtd_litros = Column(Numeric(10,3))
    valor_litro = Column(Numeric(10,3))
    valor_total = Column(Numeric(10,3))
    odometro = Column(Numeric(8,1))
    id_motorista = Column(Numeric(6,0))
    id_tanque = Column(String(3))
    id_operador_bomba = Column(Numeric(6,0))
    local_abastecimento = Column(Numeric(1,0))

    def __repr__(self):
        return self.__tablename__



class Sca_Afericao(Model):
    __tablename__ = 'sca_afericao'
    id_afericao = Column(Integer)
    data = Column(Date)
    id_tanque = Column(String(3))
    litros = Column(Numeric(10,3))
    alteracao = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Sca_Ajuste_Odometro(Model):
    __tablename__ = 'sca_ajuste_odometro'
    id_ajuste = Column(Integer)
    data_ajuste = Column(Date)
    id_veiculo = Column(String(8))
    odometro = Column(Numeric(10,1))
    alterado_por = Column(String(15))
    alterado = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Sca_Cancelamento_Form(Model):
    __tablename__ = 'sca_cancelamento_form'
    n_formulario = Column(Integer)
    motivo_cancelamento = Column(String(40))
    digitado_por = Column(String(40))
    alterado = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Sca_Combustivel(Model):
    __tablename__ = 'sca_combustivel'
    id_combustivel = Column(Integer,Sequence('sca_combustivel_id_combustivel_seq'), primary_key=True)
    nome_combustivel = Column(String(30))
    valor_litro = Column(Numeric(7,2))

    def __repr__(self):
        return self.__tablename__



class Sca_Entrada(Model):
    __tablename__ = 'sca_entrada'
    id_entrada = Column(Integer)
    data_entrada = Column(Date)
    id_tanque = Column(String(3))
    nota_fiscal = Column(String(10))
    valor_nf = Column(Numeric(10,2))
    qtde_litros = Column(Numeric(10,3))
    valor_litro = Column(Numeric(10,5))
    alteracao = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Sca_Estoque(Model):
    __tablename__ = 'sca_estoque'
    data_movimento = Column(Date)
    id_tanque = Column(String(3))
    saldo_anterior = Column(Numeric(10,3))
    saldo_atual = Column(Numeric(10,3))
    qtde_entrada = Column(Numeric(10,3))
    qtde_saida = Column(Numeric(10,3))
    alteracao = Column(DateTime)
    operacao = Column(String(10))
    id_movimento = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Sca_Parametros(Model):
    __tablename__ = 'sca_parametros'
    preco_combustivel = Column(Numeric(8,3))

    def __repr__(self):
        return self.__tablename__



class Sca_Requisicao(Model):
    __tablename__ = 'sca_requisicao'
    id_requisicao = Column(Integer,Sequence('sca_requisicao_id_requisicao_seq'), primary_key=True)
    numero_requisicao = Column(String(13))
    data_requisicao = Column(DateTime)
    numero_formulario = Column(Numeric(6,0))
    serie_formulario = Column(String(10))
    id_fornecedor = Column(Numeric(6,0))
    id_combustivel = Column(Numeric(3,0))
    id_motorista = Column(Numeric(6,0))
    codigo_filial = Column(String(3))
    impresso = Column(Numeric(1,0))
    qdt_impressoes = Column(Numeric(2,0))
    baixa = Column(Numeric(1,0))
    cancelado = Column(Numeric(1,0))
    motivo_cancelamento = Column(text)
    local_abastecimento = Column(Numeric(1,0))
    numero_abastecimento = Column(String(13))
    placa_veiculo = Column(String(8))

    def __repr__(self):
        return self.__tablename__



class Sca_Requisicao_Acoes(Model):
    __tablename__ = 'sca_requisicao_acoes'
    id_sca_requisicao_acoes = Column(Integer)
    id_requisicao = Column(Integer)
    acao_executada = Column(String(30))
    usuario = Column(String(30))
    data_hora = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Sca_Tanque(Model):
    __tablename__ = 'sca_tanque'
    id_tanque = Column(String(3))
    descricao = Column(String(20))
    capacidade = Column(Numeric(10,2))
    estoque = Column(Numeric(10,2))
    valor_litro = Column(Numeric(10,5))
    ultima_entrada = Column(Date)
    ultima_saida = Column(Date)
    alteracao = Column(DateTime)
    codigo_filial = Column(String(3))
    id_geral_tanque = Column(Integer,Sequence('sca_tanque_id_geral_tanque_seq'), primary_key=True)

    def __repr__(self):
        return self.__tablename__



class Scf_Agencias_Bancarias(Model):
    __tablename__ = 'scf_agencias_bancarias'
    id_agencia = Column(Integer,Sequence('scf_agencias_bancarias_id_agencia_seq'), primary_key=True)
    id_banco = Column(Numeric(5,0))
    numero_agencia = Column(String(8))
    nome_agencia = Column(String(50))
    endereco_agencia = Column(String(50))
    bairro_agencia = Column(String(30))
    id_cidade = Column(Numeric(5,0))
    estado_agencia = Column(String(2))
    cep_agencia = Column(String(8))
    ddd_agencia = Column(String(2))
    telefone_agencia = Column(String(8))
    usuario_inclusao = Column(Numeric(5,0))
    data_inclusao = Column(DateTime)
    ultima_alteracao = Column(DateTime)
    usuario_ultima_alteracao = Column(Numeric(5,0))
    pessoa_contato = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Scf_Caixas(Model):
    __tablename__ = 'scf_caixas'
    id_caixa = Column(Integer,Sequence('scf_caixas_id_caixa_seq'), primary_key=True)
    nome_caixa = Column(String(50))
    data_abertura = Column(Date)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    cod_operador = Column(Numeric(4,0))
    classificacao = Column(Numeric(1,0))
    saldo_atual = Column(Numeric(12,2))
    status_diario = Column(Numeric(1,0))
    ultima_abertura = Column(DateTime)
    ultimo_encerramento = Column(DateTime)
    situacao_geral = Column(Numeric(1,0))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_modificacao = Column(Numeric(5,0))
    data_modificacao = Column(DateTime)
    tabela_conta = Column(String(20))
    senha = Column(String(15))

    def __repr__(self):
        return self.__tablename__



class Scf_Caixas_Historico(Model):
    __tablename__ = 'scf_caixas_historico'
    id_historico_caixa = Column(Integer,Sequence('scf_caixas_historico_id_historico_caixa_seq'), primary_key=True)
    id_caixa = Column(Integer)
    tipo_movimento = Column(String(10))
    usuario = Column(String(20))
    data_hora = Column(DateTime)
    saldo_inicial = Column(Numeric(10,2))
    debitos = Column(Numeric(10,2))
    creditos = Column(Numeric(10,2))
    saldo_final = Column(Numeric(10,2))
    id_temp = Column(String(16))
    numero_lancamento_externo = Column(Integer)
    arq_lancamento_externo = Column(String(25))
    data_movimento = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Scf_Centro_Custos(Model):
    __tablename__ = 'scf_centro_custos'
    id_centro_custo = Column(Integer,Sequence('scf_centro_custos_id_centro_custo_seq'), primary_key=True)
    id_pai_centro_custo = Column(Numeric(6,0))
    nome_centro_custo = Column(String(50))
    imagem = Column(String(30))
    pc_conta_debito = Column(String(15))
    pc_conta_credito = Column(String(15))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    imagem_arquivo = Column(text)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    codigo_centro_custo = Column(Numeric(6,0))
    tree_centro_custo = Column(String(50))
    nivel = Column(Integer)
    atualizar = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Cheques_Cancelados(Model):
    __tablename__ = 'scf_cheques_cancelados'
    id_cheque_cancelado = Column(Integer,Sequence('scf_cheques_cancelados_id_cheque_cancelado_seq'), primary_key=True)
    numero_conta_corrente = Column(String(15))
    numero_cheque = Column(String(10))
    id_usuario = Column(Numeric(4,0))
    motivo_cancelamento = Column(String(50))
    data_cancelamento = Column(DateTime)
    tabela_conta = Column(String(25))

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Caixa_001(Model):
    __tablename__ = 'scf_conta_caixa_001'
    numero_lancamento = Column(Integer,Sequence('scf_conta_caixa_001_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    origem_transacao = Column(String(1))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Caixa_002(Model):
    __tablename__ = 'scf_conta_caixa_002'
    numero_lancamento = Column(Integer,Sequence('scf_conta_caixa_002_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    origem_transacao = Column(String(1))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Caixa_003(Model):
    __tablename__ = 'scf_conta_caixa_003'
    numero_lancamento = Column(Integer,Sequence('scf_conta_caixa_003_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    origem_transacao = Column(String(1))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Corrente_001(Model):
    __tablename__ = 'scf_conta_corrente_001'
    numero_lancamento = Column(Integer,Sequence('scf_conta_corrente_001_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    data_compensacao = Column(Date)
    origem_transacao = Column(String(1))
    tipo_lancamento = Column(String(20))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    id_usuario_conciliacao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Corrente_002(Model):
    __tablename__ = 'scf_conta_corrente_002'
    numero_lancamento = Column(Integer,Sequence('scf_conta_corrente_002_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    data_compensacao = Column(Date)
    origem_transacao = Column(String(1))
    tipo_lancamento = Column(String(20))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    id_usuario_conciliacao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Corrente_003(Model):
    __tablename__ = 'scf_conta_corrente_003'
    numero_lancamento = Column(Integer,Sequence('scf_conta_corrente_003_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    data_compensacao = Column(Date)
    origem_transacao = Column(String(1))
    tipo_lancamento = Column(String(20))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    id_usuario_conciliacao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))
    id_temp = Column(String(16))
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Conta_Tabela_Modelo(Model):
    __tablename__ = 'scf_conta_tabela_modelo'
    numero_lancamento = Column(Integer,Sequence('scf_conta_tabela_modelo_numero_lancamento_seq'), primary_key=True)
    data_lancamento = Column(DateTime)
    data_movimento = Column(Date)
    historico = Column(String(50))
    tipo_movimento = Column(String(1))
    valor = Column(Numeric(12,2))
    numero_documento = Column(String(10))
    data_compensacao = Column(Date)
    origem_transacao = Column(String(1))
    tipo_lancamento = Column(String(20))
    id_usuario_inclusao = Column(Numeric(5,0))
    id_usuario_alteracao = Column(Numeric(5,0))
    id_usuario_conciliacao = Column(Numeric(5,0))
    data_ultima_modificacao = Column(DateTime)
    arq_lancamento_externo = Column(String(25))
    numero_lancamento_externo = Column(Numeric(10,0))

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Correntes(Model):
    __tablename__ = 'scf_contas_correntes'
    id_conta_corrente = Column(Integer,Sequence('scf_contas_correntes_id_conta_corrente_seq'), primary_key=True)
    id_agencia = Column(Numeric(5,0))
    numero_conta = Column(String(15))
    senha_conta = Column(String(15))
    titular_conta = Column(String(50))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    saldo_garantido = Column(Numeric(12,2))
    cnpj_cpf = Column(String(14))
    tabela_conta = Column(String(25))
    saldo_inicial = Column(Numeric(12,2))
    data_abertura = Column(Date)
    data_encerramento = Column(Date)
    status_conta = Column(Numeric(1,0))
    ultima_alteracao = Column(DateTime)
    usuario_ultima_alteracao = Column(Integer)
    usuario_inclusao = Column(Integer)
    saldo_atual = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Pagar(Model):
    __tablename__ = 'scf_contas_pagar'
    id_conta_pagar = Column(Integer,Sequence('scf_contas_pagar_id_conta_pagar_seq'), primary_key=True)
    numero_ordem_pagamento = Column(String(13))
    filial = Column(String(3))
    empresa = Column(String(3))
    id_fornecedor = Column(Integer)
    numero_documento = Column(String(10))
    emissao_documento = Column(Date)
    data_registro = Column(Date)
    historico_conta = Column(String(100))
    data_vencimento = Column(Date)
    valor_previsto = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    juros = Column(Numeric(12,2))
    multa = Column(Numeric(12,2))
    valor_pago = Column(Numeric(12,2))
    data_pagamento = Column(Date)
    local_pagamento = Column(String(5))
    especie_pagamento = Column(Numeric(1,0))
    arquivo_local_pagamento = Column(String(25))
    numero_lancamento = Column(Integer)
    numero_doc_pagamento = Column(String(10))
    status_conta = Column(Numeric(1,0))
    status_pagamento = Column(Numeric(1,0))
    ultima_alteracao = Column(DateTime)
    pc_conta_debito = Column(String(15))
    pc_conta_credito = Column(String(15))
    pc_conta_debito_lancamento = Column(Numeric(10,0))
    pc_conta_credito_lancamento = Column(Numeric(10,0))
    codigo_centro_custo = Column(Numeric(6,0))
    nome_portador = Column(String(40))
    numero_conta_corrente = Column(String(15))
    data_cheque = Column(Date)
    id_caixa = Column(Integer)
    ordem_compra = Column(String(13))
    multiplos_custos = Column(Numeric(1,0))
    multa_apos_vencido = Column(Numeric(10,2))
    mora_dia_atraso = Column(Numeric(10,2))
    dias_protesto = Column(Integer)
    revertido = Column(Integer)
    data_referencia = Column(Date)
    data_cancelamento = Column(Date)
    id_conta_principal = Column(Integer)
    obs_conta = Column(text)
    aguardando_boleto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Pagar_Anexos(Model):
    __tablename__ = 'scf_contas_pagar_anexos'
    id_conta_pagar_anexo = Column(Integer,Sequence('scf_contas_pagar_anexos_id_conta_pagar_anexo_seq'), primary_key=True)
    id_conta_pagar = Column(Integer)
    descricao_anexo = Column(String(40))
    nome_arquivo = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Pagar_Centro_Custos(Model):
    __tablename__ = 'scf_contas_pagar_centro_custos'
    id_cpagar_custo = Column(Integer,Sequence('scf_contas_pagar_centro_custos_id_cpagar_custo_seq'), primary_key=True)
    id_conta_pagar = Column(Integer)
    id_centro_custo = Column(Integer)
    valor = Column(Numeric(10,3))
    placa_veiculo = Column(String(8))

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Pagar_Negadas(Model):
    __tablename__ = 'scf_contas_pagar_negadas'
    id_conta_pagar = Column(Numeric(10,0),Sequence('scf_contas_pagar_negadas_id_conta_pagar_seq'), primary_key=True)
    filial = Column(String(3))
    empresa = Column(String(3))
    id_fornecedor = Column(Numeric(5,0))
    numero_documento = Column(String(10))
    emissao_documento = Column(Date)
    data_registro = Column(Date)
    historico_conta = Column(String(100))
    data_vencimento = Column(Date)
    valor_previsto = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    juros = Column(Numeric(12,2))
    multa = Column(Numeric(12,2))
    valor_pago = Column(Numeric(12,2))
    data_pagamento = Column(Date)
    local_pagamento = Column(String(5))
    especie_pagamento = Column(Numeric(1,0))
    arquivo_local_pagamento = Column(String(25))
    numero_lancamento = Column(Integer)
    numero_doc_pagamento = Column(String(10))
    status_conta = Column(Numeric(1,0))
    status_pagamento = Column(Numeric(1,0))
    ultima_alteracao = Column(DateTime)
    pc_conta_debito = Column(String(15))
    pc_conta_credito = Column(String(15))
    pc_conta_debito_lancamento = Column(Numeric(10,0))
    pc_conta_credito_lancamento = Column(Numeric(10,0))
    ordem_compra = Column(String(13))

    def __repr__(self):
        return self.__tablename__



class Scf_Contas_Pagar_Workflow(Model):
    __tablename__ = 'scf_contas_pagar_workflow'
    id_contas_pagar_workflow = Column(Integer,Sequence('scf_contas_pagar_workflow_id_contas_pagar_workflow_seq'), primary_key=True)
    data_transacao = Column(DateTime)
    id_usuario = Column(Integer)
    texto_justificativo = Column(text)
    id_contas_pagar = Column(Integer)
    id_temp = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Scf_Despesas_Automaticas(Model):
    __tablename__ = 'scf_despesas_automaticas'
    id_despesa_automatica = Column(Integer,Sequence('scf_despesas_automaticas_id_despesa_automatica_seq'), primary_key=True)
    tipo = Column(Integer)
    valor = Column(Numeric(10,2))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    codigo_centro_custo = Column(Integer)
    dia_vencimento = Column(Integer)
    id_fornecedor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scf_Emprestimos_Entre_Empresas(Model):
    __tablename__ = 'scf_emprestimos_entre_empresas'
    id_emprestimo = Column(Integer,Sequence('scf_emprestimos_entre_empresas_id_emprestimo_seq'), primary_key=True)
    data_transacao = Column(Date)
    usuario_transacao = Column(Numeric(5,0))
    valor_emprestimo = Column(Numeric(10,2))
    tipo_lancamento = Column(String(20))
    numero_documento = Column(String(10))
    arquivo_origem = Column(String(25))
    numero_lancamento_origem = Column(Numeric(10,0))
    arquivo_destino = Column(String(25))
    numero_lancamento_destino = Column(Numeric(10,0))
    historico = Column(String(50))
    data_hora = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scf_Historicos(Model):
    __tablename__ = 'scf_historicos'
    id_historico = Column(Integer,Sequence('scf_historicos_id_historico_seq'), primary_key=True)
    descricao_historico = Column(String(50))
    caixa = Column(Integer)
    banco = Column(Integer)
    contas_pagar = Column(Integer)
    contas_receber = Column(Integer)
    cheques_cancelados = Column(Integer)
    formularios_ctrc = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scp_Desenho_Pneu(Model):
    __tablename__ = 'scp_desenho_pneu'
    id_desenho_pneu = Column(Integer,Sequence('scp_desenho_pneu_id_desenho_pneu_seq'), primary_key=True)
    descricao_desenho_pneu = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scp_Diagrama_Pneus(Model):
    __tablename__ = 'scp_diagrama_pneus'
    id_diagrama_pneus = Column(Integer)
    descricao_diagrama = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scp_Diagrama_Posicoes(Model):
    __tablename__ = 'scp_diagrama_posicoes'
    id_diagrama_posicoes = Column(Integer)
    codigo_diagrama = Column(String(6))
    codigo_posicao = Column(String(6))

    def __repr__(self):
        return self.__tablename__



class Scp_Laudos_Remocao(Model):
    __tablename__ = 'scp_laudos_remocao'
    id_laudo_remocao = Column(Integer,Sequence('scp_laudos_remocao_id_laudo_remocao_seq'), primary_key=True)
    codigo_laudo = Column(String(4))
    descricao_laudo = Column(String(75))

    def __repr__(self):
        return self.__tablename__



class Scp_Marca_Pneu(Model):
    __tablename__ = 'scp_marca_pneu'
    id_marca_pneu = Column(Integer,Sequence('scp_marca_pneu_id_marca_pneu_seq'), primary_key=True)
    descricao_marca = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scp_Medidas_Pneu(Model):
    __tablename__ = 'scp_medidas_pneu'
    id_medida_pneu = Column(Integer,Sequence('scp_medidas_pneu_id_medida_pneu_seq'), primary_key=True)
    descricao_medida = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scp_Posicao_Pneu(Model):
    __tablename__ = 'scp_posicao_pneu'
    id_posicao_pneu = Column(Integer,Sequence('scp_posicao_pneu_id_posicao_pneu_seq'), primary_key=True)
    codigo_posicao = Column(String(4))
    descricao_posicao = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Calculo_Status(Model):
    __tablename__ = 'scr_calculo_status'
    codigo = Column(Integer,Sequence('scr_calculo_status_codigo_seq'), primary_key=True)
    mensagem = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Carta_Correcao(Model):
    __tablename__ = 'scr_carta_correcao'
    id_carta_correcao = Column(Integer,Sequence('scr_carta_correcao_id_carta_correcao_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    data_correcao = Column(Date)
    destinatario = Column(String(50))
    remetente = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Carta_Correcao_Itens(Model):
    __tablename__ = 'scr_carta_correcao_itens'
    id_carta_correcao_itens = Column(Integer,Sequence('scr_carta_correcao_itens_id_carta_correcao_itens_seq'), primary_key=True)
    id_carta_correcao = Column(Integer)
    id_itens_correcao = Column(Integer)
    valor_corrigido = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Scr_Configuracoes_Texto(Model):
    __tablename__ = 'scr_configuracoes_texto'
    id_configuracao_texto = Column(Integer,Sequence('scr_configuracoes_texto_id_configuracao_texto_seq'), primary_key=True)
    codigo_modulo = Column(String(10))
    codigo_configuracao = Column(String(30))
    texto_configuracao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento(Model):
    __tablename__ = 'scr_conhecimento'
    id_conhecimento = Column(Integer,Sequence('scr_conhecimento_id_conhecimento_seq'), primary_key=True)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    numero_ctrc_filial = Column(String(13))
    remetente_id = Column(Integer)
    remetente_cnpj = Column(String(14))
    remetente_nome = Column(String(50))
    remetente_id_endereco = Column(Integer)
    remetente_endereco = Column(String(50))
    remetente_numero = Column(String(10))
    remetente_bairro = Column(String(30))
    remetente_cidade = Column(String(30))
    remetente_uf = Column(String(2))
    remetente_cep = Column(String(8))
    remetente_ie = Column(String(15))
    remetente_ddd = Column(String(2))
    remetente_telefone = Column(String(10))
    destinatario_id = Column(Integer)
    destinatario_cnpj = Column(String(14))
    destinatario_nome = Column(String(50))
    destinatario_id_endereco = Column(Integer)
    destinatario_endereco = Column(String(50))
    destinatario_numero = Column(String(10))
    destinatario_bairro = Column(String(30))
    destinatario_cidade = Column(String(30))
    destinatario_uf = Column(String(2))
    destinatario_cep = Column(String(8))
    destinatario_ie = Column(String(15))
    destinatario_ddd = Column(String(2))
    destinatario_telefone = Column(String(10))
    frete_cif_fob = Column(Integer)
    consig_red = Column(Integer)
    conhecimento_origem = Column(String(44))
    data_conhecimento_origem = Column(Date)
    consig_red_id = Column(Integer)
    consig_red_cnpj = Column(String(14))
    consig_red_nome = Column(String(50))
    consig_red_id_endereco = Column(Integer)
    consig_red_endereco = Column(String(50))
    consig_red_numero = Column(String(10))
    consig_red_bairro = Column(String(30))
    consig_red_cidade = Column(String(30))
    consig_red_uf = Column(String(2))
    consig_red_cep = Column(String(8))
    consig_red_ie = Column(String(15))
    consig_red_ddd = Column(String(2))
    consig_red_telefone = Column(String(10))
    consig_red_cif_fob = Column(Integer)
    observacoes_coleta = Column(text)
    observacoes_entrega = Column(text)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    natureza_carga = Column(String(40))
    especie = Column(String(10))
    placa_veiculo = Column(String(10))
    valor_nota_fiscal = Column(Numeric(11,2))
    data_emissao = Column(DateTime)
    frete_peso = Column(Numeric(10,2))
    frete_valor = Column(Numeric(10,2))
    sec_cat = Column(Numeric(10,2))
    despacho = Column(Numeric(10,2))
    gris = Column(Numeric(10,2))
    itr = Column(Numeric(10,2))
    pedagio = Column(Numeric(10,2))
    outros = Column(Numeric(10,2))
    total_frete = Column(Numeric(10,2))
    base_calculo = Column(Numeric(10,2))
    imposto = Column(Numeric(10,2))
    desconto = Column(Numeric(10,2))
    tabele_frete = Column(String(13))
    tipo_imposto = Column(Integer)
    natureza_operacao = Column(String(20))
    cod_operacao_fiscal = Column(String(5))
    observacoes_conhecimento = Column(text)
    aliquota = Column(Numeric(5,2))
    imposto_incluso = Column(Integer)
    numero_manifesto = Column(String(13))
    comprovante_entrega = Column(Integer)
    numero_fatura = Column(String(13))
    numero_formulario = Column(String(6))
    cancelado = Column(Integer)
    situacao = Column(Integer)
    canhoto = Column(Integer)
    avista = Column(Integer)
    status = Column(Integer)
    usuario_inclusao = Column(Integer)
    usuario_alteracao = Column(Integer)
    usuario_emissao = Column(Integer)
    usuario_cancelamento = Column(Integer)
    data_entrega = Column(Date)
    hora_entrega = Column(String(5))
    data_recebimento_nf = Column(Date)
    data_viagem = Column(DateTime)
    data_nota_fiscal = Column(Date)
    data_previsao_entrega = Column(Date)
    data_cancelamento = Column(DateTime)
    data_digitacao = Column(DateTime)
    tipo_transporte = Column(Integer)
    tipo_ctrc_cte = Column(Integer)
    tipo_envio = Column(Integer)
    id_lote = Column(Integer)
    codigo_cte = Column(String(9))
    chave_cte = Column(String(44))
    chave_cte_dv = Column(String(1))
    id_cte = Column(String(47))
    cstat = Column(String(3))
    xmotivo = Column(text)
    motivo_cancelamento = Column(text)
    protocolo_cancelamento = Column(String(15))
    xml_proc_cancelamento = Column(text)
    consig_red_pago_apagar = Column(Integer)
    incidencia = Column(Numeric(12,2))
    calculado_ate_id_cidade = Column(Integer)
    calculado_ate_cidade = Column(String(40))
    calculado_ate_uf = Column(String(2))
    remetente_codigo_pais = Column(String(5))
    remetente_nome_pais = Column(String(50))
    destinatario_codigo_pais = Column(String(5))
    destinatario_nome_pais = Column(String(50))
    consig_red_codigo_pais = Column(String(5))
    consig_red_nome_pais = Column(String(50))
    peso_cubado = Column(Numeric(10,3))
    id_manifesto = Column(Integer)
    numero_romaneio = Column(String(13))
    id_coleta_filial = Column(String(13))
    cpf_recebedor = Column(String(11))
    nome_recebedor = Column(String(50))
    conteudo_html = Column(text)
    conteudo_html_peq = Column(text)
    observacao_entrega = Column(text)
    versao_edi = Column(String(15))
    id_romaneio_redespacho = Column(Integer)
    calculado_de_id_cidade = Column(Integer)
    calculado_de_cidade = Column(String(40))
    calculado_de_uf = Column(String(2))
    redespachador_id = Column(Integer)
    redespachador_cnpj = Column(String(14))
    redespachador_nome = Column(String(50))
    redespachador_id_endereco = Column(Integer)
    redespachador_endereco = Column(String(50))
    redespachador_numero = Column(String(10))
    redespachador_bairro = Column(String(30))
    redespachador_cidade = Column(String(30))
    redespachador_uf = Column(String(2))
    redespachador_cep = Column(String(8))
    redespachador_ie = Column(String(15))
    redespachador_ddd = Column(String(2))
    redespachador_telefone = Column(String(10))
    usuario_fatura = Column(String(30))
    motivo_retirada_fatura = Column(text)
    id_usuario_fatura = Column(Integer)
    redespachador_codigo_pais = Column(String(5))
    redespachador_nome_pais = Column(String(50))
    status_cte = Column(Integer)
    prot_autorizacao_cte = Column(String(15))
    frete_peso_aereo = Column(Numeric(10,2))
    taxa_coleta = Column(Numeric(10,2))
    taxa_entrega = Column(Numeric(10,2))
    taxa_redespacho = Column(Numeric(10,2))
    taxa_expresso = Column(Numeric(10,2))
    taxa_emergencia = Column(Numeric(10,2))
    taxa_manuseio_embalagem = Column(Numeric(10,2))
    taxa_escolta = Column(Numeric(10,2))
    taxa_outros = Column(Numeric(10,2))
    expresso = Column(Integer)
    emergencia = Column(Integer)
    escolta = Column(Integer)
    escolta_horas_coleta = Column(Integer)
    modal = Column(Integer)
    escolta_horas_entrega = Column(Integer)
    coleta_escolta = Column(Integer)
    coleta_expresso = Column(Integer)
    coleta_emergencia = Column(Integer)
    coleta_normal = Column(Integer)
    entrega_escolta = Column(Integer)
    entrega_expresso = Column(Integer)
    entrega_emergencia = Column(Integer)
    entrega_normal = Column(Integer)
    taxa_dce = Column(Numeric(8,2))
    taxa_exclusivo = Column(Numeric(8,2))
    coleta_dificuldade = Column(Integer)
    entrega_dificuldade = Column(Integer)
    entrega_exclusiva = Column(Integer)
    coleta_exclusiva = Column(Integer)
    desc_taxa_coleta = Column(Numeric(8,2))
    desc_taxa_entrega = Column(Numeric(8,2))
    desc_taxa_redespacho = Column(Numeric(8,2))
    desc_taxa_expresso = Column(Numeric(8,2))
    desc_taxa_emergencia = Column(Numeric(8,2))
    desc_taxa_manuseio = Column(Numeric(8,2))
    desc_taxa_escolta = Column(Numeric(8,2))
    desc_frete_valor_aereo = Column(Numeric(8,2))
    tipo_doc_referenciado = Column(Integer)
    cte_referenciado = Column(String(44))
    xml_proc_cte = Column(text)
    tipo_documento = Column(Integer)
    faturar = Column(Integer)
    total_frete_origem = Column(Numeric(12,2))
    id_faturamento = Column(Integer)
    serie_doc = Column(String(10))
    pagador_id = Column(Integer)
    pagador_cnpj = Column(String(14))
    baixa_provisoria = Column(Integer)
    redespacho = Column(Integer)
    cte_ambiente = Column(Integer)
    percentual_frete = Column(Numeric(6,2))
    data_retorno = Column(Date)
    tipo_frete = Column(String(3))
    placa_reboque1 = Column(String(8))
    placa_reboque2 = Column(String(8))
    id_motorista = Column(Integer)
    dacte_impresso = Column(Integer)
    prot_inutilizacao = Column(String(15))
    xml_prot_inutilizacao = Column(text)
    distancia_combinada = Column(Integer)
    gnre = Column(Numeric(12,2))
    data_baixa = Column(Date)
    flg_viagem = Column(Integer)
    flg_importado = Column(Integer)
    numero_minuta_aereo = Column(String(9))
    ident_emissor_aereo = Column(String(20))
    classe_tarifa_aereo = Column(String(1))
    codigo_tarifa_aereo = Column(String(4))
    valor_tarifa_aereo = Column(Numeric(13,2))
    dimensao_aereo = Column(String(14))
    tipo_entrega = Column(Integer)
    id_aeroporto_origem = Column(Integer)
    id_aeroporto_destino = Column(Integer)
    observacao_etiqueta = Column(String(50))
    substituicao_tributaria = Column(Integer)
    icms_st = Column(Numeric(12,2))
    aliquota_icms_st = Column(Numeric(5,2))
    perc_reducao_base_calculo = Column(Numeric(5,2))
    base_calculo_st_reduzida = Column(Numeric(12,2))
    credito_presumido_outorgado = Column(Numeric(12,2))
    iss = Column(Numeric(12,2))
    aliquota_iss = Column(Numeric(5,2))
    cst_pis = Column(String(3))
    aliquota_pis = Column(Numeric(5,2))
    valor_pis = Column(Numeric(12,2))
    cst_cofins = Column(String(3))
    aliquota_cofins = Column(Numeric(5,2))
    valor_cofins = Column(Numeric(12,2))
    responsavel_seguro = Column(Integer)
    aprovado = Column(Integer)
    numero_awb = Column(String(15))
    perc_desconto = Column(Numeric(5,2))
    numero_documento = Column(String(13))
    infadfisco = Column(text)
    total_frete_faturado = Column(Numeric(12,2))
    desconto_faturado = Column(Numeric(12,2))
    acrescimo_faturado = Column(Numeric(12,2))
    total_entregas = Column(Integer)
    peso_agregado_nf = Column(Numeric(12,4))
    volume_cubico_agregado_nf = Column(Numeric(12,6))
    dt_agenda_coleta = Column(DateTime)
    dt_agenda_entrega = Column(DateTime)
    regime_especial_mg = Column(Integer)
    id_conhecimento_principal = Column(Integer)
    data_cte_re = Column(Date)
    flg_regime_especial = Column(Integer)
    cod_interno_frete = Column(String(13))
    id_tipo_veiculo = Column(Integer)
    vl_combinado = Column(Numeric(12,2))
    vl_tonelada = Column(Numeric(12,8))
    vl_percentual_nf = Column(Numeric(12,8))
    observacoes_conhecimento_2 = Column(text)
    id_doc_redespacho = Column(Integer)
    id_doc_vendedores = Column(Integer)
    codigo_vendedor = Column(String(10))
    data_expedicao = Column(Date)
    id_pre_fatura_entrega = Column(Integer)
    vl_frete_peso = Column(Numeric(12,2))
    consumidor_final = Column(Integer)
    base_calculo_difal = Column(Numeric(12,2))
    difal_icms = Column(Numeric(12,2))
    difal_icms_origem = Column(Numeric(12,2))
    difal_icms_destino = Column(Numeric(12,2))
    aliq_icms_interna = Column(Numeric(5,2))
    aliq_icms_inter = Column(Numeric(5,2))
    aliquota_fcp = Column(Numeric(5,2))
    valor_fcp = Column(Numeric(12,2))
    calculo_difal = Column(Integer)
    placa_coleta = Column(String(8))
    tabela_redespacho = Column(String(13))
    id_cidade_origem_redespacho = Column(Integer)
    vl_redespacho = Column(Numeric(12,2))
    valor_combinado_re = Column(Numeric(12,2))
    regime_especial_combinado = Column(Integer)
    valor_combinado_minuta_re = Column(Numeric(12,2))
    nfe_anulacao = Column(String(44))
    locent_destinatario_id = Column(Integer)
    locent_destinatario_cnpj = Column(String(14))
    locent_destinatario_id_endereco = Column(Integer)
    expedidor_cnpj = Column(String(16))
    recebedor_cnpj = Column(String(16))
    peso_transportado = Column(Numeric(12,4))
    odometro_inicial = Column(Integer)
    valor_seguro = Column(Numeric(12,2))
    numero_averbacao = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_26_03(Model):
    __tablename__ = 'scr_conhecimento_26_03'
    id_conhecimento = Column(Integer)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    numero_ctrc_filial = Column(String(13))
    remetente_id = Column(Integer)
    remetente_cnpj = Column(String(14))
    remetente_nome = Column(String(50))
    remetente_id_endereco = Column(Integer)
    remetente_endereco = Column(String(50))
    remetente_numero = Column(String(10))
    remetente_bairro = Column(String(30))
    remetente_cidade = Column(String(30))
    remetente_uf = Column(String(2))
    remetente_cep = Column(String(8))
    remetente_ie = Column(String(15))
    remetente_ddd = Column(String(2))
    remetente_telefone = Column(String(10))
    destinatario_id = Column(Integer)
    destinatario_cnpj = Column(String(14))
    destinatario_nome = Column(String(50))
    destinatario_id_endereco = Column(Integer)
    destinatario_endereco = Column(String(50))
    destinatario_numero = Column(String(10))
    destinatario_bairro = Column(String(30))
    destinatario_cidade = Column(String(30))
    destinatario_uf = Column(String(2))
    destinatario_cep = Column(String(8))
    destinatario_ie = Column(String(15))
    destinatario_ddd = Column(String(2))
    destinatario_telefone = Column(String(10))
    frete_cif_fob = Column(Integer)
    consig_red = Column(Integer)
    conhecimento_origem = Column(String(44))
    data_conhecimento_origem = Column(Date)
    consig_red_id = Column(Integer)
    consig_red_cnpj = Column(String(14))
    consig_red_nome = Column(String(50))
    consig_red_id_endereco = Column(Integer)
    consig_red_endereco = Column(String(50))
    consig_red_numero = Column(String(10))
    consig_red_bairro = Column(String(30))
    consig_red_cidade = Column(String(30))
    consig_red_uf = Column(String(2))
    consig_red_cep = Column(String(8))
    consig_red_ie = Column(String(15))
    consig_red_ddd = Column(String(2))
    consig_red_telefone = Column(String(10))
    consig_red_cif_fob = Column(Integer)
    observacoes_coleta = Column(text)
    observacoes_entrega = Column(text)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    natureza_carga = Column(String(40))
    especie = Column(String(10))
    placa_veiculo = Column(String(10))
    valor_nota_fiscal = Column(Numeric(11,2))
    data_emissao = Column(DateTime)
    frete_peso = Column(Numeric(10,2))
    frete_valor = Column(Numeric(10,2))
    sec_cat = Column(Numeric(10,2))
    despacho = Column(Numeric(10,2))
    gris = Column(Numeric(10,2))
    itr = Column(Numeric(10,2))
    pedagio = Column(Numeric(10,2))
    outros = Column(Numeric(10,2))
    total_frete = Column(Numeric(10,2))
    base_calculo = Column(Numeric(10,2))
    imposto = Column(Numeric(10,2))
    desconto = Column(Numeric(10,2))
    tabele_frete = Column(String(13))
    tipo_imposto = Column(Integer)
    natureza_operacao = Column(String(20))
    cod_operacao_fiscal = Column(String(5))
    observacoes_conhecimento = Column(text)
    aliquota = Column(Numeric(5,2))
    imposto_incluso = Column(Integer)
    numero_manifesto = Column(String(13))
    comprovante_entrega = Column(Integer)
    numero_fatura = Column(String(13))
    numero_formulario = Column(String(6))
    cancelado = Column(Integer)
    situacao = Column(Integer)
    canhoto = Column(Integer)
    avista = Column(Integer)
    status = Column(Integer)
    usuario_inclusao = Column(Integer)
    usuario_alteracao = Column(Integer)
    usuario_emissao = Column(Integer)
    usuario_cancelamento = Column(Integer)
    data_entrega = Column(Date)
    hora_entrega = Column(String(5))
    data_recebimento_nf = Column(Date)
    data_viagem = Column(DateTime)
    data_nota_fiscal = Column(Date)
    data_previsao_entrega = Column(Date)
    data_cancelamento = Column(DateTime)
    data_digitacao = Column(DateTime)
    tipo_transporte = Column(Integer)
    tipo_ctrc_cte = Column(Integer)
    tipo_envio = Column(Integer)
    id_lote = Column(Integer)
    codigo_cte = Column(String(9))
    chave_cte = Column(String(44))
    chave_cte_dv = Column(String(1))
    id_cte = Column(String(47))
    cstat = Column(String(3))
    xmotivo = Column(String(100))
    motivo_cancelamento = Column(text)
    protocolo_cancelamento = Column(String(15))
    xml_proc_cancelamento = Column(text)
    consig_red_pago_apagar = Column(Integer)
    incidencia = Column(Numeric(12,2))
    calculado_ate_id_cidade = Column(Integer)
    calculado_ate_cidade = Column(String(40))
    calculado_ate_uf = Column(String(2))
    remetente_codigo_pais = Column(String(5))
    remetente_nome_pais = Column(String(50))
    destinatario_codigo_pais = Column(String(5))
    destinatario_nome_pais = Column(String(50))
    consig_red_codigo_pais = Column(String(5))
    consig_red_nome_pais = Column(String(50))
    peso_cubado = Column(Numeric(10,3))
    id_manifesto = Column(Integer)
    numero_romaneio = Column(String(13))
    id_coleta_filial = Column(String(13))
    cpf_recebedor = Column(String(11))
    nome_recebedor = Column(String(50))
    conteudo_html = Column(text)
    conteudo_html_peq = Column(text)
    observacao_entrega = Column(String(30))
    versao_edi = Column(String(15))
    id_romaneio_redespacho = Column(Integer)
    calculado_de_id_cidade = Column(Integer)
    calculado_de_cidade = Column(String(40))
    calculado_de_uf = Column(String(2))
    redespachador_id = Column(Integer)
    redespachador_cnpj = Column(String(14))
    redespachador_nome = Column(String(50))
    redespachador_id_endereco = Column(Integer)
    redespachador_endereco = Column(String(50))
    redespachador_numero = Column(String(10))
    redespachador_bairro = Column(String(30))
    redespachador_cidade = Column(String(30))
    redespachador_uf = Column(String(2))
    redespachador_cep = Column(String(8))
    redespachador_ie = Column(String(15))
    redespachador_ddd = Column(String(2))
    redespachador_telefone = Column(String(10))
    usuario_fatura = Column(String(30))
    motivo_retirada_fatura = Column(text)
    id_usuario_fatura = Column(Integer)
    redespachador_codigo_pais = Column(String(5))
    redespachador_nome_pais = Column(String(50))
    status_cte = Column(Integer)
    prot_autorizacao_cte = Column(String(15))
    frete_peso_aereo = Column(Numeric(10,2))
    taxa_coleta = Column(Numeric(10,2))
    taxa_entrega = Column(Numeric(10,2))
    taxa_redespacho = Column(Numeric(10,2))
    taxa_expresso = Column(Numeric(10,2))
    taxa_emergencia = Column(Numeric(10,2))
    taxa_manuseio_embalagem = Column(Numeric(10,2))
    taxa_escolta = Column(Numeric(10,2))
    taxa_outros = Column(Numeric(10,2))
    expresso = Column(Integer)
    emergencia = Column(Integer)
    escolta = Column(Integer)
    escolta_horas_coleta = Column(Integer)
    modal = Column(Integer)
    escolta_horas_entrega = Column(Integer)
    coleta_escolta = Column(Integer)
    coleta_expresso = Column(Integer)
    coleta_emergencia = Column(Integer)
    coleta_normal = Column(Integer)
    entrega_escolta = Column(Integer)
    entrega_expresso = Column(Integer)
    entrega_emergencia = Column(Integer)
    entrega_normal = Column(Integer)
    taxa_dce = Column(Numeric(8,2))
    taxa_exclusivo = Column(Numeric(8,2))
    coleta_dificuldade = Column(Integer)
    entrega_dificuldade = Column(Integer)
    entrega_exclusiva = Column(Integer)
    coleta_exclusiva = Column(Integer)
    desc_taxa_coleta = Column(Numeric(8,2))
    desc_taxa_entrega = Column(Numeric(8,2))
    desc_taxa_redespacho = Column(Numeric(8,2))
    desc_taxa_expresso = Column(Numeric(8,2))
    desc_taxa_emergencia = Column(Numeric(8,2))
    desc_taxa_manuseio = Column(Numeric(8,2))
    desc_taxa_escolta = Column(Numeric(8,2))
    desc_frete_valor_aereo = Column(Numeric(8,2))
    tipo_doc_referenciado = Column(Integer)
    cte_referenciado = Column(String(44))
    xml_proc_cte = Column(text)
    tipo_documento = Column(Integer)
    faturar = Column(Integer)
    total_frete_origem = Column(Numeric(12,2))
    id_faturamento = Column(Integer)
    serie_doc = Column(String(10))
    pagador_id = Column(Integer)
    pagador_cnpj = Column(String(14))
    baixa_provisoria = Column(Integer)
    redespacho = Column(Integer)
    cte_ambiente = Column(Integer)
    percentual_frete = Column(Numeric(6,2))
    data_retorno = Column(Date)
    tipo_frete = Column(String(3))
    placa_reboque1 = Column(String(8))
    placa_reboque2 = Column(String(8))
    id_motorista = Column(Integer)
    dacte_impresso = Column(Integer)
    prot_inutilizacao = Column(String(15))
    xml_prot_inutilizacao = Column(text)
    distancia_combinada = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Averbacao(Model):
    __tablename__ = 'scr_conhecimento_averbacao'
    id = Column(Integer,Sequence('scr_conhecimento_averbacao_id_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_seguradora = Column(Integer)
    averbado = Column(Integer)
    cancelado = Column(Integer)
    data = Column(Date)
    protocolo = Column(String(60))
    cod_erro = Column(String(10))
    erro = Column(text)
    data_registro = Column(DateTime)
    data_cancelamento = Column(DateTime)
    reenvia = Column(Integer)
    xml_cancelamento = Column(text)
    numero_averbacao = Column(String(50))
    retorno_averbacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Cf(Model):
    __tablename__ = 'scr_conhecimento_cf'
    id_conhecimento_cf = Column(Integer,Sequence('scr_conhecimento_cf_id_conhecimento_cf_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_tipo_calculo = Column(Integer)
    excedente = Column(Integer)
    quantidade = Column(Numeric(16,8))
    valor_item = Column(Numeric(16,8))
    valor_total = Column(Numeric(12,2))
    valor_minimo = Column(Numeric(12,2))
    valor_pagar = Column(Numeric(12,2))
    operacao = Column(String(1))
    id_faixa = Column(Integer)
    combinado = Column(Integer)
    modo_calculo = Column(Integer)
    perc_desconto = Column(Numeric(5,2))
    valor_pagar_sdesconto = Column(Numeric(13,2))
    desconto = Column(Numeric(13,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Digitalizado(Model):
    __tablename__ = 'scr_conhecimento_digitalizado'
    id_ctrc_digitalizado = Column(Integer,Sequence('scr_conhecimento_digitalizado_id_ctrc_digitalizado_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    nome_arquivo = Column(String(120))
    data_upload = Column(Date)
    caminho_arquivo = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Entrega(Model):
    __tablename__ = 'scr_conhecimento_entrega'
    id_conhecimento_entrega = Column(Integer,Sequence('scr_conhecimento_entrega_id_conhecimento_entrega_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_romaneios = Column(Integer)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    id_ocorrencia = Column(Integer)
    id_ocorrencia_obs = Column(Integer)
    canhoto = Column(Integer)
    data_ocorrencia = Column(DateTime)
    entrega_realizada = Column(Integer)
    obs_ocorrencia = Column(String(200))
    nome_recebedor = Column(String(200))
    cpf_recebedor = Column(String(11))
    reentrega = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Entregas_Tmp(Model):
    __tablename__ = 'scr_conhecimento_entregas_tmp'
    id_conhecimento_entrega = Column(Integer)
    id_conhecimento = Column(Integer)
    id_romaneios = Column(Integer)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    id_ocorrencia = Column(Integer)
    id_ocorrencia_obs = Column(Integer)
    canhoto = Column(Integer)
    data_ocorrencia = Column(DateTime)
    entrega_realizada = Column(Integer)
    obs_ocorrencia = Column(String(200))
    nome_recebedor = Column(String(200))
    cpf_recebedor = Column(String(11))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Imagem(Model):
    __tablename__ = 'scr_conhecimento_imagem'
    id_conhecimento_imagem = Column(Integer,Sequence('scr_conhecimento_imagem_id_conhecimento_imagem_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    arquivo = Column(text)
    data_upload = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Importado(Model):
    __tablename__ = 'scr_conhecimento_importado'
    id_conhecimento = Column(Integer,Sequence('scr_conhecimento_importado_id_conhecimento_seq'), primary_key=True)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    numero_ctrc_filial = Column(String(13))
    remetente_id = Column(Integer)
    remetente_cnpj = Column(String(14))
    remetente_nome = Column(String(50))
    remetente_id_endereco = Column(Integer)
    remetente_endereco = Column(String(50))
    remetente_numero = Column(String(10))
    remetente_bairro = Column(String(30))
    remetente_cidade = Column(String(30))
    remetente_uf = Column(String(2))
    remetente_cep = Column(String(8))
    remetente_ie = Column(String(15))
    remetente_ddd = Column(String(2))
    remetente_telefone = Column(String(10))
    destinatario_id = Column(Integer)
    destinatario_cnpj = Column(String(14))
    destinatario_nome = Column(String(50))
    destinatario_id_endereco = Column(Integer)
    destinatario_endereco = Column(String(50))
    destinatario_numero = Column(String(10))
    destinatario_bairro = Column(String(30))
    destinatario_cidade = Column(String(30))
    destinatario_uf = Column(String(2))
    destinatario_cep = Column(String(8))
    destinatario_ie = Column(String(15))
    destinatario_ddd = Column(String(2))
    destinatario_telefone = Column(String(10))
    frete_cif_fob = Column(Integer)
    consig_red = Column(Integer)
    conhecimento_origem = Column(String(13))
    data_conhecimento_origem = Column(Date)
    consig_red_id = Column(Integer)
    consig_red_cnpj = Column(String(14))
    consig_red_nome = Column(String(14))
    consig_red_id_endereco = Column(Integer)
    consig_red_endereco = Column(String(50))
    consig_red_numero = Column(String(10))
    consig_red_bairro = Column(String(30))
    consig_red_cidade = Column(String(30))
    consig_red_uf = Column(String(2))
    consig_red_cep = Column(String(8))
    consig_red_ie = Column(String(15))
    consig_red_ddd = Column(String(2))
    consig_red_telefone = Column(String(10))
    consig_red_cif_fob = Column(Integer)
    observacoes_coleta = Column(text)
    observacoes_entrega = Column(text)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    natureza_carga = Column(String(30))
    especie = Column(String(10))
    valor_nota_fiscal = Column(Numeric(11,2))
    data_emissao = Column(Date)
    frete_peso = Column(Numeric(10,2))
    frete_valor = Column(Numeric(10,2))
    sec_cat = Column(Numeric(10,2))
    despacho = Column(Numeric(10,2))
    gris = Column(Numeric(10,2))
    itr = Column(Numeric(10,2))
    pedagio = Column(Numeric(10,2))
    outros = Column(Numeric(10,2))
    total_frete = Column(Numeric(10,2))
    base_calculo = Column(Numeric(10,2))
    imposto = Column(Numeric(10,2))
    desconto = Column(Numeric(10,2))
    tabele_frete = Column(String(13))
    tipo_imposto = Column(Integer)
    natureza_operacao = Column(String(20))
    cod_operacao_fiscal = Column(String(5))
    observacoes_conhecimento = Column(text)
    aliquota = Column(Numeric(5,2))
    imposto_incluso = Column(Integer)
    numero_manifesto = Column(String(13))
    comprovante_entrega = Column(Integer)
    numero_fatura = Column(String(13))
    numero_formulario = Column(String(6))
    cancelado = Column(Integer)
    situacao = Column(Integer)
    canhoto = Column(Integer)
    avista = Column(Integer)
    status = Column(Integer)
    usuario_inclusao = Column(Integer)
    usuario_alteracao = Column(Integer)
    usuario_emissao = Column(Integer)
    usuario_cancelamento = Column(Integer)
    data_entrega = Column(Date)
    hora_entrega = Column(String(5))
    data_recebimento_nf = Column(Date)
    data_viagem = Column(DateTime)
    data_nota_fiscal = Column(Date)
    data_previsao_entrega = Column(Date)
    data_cancelamento = Column(DateTime)
    data_digitacao = Column(DateTime)
    tipo_transporte = Column(Integer)
    tipo_ctrc_cte = Column(Integer)
    tipo_envio = Column(Integer)
    id_lote = Column(Integer)
    codigo_cte = Column(String(9))
    chave_cte = Column(String(44))
    chave_cte_dv = Column(String(1))
    id_cte = Column(String(47))
    cstat = Column(String(3))
    xmotivo = Column(String(100))
    motivo_cancelamento = Column(text)
    protocolo_cancelamento = Column(String(15))
    xml_proc_cancelamento = Column(text)
    consig_red_pago_apagar = Column(Integer)
    incidencia = Column(Integer)
    calculado_ate_id_cidade = Column(Integer)
    calculado_ate_cidade = Column(String(40))
    calculado_ate_uf = Column(String(2))
    remetente_codigo_pais = Column(String(5))
    remetente_nome_pais = Column(String(5))
    destinatario_codigo_pais = Column(String(5))
    destinatario_nome_pais = Column(String(50))
    consig_red_codigo_pais = Column(String(5))
    consig_red_nome_pais = Column(String(50))
    peso_cubado = Column(Numeric(10,3))
    id_manifesto = Column(Integer)
    numero_romaneio = Column(String(13))
    id_coleta_filial = Column(String(13))
    cpf_recebedor = Column(String(11))
    nome_recebedor = Column(String(50))
    conteudo_html = Column(text)
    conteudo_html_peq = Column(text)
    observacao_entrega = Column(String(30))
    versao_edi = Column(String(15))
    id_romaneio_redespacho = Column(Integer)
    calculado_de_id_cidade = Column(Integer)
    calculado_de_cidade = Column(String(40))
    calculado_de_uf = Column(String(2))
    redespachador_id = Column(Integer)
    redespachador_cnpj = Column(String(14))
    redespachador_nome = Column(String(14))
    redespachador_id_endereco = Column(Integer)
    redespachador_endereco = Column(String(50))
    redespachador_numero = Column(String(10))
    redespachador_bairro = Column(String(30))
    redespachador_cidade = Column(String(30))
    redespachador_uf = Column(String(2))
    redespachador_cep = Column(String(8))
    redespachador_ie = Column(String(15))
    redespachador_ddd = Column(String(2))
    redespachador_telefone = Column(String(10))
    usuario_fatura = Column(String(30))
    motivo_retirada_fatura = Column(text)
    id_usuario_fatura = Column(Integer)
    redespachador_codigo_pais = Column(String(5))
    redespachador_nome_pais = Column(String(50))
    status_cte = Column(Integer)
    prot_autorizacao_cte = Column(String(15))
    regiao = Column(String(30))
    tabela = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Log_Atividades(Model):
    __tablename__ = 'scr_conhecimento_log_atividades'
    id_conhecimento = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(text)
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Notas_Fiscais(Model):
    __tablename__ = 'scr_conhecimento_notas_fiscais'
    id_conhecimento_notas_fiscais = Column(Integer,Sequence('scr_conhecimento_notas_fiscais_id_conhecimento_notas_fiscais_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    data_nota_fiscal = Column(Date)
    numero_nota_fiscal = Column(String(9))
    serie_nota_fiscal = Column(String(3))
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(20,4))
    valor = Column(Numeric(10,2))
    volume_cubico = Column(Numeric(10,4))
    tipo_nota = Column(Integer)
    numero_romaneio_nf = Column(String(15))
    numero_pedido_nf = Column(String(15))
    valor_base_calculo = Column(Numeric(15,2))
    valor_icms_nf = Column(Numeric(15,2))
    valor_base_calculo_icms_st = Column(Numeric(15,2))
    valor_icms_nf_st = Column(Numeric(15,2))
    cfop_pred_nf = Column(String(4))
    valor_total_produtos = Column(Numeric(15,2))
    pin = Column(String(9))
    chave_nfe = Column(String(44))
    id_inclusao = Column(String(10))
    id_ocorrencia = Column(Integer)
    data_ocorrencia = Column(Date)
    hora_ocorrencia = Column(String(5))
    id_ocorrencia_obs = Column(Integer)
    canhoto = Column(Integer)
    incidencia = Column(Integer)
    id_natureza_carga = Column(Integer)
    modelo_nf = Column(Integer)
    especie_mercadoria = Column(String(30))
    peso_liquido = Column(Numeric(20,4))
    id_nota_fiscal_imp = Column(Integer)
    tipo_transporte = Column(Integer)
    codigo_vendedor = Column(Integer)
    supervisor = Column(String(30))
    total_frete_nf = Column(Numeric(12,2))
    total_frete_prod = Column(Numeric(12,2))
    id_romaneio_redespachador = Column(Integer)
    id_nota_fiscal_redespachador = Column(Integer)
    id_conhecimento_redespachador = Column(Integer)
    sap_docentry = Column(Integer)
    sap_serial = Column(Integer)
    sap_tipoobjeto = Column(Integer)
    sap_supervisor = Column(String(50))
    peso_transportado = Column(Numeric(20,4))

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Notas_Fiscais_Imp(Model):
    __tablename__ = 'scr_conhecimento_notas_fiscais_imp'
    id_notas_fiscais_imp = Column(Integer,Sequence('scr_conhecimento_notas_fiscais_imp_id_notas_fiscais_imp_seq'), primary_key=True)
    tipo_documento = Column(Integer)
    id_conhecimento = Column(Integer)
    status = Column(Integer)
    flg_importacao = Column(Integer)
    importado = Column(Integer)
    frete_combinado = Column(Integer)
    agrupador = Column(Integer)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    remetente_id = Column(Integer)
    remetente_id_endereco = Column(Integer)
    calculado_de_id_cidade = Column(Integer)
    destinatario_id = Column(Integer)
    destinatario_id_endereco = Column(Integer)
    calculado_ate_id_cidade = Column(Integer)
    consignatario_id = Column(Integer)
    consignatario_id_endereco = Column(Integer)
    redespachador_id = Column(Integer)
    redespachador_id_endereco = Column(Integer)
    frete_cif_fob = Column(Integer)
    consig_red = Column(Integer)
    avista = Column(Integer)
    tipo_imposto = Column(Integer)
    aliquota = Column(Numeric(5,2))
    imposto_incluso = Column(Integer)
    placa_veiculo = Column(String(8))
    id_motorista = Column(Integer)
    numero_tabela_frete = Column(String(13))
    cod_operacao_fiscal = Column(String(5))
    natureza_operacao = Column(String(20))
    data_nota_fiscal = Column(Date)
    numero_nota_fiscal = Column(String(9))
    modelo_nf = Column(Integer)
    serie_nota_fiscal = Column(String(3))
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    valor = Column(Numeric(10,2))
    volume_cubico = Column(Numeric(10,4))
    tipo_nota = Column(Integer)
    numero_pedido_nf = Column(String(15))
    valor_base_calculo = Column(Numeric(15,2))
    valor_icms_nf = Column(Numeric(15,2))
    valor_base_calculo_icms_st = Column(Numeric(15,2))
    valor_icms_nf_st = Column(Numeric(15,2))
    cfop_pred_nf = Column(String(4))
    valor_total_produtos = Column(Numeric(15,2))
    pin = Column(String(9))
    chave_nfe = Column(String(44))
    id_natureza_carga = Column(Integer)
    classificacao_fiscal = Column(String(15))
    peso_pressumido = Column(Numeric(12,4))
    volume_pressumido = Column(Numeric(12,4))
    flg_valor_pressumido = Column(Integer)
    modal = Column(Integer)
    tipo_ctrc_cte = Column(Integer)
    usuario_importacao = Column(String(30))
    data_registro = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Obs(Model):
    __tablename__ = 'scr_conhecimento_obs'
    id_conhecimento_obs = Column(Integer,Sequence('scr_conhecimento_obs_id_conhecimento_obs_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_observacao = Column(Integer)
    observacao = Column(text)
    tipo_fisco = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Obs_Template(Model):
    __tablename__ = 'scr_conhecimento_obs_template'
    id_observacao = Column(Integer,Sequence('scr_conhecimento_obs_template_id_observacao_seq'), primary_key=True)
    observacao = Column(text)
    tipo_fisco = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Ocorrencias_Nf(Model):
    __tablename__ = 'scr_conhecimento_ocorrencias_nf'
    id_conhecimento_ocorrencia_nf = Column(Integer,Sequence('scr_conhecimento_ocorrencias_nf_id_conhecimento_ocorrencia_nf_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_conhecimento_notas_fiscais = Column(Integer)
    id_ocorrencia = Column(Integer)
    data_ocorrencia = Column(Date)
    hora_ocorrencia = Column(String(5))
    incidencia = Column(Integer)
    data_registro = Column(DateTime)
    canhoto = Column(Integer)
    id_ocorrencia_obs = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Redespacho(Model):
    __tablename__ = 'scr_conhecimento_redespacho'
    id_conhecimento_redespacho = Column(Integer,Sequence('scr_conhecimento_redespacho_id_conhecimento_redespacho_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    id_romaneios = Column(Integer)
    id_acerto = Column(Integer)
    tipo_calculo = Column(Integer)
    total_frete = Column(Numeric(12,2))
    programado = Column(Integer)
    valor_entrega = Column(Numeric(12,2))
    valor_reentrega = Column(Numeric(12,2))
    codigo_calculo_status = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Conhecimento_Redespacho_Tmp(Model):
    __tablename__ = 'scr_conhecimento_redespacho_tmp'
    id_conhecimento_redespacho = Column(Integer)
    id_conhecimento = Column(Integer)
    id_romaneios = Column(Integer)
    id_acerto = Column(Integer)
    tipo_calculo = Column(Integer)
    total_frete = Column(Numeric(12,2))
    programado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao(Model):
    __tablename__ = 'scr_cotacao'
    id_cotacao = Column(Integer,Sequence('scr_cotacao_id_cotacao_seq'), primary_key=True)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    numero_ctrc_filial = Column(String(13))
    remetente_id = Column(Integer)
    remetente_cnpj = Column(String(14))
    remetente_nome = Column(String(50))
    remetente_id_endereco = Column(Integer)
    remetente_endereco = Column(String(50))
    remetente_numero = Column(String(10))
    remetente_bairro = Column(String(30))
    remetente_cidade = Column(String(30))
    remetente_uf = Column(String(2))
    remetente_cep = Column(String(8))
    remetente_ie = Column(String(15))
    remetente_ddd = Column(String(2))
    remetente_telefone = Column(String(10))
    destinatario_id = Column(Integer)
    destinatario_cnpj = Column(String(14))
    destinatario_nome = Column(String(50))
    destinatario_id_endereco = Column(Integer)
    destinatario_endereco = Column(String(50))
    destinatario_numero = Column(String(10))
    destinatario_bairro = Column(String(30))
    destinatario_cidade = Column(String(30))
    destinatario_uf = Column(String(2))
    destinatario_cep = Column(String(8))
    destinatario_ie = Column(String(15))
    destinatario_ddd = Column(String(2))
    destinatario_telefone = Column(String(10))
    frete_cif_fob = Column(Integer)
    consig_red = Column(Integer)
    cotacao_origem = Column(String(13))
    data_cotacao_origem = Column(Date)
    consig_red_id = Column(Integer)
    consig_red_cnpj = Column(String(14))
    consig_red_nome = Column(String(50))
    consig_red_id_endereco = Column(Integer)
    consig_red_endereco = Column(String(50))
    consig_red_numero = Column(String(10))
    consig_red_bairro = Column(String(30))
    consig_red_cidade = Column(String(30))
    consig_red_uf = Column(String(2))
    consig_red_cep = Column(String(8))
    consig_red_ie = Column(String(15))
    consig_red_ddd = Column(String(2))
    consig_red_telefone = Column(String(10))
    consig_red_cif_fob = Column(Integer)
    observacoes_coleta = Column(text)
    observacoes_entrega = Column(text)
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    volume_cubico = Column(Numeric(10,3))
    natureza_carga = Column(String(40))
    especie = Column(String(10))
    placa_veiculo = Column(String(10))
    valor_nota_fiscal = Column(Numeric(11,2))
    data_emissao = Column(DateTime)
    frete_peso = Column(Numeric(10,2))
    frete_valor = Column(Numeric(10,2))
    sec_cat = Column(Numeric(10,2))
    despacho = Column(Numeric(10,2))
    gris = Column(Numeric(10,2))
    itr = Column(Numeric(10,2))
    pedagio = Column(Numeric(10,2))
    outros = Column(Numeric(10,2))
    total_frete = Column(Numeric(10,2))
    base_calculo = Column(Numeric(10,2))
    imposto = Column(Numeric(10,2))
    desconto = Column(Numeric(10,2))
    tabele_frete = Column(String(13))
    tipo_imposto = Column(Integer)
    natureza_operacao = Column(String(20))
    cod_operacao_fiscal = Column(String(5))
    observacoes_cotacao = Column(text)
    aliquota = Column(Numeric(5,2))
    imposto_incluso = Column(Integer)
    comprovante_entrega = Column(Integer)
    cancelado = Column(Integer)
    situacao = Column(Integer)
    canhoto = Column(Integer)
    avista = Column(Integer)
    status = Column(Integer)
    data_cotacao = Column(Date)
    data_entrega = Column(Date)
    hora_entrega = Column(String(5))
    data_recebimento_nf = Column(Date)
    data_viagem = Column(DateTime)
    data_nota_fiscal = Column(Date)
    data_previsao_entrega = Column(Date)
    data_cancelamento = Column(DateTime)
    data_digitacao = Column(DateTime)
    tipo_transporte = Column(Integer)
    consig_red_pago_apagar = Column(Integer)
    incidencia = Column(Numeric(8,2))
    calculado_ate_id_cidade = Column(Integer)
    calculado_ate_cidade = Column(String(40))
    calculado_ate_uf = Column(String(2))
    remetente_codigo_pais = Column(String(5))
    remetente_nome_pais = Column(String(50))
    destinatario_codigo_pais = Column(String(5))
    destinatario_nome_pais = Column(String(50))
    consig_red_codigo_pais = Column(String(5))
    consig_red_nome_pais = Column(String(50))
    peso_cubado = Column(Numeric(10,3))
    observacao_entrega = Column(String(30))
    calculado_de_id_cidade = Column(Integer)
    calculado_de_cidade = Column(String(40))
    calculado_de_uf = Column(String(2))
    redespachador_id = Column(Integer)
    redespachador_cnpj = Column(String(14))
    redespachador_nome = Column(String(50))
    redespachador_id_endereco = Column(Integer)
    redespachador_endereco = Column(String(50))
    redespachador_numero = Column(String(10))
    redespachador_bairro = Column(String(30))
    redespachador_cidade = Column(String(30))
    redespachador_uf = Column(String(2))
    redespachador_cep = Column(String(8))
    redespachador_ie = Column(String(15))
    redespachador_ddd = Column(String(2))
    redespachador_telefone = Column(String(10))
    usuario_fatura = Column(String(30))
    redespachador_codigo_pais = Column(String(5))
    redespachador_nome_pais = Column(String(50))
    frete_peso_aereo = Column(Numeric(10,2))
    taxa_coleta = Column(Numeric(10,2))
    taxa_entrega = Column(Numeric(10,2))
    taxa_redespacho = Column(Numeric(10,2))
    taxa_expresso = Column(Numeric(10,2))
    taxa_emergencia = Column(Numeric(10,2))
    taxa_manuseio_embalagem = Column(Numeric(10,2))
    taxa_escolta = Column(Numeric(10,2))
    taxa_outros = Column(Numeric(10,2))
    expresso = Column(Integer)
    emergencia = Column(Integer)
    escolta = Column(Integer)
    escolta_horas_coleta = Column(Integer)
    modal = Column(Integer)
    escolta_horas_entrega = Column(Integer)
    coleta_escolta = Column(Integer)
    coleta_expresso = Column(Integer)
    coleta_emergencia = Column(Integer)
    coleta_normal = Column(Integer)
    entrega_escolta = Column(Integer)
    entrega_expresso = Column(Integer)
    entrega_emergencia = Column(Integer)
    entrega_normal = Column(Integer)
    taxa_dce = Column(Numeric(8,2))
    taxa_exclusivo = Column(Numeric(8,2))
    coleta_dificuldade = Column(Integer)
    entrega_dificuldade = Column(Integer)
    entrega_exclusiva = Column(Integer)
    coleta_exclusiva = Column(Integer)
    desc_taxa_coleta = Column(Numeric(8,2))
    desc_taxa_entrega = Column(Numeric(8,2))
    desc_taxa_redespacho = Column(Numeric(8,2))
    desc_taxa_expresso = Column(Numeric(8,2))
    desc_taxa_emergencia = Column(Numeric(8,2))
    desc_taxa_manuseio = Column(Numeric(8,2))
    desc_taxa_escolta = Column(Numeric(8,2))
    desc_frete_valor_aereo = Column(Numeric(8,2))
    tipo_coleta = Column(Integer)
    cotador = Column(Integer)
    desconto_cotacao = Column(Numeric(8,2))
    arredondamento = Column(Numeric(8,2))
    cotacao_fechada = Column(Integer)
    contato_cotacao = Column(String(50))
    telefone_cotacao = Column(String(12))
    tipo_veiculo = Column(Integer)
    data_validade = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Log_Atividades(Model):
    __tablename__ = 'scr_cotacao_log_atividades'
    id_cotacao = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(String(50))
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Notas_Fiscais(Model):
    __tablename__ = 'scr_cotacao_notas_fiscais'
    id_cotacao_notas_fiscais = Column(Integer,Sequence('scr_cotacao_notas_fiscais_id_cotacao_notas_fiscais_seq'), primary_key=True)
    id_cotacao = Column(Integer)
    data_nota_fiscal = Column(Date)
    numero_nota_fiscal = Column(String(6))
    serie_nota_fiscal = Column(String(3))
    qtd_volumes = Column(Integer)
    peso = Column(Numeric(10,3))
    valor = Column(Numeric(10,2))
    volume_cubico = Column(Numeric(10,4))
    tipo_nota = Column(Integer)
    numero_romaneio_nf = Column(String(15))
    numero_pedido_nf = Column(String(15))
    valor_base_calculo = Column(Numeric(15,2))
    valor_icms_nf = Column(Numeric(15,2))
    valor_base_calculo_icms_st = Column(Numeric(15,2))
    valor_icms_nf_st = Column(Numeric(15,2))
    cfop_pred_nf = Column(String(4))
    valor_total_produtos = Column(Numeric(15,2))
    pin = Column(String(9))
    chave_nfe = Column(String(44))
    canhoto = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Notas_Fiscais_Imp(Model):
    __tablename__ = 'scr_cotacao_notas_fiscais_imp'
    id_cotacao_nota_fiscal_imp = Column(Integer,Sequence('scr_cotacao_notas_fiscais_imp_id_cotacao_nota_fiscal_imp_seq'), primary_key=True)
    numero_cotacao = Column(String(13))
    data_cotacao = Column(Date)
    numero_tabela_frete = Column(String(13))
    cnpj_cliente = Column(String(18))
    cnpj_fornecedor = Column(String(18))
    observacao = Column(String(150))
    status = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Tabela_Frete(Model):
    __tablename__ = 'scr_cotacao_tabela_frete'
    id_cotacao_tabela_frete = Column(Integer,Sequence('scr_cotacao_tabela_frete_id_cotacao_tabela_frete_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    frete_cif_fob = Column(Integer)
    numero_cotacao_tabela_frete = Column(String(13))
    numero_tabela_frete = Column(String(13))
    tipo_operacao = Column(Integer)
    id_lista_cotacao = Column(Integer)
    combinado = Column(Integer)
    cnpj_fornecedor = Column(String(18))
    cnpj_cliente = Column(String(18))
    calculado_de_id_cidade = Column(Integer)
    calculado_ate_id_cidade = Column(Integer)
    natureza_carga = Column(String(30))
    qtd_nf = Column(Integer)
    peso = Column(Numeric(12,3))
    qtd_volumes = Column(Integer)
    valor_cubico = Column(Numeric(12,4))
    valor_nota_fiscal = Column(Numeric(12,2))
    valor_total_produtos = Column(Numeric(12,2))
    total_frete_origem = Column(Numeric(12,2))
    modal = Column(Integer)
    tipo_contribuinte = Column(String(1))
    tipo_imposto = Column(Integer)
    substituicao_tributaria = Column(Integer)
    aliquota = Column(Numeric(12,2))
    perc_desconto = Column(Numeric(12,2))
    isento_imposto = Column(Integer)
    imposto_incluso = Column(Integer)
    escolta_horas_coleta = Column(Integer)
    escolta_horas_entrega = Column(Integer)
    coleta_escolta = Column(Integer)
    coleta_expresso = Column(Integer)
    coleta_emergencia = Column(Integer)
    coleta_normal = Column(Integer)
    entrega_escolta = Column(Integer)
    entrega_expresso = Column(Integer)
    entrega_emergencia = Column(Integer)
    entrega_normal = Column(Integer)
    taxa_dce = Column(Integer)
    taxa_exclusivo = Column(Integer)
    coleta_dificuldade = Column(Integer)
    entrega_dificuldade = Column(Integer)
    entrega_exclusiva = Column(Integer)
    coleta_exclusiva = Column(Integer)
    data_cotacao = Column(Date)
    data_validade = Column(Date)
    total_frete = Column(Numeric(12,2))
    base_calculo = Column(Numeric(12,2))
    total_imposto = Column(Numeric(12,2))
    previsao_entrega = Column(DateTime)
    observacao = Column(text)
    id_cotacao_nota_fiscal_imp = Column(Integer)
    total_entregas = Column(Integer)
    peso_agregado_nf = Column(Numeric(12,4))
    volume_cubico_agregado_nf = Column(Numeric(12,6))
    dt_agenda_coleta = Column(DateTime)
    dt_agenda_entrega = Column(DateTime)
    tipo_transporte = Column(Integer)
    status = Column(Integer)
    data_avaliacao = Column(Date)
    gerar_coleta = Column(Integer)
    perc_reducao_base_calculo = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    contato_nome = Column(String(100))
    contato_fone = Column(String(30))
    contato_email = Column(text)
    id_coleta = Column(Integer)
    id_conhecimento = Column(Integer)
    tipo_cotador = Column(Integer)
    email_analitico = Column(Integer)
    cnpj_cpf_endereco = Column(String(14))
    consumidor_final = Column(Integer)
    base_calculo_difal = Column(Numeric(12,2))
    difal_icms = Column(Numeric(12,2))
    difal_icms_origem = Column(Numeric(12,2))
    difal_icms_destino = Column(Numeric(12,2))
    aliq_icms_interna = Column(Numeric(5,2))
    aliq_icms_inter = Column(Numeric(5,2))
    aliquota_fcp = Column(Numeric(5,2))
    valor_fcp = Column(Numeric(12,2))
    calculo_difal = Column(Integer)
    destinatario_cnpj = Column(String(14))
    pagador_cnpj = Column(String(14))

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Tabela_Frete_Cf(Model):
    __tablename__ = 'scr_cotacao_tabela_frete_cf'
    id_cotacao_tabela_frete_cf = Column(Integer,Sequence('scr_cotacao_tabela_frete_cf_id_cotacao_tabela_frete_cf_seq'), primary_key=True)
    id_cotacao_tabela_frete = Column(Integer)
    id_tipo_calculo = Column(Integer)
    excedente = Column(Integer)
    quantidade = Column(Numeric(16,8))
    valor_item = Column(Numeric(16,8))
    valor_total = Column(Numeric(12,2))
    valor_minimo = Column(Numeric(12,2))
    valor_pagar = Column(Numeric(12,2))
    operacao = Column(String(1))
    id_faixa = Column(Integer)
    combinado = Column(Integer)
    modo_calculo = Column(Integer)
    perc_desconto = Column(Numeric(5,2))
    valor_pagar_sdesconto = Column(Numeric(13,2))
    desconto = Column(Numeric(13,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Cotacao_Tabela_Frete_Log(Model):
    __tablename__ = 'scr_cotacao_tabela_frete_log'
    id_cotacao_tabela_frete_log = Column(Integer,Sequence('scr_cotacao_tabela_frete_log_id_cotacao_tabela_frete_log_seq'), primary_key=True)
    id_cotacao_tabela_frete = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(text)
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Cce(Model):
    __tablename__ = 'scr_cte_cce'
    id_cte_cce = Column(Integer,Sequence('scr_cte_cce_id_cte_cce_seq'), primary_key=True)
    id_conhecimento = Column(Integer)
    data_cce = Column(DateTime)
    numero_recibo = Column(String(15))
    numero_protocolo = Column(String(15))
    dh_reg_evento = Column(DateTime)
    numero_sequencia = Column(Integer)
    cstat_cce = Column(String(3))
    xmotivo_cce = Column(String(150))
    xml_cce_assinado = Column(text)
    xml_proc_cce = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Cce_Itens(Model):
    __tablename__ = 'scr_cte_cce_itens'
    id_cte_cce_itens = Column(Integer,Sequence('scr_cte_cce_itens_id_cte_cce_itens_seq'), primary_key=True)
    id_cte_cce = Column(Integer)
    id_cte_cce_item = Column(Integer)
    valor_corrigido = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Itens_Correcao(Model):
    __tablename__ = 'scr_cte_itens_correcao'
    id_cte_item_correcao = Column(Integer,Sequence('scr_cte_itens_correcao_id_cte_item_correcao_seq'), primary_key=True)
    item_cce_descricao = Column(String(100))
    campo_alterado = Column(String(50))
    grupo = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Lote(Model):
    __tablename__ = 'scr_cte_lote'
    id_lote = Column(Integer,Sequence('scr_cte_lote_id_lote_seq'), primary_key=True)
    numero_lote = Column(Integer)
    data_hora_geracao = Column(DateTime)
    data_hora_trasmissao = Column(DateTime)
    data_hora_cancelamento = Column(DateTime)
    data_hora_correcao = Column(DateTime)
    numero_recibo_1 = Column(String(30))
    numero_recibo_2 = Column(String(30))
    numero_recibo_3 = Column(String(30))
    numero_recibo_4 = Column(String(30))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    recebeu_retorno = Column(Integer)
    cstat = Column(String(3))
    xmotivo = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Lote_Itens(Model):
    __tablename__ = 'scr_cte_lote_itens'
    id_lote_itens = Column(Integer,Sequence('scr_cte_lote_itens_id_lote_itens_seq'), primary_key=True)
    numero_lote = Column(Integer)
    id_conhecimento = Column(Integer)
    xml_cte_original = Column(text)
    xml_cte_com_assinatura = Column(text)
    xml_retorno = Column(text)
    numero_recibo = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Scr_Cte_Parametros(Model):
    __tablename__ = 'scr_cte_parametros'
    id_cte_parametro = Column(Integer,Sequence('scr_cte_parametros_id_cte_parametro_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    certificado = Column(text)
    cte_versao = Column(String(4))
    sigla_ws = Column(String(6))
    sigla_uf = Column(String(2))
    cte_modelo = Column(String(3))
    cte_serie = Column(String(3))
    cte_ambiente = Column(Integer)
    cte_proxy = Column(String(50))
    cte_usuario_proxy = Column(String(30))
    cte_senha_proxy = Column(String(15))
    cte_licenca = Column(text)
    cte_tipo_emissao = Column(Integer)
    cert_data_inicio = Column(DateTime)
    cert_data_final = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Despesas_Viagem(Model):
    __tablename__ = 'scr_despesas_viagem'
    id_despesa = Column(Integer,Sequence('scr_despesas_viagem_id_despesa_seq'), primary_key=True)
    descricao_despesa = Column(String(50))
    cc_frota_propria = Column(Integer)
    cc_frota_terceiro = Column(Integer)
    tipo_controle = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Doc_Anulado(Model):
    __tablename__ = 'scr_doc_anulado'
    id_anulacao = Column(Integer,Sequence('scr_doc_anulado_id_anulacao_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    tipo_documento = Column(Integer)
    numero_documento = Column(Integer)
    serie = Column(Integer)
    cstat = Column(String(3))
    xmotivo = Column(String(200))
    xml_proc_anulacao = Column(text)
    data_hora = Column(DateTime)
    usuario = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Scr_Doc_Integracao(Model):
    __tablename__ = 'scr_doc_integracao'
    id_doc_integracao = Column(Integer,Sequence('scr_doc_integracao_id_doc_integracao_seq'), primary_key=True)
    doc_xml = Column(text)
    tipo_doc = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    data_recebimento = Column(DateTime)
    chave_doc = Column(String(44))
    id_uid_imap = Column(Integer)
    entrou_repetida = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Doc_Integracao_Nfe(Model):
    __tablename__ = 'scr_doc_integracao_nfe'
    id = Column(Integer,Sequence('scr_doc_integracao_nfe_id_seq'), primary_key=True)
    id_doc_integracao = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)
    chave_doc = Column(String(44))
    data_registro = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Docs_Digitalizados(Model):
    __tablename__ = 'scr_docs_digitalizados'
    id = Column(Integer,Sequence('scr_docs_digitalizados_id_seq'), primary_key=True)
    tipo_doc = Column(Integer)
    data_registro = Column(DateTime)
    link_img = Column(text)
    id_conhecimento = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)
    id_conhecimento_notas_fiscais = Column(Integer)
    id_ocorrencia_nota_fiscal_imp = Column(Integer)
    id_ocorrencia_nota_fiscal = Column(Integer)
    tipo_url = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Docs_Notrexo(Model):
    __tablename__ = 'scr_docs_notrexo'
    id = Column(Integer,Sequence('scr_docs_notrexo_id_seq'), primary_key=True)
    id_notrecho = Column(Integer)
    chave = Column(String(44))
    data_hora_inclusao = Column(DateTime)
    data_inclusao = Column(DateTime)
    cuf = Column(Integer)
    uf = Column(String(2))
    email = Column(String(200))
    ano_emissao = Column(Integer)
    mes_emissao = Column(Integer)
    emissor = Column(String(14))
    modelo_documento = Column(String(2))
    tipo_modelo_documento = Column(String(5))
    serie_documento = Column(String(3))
    motorista = Column(String(11))
    data_execucao = Column(DateTime)
    tipo_status_id = Column(Integer)
    recebedor = Column(String(150))
    observacao = Column(String(250))
    latitude = Column(Float)
    longitude = Column(Float)
    path_file = Column(text)
    is_sync = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)
    id_conhecimento_nota_fiscal_imp = Column(Integer)
    id_conhecimento = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Docs_Notrexo_Controle(Model):
    __tablename__ = 'scr_docs_notrexo_controle'
    id = Column(Integer,Sequence('scr_docs_notrexo_controle_id_seq'), primary_key=True)
    id_ultimo_notrexo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Docs_Notrexo_Status(Model):
    __tablename__ = 'scr_docs_notrexo_status'
    id = Column(Integer,Sequence('scr_docs_notrexo_status_id_seq'), primary_key=True)
    nome = Column(text)
    habilitado = Column(Integer)
    tipo = Column(Integer)
    id_ocorrencia_softlog = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Faturamento(Model):
    __tablename__ = 'scr_faturamento'
    id_faturamento = Column(Integer,Sequence('scr_faturamento_id_faturamento_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    numero_fatura = Column(String(13))
    status = Column(Integer)
    numero_boleto = Column(String(16))
    digito_boleto = Column(String(2))
    fatura_sacado_id = Column(Integer)
    fatura_cnpj = Column(String(14))
    fatura_nome = Column(String(50))
    fatura_id_endereco = Column(Integer)
    fatura_endereco = Column(String(50))
    fatura_numero = Column(String(10))
    fatura_bairro = Column(String(30))
    fatura_cidade = Column(String(30))
    fatura_uf = Column(String(2))
    fatura_cep = Column(String(8))
    fatura_ie = Column(String(15))
    fatura_ddd = Column(String(3))
    fatura_telefone = Column(String(10))
    fatura_email = Column(String(150))
    fatura_banco = Column(String(3))
    fatura_agencia = Column(String(10))
    fatura_conta_corrente = Column(String(16))
    tipo_imposto = Column(Integer)
    valor_fatura = Column(Numeric(12,2))
    valor_total = Column(Numeric(12,2))
    valor_pago = Column(Numeric(12,2))
    imposto = Column(Numeric(12,2))
    perc_desconto = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    perc_juros = Column(Numeric(12,2))
    juros = Column(Numeric(12,2))
    abatimento = Column(Numeric(12,2))
    tarifa = Column(Numeric(12,2))
    multa = Column(Numeric(12,2))
    valor_inss = Column(Numeric(12,2))
    data_processamento = Column(DateTime)
    data_fechamento = Column(Date)
    data_emissao = Column(Date)
    data_vencimento = Column(Date)
    data_pagamento = Column(Date)
    data_lim_desconto = Column(Date)
    data_cancelamento = Column(Date)
    motivo_cancelamento = Column(String(100))
    qtde_ctrc = Column(Integer)
    obs = Column(text)
    id_vendedor = Column(Integer)
    protesto = Column(Integer)
    atraso = Column(Integer)
    id_cobrador = Column(Integer)
    prazo_desconto = Column(Integer)
    prazo_protesto = Column(Integer)
    id_remessa = Column(Integer)
    acrescimos = Column(Numeric(12,2))
    valor_recebido = Column(Numeric(12,2))
    data_remessa = Column(DateTime)
    perc_multa = Column(Numeric(5,2))
    acrescimo = Column(Numeric(12,2))
    portador = Column(Integer)
    valor_adicional = Column(Numeric(12,2))
    valor_total_ctrc = Column(Numeric(12,2))
    valor_total_servicos = Column(Numeric(12,2))
    qtde_servicos = Column(Integer)
    inconsistencia = Column(Integer)
    obs_inconsistencia = Column(String(30))
    valor_total_minutas = Column(Numeric(12,2))
    qtde_minutas = Column(Integer)
    id_conta_corrente = Column(Integer)
    id_caixa = Column(Integer)
    id_usuario_operacao = Column(Integer)
    tabela_credito_sistema = Column(String(25))
    numero_lancamento = Column(Integer)
    conta_credito = Column(Integer)
    especie_pagamento = Column(Integer)
    numero_doc_pagamento = Column(String(10))
    data_cheque = Column(Date)
    baixa_automatica = Column(Integer)
    arquivo_retorno = Column(Integer)
    data_credito = Column(Date)
    ultimo_aviso = Column(Date)
    posicao_aviso = Column(Integer)
    nr_nfs = Column(Integer)
    bloqueia_servico = Column(Integer)
    envia_notificacao = Column(Integer)
    imprimiu_fatura = Column(Integer)
    imprimiu_boleto = Column(Integer)
    perc_juros_parc = Column(Numeric(5,2))
    vl_juros_parc = Column(Numeric(12,2))
    vl_entrada = Column(Numeric(12,2))
    dt_parcelamento = Column(Date)
    vl_parcelas_pagas = Column(Numeric(12,2))
    qt_parcelas_pagas = Column(Numeric(12,2))
    tipo_fatura = Column(Integer)
    id_faturamento_principal = Column(Integer)
    qtd_parcelas = Column(Integer)
    periodicidade = Column(Integer)
    valor_a_parcelar = Column(Numeric(12,2))
    num_parcela = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Faturamento_Contato(Model):
    __tablename__ = 'scr_faturamento_contato'
    id_faturamento_contato = Column(Integer,Sequence('scr_faturamento_contato_id_faturamento_contato_seq'), primary_key=True)
    id_faturamento = Column(Integer)
    data_contato = Column(Date)
    contato = Column(String(50))
    telefone = Column(String(13))
    usuario = Column(String(30))
    previsao_pagto = Column(Date)
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Faturamento_Log_Atividades(Model):
    __tablename__ = 'scr_faturamento_log_atividades'
    id_faturamento_log_atividade = Column(Integer,Sequence('scr_faturamento_log_atividades_id_faturamento_log_atividade_seq'), primary_key=True)
    id_faturamento = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(String(100))
    historico = Column(text)
    usuario = Column(String(30))
    id_retorno = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Faturamento_Ocorrencias(Model):
    __tablename__ = 'scr_faturamento_ocorrencias'
    id_faturamento_ocorrencia = Column(Integer,Sequence('scr_faturamento_ocorrencias_id_faturamento_ocorrencia_seq'), primary_key=True)
    id_faturamento = Column(Integer)
    codigo_ocorrencia = Column(String(6))
    codigo_motivo = Column(String(10))
    ocorrencia = Column(String(254))
    data = Column(Date)
    id_arquivo = Column(Integer)
    usuario = Column(String(30))
    id_log_retorno_banco = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Filiais_Comissoes(Model):
    __tablename__ = 'scr_filiais_comissoes'
    id_filial_comissao = Column(Integer,Sequence('scr_filiais_comissoes_id_filial_comissao_seq'), primary_key=True)
    id_filial = Column(Integer)
    id_tipo_comissao = Column(Integer)
    descontar_impostos = Column(Integer)
    perc_comissao = Column(Numeric(6,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Filiais_Tipo_Comissao(Model):
    __tablename__ = 'scr_filiais_tipo_comissao'
    id_tipo_comissao = Column(Integer,Sequence('scr_filiais_tipo_comissao_id_tipo_comissao_seq'), primary_key=True)
    descricao = Column(String(50))
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Formularios_Cancelados(Model):
    __tablename__ = 'scr_formularios_cancelados'
    id_formulario_cancelado = Column(Integer,Sequence('scr_formularios_cancelados_id_formulario_cancelado_seq'), primary_key=True)
    numero_formulario = Column(String(6))
    motivo_cancelamento = Column(text)
    data_cancelamento = Column(DateTime)
    id_usuario = Column(Integer)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    tipo_formulario = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Itens_Correcao(Model):
    __tablename__ = 'scr_itens_correcao'
    id_itens_correcao = Column(Integer,Sequence('scr_itens_correcao_id_itens_correcao_seq'), primary_key=True)
    item = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Log_Ocorrencias_Imp(Model):
    __tablename__ = 'scr_log_ocorrencias_imp'
    id_log_ocorrencia_imp = Column(Integer,Sequence('scr_log_ocorrencias_imp_id_log_ocorrencia_imp_seq'), primary_key=True)
    id_nota_fiscal_imp = Column(Integer)
    codigo_ocorrencia = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Scr_Log_Valores_Tabelas_Frete(Model):
    __tablename__ = 'scr_log_valores_tabelas_frete'
    id_log_valores_tabelas_frete = Column(Integer)
    nome_tabela = Column(String(250))
    nome_campo = Column(String(250))
    id_registro = Column(Integer)
    data_alteracao = Column(DateTime)
    valor_antigo = Column(Numeric(12,2))
    valor_novo = Column(Numeric(12,2))
    id_log_atividades = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto(Model):
    __tablename__ = 'scr_manifesto'
    id_manifesto = Column(Integer,Sequence('scr_manifesto_id_manifesto_seq'), primary_key=True)
    filial_manifesto = Column(String(3))
    empresa_manifesto = Column(String(3))
    numero_manifesto = Column(String(13))
    tipo_manifesto = Column(Integer)
    data_emissao = Column(DateTime)
    data_viagem = Column(DateTime)
    data_chegada = Column(DateTime)
    placa_veiculo = Column(String(8))
    placa_carreta = Column(String(8))
    capacidade_kg = Column(Numeric(8,2))
    capacidade_m3 = Column(Numeric(8,3))
    id_motorista = Column(Integer)
    id_proprietario = Column(Integer)
    qtde_ctrc = Column(Numeric(10,0))
    qtde_volume = Column(Numeric(10,3))
    limite_valor_nf = Column(Numeric(10,2))
    valor_total_nf = Column(Numeric(10,2))
    total_frete = Column(Numeric(10,2))
    frete_pago_terceiro = Column(Numeric(10,2))
    peso_pago = Column(Numeric(10,2))
    peso_calculado = Column(Numeric(10,2))
    cubagem_calculada = Column(Numeric(10,3))
    id_cidade_origem = Column(Integer)
    id_cidade_destino = Column(Integer)
    total_km_percurso = Column(Numeric(10,2))
    averbar = Column(Integer)
    numero_averbacao = Column(String(10))
    consulta_averbacao = Column(String(10))
    lacre = Column(String(30))
    observacao = Column(text)
    cpf_motorista = Column(String(14))
    cnpj_cpf_proprietario = Column(String(14))
    frete_terceirizado = Column(Integer)
    id_carta_frete = Column(Integer)
    data_registro = Column(DateTime)
    status = Column(Integer)
    ocorrencia = Column(String(50))
    arrumador = Column(String(50))
    conferente = Column(String(50))
    placa_carreta2 = Column(String(8))
    frete_adiantamento_terceiro = Column(Numeric(10,2))
    unidade_origem = Column(String(3))
    unidade_destino = Column(String(3))
    tipo_mdfe = Column(Integer)
    chave_mdfe = Column(String(44))
    chave_mdfe_dv = Column(String(1))
    codigo_mdfe = Column(String(9))
    serie_mdfe = Column(String(3))
    cstat = Column(String(3))
    xmotivo = Column(text)
    prot_autorizacao_mdfe = Column(String(15))
    xml_proc_mdfe = Column(text)
    protocolo_cancelamento = Column(String(15))
    xml_proc_cancelamento = Column(text)
    tipo_destino = Column(String(1))
    xml_proc_encerramento = Column(text)
    protocolo_encerramento = Column(text)
    data_encerramento = Column(DateTime)
    data_cancelamento = Column(DateTime)
    flg_viagem = Column(Integer)
    data_hora_transmissao = Column(DateTime)
    numero_recibo_1 = Column(String(30))
    xml_mdfe_com_assinatura = Column(text)
    odometro_inicial = Column(Numeric(10,1))
    odometro_final = Column(Numeric(10,1))
    horimetro_inicial = Column(Numeric(9,2))
    horimetro_final = Column(Numeric(9,2))
    placas_engates = Column(String(60))
    qtde_nfe = Column(Integer)
    tipo_emitente = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Averbacao(Model):
    __tablename__ = 'scr_manifesto_averbacao'
    id = Column(Integer,Sequence('scr_manifesto_averbacao_id_seq'), primary_key=True)
    id_manifesto = Column(Integer)
    id_seguradora = Column(Integer)
    averbado = Column(Integer)
    cancelado = Column(Integer)
    encerrado = Column(Integer)
    data_chancela = Column(DateTime)
    data_cancelamento = Column(DateTime)
    data_encerramento = Column(DateTime)
    protocolo = Column(String(60))
    data_registro = Column(DateTime)
    data_registro_encerramento = Column(DateTime)
    tem_erro = Column(Integer)
    data_processamento_chancela = Column(DateTime)
    data_processamento_cancelamento = Column(DateTime)
    data_processamento_encerramento = Column(DateTime)
    reenvia = Column(Integer)
    chancelou = Column(Integer)
    cancelou = Column(Integer)
    encerrrou = Column(Integer)
    id_processamento_chancela = Column(Integer)
    id_processamento_cancelamento = Column(Integer)
    id_processamento_encerramento = Column(Integer)
    id_acesso_servico = Column(Integer)
    numero_averbacao = Column(String(50))
    retorno_averbacao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Averbacao_Erros(Model):
    __tablename__ = 'scr_manifesto_averbacao_erros'
    id = Column(Integer,Sequence('scr_manifesto_averbacao_erros_id_seq'), primary_key=True)
    manifesto_averbacao_id = Column(Integer)
    codigo_erro = Column(String(5))
    descricao_erro = Column(String(100))
    valor_esperado = Column(String(70))
    valor_informado = Column(String(70))
    id_processamento = Column(Integer)
    data_registro = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Comissoes(Model):
    __tablename__ = 'scr_manifesto_comissoes'
    id_manifesto_comissoes = Column(Integer,Sequence('scr_manifesto_comissoes_id_manifesto_comissoes_seq'), primary_key=True)
    tipo_manifesto = Column(Integer)
    id_tipo_comissao_origem = Column(Integer)
    id_tipo_comissao_destino = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Despesas_Viagem(Model):
    __tablename__ = 'scr_manifesto_despesas_viagem'
    id_despesa_manifesto = Column(Integer,Sequence('scr_manifesto_despesas_viagem_id_despesa_manifesto_seq'), primary_key=True)
    id_manifesto = Column(Integer)
    data_despesa = Column(Date)
    id_despesa = Column(Integer)
    valor_despesa = Column(Numeric(8,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Docs(Model):
    __tablename__ = 'scr_manifesto_docs'
    id_manifesto_docs = Column(Integer,Sequence('scr_manifesto_docs_id_manifesto_docs_seq'), primary_key=True)
    id_manifesto = Column(Integer)
    tipo_documento = Column(Integer)
    chave_documento = Column(String(44))
    peso = Column(Numeric(12,2))
    qt_volumes = Column(Integer)
    valor = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Log_Atividades(Model):
    __tablename__ = 'scr_manifesto_log_atividades'
    data_hora = Column(DateTime)
    atividade_executada = Column(String(50))
    usuario = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Tipo(Model):
    __tablename__ = 'scr_manifesto_tipo'
    id_tipo_manifesto = Column(Integer,Sequence('scr_manifesto_tipo_id_tipo_manifesto_seq'), primary_key=True)
    descricao = Column(String(50))
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Manifesto_Uf_Percurso(Model):
    __tablename__ = 'scr_manifesto_uf_percurso'
    id_manifesto_uf_percurso_id = Column(Integer,Sequence('scr_manifesto_uf_percurso_id_manifesto_uf_percurso_id_seq'), primary_key=True)
    id_manifesto = Column(Integer)
    id_estado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Mdfe_Lote(Model):
    __tablename__ = 'scr_mdfe_lote'
    id_lote = Column(Integer,Sequence('scr_mdfe_lote_id_lote_seq'), primary_key=True)
    numero_lote = Column(Integer)
    data_hora_geracao = Column(DateTime)
    data_hora_trasmissao = Column(DateTime)
    data_hora_cancelamento = Column(DateTime)
    data_hora_correcao = Column(DateTime)
    numero_recibo_1 = Column(String(30))
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    recebeu_retorno = Column(Integer)
    cstat = Column(String(3))
    xmotivo = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Scr_Mdfe_Lote_Itens(Model):
    __tablename__ = 'scr_mdfe_lote_itens'
    id_mdfe_lote_itens = Column(Integer,Sequence('scr_mdfe_lote_itens_id_mdfe_lote_itens_seq'), primary_key=True)
    numero_lote = Column(Integer)
    id_manifesto = Column(Integer)
    xml_mdfe_original = Column(text)
    xml_mdfe_com_assinatura = Column(text)
    xml_retorno = Column(text)
    numero_recibo = Column(String(30))
    xml_mdfe_lote = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Mdfe_Parametros(Model):
    __tablename__ = 'scr_mdfe_parametros'
    id_mdfe_parametro = Column(Integer,Sequence('scr_mdfe_parametros_id_mdfe_parametro_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    certificado = Column(text)
    mdfe_versao = Column(String(4))
    sigla_ws = Column(String(6))
    sigla_uf = Column(String(2))
    mdfe_modelo = Column(String(3))
    mdfe_serie = Column(String(3))
    mdfe_ambiente = Column(Integer)
    mdfe_proxy = Column(String(50))
    mdfe_usuario_proxy = Column(String(30))
    mdfe_senha_proxy = Column(String(15))
    mdfe_licenca = Column(text)
    mdfe_tipo_emissao = Column(Integer)
    cert_data_inicio = Column(DateTime)
    cert_data_final = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Natureza_Carga(Model):
    __tablename__ = 'scr_natureza_carga'
    id_natureza_carga = Column(Integer,Sequence('scr_natureza_carga_id_natureza_carga_seq'), primary_key=True)
    natureza_carga = Column(String(40))
    categoria = Column(String(4))
    isento_iss = Column(Integer)
    isento_icms = Column(Integer)
    cod_tarifa_rodoviario = Column(String(4))
    cod_tarifa_aereo = Column(String(4))
    perc_red_bc = Column(Numeric(5,2))
    densidade = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Natureza_Prestacao(Model):
    __tablename__ = 'scr_natureza_prestacao'
    id_natureza_prestacao = Column(Integer,Sequence('scr_natureza_prestacao_id_natureza_prestacao_seq'), primary_key=True)
    cfop = Column(String(5))
    descricao_natureza = Column(String(40))
    classificacao_fiscal = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Scr_Nf_Protocolo(Model):
    __tablename__ = 'scr_nf_protocolo'
    id_nf_protocolo = Column(Integer,Sequence('scr_nf_protocolo_id_nf_protocolo_seq'), primary_key=True)
    data_protocolo = Column(DateTime)
    data_conferencia = Column(DateTime)
    usuario_protocolo = Column(Integer)
    usuario_conferencia = Column(Integer)
    status = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Nf_Protocolo_Nf(Model):
    __tablename__ = 'scr_nf_protocolo_nf'
    id_nf_protocolo_nf = Column(Integer,Sequence('scr_nf_protocolo_nf_id_nf_protocolo_nf_seq'), primary_key=True)
    id_nf_protocolo = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Nf_Protocolo_Setor(Model):
    __tablename__ = 'scr_nf_protocolo_setor'
    id_nf_protocolo_setor = Column(Integer,Sequence('scr_nf_protocolo_setor_id_nf_protocolo_setor_seq'), primary_key=True)
    id_nf_protocolo = Column(Integer)
    id_setor = Column(Integer)
    qtd_volumes = Column(Integer)
    qtd_conferencia = Column(Integer)
    id_usuario_conferencia = Column(Integer)
    data_conferencia = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Nfe_Rastreamentos(Model):
    __tablename__ = 'scr_nfe_rastreamentos'
    id = Column(Integer,Sequence('scr_nfe_rastreamentos_id_seq'), primary_key=True)
    chave = Column(text)
    ident_sistema = Column(Integer)
    data_registro = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_A_Imp(Model):
    __tablename__ = 'scr_notas_fiscais_a_imp'
    id_nfe = Column(Integer,Sequence('scr_notas_fiscais_a_imp_id_nfe_seq'), primary_key=True)
    chave_nfe = Column(String(44))
    data_registro = Column(DateTime)
    usuario = Column(String(50))
    id_romaneio = Column(Integer)
    importado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Imp(Model):
    __tablename__ = 'scr_notas_fiscais_imp'
    id_nota_fiscal_imp = Column(Integer,Sequence('scr_notas_fiscais_imp_id_nota_fiscal_imp_seq'), primary_key=True)
    selecionado = Column(Integer)
    id_conhecimento = Column(Integer)
    id_cotacao_frete = Column(Integer)
    tipo_operacao = Column(Integer)
    tipo_documento = Column(Integer)
    modal = Column(Integer)
    tipo_ctrc_cte = Column(Integer)
    tipo_transporte = Column(Integer)
    serie_cte = Column(Integer)
    especie = Column(String(30))
    natureza_carga = Column(String(40))
    status = Column(Integer)
    id_agrupador = Column(Integer)
    nao_agrupa = Column(Integer)
    empresa_emitente = Column(String(3))
    filial_emitente = Column(String(3))
    frete_cif_fob = Column(Integer)
    remetente_id = Column(Integer)
    calculado_de_id_cidade = Column(Integer)
    destinatario_id = Column(Integer)
    calculado_ate_id_cidade = Column(Integer)
    consignatario_id = Column(Integer)
    classificacao_fiscal = Column(String(15))
    redespachador_id = Column(Integer)
    avista = Column(Integer)
    tipo_imposto = Column(Integer)
    aliquota = Column(Numeric(5,2))
    aliquota_st = Column(Numeric(5,2))
    perc_base_calculo = Column(Numeric(12,2))
    perc_base_calculo_st = Column(Numeric(12,2))
    imposto_incluso = Column(Integer)
    placa_veiculo = Column(String(8))
    placa_carreta1 = Column(String(8))
    placa_carreta2 = Column(String(8))
    id_motorista = Column(Integer)
    numero_tabela_frete = Column(String(13))
    cfop = Column(String(5))
    natureza_operacao = Column(String(20))
    data_emissao = Column(Date)
    data_registro = Column(DateTime)
    numero_nota_fiscal = Column(String(9))
    modelo_nf = Column(Integer)
    serie_nota_fiscal = Column(String(3))
    qtd_volumes = Column(Integer)
    usa_valor_presumido = Column(Integer)
    peso = Column(Numeric(20,4))
    peso_presumido = Column(Numeric(12,4))
    valor = Column(Numeric(10,2))
    volume_cubico = Column(Numeric(10,4))
    volume_presumido = Column(Numeric(12,4))
    tipo_nota = Column(Integer)
    numero_pedido_nf = Column(String(15))
    valor_base_calculo = Column(Numeric(15,2))
    valor_icms_nf = Column(Numeric(15,2))
    valor_base_calculo_icms_st = Column(Numeric(15,2))
    valor_icms_nf_st = Column(Numeric(15,2))
    cfop_pred_nf = Column(String(4))
    valor_total_produtos = Column(Numeric(15,2))
    pin = Column(String(9))
    chave_nfe = Column(String(44))
    chave_cte = Column(String(44))
    numero_doc_referenciado = Column(String(13))
    viagem_automatica = Column(Integer)
    pendencia = Column(Integer)
    pendencia_valores = Column(Integer)
    pendencia_rota = Column(Integer)
    pendencia_responsavel = Column(Integer)
    pendencia_tabela = Column(Integer)
    pendencia_emissao = Column(Integer)
    pendencia_tributacao = Column(Integer)
    pendencia_viagem = Column(Integer)
    id_usuario = Column(Integer)
    coleta_escolta = Column(Integer)
    coleta_expresso = Column(Integer)
    coleta_emergencia = Column(Integer)
    coleta_normal = Column(Integer)
    entrega_escolta = Column(Integer)
    entrega_expresso = Column(Integer)
    entrega_emergencia = Column(Integer)
    entrega_normal = Column(Integer)
    taxa_dce = Column(Integer)
    taxa_exclusivo = Column(Integer)
    coleta_dificuldade = Column(Integer)
    entrega_dificuldade = Column(Integer)
    entrega_exclusiva = Column(Integer)
    coleta_exclusiva = Column(Integer)
    id_romaneio = Column(Integer)
    id_ocorrencia = Column(Integer)
    id_ocorrencia_obs = Column(Integer)
    canhoto = Column(Integer)
    data_ocorrencia = Column(DateTime)
    entrega_realizada = Column(Integer)
    obs_ocorrencia = Column(text)
    nome_recebedor = Column(String(50))
    cpf_recebedor = Column(String(11))
    data_expedicao = Column(Date)
    total_entregas = Column(Integer)
    peso_agregado_nf = Column(Numeric(12,4))
    volume_cubico_agregado_nf = Column(Numeric(12,6))
    dt_agenda_coleta = Column(DateTime)
    dt_agenda_entrega = Column(DateTime)
    regime_especial_mg = Column(Integer)
    id_conhecimento_principal = Column(Integer)
    data_cte_re = Column(Date)
    cod_interno_frete = Column(String(13))
    id_protocolo_dev = Column(Integer)
    id_tipo_veiculo = Column(Integer)
    vl_combinado = Column(Numeric(12,2))
    vl_tonelada = Column(Numeric(12,8))
    vl_percentual_nf = Column(Numeric(12,8))
    especie_mercadoria = Column(String(30))
    peso_liquido = Column(Numeric(20,4))
    codigo_vendedor = Column(String(10))
    data_previsao_entrega = Column(Date)
    codigo_nota = Column(text)
    id_pre_fatura_entrega = Column(Integer)
    vl_frete_peso = Column(Numeric(12,2))
    consumidor_final = Column(Integer)
    base_calculo_difal = Column(Numeric(12,2))
    difal_icms = Column(Numeric(12,2))
    difal_icms_origem = Column(Numeric(12,2))
    difal_icms_destino = Column(Numeric(12,2))
    aliq_icms_interna = Column(Numeric(5,2))
    aliq_icms_inter = Column(Numeric(5,2))
    aliquota_fcp = Column(Numeric(5,2))
    valor_fcp = Column(Numeric(12,2))
    calculo_difal = Column(Integer)
    obs = Column(text)
    tipo_carga = Column(Integer)
    inverter_rem_dest = Column(Integer)
    placa_coleta = Column(String(8))
    tabela_redespacho = Column(String(13))
    id_cidade_origem_redespacho = Column(Integer)
    id_romaneio_parceiro = Column(Integer)
    id_nota_fiscal_parceiro = Column(Integer)
    id_conhecimento_parceiro = Column(Integer)
    id_romaneio_redespachador = Column(Integer)
    id_nota_fiscal_redespachador = Column(Integer)
    id_conhecimento_redespachador = Column(Integer)
    valor_combinado_re = Column(Numeric(12,2))
    valor_combinado_minuta_re = Column(Numeric(12,2))
    vl_frete_nota = Column(Numeric(12,2))
    logistica_reversa = Column(Integer)
    id_ocorrencia_reversa = Column(Integer)
    qtd_devolvida = Column(Integer)
    limite_minimo_re = Column(Integer)
    flg_calculo_frete = Column(Integer)
    id_minuta_re = Column(Integer)
    data_emissao_hr = Column(DateTime)
    id_transportador_nfe = Column(Integer)
    sap_docentry = Column(Integer)
    sap_serial = Column(Integer)
    sap_tipoobjeto = Column(Integer)
    sap_supervisor = Column(String(50))
    digitalizado = Column(Integer)
    codigo_softlog_parceiro = Column(Integer)
    codigo_integracao = Column(Integer)
    id_conhecimento_notas_fiscais_parceiro = Column(Integer)
    expedidor_cnpj = Column(String(16))
    peso_transportado = Column(Numeric(12,4))
    flg_viagem_automatica = Column(Integer)
    data_viagem = Column(Date)
    odometro_inicial = Column(Integer)
    total_frete_origem = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Imp_Anexos(Model):
    __tablename__ = 'scr_notas_fiscais_imp_anexos'
    id_nota_fiscal_anexo = Column(Integer,Sequence('scr_notas_fiscais_imp_anexos_id_nota_fiscal_anexo_seq'), primary_key=True)
    id_nota_fiscal_imp = Column(Integer)
    tipo_anexo = Column(Integer)
    data_anexo = Column(Date)
    usuario_anexo = Column(String(30))
    descricao_anexo = Column(String(100))
    conteudo_anexo = Column(text)
    nome_anexo = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Imp_Log_Atividades(Model):
    __tablename__ = 'scr_notas_fiscais_imp_log_atividades'
    id_nota_fiscal_imp_log_atividade = Column(Integer,Sequence('scr_notas_fiscais_imp_log_atividades_id_nota_fiscal_imp_log_atividade_seq'), primary_key=True)
    id_nota_fiscal_imp = Column(Integer)
    data_hora = Column(DateTime)
    atividade_executada = Column(String(50))
    usuario = Column(String(30))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Imp_Ocorrencias(Model):
    __tablename__ = 'scr_notas_fiscais_imp_ocorrencias'
    id_ocorrencia_nf = Column(Integer,Sequence('scr_notas_fiscais_imp_ocorrencias_id_ocorrencia_nf_seq'), primary_key=True)
    id_nota_fiscal_imp = Column(Integer)
    id_ocorrencia = Column(Integer)
    data_ocorrencia = Column(DateTime)
    data_registro = Column(DateTime)
    canhoto = Column(Integer)
    sequencia = Column(Integer)
    obs_ocorrencia = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Nao_Imp(Model):
    __tablename__ = 'scr_notas_fiscais_nao_imp'
    id = Column(Integer,Sequence('scr_notas_fiscais_nao_imp_id_seq'), primary_key=True)
    dados_parametros = Column(text)
    numero_nota_fiscal = Column(String(9))
    serie_nota_fiscal = Column(String(3))
    remetente_id = Column(Integer)
    observacao = Column(text)
    data_registro = Column(DateTime)
    importada = Column(Integer)
    usuario = Column(String(50))
    data_importacao = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Scr_Notas_Fiscais_Segmento(Model):
    __tablename__ = 'scr_notas_fiscais_segmento'
    id = Column(Integer,Sequence('scr_notas_fiscais_segmento_id_seq'), primary_key=True)
    codigo_cliente = Column(Integer)
    codigo_segmento = Column(text)
    segmento = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Ocorrencia_Edi(Model):
    __tablename__ = 'scr_ocorrencia_edi'
    id_scr_ocorrencia_edi = Column(Integer,Sequence('scr_ocorrencia_edi_id_scr_ocorrencia_edi_seq'), primary_key=True)
    codigo_edi = Column(Integer)
    ocorrencia = Column(String(150))
    tipo_edi = Column(String(10))
    pendencia = Column(Integer)
    gera_acerto = Column(Integer)
    status_ctrc = Column(Integer)
    gera_notificacao = Column(Integer)
    ocorrencia_coleta = Column(Integer)
    publica = Column(Integer)
    gera_reentrega = Column(Integer)
    gera_devolucao = Column(Integer)
    id_ocorrencia_proceda = Column(Integer)
    aplicativo_mobile = Column(Integer)
    aplicativo_sconferencia = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Ocorrencia_Obs_Edi(Model):
    __tablename__ = 'scr_ocorrencia_obs_edi'
    id_scr_ocorrencia_obs_edi = Column(Integer,Sequence('scr_ocorrencia_obs_edi_id_scr_ocorrencia_obs_edi_seq'), primary_key=True)
    codigo_edi_obs = Column(Integer)
    ocorrencia_obs = Column(String(100))
    tipo_edi = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Scr_Ocorrencias_Imp(Model):
    __tablename__ = 'scr_ocorrencias_imp'
    codigo_ocorrencia = Column(String(3),Sequence('scr_ocorrencias_imp_codigo_ocorrencia_seq'), primary_key=True)
    ocorrencia = Column(text)
    pendencia_conhecimento = Column(Integer)
    pendencia_manifesto = Column(Integer)
    pendencia_romaneio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Ocorrencias_Proceda(Model):
    __tablename__ = 'scr_ocorrencias_proceda'
    id = Column(Integer,Sequence('scr_ocorrencias_proceda_id_seq'), primary_key=True)
    ocorrencia = Column(String(250))

    def __repr__(self):
        return self.__tablename__



class Scr_Pre_Fatura_Entregas(Model):
    __tablename__ = 'scr_pre_fatura_entregas'
    id_pre_fatura_entrega = Column(Integer,Sequence('scr_pre_fatura_entregas_id_pre_fatura_entrega_seq'), primary_key=True)
    id_pre_fatura = Column(Integer)
    id_origem = Column(Integer)
    id_destino = Column(Integer)
    vl_veiculo_ref = Column(Numeric(20,4))
    peso_total = Column(Numeric(20,8))
    peso_faixa = Column(Numeric(20,8))
    peso_excedente = Column(Numeric(20,8))
    valor_variavel = Column(Numeric(20,8))
    valor_variavel_excedente = Column(Numeric(20,8))
    ind_perc_rateio = Column(Numeric(20,8))
    volume_cubico_total = Column(Numeric(20,8))
    frete_peso_faixa = Column(Numeric(12,2))
    frete_peso_excedente = Column(Numeric(12,2))
    frete_peso_total = Column(Numeric(15,2))
    densidade = Column(Integer)
    msg = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Pre_Faturas(Model):
    __tablename__ = 'scr_pre_faturas'
    id_pre_fatura = Column(Integer,Sequence('scr_pre_faturas_id_pre_fatura_seq'), primary_key=True)
    cod_interno_frete = Column(String(10))
    remetente_id = Column(Integer)
    id_tipo_veiculo = Column(Integer)
    tipo_carga = Column(Integer)
    total_frete = Column(Numeric(12,2))
    status = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Protocolo_Dev_Canhoto(Model):
    __tablename__ = 'scr_protocolo_dev_canhoto'
    id_protocolo_dev = Column(Integer,Sequence('scr_protocolo_dev_canhoto_id_protocolo_dev_seq'), primary_key=True)
    numero_protocolo = Column(String(13))
    codigo_cliente = Column(Integer)
    data_protocolo = Column(DateTime)
    usuario_criacao = Column(Integer)
    data_alteracao = Column(DateTime)
    usuario_alteracao = Column(Integer)
    cancelado = Column(Integer)
    usuario_cancelamento = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Rastreamento(Model):
    __tablename__ = 'scr_rastreamento'
    id_rastreamento = Column(Integer,Sequence('scr_rastreamento_id_rastreamento_seq'), primary_key=True)
    rastreamento = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem(Model):
    __tablename__ = 'scr_relatorio_viagem'
    id_relatorio_viagem = Column(Integer,Sequence('scr_relatorio_viagem_id_relatorio_viagem_seq'), primary_key=True)
    categoria_acerto = Column(Integer)
    filial = Column(String(3))
    empresa = Column(String(3))
    id_fornecedor = Column(Integer)
    numero_relatorio = Column(String(13))
    fechamento_inicial = Column(Date)
    fechamento_final = Column(Date)
    data_relatorio = Column(Date)
    historico = Column(String(100))
    qtde_diarias = Column(Numeric(12,2))
    qtde_dias_parados = Column(Numeric(12,2))
    qtde_horas_extras = Column(Integer)
    numero_tabela_motorista = Column(String(13))
    total_frete = Column(Numeric(12,2))
    total_despesas_diretas = Column(Numeric(12,2))
    total_despesas_indiretas = Column(Numeric(12,2))
    vl_fretes_recebidos = Column(Numeric(12,2))
    vl_servico_for = Column(Numeric(12,2))
    vl_adiantamentos_for = Column(Numeric(12,2))
    vl_acrescimos_for = Column(Numeric(12,2))
    vl_pagar_for = Column(Numeric(12,2))
    codigo_centro_custo = Column(Integer)
    observacao = Column(text)
    tipo_parcela = Column(Integer)
    parcelas = Column(Integer)
    periodicidade = Column(Integer)
    lancamento_conta_pagar = Column(Integer)
    total_diarias_viagens = Column(Numeric(12,2))
    placa_veiculo = Column(String(8))
    vl_despesas_viagem = Column(Numeric(12,2))
    vl_despesas_a_vista = Column(Numeric(12,2))
    vl_despesas_a_prazo = Column(Numeric(12,2))
    vl_provisao_viagem = Column(Numeric(12,2))
    vl_provisao_saldo = Column(Numeric(12,2))
    vl_provisao_reembolsar = Column(Numeric(12,2))
    vl_provisao_devolucao = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Centro_Custos(Model):
    __tablename__ = 'scr_relatorio_viagem_centro_custos'
    id_relatorio_centro_custo = Column(Integer,Sequence('scr_relatorio_viagem_centro_custos_id_relatorio_centro_custo_seq'), primary_key=True)
    id_relatorio_viagem = Column(Integer)
    grupo_acerto = Column(Integer)
    codigo_centro_custo = Column(Integer)
    valor_por_centro_custo = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Fechamentos(Model):
    __tablename__ = 'scr_relatorio_viagem_fechamentos'
    id_relatorio_viagem = Column(Integer)
    tipo_calculo = Column(Integer)
    excedente = Column(Integer)
    base_calculo = Column(Numeric(12,3))
    valor_item = Column(Numeric(12,2))
    total_itens = Column(Numeric(12,2))
    valor_minimo = Column(Numeric(12,2))
    valor_pagar = Column(Numeric(12,2))
    programado = Column(Integer)
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Log_Atividades(Model):
    __tablename__ = 'scr_relatorio_viagem_log_atividades'
    id_log_atividade = Column(Integer,Sequence('scr_relatorio_viagem_log_atividades_id_log_atividade_seq'), primary_key=True)
    id_relatorio_viagem = Column(Integer)
    data_transacao = Column(DateTime)
    usuario = Column(String(30))
    acao_executada = Column(String(50))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Parcelas(Model):
    __tablename__ = 'scr_relatorio_viagem_parcelas'
    id_parcela = Column(Integer,Sequence('scr_relatorio_viagem_parcelas_id_parcela_seq'), primary_key=True)
    numero_parcela = Column(Integer)
    id_relatorio_viagem = Column(Integer)
    id_conta_pagar = Column(Integer)
    data_vencimento = Column(Date)
    valor_parcela = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Redespachos(Model):
    __tablename__ = 'scr_relatorio_viagem_redespachos'
    id_relatorio_viagem_redespacho = Column(Integer,Sequence('scr_relatorio_viagem_redespachos_id_relatorio_viagem_redespacho_seq'), primary_key=True)
    id_conhecimento_redespacho = Column(Integer)
    id_relatorio_viagem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Relatorio_Viagem_Romaneios(Model):
    __tablename__ = 'scr_relatorio_viagem_romaneios'
    id_relatorio_viagem_romaneio = Column(Integer,Sequence('scr_relatorio_viagem_romaneios_id_relatorio_viagem_romaneio_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    id_relatorio_viagem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Ajudantes(Model):
    __tablename__ = 'scr_romaneio_ajudantes'
    id_romaneio_ajudante = Column(Integer,Sequence('scr_romaneio_ajudantes_id_romaneio_ajudante_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    id_ajudante = Column(Numeric(6,0))
    valor_pagar = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Despesas(Model):
    __tablename__ = 'scr_romaneio_despesas'
    id_romaneio_despesa = Column(Integer,Sequence('scr_romaneio_despesas_id_romaneio_despesa_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    id_fornecedor = Column(Integer)
    id_despesa = Column(Integer)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    id_unidade = Column(Integer)
    quantidade = Column(Numeric(12,5))
    vl_unitario = Column(Numeric(12,5))
    valor_despesa = Column(Numeric(12,2))
    codigo_centro_custo = Column(Integer)
    observacao = Column(String(50))
    data_referencia = Column(Date)
    descricao = Column(String(50))
    tipo_operacao = Column(Integer)
    credito_debito = Column(Integer)
    forma_pagamento = Column(Integer)
    id_acerto = Column(Integer)
    odometro = Column(Integer)
    numero_documento = Column(String(13))
    lancar_conta = Column(Integer)
    id_conta_pagar = Column(Integer)
    data_vencimento = Column(Date)
    data_emissao = Column(Date)
    ab_origem = Column(Integer)
    ab_id_combust = Column(Integer)
    ab_id_bomba = Column(Integer)
    id_ab = Column(Integer)
    id_ab_item = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Fechamentos(Model):
    __tablename__ = 'scr_romaneio_fechamentos'
    id_fechamento = Column(Integer,Sequence('scr_romaneio_fechamentos_id_fechamento_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    tipo_calculo = Column(Integer)
    excedente = Column(Integer)
    base_calculo = Column(Numeric(12,5))
    valor_item = Column(Numeric(12,6))
    total_itens = Column(Numeric(12,2))
    valor_minimo = Column(Numeric(12,2))
    valor_pagar = Column(Numeric(12,2))
    programado = Column(Integer)
    codigo_centro_custo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Log_Atividades(Model):
    __tablename__ = 'scr_romaneio_log_atividades'
    id_log_atividade = Column(Integer,Sequence('scr_romaneio_log_atividades_id_log_atividade_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    data_transacao = Column(DateTime)
    usuario = Column(String(30))
    acao_executada = Column(String(50))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Nf(Model):
    __tablename__ = 'scr_romaneio_nf'
    id_romaneio_nf = Column(Integer,Sequence('scr_romaneio_nf_id_romaneio_nf_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    id_nota_fiscal_imp = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneio_Redespacho(Model):
    __tablename__ = 'scr_romaneio_redespacho'
    id_romaneio_redespacho = Column(Integer,Sequence('scr_romaneio_redespacho_id_romaneio_redespacho_seq'), primary_key=True)
    numero_romaneio_redespacho = Column(String(13))
    data_romaneio = Column(Date)
    data_registro = Column(DateTime)
    nome_recebedor = Column(String(50))
    cpf_recebedor = Column(String(14))
    id_transportadora = Column(Integer)
    placa_veiculo = Column(String(8))
    placa_carreta = Column(String(8))
    qtd_volumes = Column(Integer)
    peso_total = Column(Numeric(8,2))
    volume_cubado = Column(Numeric(8,4))
    status = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    tabela_frete = Column(String(13))

    def __repr__(self):
        return self.__tablename__



class Scr_Romaneios(Model):
    __tablename__ = 'scr_romaneios'
    id_romaneio = Column(Integer,Sequence('scr_romaneios_id_romaneio_seq'), primary_key=True)
    tipo_romaneio = Column(Integer)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))
    numero_romaneio = Column(String(13))
    data_romaneio = Column(DateTime)
    id_origem = Column(Integer)
    id_destino = Column(Integer)
    data_saida = Column(DateTime)
    data_chegada = Column(DateTime)
    diarias = Column(Numeric(5,1))
    baixa = Column(Integer)
    tipo_frota = Column(Integer)
    placa_veiculo = Column(String(8))
    placa_reboque = Column(String(8))
    placa_reboque2 = Column(String(8))
    cnpj_cpf_proprietario = Column(String(14))
    capacidade_kg = Column(Numeric(8,2))
    capacidade_m3 = Column(Numeric(8,3))
    id_motorista = Column(Integer)
    cpf_motorista = Column(String(14))
    numero_tabela_motorista = Column(String(13))
    redespacho = Column(Integer)
    id_transportador_redespacho = Column(Integer)
    numero_tabela_redespacho = Column(String(13))
    odometro_inicial = Column(Numeric(10,1))
    odometro_final = Column(Numeric(10,1))
    km_rodados = Column(Numeric(12,2))
    emitido = Column(Integer)
    cancelado = Column(Integer)
    motivo_cancelamento = Column(String(50))
    usuario_cancelamento = Column(String(30))
    total_peso = Column(Numeric(8,2))
    total_volume_cubado = Column(Numeric(8,2))
    total_peso_cubado = Column(Numeric(8,4))
    total_volumes = Column(Integer)
    total_frete = Column(Numeric(12,2))
    total_nf = Column(Numeric(12,2))
    conferente = Column(String(50))
    numero_lacres = Column(String(50))
    observacoes = Column(text)
    imposto = Column(Numeric(12,2))
    vl_fretes_recebidos = Column(Numeric(12,2))
    vl_servico_for = Column(Numeric(12,2))
    vl_despesas_diretas = Column(Numeric(12,2))
    vl_adiantamentos_for = Column(Numeric(12,2))
    vl_acrescimos_for = Column(Numeric(12,2))
    vl_pagar_for = Column(Numeric(12,2))
    fechamento = Column(Integer)
    id_acerto = Column(Integer)
    atingiu_meta = Column(Integer)
    id_pk_old = Column(Integer)
    tipo_modal = Column(Integer)
    numero_awb = Column(String(15))
    valor_awb = Column(Numeric(12,2))
    id_companhia_aerea = Column(Integer)
    tipo_servico_awb = Column(Integer)
    id_aeroporto = Column(Integer)
    numero_voo = Column(String(8))
    saida_voo = Column(DateTime)
    chegada_voo = Column(DateTime)
    data_cancelamento = Column(DateTime)
    data_chegada_coleta = Column(DateTime)
    data_saida_coleta = Column(DateTime)
    data_entrega_entrada = Column(DateTime)
    data_entrega_saida = Column(DateTime)
    vl_despesas_viagem = Column(Numeric(12,2))
    vl_despesas_a_vista = Column(Numeric(12,2))
    vl_despesas_a_prazo = Column(Numeric(12,2))
    vl_provisao_viagem = Column(Numeric(12,2))
    vl_provisao_saldo = Column(Numeric(12,2))
    vl_provisao_reembolsar = Column(Numeric(12,2))
    vl_provisao_devolucao = Column(Numeric(12,2))
    id_setor = Column(Integer)
    status_rodagem = Column(Integer)
    horimetro_inicial = Column(Numeric(9,2))
    horimetro_final = Column(Numeric(9,2))
    placas_engates = Column(String(60))
    notifica_parceiro = Column(Integer)
    km_final_informado = Column(Integer)
    id_regiao = Column(Integer)
    tipo_destino = Column(String(1))
    id_romaneio_vinculado = Column(Integer)
    flg_fechamento_automatico = Column(Integer)
    carregado = Column(Integer)
    dispara_integracao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Servicos(Model):
    __tablename__ = 'scr_servicos'
    id_servico = Column(Integer,Sequence('scr_servicos_id_servico_seq'), primary_key=True)
    servico = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Servicos_Executados(Model):
    __tablename__ = 'scr_servicos_executados'
    id_servico_executado = Column(Integer,Sequence('scr_servicos_executados_id_servico_executado_seq'), primary_key=True)
    numero_servico = Column(String(13))
    id_conhecimento = Column(Integer)
    codigo_cliente = Column(Integer)
    id_faturamento = Column(Integer)
    data_servico = Column(Date)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Scr_Servicos_Executados_Itens(Model):
    __tablename__ = 'scr_servicos_executados_itens'
    id_servico_executado_item = Column(Integer,Sequence('scr_servicos_executados_itens_id_servico_executado_item_seq'), primary_key=True)
    id_servico_executado = Column(Integer)
    servico_executado = Column(String(50))
    id_servico = Column(Integer)
    valor_servico = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Tab_Observacoes(Model):
    __tablename__ = 'scr_tab_observacoes'
    id_ocorrencia = Column(Integer,Sequence('scr_tab_observacoes_id_ocorrencia_seq'), primary_key=True)
    descricao_ocorrencia = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Feriados(Model):
    __tablename__ = 'scr_tabela_feriados'
    id_feriado = Column(Integer,Sequence('scr_tabela_feriados_id_feriado_seq'), primary_key=True)
    data_feriado = Column(String(4))
    tipo_feriado = Column(String(1))
    id_cidade = Column(Numeric(5,0))
    id_estado = Column(String(2))
    descricao_do_feriado = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Motorista(Model):
    __tablename__ = 'scr_tabela_motorista'
    id_tabela_motorista = Column(Integer,Sequence('scr_tabela_motorista_id_tabela_motorista_seq'), primary_key=True)
    cpf_motorista = Column(String(11))
    vigencia_tabela = Column(Date)
    aplicacao_tabela = Column(Date)
    moeda = Column(String(10))
    observacoes = Column(text)
    descricao_tabela = Column(String(100))
    numero_tabela_motorista = Column(String(13))
    ultima_utilizacao = Column(DateTime)
    reajuste_automatico = Column(Integer)
    ativa = Column(Integer)
    id_tabela_origem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Motorista_Log_Atividades(Model):
    __tablename__ = 'scr_tabela_motorista_log_atividades'
    id_tabela_motorista_log_atividade = Column(Integer,Sequence('scr_tabela_motorista_log_atividades_id_tabela_motorista_log_atividade_seq'), primary_key=True)
    data_transacao = Column(DateTime)
    id_usuario = Column(Integer)
    acao_executada = Column(String(50))
    historico = Column(text)
    id_tabela_motorista = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Motorista_Regiao_Calculos(Model):
    __tablename__ = 'scr_tabela_motorista_regiao_calculos'
    id_calculo = Column(Integer,Sequence('scr_tabela_motorista_regiao_calculos_id_calculo_seq'), primary_key=True)
    id_tabela_motorista_regiao = Column(Integer)
    medida_inicial = Column(Numeric(12,3))
    medida_final = Column(Numeric(12,3))
    valor_variavel = Column(Numeric(12,5))
    valor_fixo = Column(Numeric(12,5))
    valor_variavel_excedido = Column(Numeric(12,5))
    valor_fixo_excedido = Column(Numeric(12,5))
    tipo_calculo = Column(Integer)
    tipo_veiculo = Column(Integer)
    unidade_multiplicacao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Motorista_Regioes(Model):
    __tablename__ = 'scr_tabela_motorista_regioes'
    id_tabela_motorista_regiao = Column(Integer,Sequence('scr_tabela_motorista_regioes_id_tabela_motorista_regiao_seq'), primary_key=True)
    id_tabela_motorista = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    tipo_pedagio = Column(Integer)
    valor_pedagio = Column(Numeric(12,2))
    fracao_pedagio = Column(Numeric(12,3))
    placa_veiculo = Column(String(8))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabela_Motorista_Tipo_Calculo(Model):
    __tablename__ = 'scr_tabela_motorista_tipo_calculo'
    id_tipo_calculo = Column(Integer,Sequence('scr_tabela_motorista_tipo_calculo_id_tipo_calculo_seq'), primary_key=True)
    descricao = Column(String(50))
    dividir_por = Column(Integer)
    negativo = Column(Integer)
    cc_proprio = Column(Integer)
    cc_terceiro = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas(Model):
    __tablename__ = 'scr_tabelas'
    id_tabela_frete = Column(Integer,Sequence('scr_tabelas_id_tabela_frete_seq'), primary_key=True)
    numero_tabela_frete = Column(String(13))
    combinado = Column(Integer)
    padrao = Column(Integer)
    cnpj_cliente = Column(String(18))
    descricao_tabela = Column(String(100))
    informacoes_tabela = Column(String(50))
    cabecalho = Column(String(50))
    observacoes = Column(text)
    vigencia_tabela = Column(Date)
    aplicacao_tabela = Column(Date)
    validade_dias = Column(Integer)
    ultima_alteracao = Column(DateTime)
    ultima_utilizacao = Column(DateTime)
    usar_descontos = Column(Integer)
    imposto_incluso = Column(Integer)
    isento_imposto = Column(Integer)
    tipo_tabela = Column(Integer)
    a_vista = Column(Integer)
    reajuste_automatico = Column(Integer)
    ativa = Column(Integer)
    limite_peso_isento = Column(Numeric(8,3))
    limite_valor_isento = Column(Numeric(8,2))
    calcular_a_partir_de = Column(Integer)
    id_tabela_origem = Column(Integer)
    cnpj_transportador = Column(String(14))
    is_tabela_principal = Column(Integer)
    is_tabela_vinculada = Column(Integer)
    id_tabela_frete_principal = Column(Integer)
    perc_max_desconto = Column(Numeric(5,2))
    nao_cotar = Column(Integer)
    percentual_devolucao = Column(Numeric(6,2))
    percentual_reentrega = Column(Numeric(6,2))
    usa_valor_veiculo_maior = Column(Integer)
    usa_limite_fracionado_menor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Audit(Model):
    __tablename__ = 'scr_tabelas_audit'
    id_tabela_frete = Column(Integer,Sequence('scr_tabelas_audit_id_tabela_frete_seq'), primary_key=True)
    numero_tabela_frete = Column(String(13))
    combinado = Column(Integer)
    padrao = Column(Integer)
    cnpj_cliente = Column(String(18))
    descricao_tabela = Column(String(100))
    informacoes_tabela = Column(String(50))
    cabecalho = Column(String(50))
    observacoes = Column(text)
    vigencia_tabela = Column(Date)
    aplicacao_tabela = Column(Date)
    validade_dias = Column(Integer)
    ultima_alteracao = Column(DateTime)
    ultima_utilizacao = Column(DateTime)
    usar_descontos = Column(Integer)
    imposto_incluso = Column(Integer)
    isento_imposto = Column(Integer)
    tipo_tabela = Column(Integer)
    a_vista = Column(Integer)
    reajuste_automatico = Column(Integer)
    ativa = Column(Integer)
    limite_peso_isento = Column(Numeric(8,3))
    limite_valor_isento = Column(Numeric(8,2))
    calcular_a_partir_de = Column(Integer)
    id_tabela_origem = Column(Integer)
    cnpj_transportador = Column(String(14))
    is_tabela_principal = Column(Integer)
    is_tabela_vinculada = Column(Integer)
    id_tabela_frete_principal = Column(Integer)
    perc_max_desconto = Column(Numeric(5,2))
    nao_cotar = Column(Integer)
    percentual_devolucao = Column(Numeric(6,2))
    percentual_reentrega = Column(Numeric(6,2))
    usa_valor_veiculo_maior = Column(Integer)
    usa_limite_fracionado_menor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Calculos(Model):
    __tablename__ = 'scr_tabelas_calculos'
    id_calculo = Column(Integer,Sequence('scr_tabelas_calculos_id_calculo_seq'), primary_key=True)
    id_cf = Column(Integer)
    medida_inicial = Column(Numeric(12,3))
    medida_final = Column(Numeric(12,3))
    valor_variavel = Column(Numeric(14,8))
    valor_fixo = Column(Numeric(12,5))
    valor_variavel_excedido = Column(Numeric(14,8))
    valor_fixo_excedido = Column(Numeric(12,5))
    fracao = Column(Integer)
    id_natureza_carga = Column(Integer)
    unidade_divisao = Column(Integer)
    tipo_veiculo = Column(Integer)
    tipo_carroceria = Column(Integer)
    id_calculo_principal = Column(Integer)
    s1 = Column(Integer)
    s2 = Column(Integer)
    s3 = Column(Integer)
    s4 = Column(Integer)
    s5 = Column(Integer)
    s6 = Column(Integer)
    s7 = Column(Integer)
    feriado = Column(Integer)
    adicional_frete = Column(Numeric(6,2))
    tipo_carga = Column(Integer)
    vl_frete_veiculo = Column(Numeric(12,4))
    limite_fracao = Column(Integer)
    id_tipo_veiculo = Column(Integer)
    tipo_transporte = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Calculos_Audit(Model):
    __tablename__ = 'scr_tabelas_calculos_audit'
    id_calculo = Column(Integer,Sequence('scr_tabelas_calculos_audit_id_calculo_seq'), primary_key=True)
    id_cf = Column(Integer)
    medida_inicial = Column(Numeric(12,3))
    medida_final = Column(Numeric(12,3))
    valor_variavel = Column(Numeric(14,8))
    valor_fixo = Column(Numeric(12,5))
    valor_variavel_excedido = Column(Numeric(14,8))
    valor_fixo_excedido = Column(Numeric(12,5))
    fracao = Column(Integer)
    id_natureza_carga = Column(Integer)
    unidade_divisao = Column(Integer)
    tipo_veiculo = Column(Integer)
    tipo_carroceria = Column(Integer)
    id_calculo_principal = Column(Integer)
    s1 = Column(Integer)
    s2 = Column(Integer)
    s3 = Column(Integer)
    s4 = Column(Integer)
    s5 = Column(Integer)
    s6 = Column(Integer)
    s7 = Column(Integer)
    feriado = Column(Integer)
    adicional_frete = Column(Numeric(6,2))
    tipo_carga = Column(Integer)
    vl_frete_veiculo = Column(Numeric(12,4))
    limite_fracao = Column(Integer)
    id_tipo_veiculo = Column(Integer)
    tipo_transporte = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Cf(Model):
    __tablename__ = 'scr_tabelas_cf'
    id_cf = Column(Integer,Sequence('scr_tabelas_cf_id_cf_seq'), primary_key=True)
    id_origem_destino = Column(Integer)
    id_tipo_calculo = Column(Integer)
    isento_minimo = Column(Integer)
    compoe_bc = Column(Integer)
    id_faixa = Column(Integer)
    id_cf_principal = Column(Integer)
    cond_ctrc = Column(Integer)
    limite_fracao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Cf_Audit(Model):
    __tablename__ = 'scr_tabelas_cf_audit'
    id_cf = Column(Integer,Sequence('scr_tabelas_cf_audit_id_cf_seq'), primary_key=True)
    id_origem_destino = Column(Integer)
    id_tipo_calculo = Column(Integer)
    isento_minimo = Column(Integer)
    compoe_bc = Column(Integer)
    id_faixa = Column(Integer)
    cond_ctrc = Column(Integer)
    id_cf_principal = Column(Integer)
    limite_fracao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete(Model):
    __tablename__ = 'scr_tabelas_frete'
    id_cliente = Column(Integer)
    vigencia_tabela = Column(Date)
    aplicacao_tabela = Column(Date)
    densidade = Column(Numeric(8,3))
    moeda = Column(String(10))
    ultima_alteracao = Column(DateTime)
    usar_descontos = Column(Integer)
    sec_cat = Column(Numeric(8,2))
    despacho = Column(Numeric(8,2))
    itr = Column(Numeric(8,2))
    gris = Column(Numeric(8,2))
    percentual_gris = Column(Numeric(6,2))
    pedagio = Column(Numeric(8,2))
    fracao_pedagio = Column(Numeric(6,2))
    frete_minimo = Column(Numeric(8,2))
    peso_isento = Column(Numeric(8,3))
    valor_isento = Column(Numeric(8,2))
    advalorem = Column(Numeric(6,2))
    taxa_estadual = Column(Numeric(8,2))
    outros = Column(Numeric(8,2))
    imposto_incluso = Column(Integer)
    isento_taxas = Column(Integer)
    isento_gris = Column(Integer)
    isento_pedagio = Column(Integer)
    isento_imposto = Column(Integer)
    isento_advalorem = Column(Integer)
    observacoes = Column(text)
    descricao_tabela = Column(String(100))
    ressalva = Column(Numeric(8,2))
    numero_tabela_frete = Column(String(13))
    cnpj_cliente = Column(String(14))
    tipo_tabela = Column(Integer)
    ultima_utilizacao = Column(DateTime)
    a_vista = Column(Integer)
    reajuste_automatico = Column(Integer)
    id_tabela_frete = Column(Integer,Sequence('scr_tabelas_frete_id_tabela_frete_seq'), primary_key=True)
    desconto = Column(Numeric(8,2))
    suframa = Column(Numeric(8,2))
    calcular_faixa_somente_excedente = Column(Integer)
    isentar_tx_somente_minimo = Column(Integer)
    tx_coleta_10_kg = Column(Numeric(8,2))
    tx_coleta_exced_kg = Column(Numeric(8,2))
    tx_entrega_10_kg = Column(Numeric(8,2))
    tx_entrega_exced_kg = Column(Numeric(8,2))
    tx_redespacho_10_kg = Column(Numeric(8,2))
    tx_redespacho_exced_kg = Column(Numeric(8,2))
    tx_expresso_10_kg = Column(Numeric(8,2))
    tx_expresso_exced_kg = Column(Numeric(8,2))
    tx_emergencia_km_rodado = Column(Numeric(8,2))
    tx_emergencia_minimo = Column(Numeric(8,2))
    tx_manuseio_embalagem = Column(Numeric(8,2))
    tx_escolta_minimo_3_horas = Column(Numeric(8,2))
    tx_escolta_exced_hora = Column(Numeric(8,2))
    tx_outros = Column(Numeric(8,2))
    advalorem_capital_bases = Column(Numeric(6,2))
    advalorem_interior_redespacho = Column(Numeric(6,2))
    isento_tx_coleta = Column(Integer)
    isento_tx_entrega = Column(Integer)
    isento_tx_manuseio_embalagem = Column(Integer)
    tx_reentrega_percentual = Column(Numeric(6,2))
    tx_rodoviario_minimo = Column(Numeric(8,2))
    tx_rodoviario_kg = Column(Numeric(8,2))
    isento_tx_advalorem_capital = Column(Integer)
    isento_tx_advalorem_interior = Column(Integer)
    tx_coleta_satelite_10_kg = Column(Numeric(8,2))
    tx_coleta_satelite_exced_kg = Column(Numeric(8,2))
    tx_entrega_satelite_10_kg = Column(Numeric(8,2))
    tx_entrega_satelite_exced_kg = Column(Numeric(8,2))
    advalorem_interior_fluvial = Column(Numeric(6,2))
    isento_tx_advalorem_interior_fluvial = Column(Integer)
    tx_dificuldade_coleta_entrega = Column(Numeric(8,2))
    tx_veiculo_exclusivo_minimo = Column(Numeric(8,2))
    tx_veiculo_exclusivo_km = Column(Numeric(8,2))
    pedagio_fixo = Column(Integer)
    ativa = Column(Integer)
    id_tabela_origem = Column(Integer)
    informacoes_tabela = Column(String(50))
    cabecalho = Column(String(50))
    calcular_a_partir_de = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Aereo_Origem_Destino(Model):
    __tablename__ = 'scr_tabelas_frete_aereo_origem_destino'
    id_origem_destino_aereo = Column(Integer,Sequence('scr_tabelas_frete_aereo_origem_destino_id_origem_destino_aereo_seq'), primary_key=True)
    id_tabela_frete = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    prazo_entrega = Column(Integer)
    taxa_minima = Column(Numeric(8,2))
    valor_kg_ate_20_kg = Column(Numeric(8,2))
    valor_kg_ate_50_kg = Column(Numeric(8,2))
    valor_kg_ate_300_kg = Column(Numeric(8,2))
    valor_kg_ate_500_kg = Column(Numeric(8,2))
    valor_kg_ate_1000_kg = Column(Numeric(8,2))
    valor_kg_acima_1000_kg = Column(Numeric(8,2))
    tarifa_001 = Column(Numeric(8,2))
    tarifa_010 = Column(Numeric(8,2))
    tarifa_020 = Column(Numeric(8,2))
    tarifa_070 = Column(Numeric(8,2))
    tarifa_080 = Column(Numeric(8,2))
    tarifa_140 = Column(Numeric(8,2))
    tarifa_180 = Column(Numeric(8,2))
    tarifa_200 = Column(Numeric(8,2))
    tarifa_240 = Column(Numeric(8,2))
    id_inclusao = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Origem_Destino(Model):
    __tablename__ = 'scr_tabelas_frete_origem_destino'
    id_origem_destino = Column(Integer,Sequence('scr_tabelas_frete_origem_destino_id_origem_destino_seq'), primary_key=True)
    id_tabela_frete = Column(Integer)
    id_cidade_origem = Column(Integer)
    id_cidade_destino = Column(Integer)
    id_inclusao = Column(String(10))
    distancia = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Origem_Destino_Faixas(Model):
    __tablename__ = 'scr_tabelas_frete_origem_destino_faixas'
    id_origem_destino_faixa = Column(Integer,Sequence('scr_tabelas_frete_origem_destino_faixas_id_origem_destino_faixa_seq'), primary_key=True)
    peso_inicial = Column(Numeric(8,1))
    peso_final = Column(Numeric(8,1))
    frete_minimo = Column(Numeric(8,2))
    frete_tonelada = Column(Numeric(8,2))
    pedagio = Column(Numeric(8,2))
    perc_gris = Column(Numeric(6,2))
    advalorem = Column(Numeric(6,2))
    despacho = Column(Numeric(8,2))
    id_inclusao = Column(String(10))
    id_origem_destino = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Peso(Model):
    __tablename__ = 'scr_tabelas_frete_peso'
    id_tabelas_frete_peso = Column(Integer,Sequence('scr_tabelas_frete_peso_id_tabelas_frete_peso_seq'), primary_key=True)
    peso_inicial = Column(Numeric(10,1))
    peso_final = Column(Numeric(10,1))
    frete_peso_fixo = Column(Numeric(10,2))
    frete_peso_tonelada = Column(Numeric(10,2))
    id_temp = Column(String(10))
    id_tabela_frete = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Regiao(Model):
    __tablename__ = 'scr_tabelas_frete_regiao'
    id_regiao = Column(Integer,Sequence('scr_tabelas_frete_regiao_id_regiao_seq'), primary_key=True)
    id_tabela_frete = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    id_inclusao = Column(String(10))
    pedagio = Column(Numeric(8,2))
    perc_gris = Column(Numeric(6,2))
    gris_minimo = Column(Numeric(8,2))
    frete_minimo = Column(Numeric(8,2))
    despacho = Column(Numeric(8,2))
    sec_cat = Column(Numeric(8,2))
    itr = Column(Numeric(8,2))
    ressalva = Column(Numeric(8,2))
    limite_peso = Column(Integer)
    advalorem = Column(Numeric(8,2))
    limite_valor = Column(Numeric(8,2))
    advalorem_capital_bases = Column(Numeric(8,2))
    advalorem_interior_redespacho = Column(Numeric(8,2))
    advalorem_interior_fluvial = Column(Numeric(8,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Regiao_Faixas_Peso(Model):
    __tablename__ = 'scr_tabelas_frete_regiao_faixas_peso'
    id_regiao_faixa_peso = Column(Integer,Sequence('scr_tabelas_frete_regiao_faixas_peso_id_regiao_faixa_peso_seq'), primary_key=True)
    id_regiao = Column(Integer)
    peso_inicial = Column(Numeric(8,1))
    peso_final = Column(Numeric(8,1))
    frete_minimo = Column(Numeric(8,2))
    frete_tonelada = Column(Numeric(8,2))
    id_inclusao = Column(String(10))
    frete_kg_adicional = Column(Numeric(8,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Regiao_Faixas_Valor(Model):
    __tablename__ = 'scr_tabelas_frete_regiao_faixas_valor'
    id_regiao_faixa_valor = Column(Integer,Sequence('scr_tabelas_frete_regiao_faixas_valor_id_regiao_faixa_valor_seq'), primary_key=True)
    valor_inicial = Column(Numeric(10,2))
    valor_final = Column(Numeric(10,2))
    frete_valor_fixo = Column(Numeric(10,2))
    frete_valor_percentual = Column(Numeric(5,2))
    id_inclusao = Column(String(10))
    id_regiao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Tipo_Calculo(Model):
    __tablename__ = 'scr_tabelas_frete_tipo_calculo'
    id_tipo_calculo = Column(Integer,Sequence('scr_tabelas_frete_tipo_calculo_id_tipo_calculo_seq'), primary_key=True)
    descricao = Column(String(50))
    dividir_por = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Valor(Model):
    __tablename__ = 'scr_tabelas_frete_valor'
    id_tabelas_frete_valor = Column(Integer,Sequence('scr_tabelas_frete_valor_id_tabelas_frete_valor_seq'), primary_key=True)
    valor_inicial = Column(Numeric(10,2))
    valor_final = Column(Numeric(10,2))
    frete_valor_fixo = Column(Numeric(10,2))
    frete_valor_percentual = Column(Numeric(5,2))
    id_temp = Column(String(10))
    id_tabela_frete = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Frete_Workflow(Model):
    __tablename__ = 'scr_tabelas_frete_workflow'
    id_tabelas_frete_workflow = Column(Integer,Sequence('scr_tabelas_frete_workflow_id_tabelas_frete_workflow_seq'), primary_key=True)
    data_transacao = Column(DateTime)
    id_usuario = Column(Integer)
    acao_executada = Column(String(50))
    historico = Column(text)
    id_tabelas_frete = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Origem_Destino(Model):
    __tablename__ = 'scr_tabelas_origem_destino'
    id_origem_destino = Column(Integer,Sequence('scr_tabelas_origem_destino_id_origem_destino_seq'), primary_key=True)
    tipo_rota = Column(Integer)
    id_tabela_frete = Column(Integer)
    id_origem = Column(Integer)
    id_destino = Column(Integer)
    prazo_entrega = Column(Integer)
    densidade = Column(Integer)
    limite_peso_isento = Column(Numeric(8,3))
    limite_valor_isento = Column(Numeric(8,2))
    calcular_a_partir_de = Column(Integer)
    ida_volta = Column(Integer)
    id_origem_destino_principal = Column(Integer)
    cumulativa = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Origem_Destino_Audit(Model):
    __tablename__ = 'scr_tabelas_origem_destino_audit'
    id_origem_destino = Column(Integer,Sequence('scr_tabelas_origem_destino_audit_id_origem_destino_seq'), primary_key=True)
    tipo_rota = Column(Integer)
    id_tabela_frete = Column(Integer)
    id_origem = Column(Integer)
    id_destino = Column(Integer)
    prazo_entrega = Column(Integer)
    densidade = Column(Integer)
    limite_peso_isento = Column(Numeric(8,3))
    limite_valor_isento = Column(Numeric(8,2))
    calcular_a_partir_de = Column(Integer)
    ida_volta = Column(Integer)
    id_origem_destino_principal = Column(Integer)
    cumulativa = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Origem_Destino_Calculos(Model):
    __tablename__ = 'scr_tabelas_origem_destino_calculos'
    id_calculo = Column(Integer,Sequence('scr_tabelas_origem_destino_calculos_id_calculo_seq'), primary_key=True)
    id_origem_destino = Column(Integer)
    medida_inicial = Column(Numeric(12,3))
    medida_final = Column(Numeric(12,3))
    valor_variavel = Column(Numeric(12,5))
    valor_fixo = Column(Numeric(12,5))
    valor_variavel_excedido = Column(Numeric(12,5))
    valor_fixo_excedido = Column(Numeric(12,5))
    fracao = Column(Integer)
    tipo_calculo = Column(Integer)
    id_natureza_carga = Column(Integer)
    unidade_divisao = Column(Integer)
    tipo_veiculo = Column(Integer)
    tipo_carroceria = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Redespacho(Model):
    __tablename__ = 'scr_tabelas_redespacho'
    id_tabela_redespacho = Column(Integer,Sequence('scr_tabelas_redespacho_id_tabela_redespacho_seq'), primary_key=True)
    id_transportadora = Column(Integer)
    vigencia_tabela = Column(Date)
    aplicacao_tabela = Column(Date)
    densidade = Column(Numeric(8,3))
    moeda = Column(String(10))
    ultima_alteracao = Column(DateTime)
    usar_descontos = Column(Integer)
    sec_cat = Column(Numeric(8,2))
    despacho = Column(Numeric(8,2))
    itr = Column(Numeric(8,2))
    gris = Column(Numeric(8,2))
    percentual_gris = Column(Numeric(6,2))
    pedagio = Column(Numeric(8,2))
    fracao_pedagio = Column(Numeric(6,2))
    frete_minimo = Column(Numeric(8,2))
    peso_isento = Column(Numeric(8,3))
    valor_isento = Column(Numeric(8,2))
    advalorem = Column(Numeric(6,2))
    taxa_estadual = Column(Numeric(8,2))
    outros = Column(Numeric(8,2))
    imposto_incluso = Column(Integer)
    isento_taxas = Column(Integer)
    isento_gris = Column(Integer)
    isento_pedagio = Column(Integer)
    isento_imposto = Column(Integer)
    isento_advalorem = Column(Integer)
    observacoes = Column(text)
    descricao_tabela = Column(String(100))
    ressalva = Column(Numeric(8,2))
    numero_tabela_redespacho = Column(String(13))
    cnpj_transportadora = Column(String(14))
    tipo_tabela = Column(Integer)
    ultima_utilizacao = Column(DateTime)
    a_vista = Column(Integer)
    reajuste_automatico = Column(Integer)
    desconto = Column(Numeric(8,2))
    suframa = Column(Numeric(8,2))
    calcular_faixa_somente_excedente = Column(Integer)
    isentar_tx_somente_minimo = Column(Integer)
    tipo_calculo_frete_valor = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Redespacho_Regiao(Model):
    __tablename__ = 'scr_tabelas_redespacho_regiao'
    id_regiao = Column(Integer,Sequence('scr_tabelas_redespacho_regiao_id_regiao_seq'), primary_key=True)
    id_tabela_redespacho = Column(Integer)
    id_regiao_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    id_inclusao = Column(String(10))
    pedagio = Column(Numeric(8,2))
    perc_gris = Column(Numeric(6,2))
    gris_minimo = Column(Numeric(8,2))
    frete_minimo = Column(Numeric(8,2))
    despacho = Column(Numeric(8,2))
    sec_cat = Column(Numeric(8,2))
    itr = Column(Numeric(8,2))
    ressalva = Column(Numeric(8,2))
    limite_peso = Column(Integer)
    advalorem = Column(Numeric(8,2))
    limite_valor = Column(Numeric(8,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Redespacho_Regiao_Calculos(Model):
    __tablename__ = 'scr_tabelas_redespacho_regiao_calculos'
    id_calculo = Column(Integer,Sequence('scr_tabelas_redespacho_regiao_calculos_id_calculo_seq'), primary_key=True)
    id_regiao = Column(Integer)
    medida_inicial = Column(Numeric(12,3))
    medida_final = Column(Numeric(12,3))
    valor_variavel = Column(Numeric(12,2))
    valor_fixo = Column(Numeric(12,2))
    valor_variavel_excedido = Column(Numeric(12,2))
    valor_fixo_excedido = Column(Numeric(12,2))
    tipo_calculo = Column(Integer)
    unidade_divisao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Redespacho_Tipo_Calculo(Model):
    __tablename__ = 'scr_tabelas_redespacho_tipo_calculo'
    id_tipo_calculo = Column(Integer,Sequence('scr_tabelas_redespacho_tipo_calculo_id_tipo_calculo_seq'), primary_key=True)
    descricao = Column(String(50))
    dividir_por = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Redespacho_Workflow(Model):
    __tablename__ = 'scr_tabelas_redespacho_workflow'
    id_tabelas_redespacho_workflow = Column(Integer,Sequence('scr_tabelas_redespacho_workflow_id_tabelas_redespacho_workflow_seq'), primary_key=True)
    data_transacao = Column(DateTime)
    id_usuario = Column(Integer)
    acao_executada = Column(String(50))
    historico = Column(text)
    id_tabelas_redespacho = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Tipo_Calculo(Model):
    __tablename__ = 'scr_tabelas_tipo_calculo'
    id_tipo_calculo = Column(Integer,Sequence('scr_tabelas_tipo_calculo_id_tipo_calculo_seq'), primary_key=True)
    descricao = Column(String(50))
    descricao_extensa = Column(String(50))
    dividir_por = Column(Integer)
    ativo = Column(Integer)
    observacao = Column(text)
    tipo = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Tipo_Veiculo(Model):
    __tablename__ = 'scr_tabelas_tipo_veiculo'
    id_tipo_veiculo = Column(Integer,Sequence('scr_tabelas_tipo_veiculo_id_tipo_veiculo_seq'), primary_key=True)
    tipo_veiculo = Column(String(20))
    faixa_por_vol3 = Column(Integer)
    capacidade_peso_inicial = Column(Numeric(12,4))
    capacidade_peso_final = Column(Numeric(12,4))

    def __repr__(self):
        return self.__tablename__



class Scr_Tabelas_Workflow(Model):
    __tablename__ = 'scr_tabelas_workflow'
    id_tabelas_workflow = Column(Integer,Sequence('scr_tabelas_workflow_id_tabelas_workflow_seq'), primary_key=True)
    data_transacao = Column(DateTime)
    id_usuario = Column(Integer)
    acao_executada = Column(String(50))
    historico = Column(text)
    id_tabelas_frete = Column(Integer)
    id_tabela_audit = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Tipos_Calculo(Model):
    __tablename__ = 'scr_tipos_calculo'
    id_tipo_calculo = Column(Integer,Sequence('scr_tipos_calculo_id_tipo_calculo_seq'), primary_key=True)
    descricao = Column(String(50))
    dividir_por = Column(Integer)
    credito_debito = Column(Integer)
    cc_proprio = Column(Integer)
    cc_terceiro = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Versao_Edi(Model):
    __tablename__ = 'scr_versao_edi'
    id_versao_edi = Column(Integer,Sequence('scr_versao_edi_id_versao_edi_seq'), primary_key=True)
    versao_edi = Column(String(15))

    def __repr__(self):
        return self.__tablename__



class Scr_Viagens(Model):
    __tablename__ = 'scr_viagens'
    id_viagem = Column(Integer,Sequence('scr_viagens_id_viagem_seq'), primary_key=True)
    numero_viagem = Column(String(13))
    placa_veiculo = Column(String(8))
    data_registro = Column(DateTime)
    inicio_viagem = Column(DateTime)
    fim_viagem = Column(DateTime)
    diarias = Column(Numeric(5,1))
    tipo_frota = Column(Integer)
    cpf_motorista = Column(String(9))
    id_motorista = Column(Integer)
    odometro_inicial = Column(Numeric(10,1))
    odometro_final = Column(Numeric(10,1))
    km_percorrido = Column(Numeric(12,2))
    emitido = Column(Numeric(1,0))
    cod_filial = Column(String(3))
    cod_empresa = Column(String(3))
    placa_reboque = Column(String(8))
    motivo_cancelamento = Column(String(50))
    peso_total = Column(Numeric(8,2))
    volume_cubado = Column(Numeric(8,2))
    peso_cubado = Column(Numeric(8,4))
    qtd_volumes = Column(Integer)
    total_frete = Column(Numeric(12,2))
    id_cidade_origem = Column(Integer)
    id_regiao_destino = Column(Integer)
    observacoes = Column(String(50))
    numero_tabela_motorista = Column(String(13))
    total_itens = Column(Numeric(12,2))
    adiantamento = Column(Numeric(12,2))
    outras_despesas = Column(Numeric(12,2))
    imposto = Column(Numeric(12,2))
    total_despesas = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    total_itens_motorista = Column(Numeric(12,2))
    total_motorista = Column(Numeric(12,2))
    total_fechamento = Column(Numeric(12,2))
    fechamento = Column(Integer)
    id_acerto = Column(Integer)
    baixa = Column(Integer)
    cancelado = Column(Integer)
    comissao = Column(Numeric(3,2))
    valor_fixo = Column(Numeric(12,2))
    atingiu_meta = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Viagens_Despesas(Model):
    __tablename__ = 'scr_viagens_despesas'
    id_viagem_despesa = Column(Integer,Sequence('scr_viagens_despesas_id_viagem_despesa_seq'), primary_key=True)
    id_viagem = Column(Integer)
    id_despesa = Column(Integer)
    valor_despesa = Column(Numeric(12,2))
    observacao = Column(String(50))
    data_referencia = Column(Date)
    descricao = Column(String(50))
    credito_debito = Column(Integer)
    forma_pagamento = Column(Integer)
    id_acerto = Column(Integer)
    cod_empresa = Column(String(3))
    cod_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Scr_Viagens_Docs(Model):
    __tablename__ = 'scr_viagens_docs'
    id_viagem_doc = Column(Integer,Sequence('scr_viagens_docs_id_viagem_doc_seq'), primary_key=True)
    id_romaneio = Column(Integer)
    id_documento = Column(Integer)
    tipo_documento = Column(Integer)
    peso_total = Column(Numeric(8,2))
    volume_cubado = Column(Numeric(8,3))
    peso_cubado = Column(Numeric(8,4))
    qtd_volumes = Column(Integer)
    data_saida = Column(DateTime)
    total_frete = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Scr_Viagens_Fechamento(Model):
    __tablename__ = 'scr_viagens_fechamento'
    id_viagem = Column(Integer)
    tipo_calculo = Column(Integer)
    excedente = Column(Integer)
    base_calculo = Column(Numeric(12,3))
    valor_item = Column(Numeric(12,2))
    total_itens = Column(Numeric(12,2))
    valor_minimo = Column(Numeric(12,2))
    valor_pagar = Column(Numeric(12,2))
    programado = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Scr_Viagens_Log_Atividades(Model):
    __tablename__ = 'scr_viagens_log_atividades'
    id_viagens_log_atividade = Column(Integer,Sequence('scr_viagens_log_atividades_id_viagens_log_atividade_seq'), primary_key=True)
    id_viagem = Column(Integer)
    data_transacao = Column(DateTime)
    usuario = Column(String(30))
    acao_executada = Column(String(50))
    historico = Column(text)

    def __repr__(self):
        return self.__tablename__



class Scripts(Model):
    __tablename__ = 'scripts'
    id_script = Column(Integer,Sequence('scripts_id_script_seq'), primary_key=True)
    nome_script = Column(String(30))
    codigo_script = Column(text)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))

    def __repr__(self):
        return self.__tablename__



class Sec_Aplicacoes(Model):
    __tablename__ = 'sec_aplicacoes'
    id_aplicacao = Column(Integer,Sequence('sec_aplicacoes_id_aplicacao_seq'), primary_key=True)
    codigo_aplicacao = Column(String(150))
    nome_aplicacao = Column(String(170))

    def __repr__(self):
        return self.__tablename__



class Sec_Aplicacoes_Permissoes(Model):
    __tablename__ = 'sec_aplicacoes_permissoes'
    id_permissao_aplicacao = Column(Integer,Sequence('sec_aplicacoes_permissoes_id_permissao_aplicacao_seq'), primary_key=True)
    codigo_aplicacao = Column(String(150))
    login_name = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Sec_Apps(Model):
    __tablename__ = 'sec_apps'
    app_name = Column(String(128),Sequence('sec_apps_app_name_seq'), primary_key=True)
    app_type = Column(String(255))
    description = Column(String(255))

    def __repr__(self):
        return self.__tablename__



class Sec_Groups(Model):
    __tablename__ = 'sec_groups'
    group_id = Column(Integer,Sequence('sec_groups_group_id_seq'), primary_key=True)
    description = Column(String(255))

    def __repr__(self):
        return self.__tablename__



class Sec_Groups_Apps(Model):
    __tablename__ = 'sec_groups_apps'
    group_id = Column(Integer,Sequence('sec_groups_apps_group_id_seq'), primary_key=True)
    app_name = Column(String(128))
    priv_access = Column(String(1))
    priv_insert = Column(String(1))
    priv_delete = Column(String(1))
    priv_update = Column(String(1))
    priv_export = Column(String(1))
    priv_print = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Sec_Logged(Model):
    __tablename__ = 'sec_logged'
    login = Column(String(255))
    date_login = Column(String(128))
    sc_session = Column(String(32))
    ip = Column(String(32))

    def __repr__(self):
        return self.__tablename__



class Sec_Users(Model):
    __tablename__ = 'sec_users'
    login = Column(String(255),Sequence('sec_users_login_seq'), primary_key=True)
    pswd = Column(String(32))
    name = Column(String(64))
    email = Column(String(64))
    active = Column(String(1))
    activation_code = Column(String(32))
    priv_admin = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Sec_Users_Groups(Model):
    __tablename__ = 'sec_users_groups'
    login = Column(String(255),Sequence('sec_users_groups_login_seq'), primary_key=True)
    group_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Sec_Usuarios_Web(Model):
    __tablename__ = 'sec_usuarios_web'
    id_usuario = Column(Integer,Sequence('sec_usuarios_web_id_usuario_seq'), primary_key=True)
    nome_usuario = Column(String(40))
    email = Column(String(50))
    senha = Column(String(40))
    login_name = Column(String(30))
    codigo_filial = Column(String(3))
    codigo_empresa = Column(String(3))
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Seguro_Veiculo(Model):
    __tablename__ = 'seguro_veiculo'
    placa_veiculo = Column(String(8))
    ano_seguro = Column(String(4))
    data_inicio_vigencia = Column(Date)
    data_fim_vigencia = Column(Date)
    valor_anual_seguro = Column(Numeric(9,2))
    seg_resp_civil = Column(Numeric(10,2))

    def __repr__(self):
        return self.__tablename__



class Seguros(Model):
    __tablename__ = 'seguros'
    tipo_seguro = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Servicos_Integracao(Model):
    __tablename__ = 'servicos_integracao'
    id = Column(Integer,Sequence('servicos_integracao_id_seq'), primary_key=True)
    identificador = Column(text)
    descricao = Column(text)
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class String_Conexoes(Model):
    __tablename__ = 'string_conexoes'
    id_string_conexao = Column(Integer,Sequence('string_conexoes_id_string_conexao_seq'), primary_key=True)
    banco_dados = Column(String(50))
    string_softlog = Column(text)
    string_php = Column(text)
    codigo_autorizacao = Column(String(20))
    usuario = Column(text)
    senha = Column(text)
    cliente_ativo = Column(Integer)
    port = Column(text)
    host = Column(text)
    softlog_web = Column(Integer)
    softlog_integracao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Sys_Avisos(Model):
    __tablename__ = 'sys_avisos'
    id_aviso = Column(Integer,Sequence('sys_avisos_id_aviso_seq'), primary_key=True)
    mensagem_aviso = Column(text)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Sys_Relatorios(Model):
    __tablename__ = 'sys_relatorios'
    id_sys_relatorio = Column(Integer,Sequence('sys_relatorios_id_sys_relatorio_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    codigo_relatorio = Column(String(30))
    nome_arquivo = Column(String(50))
    nome_relatorio = Column(String(50))
    altura = Column(Numeric(10,4))
    largura = Column(Numeric(10,4))
    conteudo_arquivo_b64 = Column(text)

    def __repr__(self):
        return self.__tablename__



class Sys_Relatorios_Custom(Model):
    __tablename__ = 'sys_relatorios_custom'
    id_sys_relatorio = Column(Integer,Sequence('sys_relatorios_custom_id_sys_relatorio_seq'), primary_key=True)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    codigo_relatorio = Column(String(30))
    nome_arquivo = Column(String(50))
    nome_relatorio = Column(String(50))
    altura = Column(Numeric(10,4))
    largura = Column(Numeric(10,4))
    conteudo_arquivo_b64 = Column(text)

    def __repr__(self):
        return self.__tablename__



class Tab_Obs(Model):
    __tablename__ = 'tab_obs'
    id_obs = Column(Numeric(2,0))
    descricao = Column(String(45))

    def __repr__(self):
        return self.__tablename__



class Tabela_Metas(Model):
    __tablename__ = 'tabela_metas'
    id_tabela_meta = Column(Integer,Sequence('tabela_metas_id_tabela_meta_seq'), primary_key=True)
    tipo_meta = Column(Integer)
    ano = Column(Integer)
    mes = Column(String(3))
    valor_meta = Column(Numeric(12,2))

    def __repr__(self):
        return self.__tablename__



class Tb_Acessorios(Model):
    __tablename__ = 'tb_acessorios'
    id_acessorio = Column(Integer,Sequence('tb_acessorios_id_acessorio_seq'), primary_key=True)
    nm_acessorio = Column(String(30))
    tp_rodoar = Column(Integer)
    tp_sanitario = Column(Integer)
    tp_arcondic = Column(Integer)
    tp_apsom = Column(Integer)
    tp_tv = Column(Integer)
    tp_dvd = Column(Integer)
    tp_comunic = Column(Integer)
    tp_bar = Column(Integer)
    tp_gelad = Column(Integer)
    tp_outros = Column(Integer)
    tp_obs = Column(String(50))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Check(Model):
    __tablename__ = 'tb_categ_check'
    id_categ_check = Column(Integer,Sequence('tb_categ_check_id_categ_check_seq'), primary_key=True)
    id_categ_trans = Column(Integer)
    id_check = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Doc(Model):
    __tablename__ = 'tb_categ_doc'
    id_categ_doc = Column(Integer,Sequence('tb_categ_doc_id_categ_doc_seq'), primary_key=True)
    id_categ_trans = Column(Integer)
    id_doc_veic = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Trans(Model):
    __tablename__ = 'tb_categ_trans'
    id_categ_trans = Column(Integer,Sequence('tb_categ_trans_id_categ_trans_seq'), primary_key=True)
    nm_categ_trans = Column(String(100))
    dc_categ_trans = Column(text)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Veic(Model):
    __tablename__ = 'tb_categ_veic'
    id_categ_veic = Column(Integer,Sequence('tb_categ_veic_id_categ_veic_seq'), primary_key=True)
    id_categ_trans = Column(Integer)
    placa_veiculo = Column(String(8))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Veic_Check(Model):
    __tablename__ = 'tb_categ_veic_check'
    id_categ_veic_check = Column(Integer,Sequence('tb_categ_veic_check_id_categ_veic_check_seq'), primary_key=True)
    id_categ_trans = Column(Integer)
    placa_veiculo = Column(String(8))
    id_categ_check = Column(Integer)
    id_check = Column(Integer)
    check_feitoem = Column(Date)
    check_validade = Column(Date)
    check_status = Column(Integer)
    check_status_prazo = Column(Date)
    check_veic_chk01 = Column(Integer)
    check_veic_chk02 = Column(Integer)
    check_veic_chk03 = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Categ_Veic_Doc(Model):
    __tablename__ = 'tb_categ_veic_doc'
    id_categ_veic_doc = Column(Integer,Sequence('tb_categ_veic_doc_id_categ_veic_doc_seq'), primary_key=True)
    id_categ_trans = Column(Integer)
    placa_veiculo = Column(String(8))
    id_categ_doc = Column(Integer)
    doc_numero = Column(String(50))
    doc_serie = Column(String(20))
    doc_emissao = Column(Date)
    doc_validade = Column(Date)
    doc_status = Column(Integer)
    doc_status_prazo = Column(Date)
    doc_obs = Column(text)
    doc_veic_chk01 = Column(Integer)
    doc_veic_chk02 = Column(Integer)
    doc_veic_chk03 = Column(Integer)
    atual_em = Column(DateTime)
    id_categ_veic = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tb_Check(Model):
    __tablename__ = 'tb_check'
    id_check = Column(Integer,Sequence('tb_check_id_check_seq'), primary_key=True)
    sq_check = Column(String(3))
    nm_check = Column(String(100))
    dc_check = Column(text)
    pr_check = Column(Integer)
    atual_em = Column(DateTime)
    ob_check = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tb_Combust_Lub(Model):
    __tablename__ = 'tb_combust_lub'
    id_combust_lub = Column(Integer,Sequence('tb_combust_lub_id_combust_lub_seq'), primary_key=True)
    tp_combust_lub = Column(String(1))
    nm_combust_lub = Column(String(50))
    un_combust_lub = Column(String(3))
    cd_combust_sefaz = Column(String(4))
    cd_combust_anp = Column(String(9))
    obs_combust_lub = Column(String(150))
    atual_em = Column(DateTime)
    gr_combust = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tb_Combust_Lub_Itens(Model):
    __tablename__ = 'tb_combust_lub_itens'
    id_item = Column(Integer,Sequence('tb_combust_lub_itens_id_item_seq'), primary_key=True)
    id_combust_lub = Column(Integer)
    id_produto = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Compo(Model):
    __tablename__ = 'tb_compo'
    id_cpt = Column(Integer,Sequence('tb_compo_id_cpt_seq'), primary_key=True)
    cpt_cd = Column(String(15))
    cpt_dc = Column(String(50))
    cpt_tp = Column(Integer)
    cpt_fab = Column(Integer)
    cpt_serie = Column(String(20))
    cpt_medidas = Column(String(150))
    cpt_local = Column(Integer)
    cpt_placa = Column(String(8))
    cpt_km_atual = Column(Numeric(10,1))
    cpt_km_troca = Column(Numeric(10,1))
    cpt_hr_atual = Column(Numeric(9,2))
    cpt_hr_troca = Column(Numeric(9,2))
    cpt_bx = Column(Integer)
    cpt_vlr_atual = Column(Numeric(12,2))
    cpt_trocar = Column(Integer)
    cpt_combust = Column(Integer)
    cpt_lt_lubrif = Column(Numeric(7,2))
    cpt_lt_remonte = Column(Numeric(7,2))
    cpt_obs = Column(String(40))
    atual_em = Column(DateTime)
    cpt_km_trocou = Column(Numeric(10,1))
    cpt_hr_trocou = Column(Numeric(9,2))
    cpt_km_proxima = Column(Numeric(10,1))
    cpt_hr_proxima = Column(Numeric(9,2))

    def __repr__(self):
        return self.__tablename__



class Tb_Compo_Eve(Model):
    __tablename__ = 'tb_compo_eve'
    id_cpt_eve = Column(Integer,Sequence('tb_compo_eve_id_cpt_eve_seq'), primary_key=True)
    id_cpt = Column(Integer)
    id_eve = Column(Integer)
    cpt_eve_local = Column(Integer)
    cpt_eve_placa = Column(String(8))
    cpt_eve_dh = Column(DateTime)
    cpt_eve_dc = Column(String(50))
    cpt_eve_km = Column(Numeric(9,1))
    cpt_eve_hr = Column(Numeric(9,2))
    cpt_eve_gkm = Column(Integer)
    cpt_eve_ghr = Column(Integer)
    cpt_eve_gdd = Column(Integer)
    cpt_eve_qtd = Column(Numeric(12,2))
    cpt_eve_vlr = Column(Numeric(12,2))
    cpt_eve_for = Column(Integer)
    cpt_eve_nfnr = Column(Integer)
    cpt_eve_nfser = Column(String(5))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Compo_Km(Model):
    __tablename__ = 'tb_compo_km'
    id_compo_km = Column(Integer,Sequence('tb_compo_km_id_compo_km_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    id_compo = Column(Integer)
    tb_origem = Column(String(100))
    compo_km = Column(Numeric(10,1))
    compo_km_dh = Column(DateTime)
    compo_km_sd = Column(Numeric(10,1))
    compo_km_obs = Column(String(150))
    atual_em = Column(DateTime)
    id_origem = Column(Integer)
    compo_km_rd = Column(Numeric(10,1))

    def __repr__(self):
        return self.__tablename__



class Tb_Doc_Veic(Model):
    __tablename__ = 'tb_doc_veic'
    id_doc_veic = Column(Integer,Sequence('tb_doc_veic_id_doc_veic_seq'), primary_key=True)
    doc_descr = Column(String(150))
    doc_orgao = Column(String(100))
    doc_sigla = Column(String(10))
    doc_obrig = Column(Integer)
    doc_periodo = Column(Integer)
    doc_chk01 = Column(Integer)
    doc_chk02 = Column(Integer)
    doc_chk03 = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Eve_Compo(Model):
    __tablename__ = 'tb_eve_compo'
    id_eve = Column(Integer,Sequence('tb_eve_compo_id_eve_seq'), primary_key=True)
    eve_descr = Column(String(50))
    eve_local = Column(Integer)
    eve_custo = Column(Integer)
    eve_compr = Column(Integer)
    eve_instal = Column(Integer)
    eve_repar = Column(Integer)
    eve_desinstal = Column(Integer)
    eve_baixa = Column(Integer)
    eve_venda = Column(Integer)
    eve_lubrif = Column(Integer)
    eve_abast = Column(Integer)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Ipva(Model):
    __tablename__ = 'tb_ipva'
    id_ipva = Column(Integer,Sequence('tb_ipva_id_ipva_seq'), primary_key=True)
    ipva_placa = Column(String(7))
    ipva_ano_val = Column(Numeric(4,0))
    ipva_tt_cota = Column(Integer)
    ipva_nr_cota = Column(Numeric(2,0))
    ipva_dt_venc = Column(DateTime)
    ipva_vr_prev = Column(Numeric(10,2))
    ipva_dt_pago = Column(DateTime)
    ipva_vr_pago = Column(Numeric(10,2))
    ipva_doc_nr = Column(Numeric(15,0))
    ipva_doc_emis = Column(DateTime)
    ipva_empresa = Column(String(3))
    ipva_filial_resp = Column(String(3))
    ipva_status = Column(Numeric(1,0))
    dt_cadastro = Column(DateTime)
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Mod_Cpt(Model):
    __tablename__ = 'tb_mod_cpt'
    id_mod_cpt = Column(Integer,Sequence('tb_mod_cpt_id_mod_cpt_seq'), primary_key=True)
    mod_cpt_dc = Column(String(50))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Pagamentos(Model):
    __tablename__ = 'tb_pagamentos'
    id_pagamento = Column(Integer,Sequence('tb_pagamentos_id_pagamento_seq'), primary_key=True)
    dc_pagamento = Column(String(50))
    obs_pagamento = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Tb_Servicos(Model):
    __tablename__ = 'tb_servicos'
    id_servico = Column(Integer,Sequence('tb_servicos_id_servico_seq'), primary_key=True)
    nm_servico = Column(String(50))
    vlr_sugerido = Column(Numeric(12,2))
    obs_servico = Column(String(100))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Tp_Cpt(Model):
    __tablename__ = 'tb_tp_cpt'
    id_tp_cpt = Column(Integer,Sequence('tb_tp_cpt_id_tp_cpt_seq'), primary_key=True)
    tp_cpt_dc = Column(String(50))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Veic_Acess(Model):
    __tablename__ = 'tb_veic_acess'
    id_veic_acess = Column(Integer,Sequence('tb_veic_acess_id_veic_acess_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    id_acessorio = Column(Integer)
    veic_acess_obs = Column(String(150))
    atual_em = Column(DateTime)
    id_veiculo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tb_Veic_Compo(Model):
    __tablename__ = 'tb_veic_compo'
    id_veic_compo = Column(Integer,Sequence('tb_veic_compo_id_veic_compo_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    id_compo = Column(Integer)
    veic_compo_obs = Column(String(150))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tb_Veic_Km(Model):
    __tablename__ = 'tb_veic_km'
    id_veic_km = Column(Integer,Sequence('tb_veic_km_id_veic_km_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    tb_origem = Column(String(100))
    veic_km = Column(Numeric(10,1))
    veic_km_dh = Column(DateTime)
    veic_km_sd = Column(Numeric(10,1))
    veic_km_obs = Column(String(150))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Tbl_Aeroportos(Model):
    __tablename__ = 'tbl_aeroportos'
    id_aeroporto = Column(Integer,Sequence('tbl_aeroportos_id_aeroporto_seq'), primary_key=True)
    nome_aeroporto = Column(String(80))
    id_cidade = Column(Integer)
    codigo_iata = Column(String(3))
    codigo_oaci = Column(String(4))

    def __repr__(self):
        return self.__tablename__



class Tbl_Agencias(Model):
    __tablename__ = 'tbl_agencias'
    agencod = Column(Integer,Sequence('tbl_agencias_agencod_seq'), primary_key=True)
    bancod = Column(Integer)
    agennome = Column(String(30))
    agennumeroagencia = Column(String(18))

    def __repr__(self):
        return self.__tablename__



class Tbl_Bancos(Model):
    __tablename__ = 'tbl_bancos'
    bancod = Column(Integer)
    bannome = Column(String(50))
    bannumerobanco = Column(String(10))
    banlogo = Column(String(100))
    banseparador = Column(String(100))
    bancarteira = Column(String(10))
    bancarteirades = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Tbl_Composicao_Plano(Model):
    __tablename__ = 'tbl_composicao_plano'
    plancod = Column(Integer)
    plancoddest = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tbl_Configuracoes(Model):
    __tablename__ = 'tbl_configuracoes'
    cod_configuracao = Column(Integer,Sequence('tbl_configuracoes_cod_configuracao_seq'), primary_key=True)
    tempo_sessao = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tbl_Contas_Correntes(Model):
    __tablename__ = 'tbl_contas_correntes'
    bancod = Column(Integer)
    agencod = Column(Integer)
    contnumero = Column(String(18))

    def __repr__(self):
        return self.__tablename__



class Tbl_Empresas(Model):
    __tablename__ = 'tbl_empresas'
    empcod = Column(Integer)
    empcidade = Column(String(30))
    estadouf = Column(String(2))
    emprazaosocial = Column(String(50))
    empnatureza = Column(String(1))
    empcpfcnpj = Column(String(14))
    empendereco = Column(String(50))
    empcep = Column(String(9))
    empnumero = Column(String(10))
    empcomplemento = Column(String(10))
    empbairro = Column(String(25))
    empddd = Column(String(3))
    emptelefone = Column(String(10))
    emptipo = Column(String(1))
    empemail = Column(String(70))
    emplogo = Column(String(100))
    empinscestadual = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Tbl_Estados(Model):
    __tablename__ = 'tbl_estados'
    estadouf = Column(String(2))
    estadonome = Column(String(25))

    def __repr__(self):
        return self.__tablename__



class Tbl_Evento(Model):
    __tablename__ = 'tbl_evento'
    evento_id = Column(Integer,Sequence('tbl_evento_evento_id_seq'), primary_key=True)
    evento_titulo = Column(text)
    evento_datainicio = Column(Date)
    evento_datafinal = Column(Date)
    evento_recorrencia = Column(String(10))
    evento_periodo = Column(String(10))
    evento_fatcod = Column(String(10))
    evento_fatserie = Column(String(10))
    evento_orgcod = Column(String(10))
    evento_pago = Column(String(10))
    evento_reccod = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Tbl_Evento_Pag(Model):
    __tablename__ = 'tbl_evento_pag'
    eventopag_id = Column(Integer,Sequence('tbl_evento_pag_eventopag_id_seq'), primary_key=True)
    eventopag_titulo = Column(text)
    eventopag_datainicio = Column(Date)
    eventopag_datafinal = Column(Date)
    eventopag_recorrencia = Column(String(10))
    eventopag_periodo = Column(String(10))
    eventopag_pagcod = Column(String(10))
    eventopag_orgcod = Column(String(10))
    eventopag_empcod = Column(String(10))
    eventopag_pago = Column(String(10))

    def __repr__(self):
        return self.__tablename__



class Tbl_Faturamento(Model):
    __tablename__ = 'tbl_faturamento'
    fatcod = Column(Integer,Sequence('tbl_faturamento_fatcod_seq'), primary_key=True)
    fatserie = Column(Integer)
    plancod = Column(Integer)
    orgcod = Column(Integer)
    empcod = Column(Integer)
    portcod = Column(Integer)
    fatdtlancamento = Column(DateTime)
    fatvalor = Column(Float)
    fataliquotaimposto = Column(Float)
    fatvalorimposto = Column(Float)
    fatnumeroparcelas = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tbl_Faturamento_X_Itens(Model):
    __tablename__ = 'tbl_faturamento_x_itens'
    fatseq = Column(Integer,Sequence('tbl_faturamento_x_itens_fatseq_seq'), primary_key=True)
    fatcod = Column(Integer)
    fatserie = Column(Integer)
    orgcod = Column(Integer)
    fatvalorunitario = Column(Float)
    prodcod = Column(Integer)
    fatqtde = Column(Float)
    fatvalortotal = Column(Float)

    def __repr__(self):
        return self.__tablename__



class Tbl_Instrucao_Boleto(Model):
    __tablename__ = 'tbl_instrucao_boleto'
    msg_id = Column(Integer,Sequence('tbl_instrucao_boleto_msg_id_seq'), primary_key=True)
    msg_instrucao = Column(text)

    def __repr__(self):
        return self.__tablename__



class Tbl_Organizacoes(Model):
    __tablename__ = 'tbl_organizacoes'
    orgcod = Column(Integer)
    orgnome = Column(String(50))
    orgcpfcnpj = Column(String(30))
    orgnatureza = Column(String(80))
    orginscestadual = Column(String(30))
    orgendereco = Column(String(200))
    orgcep = Column(String(10))
    orgcidade = Column(String(50))
    orgestado = Column(String(4))
    orgrazaosocial = Column(String(50))
    orglogo = Column(String(50))
    orgbairro = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Tbl_Pagamentos(Model):
    __tablename__ = 'tbl_pagamentos'
    pagcod = Column(Integer,Sequence('tbl_pagamentos_pagcod_seq'), primary_key=True)
    bancod = Column(Integer)
    orgcod = Column(Integer)
    empcod = Column(Integer)
    agencod = Column(Integer)
    contnumero = Column(String(18))
    plancod = Column(Integer)
    pagdtlancamento = Column(DateTime)
    pagdtvencimento = Column(DateTime)
    pagdtpagamento = Column(DateTime)
    pagvalorprincipal = Column(Float)
    pagvalorjuros = Column(Float)
    pagvalormora = Column(Float)
    pagvalortotal = Column(Float)

    def __repr__(self):
        return self.__tablename__



class Tbl_Planos_Contas(Model):
    __tablename__ = 'tbl_planos_contas'
    plancod = Column(Integer)
    plandescricao = Column(String(50))
    plantipo = Column(String(1))
    plantotalizadora = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Tbl_Portadores(Model):
    __tablename__ = 'tbl_portadores'
    portcod = Column(Integer)
    portnome = Column(String(20))
    portimpressao = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Tbl_Produtos(Model):
    __tablename__ = 'tbl_produtos'
    prodcod = Column(Integer)
    proddesc = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Tbl_Recebimento_X_Parcelas(Model):
    __tablename__ = 'tbl_recebimento_x_parcelas'
    reccod = Column(Integer)
    recparcela = Column(String(4))
    fatcod = Column(String(6))
    fatserie = Column(String(3))
    orgcod = Column(Integer)
    bancod = Column(Integer)
    agencod = Column(Integer)
    contnumero = Column(String(18))
    recdtlancamento = Column(DateTime)
    recdtvencimento = Column(DateTime)
    recdtrecebimento = Column(DateTime)
    recvalorprincipal = Column(Float)
    recvalorjuros = Column(Float)
    recvalormora = Column(Float)
    recvalortotal = Column(Float)

    def __repr__(self):
        return self.__tablename__



class Tbl_Sec_Apps(Model):
    __tablename__ = 'tbl_sec_apps'
    app_name = Column(String(128),Sequence('tbl_sec_apps_app_name_seq'), primary_key=True)
    app_type = Column(String(255))
    description = Column(String(255))

    def __repr__(self):
        return self.__tablename__



class Tbl_Sec_Groups(Model):
    __tablename__ = 'tbl_sec_groups'
    group_id = Column(Integer,Sequence('tbl_sec_groups_group_id_seq'), primary_key=True)
    description = Column(String(64))

    def __repr__(self):
        return self.__tablename__



class Tbl_Sec_Groups_Apps(Model):
    __tablename__ = 'tbl_sec_groups_apps'
    group_id = Column(Integer,Sequence('tbl_sec_groups_apps_group_id_seq'), primary_key=True)
    app_name = Column(String(128))
    priv_access = Column(String(1))
    priv_insert = Column(String(1))
    priv_delete = Column(String(1))
    priv_update = Column(String(1))
    priv_export = Column(String(1))
    priv_print = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Tbl_Sec_Users(Model):
    __tablename__ = 'tbl_sec_users'
    login = Column(String(32),Sequence('tbl_sec_users_login_seq'), primary_key=True)
    pswd = Column(String(32))
    name = Column(String(64))
    email = Column(String(64))
    usr_active = Column(String(1))
    activation_code = Column(String(32))
    priv_admin = Column(String(1))

    def __repr__(self):
        return self.__tablename__



class Tbl_Sec_Users_Groups(Model):
    __tablename__ = 'tbl_sec_users_groups'
    login = Column(String(32),Sequence('tbl_sec_users_groups_login_seq'), primary_key=True)
    group_id = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tbl_Tipo_Contato(Model):
    __tablename__ = 'tbl_tipo_contato'
    id_tipo_contato = Column(Integer,Sequence('tbl_tipo_contato_id_tipo_contato_seq'), primary_key=True)
    descricao_tipo_contato = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Tbl_Usuario_X_Organizacoes(Model):
    __tablename__ = 'tbl_usuario_x_organizacoes'
    orgcod = Column(Integer)
    login = Column(String(20))

    def __repr__(self):
        return self.__tablename__



class Teste_Imagem(Model):
    __tablename__ = 'teste_imagem'
    id_imagem = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Tmp_Fat_19(Model):
    __tablename__ = 'tmp_fat_19'
    selecionar = Column(Integer)
    sel_report = Column(Integer)
    id_faturamento = Column(Integer)
    numero_fatura = Column(String(13))
    numero_boleto = Column(String(16))
    data_vencimento = Column(Date)
    data_pagamento = Column(Date)
    atraso = Column(Integer)
    dias_de_atraso = Column(Integer)
    data_fechamento = Column(Date)
    data_processamento = Column(DateTime)
    data_cancelamento = Column(Date)
    motivo_cancelamento = Column(String(100))
    status = Column(Integer)
    id_cobrador = Column(Integer)
    id_vendedor = Column(Integer)
    fatura_nome = Column(String(50))
    qtde_ctrc = Column(Integer)
    fatura_banco = Column(String(3))
    fatura_agencia = Column(String(10))
    fatura_conta_corrente = Column(String(16))
    fatura_cnpj = Column(String(14))
    fatura_cidade = Column(String(30))
    valor_fatura = Column(Numeric(12,2))
    perc_desconto = Column(Numeric(12,2))
    desconto = Column(Numeric(12,2))
    valor_recebido = Column(Numeric(12,2))
    juros = Column(Numeric(12,2))
    multa = Column(Numeric(12,2))
    abatimento = Column(Numeric(12,2))
    tarifa = Column(Numeric(12,2))
    imposto = Column(Numeric(12,2))
    valor_inss = Column(Numeric(12,2))
    acrescimos = Column(Numeric(12,2))
    valor_liquido = Column(Numeric(12,2))
    mais_menos = Column(Numeric)
    id_remessa = Column(Integer)
    nome_cobrador = Column(String(50))
    nome_cidade = Column(String(50))
    numero_banco = Column(String(3))
    numero_agencia = Column(String(8))
    numero_conta = Column(String(15))
    multa_perc = Column(Numeric(5,2))
    juros_perc = Column(Numeric(5,2))
    valor_corrigido = Column(Numeric(12,2))
    nome_portador = Column(String(50))
    nome_vendedor = Column(String(50))
    classe_cliente = Column(String(1))
    data_emi = Column(Date)
    lista_ctrcs = Column(String(200))

    def __repr__(self):
        return self.__tablename__



class Totvs_Condicoespagamento(Model):
    __tablename__ = 'totvs_condicoespagamento'
    id = Column(Integer,Sequence('totvs_condicoespagamento_id_seq'), primary_key=True)
    id_condicao_pagamento = Column(Integer)
    parametro = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Totvs_Config(Model):
    __tablename__ = 'totvs_config'
    id_parametro = Column(Integer,Sequence('totvs_config_id_parametro_seq'), primary_key=True)
    codigo_controle = Column(Integer)
    parametro = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Totvs_Formapagamento(Model):
    __tablename__ = 'totvs_formapagamento'
    id = Column(Integer,Sequence('totvs_formapagamento_id_seq'), primary_key=True)
    id_pagamento_softlog = Column(Integer)
    parametro = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Totvs_Parametros_Filial(Model):
    __tablename__ = 'totvs_parametros_filial'
    id = Column(Integer,Sequence('totvs_parametros_filial_id_seq'), primary_key=True)
    empresa = Column(String(3))
    filial = Column(String(3))
    id_parametro_totvs = Column(Integer)
    valor = Column(String(30))

    def __repr__(self):
        return self.__tablename__



class Totvs_Produtos(Model):
    __tablename__ = 'totvs_produtos'
    id = Column(Integer,Sequence('totvs_produtos_id_seq'), primary_key=True)
    id_produto = Column(Integer)
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    totvs_idprd = Column(String(15))
    totvs_idnat = Column(String(15))
    totvs_cod_tb1_flx = Column(String(30))
    totvs_cod_tb2_flx = Column(String(30))
    totvs_cod_tb3_flx = Column(String(30))
    totvs_cod_tb4_flx = Column(String(30))
    totvs_conta_cotabil = Column(String(55))
    parametro = Column(String(100))

    def __repr__(self):
        return self.__tablename__



class Tracking_Gps(Model):
    __tablename__ = 'tracking_gps'
    id = Column(Integer,Sequence('tracking_gps_id_seq'), primary_key=True)
    placa_veiculo = Column(String(7))
    motorista_cpf = Column(String(11))
    data_registro = Column(DateTime)
    data_localizacao = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    id_romaneio = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Unidade(Model):
    __tablename__ = 'unidade'
    id_unidade = Column(Numeric(2,0))
    nome_unidade = Column(String(40))
    fantasia = Column(String(40))
    endereco = Column(String(40))
    cidade = Column(String(30))
    uf = Column(String(2))
    cep = Column(String(8))
    ddd = Column(Numeric(2,0))
    pbx = Column(Numeric(8,0))
    fax = Column(Numeric(8,0))
    email = Column(String(40))
    alteracao = Column(DateTime)
    cnpj = Column(Numeric(14,0))
    inscricao_municipal = Column(Numeric(11,0))
    inscricao_estadual = Column(Numeric(14,0))
    suframa = Column(Numeric(15,0))
    responsavel_1 = Column(String(40))
    telefone_1 = Column(Numeric(8,0))
    responsavel_2 = Column(String(40))
    telefone_2 = Column(Numeric(8,0))
    responsavel_3 = Column(String(40))
    telefone_3 = Column(Numeric(8,0))

    def __repr__(self):
        return self.__tablename__



class Users_Api_Softlog(Model):
    __tablename__ = 'users_api_softlog'
    id = Column(Integer,Sequence('users_api_softlog_id_seq'), primary_key=True)
    username = Column(String(100))
    password_hash = Column(text)
    id_ambiente = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Usuarios(Model):
    __tablename__ = 'usuarios'
    nome_usuario = Column(String(40))
    email = Column(String(50))
    senha = Column(String(30))
    login_name = Column(String(30))
    codigo_filial = Column(String(3))
    codigo_empresa = Column(String(3))
    ativo = Column(Integer)
    exibir_dashboard = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Usuarios_Permissoes(Model):
    __tablename__ = 'usuarios_permissoes'
    id_permissao = Column(Integer,Sequence('usuarios_permissoes_id_permissao_seq'), primary_key=True)
    codigo_permissao = Column(String(10))
    codigo_modulo = Column(String(10))
    nome_processo = Column(String(50))
    permissao = Column(Integer)
    login_name = Column(String(30))
    codigo_empresa = Column(String(3))
    codigo_filial = Column(String(3))
    permitido = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Usuarios_Ws(Model):
    __tablename__ = 'usuarios_ws'
    id_usuario_ws = Column(Integer,Sequence('usuarios_ws_id_usuario_ws_seq'), primary_key=True)
    login = Column(String(50))
    senha = Column(String(20))
    obs = Column(text)

    def __repr__(self):
        return self.__tablename__



class V_Result(Model):
    __tablename__ = 'v_result'
    pg_notify = Column(text)

    def __repr__(self):
        return self.__tablename__



class Veic_Atrelamento(Model):
    __tablename__ = 'veic_atrelamento'
    id_atrelamento = Column(Integer,Sequence('veic_atrelamento_id_atrelamento_seq'), primary_key=True)
    placa_tracao = Column(String(7))
    placa_reboque = Column(String(7))
    tp_atrela = Column(String(1))
    dthr_atrela = Column(DateTime)
    km_atrela_tracao = Column(Numeric(7,0))
    hr_atrela_tracao = Column(Numeric(9,2))
    km_atrela_reboque = Column(Numeric(7,0))
    hr_atrela_reboque = Column(Numeric(9,2))
    obs_atrela = Column(String(100))
    tp_desatrela = Column(String(1))
    dthr_desatrela = Column(DateTime)
    km_desatrela_tracao = Column(Numeric(7,0))
    hr_desatrela_tracao = Column(Numeric(9,2))
    km_desatrela_reboque = Column(Numeric(7,0))
    hr_desatrela_reboque = Column(Numeric(9,2))
    obs_desatrela = Column(String(100))
    atual_em = Column(DateTime)

    def __repr__(self):
        return self.__tablename__



class Veiculos(Model):
    __tablename__ = 'veiculos'
    placa_veiculo = Column(String(8),Sequence('veiculos_placa_veiculo_seq'), primary_key=True)
    cidade_veiculo = Column(String(15))
    uf_veiculo = Column(String(2))
    cor_veiculo = Column(String(12))
    ano_modelo_veiculo = Column(String(4))
    nrchassis = Column(String(18))
    nrmotor = Column(String(18))
    renavan = Column(String(12))
    data_alteracao = Column(DateTime)
    numero_frota = Column(String(6))
    ano_fabricacao_veiculo = Column(String(4))
    valor_veiculo = Column(Numeric(10,2))
    valor_veiculo_sem_pneus = Column(Numeric(10,2))
    rendimento_combustivel = Column(Numeric(8,3))
    veiculo_proprio = Column(Numeric(1,0))
    id_proprietario = Column(Numeric(5,0))
    id_tipo_veiculo = Column(Numeric(5,0))
    capacidade_tanque = Column(Numeric(6,1))
    id_veiculo = Column(Integer)
    status_veiculo = Column(Integer)
    id_cidade_veiculo = Column(Integer)
    tipo_frota = Column(Integer)
    ativo = Column(Integer)
    rntrc = Column(String(15))
    validade_rntrc = Column(Date)
    id_rastreadora = Column(Integer)
    bloqueado = Column(Integer)
    odometro_atual = Column(Numeric(10,1))
    data_inclusao = Column(DateTime)
    placa_odometro = Column(String(7))
    data_engate = Column(DateTime)
    id_motorista = Column(Integer)
    chk_preven = Column(Integer)
    chk_licenc = Column(Integer)
    chk_pneus = Column(Integer)
    chk_seguro = Column(Integer)
    chk_ipva = Column(Integer)
    chk_dispon = Column(Integer)
    id_marca = Column(Integer)
    id_modelo = Column(Integer)
    id_chassi = Column(Integer)
    porte = Column(Integer)
    tracionado = Column(Integer)
    tp_carroceria = Column(Integer)
    tipo_combustivel = Column(String(10))
    capacidade_cubica = Column(Numeric(8,4))
    capacidade_tonelada = Column(Numeric(6,3))
    numero_eixos = Column(Numeric(2,0))
    potencia = Column(Integer)
    comprimento = Column(Numeric(10,2))
    largura = Column(Numeric(10,2))
    altura = Column(Numeric(10,2))
    disponivel = Column(Integer)
    veic_obs = Column(text)
    frotista = Column(Integer)
    dt_compra = Column(Date)
    vr_compra = Column(Numeric(12,2))
    dt_venda = Column(Date)
    vr_venda = Column(Numeric(12,2))
    depreciacao = Column(Numeric(8,2))
    horimetro_atual = Column(Numeric(9,2))
    veic_obs_ativ = Column(text)
    veic_obs_bloq = Column(text)
    num_equip_rastreador = Column(String(30))
    atual_em = Column(DateTime)
    veic_tara = Column(Integer)
    totvs_centro_custo = Column(String(20))

    def __repr__(self):
        return self.__tablename__



class Veiculos_Marcas(Model):
    __tablename__ = 'veiculos_marcas'
    id_marca_veiculo = Column(Integer,Sequence('veiculos_marcas_id_marca_veiculo_seq'), primary_key=True)
    nome_marca = Column(String(40))

    def __repr__(self):
        return self.__tablename__



class Veiculos_Modelos(Model):
    __tablename__ = 'veiculos_modelos'
    id_modelo_veiculo = Column(Integer,Sequence('veiculos_modelos_id_modelo_veiculo_seq'), primary_key=True)
    descricao_modelo = Column(String(40))
    id_marca_veiculo = Column(Numeric(5,0))
    codigo_fipe = Column(String(8))
    deprec_pc = Column(Numeric(7,2))
    deprec_meses = Column(Integer)
    var_km = Column(Integer)
    var_hr = Column(Integer)
    lt_lubrif = Column(Numeric(7,2))
    aceita_pc = Column(Numeric(7,2))
    veic_tara = Column(Integer)
    veic_lota = Column(Integer)
    veic_pbt = Column(Integer)
    veic_pbtc = Column(Integer)
    veic_cmt = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Veiculos_Tipos(Model):
    __tablename__ = 'veiculos_tipos'
    id_tipo_veiculo = Column(Integer,Sequence('veiculos_tipos_id_tipo_veiculo_seq'), primary_key=True)
    id_marca = Column(Numeric(6,0))
    id_modelo = Column(Numeric(6,0))
    tipo_combustivel = Column(String(10))
    tipo_carroceria = Column(String(15))
    capacidade_cubica = Column(Numeric(8,4))
    capacidade_tonelada = Column(Numeric(6,3))
    numero_eixos = Column(Numeric(2,0))
    descricao_tipo_veiculo = Column(String(40))
    classificacao = Column(String(20))
    valor_lub_motor = Column(Numeric(8,2))
    km_troca_oleo_motor = Column(Numeric(10,1))
    taxa_reposicao_lub = Column(Numeric(8,2))
    capacidade_caixa_diferencial = Column(Numeric(10,3))
    capacidade_cambio = Column(Numeric(10,3))
    valor_lub_transmissao = Column(Numeric(8,2))
    km_troca_transmissao = Column(Numeric(10,1))
    valor_lavagem_veiculo = Column(Numeric(10,2))
    km_recomendada_fab_lavagem = Column(Numeric(10,1))
    valor_pneu_novo = Column(Numeric(10,2))
    valor_camara_nova = Column(Numeric(10,2))
    valor_protetor_novo = Column(Numeric(10,2))
    valor_recauchutagem = Column(Numeric(10,2))
    km_vida_util_pneu = Column(Numeric(10,1))
    total_pneus_veiculo = Column(Numeric(3,0))
    volume_carter = Column(Numeric(10,3))
    tipo_veiculo = Column(Numeric(1,0))
    potencia = Column(Integer)
    comprimento = Column(Numeric(10,2))
    largura = Column(Numeric(10,2))
    altura = Column(Numeric(10,2))
    id_chassi = Column(Integer)
    tp_carroceria = Column(Integer)
    tp_combust1 = Column(Integer)
    tp_combust2 = Column(Integer)
    tp_combust3 = Column(Integer)
    media_combust1 = Column(Numeric(7,3))
    media_combust2 = Column(Numeric(7,3))
    media_combust3 = Column(Numeric(7,3))

    def __repr__(self):
        return self.__tablename__



class Ven_Prop(Model):
    __tablename__ = 'ven_prop'
    id_ven_prop = Column(Integer,Sequence('ven_prop_id_ven_prop_seq'), primary_key=True)
    id_vendedor = Column(Integer)
    codigo_cliente = Column(Integer)
    nome_cliente = Column(String(50))
    cnpj_cpf = Column(String(18))
    inscricao_estadual = Column(String(18))
    ddd = Column(String(2))
    telefone = Column(String(8))
    contato_nome = Column(String(25))
    contato_fone = Column(String(8))
    contato_email = Column(String(100))
    endereco = Column(String(100))
    numero = Column(String(6))
    end_complemento = Column(String(100))
    cep = Column(String(8))
    bairro = Column(String(30))
    id_cidade = Column(Numeric(5,0))
    ramo_atividade = Column(String(40))
    ven_prop_obs = Column(text)
    dt_cadastro = Column(DateTime)
    dt_emissao = Column(Date)
    dt_retorno = Column(Date)

    def __repr__(self):
        return self.__tablename__



class Ven_Prop_It(Model):
    __tablename__ = 'ven_prop_it'
    id_ven_prop_it = Column(Integer,Sequence('ven_prop_it_id_ven_prop_it_seq'), primary_key=True)
    id_ven_prop = Column(Integer)
    id_cidade_origem = Column(Integer)
    id_cidade_destino = Column(Integer)
    min_100kg = Column(Numeric(10,2))
    frete_peso_kg = Column(Numeric(10,2))
    advalorem = Column(Numeric(10,2))
    pedagio = Column(Numeric(10,2))
    gris = Column(Numeric(10,2))
    despacho = Column(Numeric(10,2))
    prazo_cap_medio = Column(String(10))
    ven_prop_it_obs = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Vm_Historicos(Model):
    __tablename__ = 'vm_historicos'
    id_historico = Column(Integer,Sequence('vm_historicos_id_historico_seq'), primary_key=True)
    descricao_historico = Column(String(50))

    def __repr__(self):
        return self.__tablename__



class Vm_Login(Model):
    __tablename__ = 'vm_login'
    id_login = Column(Integer,Sequence('vm_login_id_login_seq'), primary_key=True)
    nome_login = Column(String(30))
    nome_completo = Column(String(50))
    email = Column(String(50))
    visualizar_notas = Column(Integer)
    aprovar_nota = Column(Integer)
    maisprazo_nota = Column(Integer)
    devolver_nota = Column(Integer)
    visualizar_ctrc = Column(Integer)
    aprovar_ctrc = Column(Integer)
    maisprazo_ctrc = Column(Integer)
    devolver_ctrc = Column(Integer)
    recebe_email = Column(Integer)
    nivel_usuario = Column(Integer)
    senha = Column(String(20))
    empresa = Column(String(2))
    cadastrar_usuario = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Vm_Notas(Model):
    __tablename__ = 'vm_notas'
    id_nota = Column(Integer,Sequence('vm_notas_id_nota_seq'), primary_key=True)
    cnpj_emitente = Column(String(18))
    cnpj_destinatario = Column(String(18))
    pedido_compra_vm = Column(text)
    numero_nota_fiscal = Column(String(10))
    data_emissao_nf = Column(Date)
    data_coleta = Column(Date)
    tipo_operacao = Column(String(15))
    status_nota = Column(Integer)
    data_registro = Column(DateTime)
    aguardar_dias = Column(Integer)
    aguardar_motivo = Column(text)
    conteudo = Column(text)
    data_venc_processo = Column(Date)
    data_conclusao = Column(Date)
    cnpj_transportadora = Column(String(14))
    conteudo_pequeno = Column(text)
    data_ultimo_mov_fornecedor = Column(DateTime)
    data_ultimo_mov_cliente = Column(DateTime)
    excluido = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Vm_Notas_Acompanhamento(Model):
    __tablename__ = 'vm_notas_acompanhamento'
    id_acompanhamento = Column(Integer,Sequence('vm_notas_acompanhamento_id_acompanhamento_seq'), primary_key=True)
    id_nota = Column(Integer)
    movimentado_por = Column(String(40))
    justificativa = Column(text)
    data_movimento = Column(DateTime)
    aguardar_dias = Column(Integer)
    status_nota = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Vm_Notas_Anexos(Model):
    __tablename__ = 'vm_notas_anexos'
    id_notas_anexo = Column(Integer,Sequence('vm_notas_anexos_id_notas_anexo_seq'), primary_key=True)
    id_nota = Column(Integer)
    nome_arquivo = Column(String(120))
    data_upload = Column(Date)
    caminho_arquivo = Column(String(150))

    def __repr__(self):
        return self.__tablename__



class Web_Ctrc_Caoa(Model):
    __tablename__ = 'web_ctrc_caoa'
    id_lista = Column(Integer,Sequence('web_ctrc_caoa_id_lista_seq'), primary_key=True)
    data_movimento = Column(Date)
    data_viagem = Column(Date)
    origem = Column(String(50))
    destino = Column(String(50))
    id_motorista = Column(Integer)
    placa_veiculo = Column(String(8))
    conferente = Column(String(50))
    status_listagem = Column(Numeric(1,0))

    def __repr__(self):
        return self.__tablename__



class Web_Ctrc_Caoa_Itens(Model):
    __tablename__ = 'web_ctrc_caoa_itens'
    id_lista_item = Column(Integer,Sequence('web_ctrc_caoa_itens_id_lista_item_seq'), primary_key=True)
    id_lista = Column(Integer)
    origem = Column(String(50))
    cnpj_destinatario = Column(String(18))
    nome_destinatario = Column(String(50))
    cidade_destino = Column(String(50))
    numero_nf = Column(String(10))
    valor_nf = Column(Numeric(10,2))
    qtd_volumes = Column(Numeric(4,0))
    peso_real = Column(Numeric(10,3))
    peso_cubico = Column(Numeric(10,4))

    def __repr__(self):
        return self.__tablename__



class Web_Login_Cd(Model):
    __tablename__ = 'web_login_cd'
    id_web_login = Column(Integer,Sequence('web_login_cd_id_web_login_seq'), primary_key=True)
    placa_veiculo = Column(String(8))
    senha = Column(String(15))
    ativo = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Web_Login_Cd_Log(Model):
    __tablename__ = 'web_login_cd_log'
    id_log_web_login = Column(Integer,Sequence('web_login_cd_log_id_log_web_login_seq'), primary_key=True)
    data_hora = Column(DateTime)
    id_web_login = Column(Integer)
    atividade = Column(String(60))

    def __repr__(self):
        return self.__tablename__



class Web_Login_Redespacho(Model):
    __tablename__ = 'web_login_redespacho'
    id_redespacho = Column(Integer,Sequence('web_login_redespacho_id_redespacho_seq'), primary_key=True)
    cnpj = Column(String(18))
    senha = Column(String(15))
    nivel_usuario = Column(Integer)

    def __repr__(self):
        return self.__tablename__



class Webtrack_Login(Model):
    __tablename__ = 'webtrack_login'
    id_webtrack_login = Column(Integer,Sequence('webtrack_login_id_webtrack_login_seq'), primary_key=True)
    login_name = Column(String(40))
    cnpj_cliente = Column(String(14))
    senha = Column(String(20))
    nivel_acesso = Column(Integer)
    acesso_raiz = Column(Integer)
    email = Column(text)

    def __repr__(self):
        return self.__tablename__

