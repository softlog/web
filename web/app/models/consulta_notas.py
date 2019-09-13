import psycopg2
import psycopg2.extensions
from psycopg2.extras import DictCursor

class ConsultaNotas(object):
    def get_nf(self):
        str_sql = """
        select
	        nf.id_nota_fiscal_imp,
	        nf.chave_nfe,
	        nf.serie_nota_fiscal,
	        nf.numero_nota_fiscal,
	        nf.data_emissao,
	        nf.remetente_id,
	        r.nome_cliente as remetente_nome,
	        rc.nome_cidade as remetente_cidade,
	        rc.uf as remetente_uf,
	        nf.destinatario_id,
	        d.nome_cliente as destinatario_nome,
	        dc.nome_cidade as destinatario_cidade,
	        dc.uf as destinatario_uf,
	        nf.valor

        from scr_notas_fiscais_imp nf
        left join cliente r
	        ON r.codigo_cliente = nf.remetente_id
        left join cidades rc ON rc.id_cidade = r.id_cidade
        left join cliente d
	        ON d.codigo_cliente = nf.destinatario_id
        left join cidades dc ON dc.id_cidade = d.id_cidade
        limit 100"""

        string_conexao = 'dbname=softlog_bsb2 user=softlog_bsb2 port=5432 password=paulino host=pg.softlog.eti.br'

        conn = psycopg2.connect(string_conexao)

        cursor = conn.cursor(cursor_factory=DictCursor)

        cursor.execute(str_sql)
        resultado = cursor.fetchall()

        cursor.close()

        conn.close()

        return resultado

