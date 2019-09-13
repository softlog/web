import json
from app import query_db, execute_db

class RomaneiosAppModel(object):

    def set(self,codigo_acesso, romaneios):

        dados = json.loads(romaneios)
        if len(dados) == 0:
            return None

        comandos = []
        for romaneio in dados:                       

            romaneio['lst_notas'] = ','.join([ str(x) for x in romaneio["notas_fiscais"]])

            sql_romaneio = """
            INSERT INTO edi_romaneios (
                codigo_empresa,
                codigo_filial,
                placa_veiculo,
                id_motorista,
                data_romaneio,
                tipo_destino,
                id_origem,
                id_destino,
                id_setor,
                data_registro,
                id_usuario,                
                lst_notas
            ) VALUES (
                '001',
                '001',
                '%(placa_veiculo)s',
                %(id_motorista)i,
                '%(data_romaneio)s',
                'D',
                %(id_origem)i,
                %(id_destino)i,
                %(id_setor)i,
                now(),
                %(id_usuario)i,                
                '{%(lst_notas)s}'
            )""" % romaneio


            comandos.append(sql_romaneio)

        sql = ";".join(comandos)
        try:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
        except:
            execute_db(codigo_acesso,'begin')
            execute_db(codigo_acesso,sql)
            execute_db(codigo_acesso,'commit;')
            return None
        
        return comandos

