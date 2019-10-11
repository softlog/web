from sqlalchemy import create_engine
from flask import render_template
from flask_login import current_user
from app import get_uri_db


class Filter:

    select = """
        SELECT	
            dest.nome_cliente as destinatario,
            dest.cnpj_cpf as cnpj_cpf_destinatario,
	        numero_nota_fiscal,
	        data_emissao,
	        status,
            '01' || lpad(fd_get_id_banco_dados(current_database())::text,5,'0') ||
            lpad(id_nota_fiscal_imp::text,12,'0') as codigo_rastreamento,
            oco.ocorrencia::character(50) as ocorrencia
        FROM 
	        scr_notas_fiscais_imp
        LEFT JOIN cliente as dest
            ON scr_notas_fiscais_imp.destinatario_id::integer = dest.codigo_cliente::integer
        LEFT JOIN scr_ocorrencia_edi as oco 
            ON oco.codigo_edi::integer = scr_notas_fiscais_imp.id_ocorrencia::integer

        """

    def connect(self, dados, ambiente):
        
        amb = ambiente
        engine = create_engine(get_uri_db(amb))
        conn = engine.connect()
        result_proxy = conn.execute(dados)
        results = result_proxy.fetchall()
        conn.close()

        return results

    def filter_by_numero_nota(self, nota, ambiente, limite=10000):
   
        dados = self.select + """
        WHERE
             numero_nota_fiscal = '{}'
        LIMIT {}
        """.format(nota.zfill(9), limite)

        return self.connect(dados, ambiente)

   
    def filter_by_destinatario(self, destinatario, ambiente, limite=10000):
   
        dados = self.select + """
        WHERE
            dest.nome_cliente LIKE '%%{}%%'
        LIMIT {}
        """.format(destinatario, limite)

        return self.connect(dados, ambiente)

    
    def filter_by_destinatario_cpf_cnpj(self, destinatario, ambiente, limite=10000):
   
        dados = self.select + """
        WHERE
            dest.cnpj_cpf LIKE '%%{}%%'
        LIMIT {}
        """.format(destinatario, limite)
       
        return self.connect(dados, ambiente)
   
    def filter_by_cpf_cnpj_nnota(self, destinatario, nota, ambiente, limite=10000):
   
        dados = self.select + """
        WHERE
            dest.cnpj_cpf LIKE '%%{}%%' 
            AND numero_nota_fiscal = '{}'
        LIMIT {}
        """.format(destinatario, nota.zfill(9), limite)

        return self.connect(dados, ambiente)