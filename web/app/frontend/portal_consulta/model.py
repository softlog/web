from sqlalchemy import create_engine
from flask import session
#from flask import g 
from flask_login import current_user
from app.util import format_dmy_to_ymd

class Filter:

    select = """
        SELECT	
	        rem.nome_cliente as remetente,
	        rem.cnpj_cpf cnpj_cpf_remetente,
            dest.nome_cliente as destinatario,
            dest.cnpj_cpf as cnpj_cpf_destinatario,
	        numero_nota_fiscal,
	        serie_nota_fiscal,
            chave_cte, 
	        chave_nfe,
	        data_emissao,
	        status,
            '01' || lpad(fd_get_id_banco_dados(current_database())::text,5,'0') ||
            lpad(id_nota_fiscal_imp::text,12,'0') as codigo_rastreamento,
            oco.ocorrencia::character(50) as ocorrencia
        FROM 
	        scr_notas_fiscais_imp
        LEFT JOIN cliente rem
            ON scr_notas_fiscais_imp.remetente_id::integer = rem.codigo_cliente::integer
        LEFT JOIN cliente dest
            ON scr_notas_fiscais_imp.destinatario_id::integer = dest.codigo_cliente::integer
        LEFT JOIN scr_ocorrencia_edi oco 
            ON oco.codigo_edi::integer = scr_notas_fiscais_imp.id_ocorrencia::integer

        """
    cnpj_cliente = current_user

    def connect(self, dados):
        
        ambiente = session.get("ambiente")

        #create_engine(dialect://username:password@host:port/database)
        engine = create_engine('postgresql://softlog_{}:paulino@pg.softlog.eti.br:5432/softlog_{}'.format(ambiente, ambiente))
        conn = engine.connect()
        result_proxy = conn.execute(dados)
        results = result_proxy.fetchall()
        conn.close()

        return results


    def filter_by_periodo(self, data1, data2, limite=10000):
   
        dados = self.select + """
        WHERE (rem.cnpj_cpf = '{}' OR dest.cnpj_cpf = '{}')
            AND data_emissao BETWEEN '{}' AND '{}'
        LIMIT {}
        """.format(self.cnpj_cliente, self.cnpj_cliente, format_dmy_to_ymd(data1), format_dmy_to_ymd(data2), limite)
 
        return self.connect(dados)

    def filter_by_numero_nota(self, nota, limite=10000):
   
        dados = self.select + """
        WHERE (rem.cnpj_cpf = '{}' OR dest.cnpj_cpf = '{}')
            AND numero_nota_fiscal = '{}'
        LIMIT {}
        """.format(self.cnpj_cliente, self.cnpj_cliente, nota.zfill(9), limite)

        return self.connect(dados)
   
    def filter_by_destinatario(self, destinatario, limite=10000):
   
        dados = self.select + """
        WHERE (rem.cnpj_cpf = '{}' OR dest.cnpj_cpf = '{}')
            AND  dest.nome_cliente LIKE '%%{}%%'
        LIMIT {}
        """.format(self.cnpj_cliente, self.cnpj_cliente, destinatario, limite)

        return self.connect(dados)


    def filter_by_chave_nfe(self, chave, limite=10000):
    
        ambiente = session.get("ambiente")

        dados = self.select + """
        WHERE (rem.cnpj_cpf = '{}' OR dest.cnpj_cpf = '{}')
            AND chave_nfe LIKE '%%{}%%'
        LIMIT {}
        """.format(self.cnpj_cliente, self.cnpj_cliente, chave, limite)
 
        return self.connect(dados)
    
    def filter_by_chave_cte(self, chave, limite=10000):
   
        dados = self.select + """
        WHERE (rem.cnpj_cpf = '{}' OR dest.cnpj_cpf = '{}')
            AND chave_cte LIKE '%%{}%%' AND chave_cte IS NOT NULL
        LIMIT {}
        """.format(self.cnpj_cliente, self.cnpj_cliente, chave, limite)

        return self.connect(dados)