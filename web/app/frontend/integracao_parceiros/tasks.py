from app import celery
from celery.utils.log import get_task_logger

from app import app
import requests
import os
import time
from app import query_db_cursor
import requests
import json
from math import ceil

logger = get_task_logger(__name__)

@celery.task(bind=True,name='tasks.importa_docs_task')
def importa_docs_task(self,id_db,lst_notas, lst_clientes,id_db_main,acesso,tp_romaneio):
    """Background task that runs a long function with progress reports."""



    #print('id_db',id_db)
    #print('lst_notas',lst_notas)
    #print('lst_clientes',lst_clientes)
    #print('id_db_main',id_db_main)
    #print('acesso',acesso)
    #print('tp_romaneio',tp_romaneio)
    # Extrai dados do acesso
    total = 0
    partes = acesso.split('_')

    empresa = partes[0]
    filial = partes[1]
    id_usuario = partes[2]


    # 1 - Importacao dos clientes

    args = [lst_clientes]
    d = {
            'id_db':id_db,
            'lst_clientes':lst_clientes
    }

    quantidade = 30
    #url = "http://api.softlog.eti.br/api/logistica/clientes"
    url = "http://localhost:50000/api/logistica/clientes"

    logger.info('POST {0} '.format(url))

    #Obtem os dados dos clientes em json na base do contratante do frete
    r = requests.post(url,data=d)
    logger.info(r.text)

    nfes = lst_notas.split(',')

    #Grava dados dos clientes do parceiro na base de dados do sub-contratador
    if r.status_code in (200,201):
        clientes = json.loads(r.text)

        #total = len(cur_clientes)
        qt_partes = 20
        quantidade  = ceil(len(nfes)/qt_partes)

        bloco_clientes = [clientes[qt_partes*y:qt_partes*(y+1)] for y in range(quantidade)]
        i = 0
        total = len(bloco_clientes)

        for cliente in bloco_clientes:
            #message = cliente[0]['part_nome']
            dados = {
                        'id_db':id_db_main,
                        'dados': json.dumps(cliente),
                        'empresa':empresa,
                        'filial':filial,
                        'id_usuario':id_usuario
                    }
            logger.info('PUT {0} {1} '.format(url,dados))
            r = requests.put(url,data=dados)
            logger.info(r.text)

            self.update_state(state='EXECUTANDO',
                              meta={'current': i, 'total': total,
                                    'status':'Importando Clientes'})
            i = i + 1
    else:
        return self.update_state(state='Importacao Pendente',
                            meta={'current': total, 'total': total,
                                'status':'Servidor nao respondendo'})

    # 2 - Importacao das Notas Fiscais
    args = [lst_notas]
    d = {
            'id_db':id_db,
            'lst_notas':lst_notas,
            'tp_romaneio':tp_romaneio
    }

    #url = "http://api.softlog.eti.br/api/logistica/documentos_disponiveis"
    url = "http://localhost:50000/api/logistica/documentos_disponiveis"

    logger.info('POST {0} '.format(url))

    r = requests.post(url,data=d)
    i = 0
    logger.info('Status {0}'.format(r.status_code))
    logger.info('Resultado {0} '.format(r.text))

    if r.status_code in (200,201):
        nfes = json.loads(r.text)
        #qt_partes  = int(len(nfes)/quantidade)
        qt_partes = 20
        quantidade  = ceil(len(nfes)/qt_partes)

        bloco_nfes = [nfes[qt_partes*y:qt_partes*(y+1)] for y in range(quantidade)]
        i = 0
        total = len(bloco_nfes)

        for nf in bloco_nfes:
            #message = cliente[0]['part_nome']
            dados = {
                        'id_db':id_db_main,
                        'dados': json.dumps(nf),
                        'empresa':empresa,
                        'filial':filial,
                        'id_usuario':id_usuario,
                        'id_db_origem':id_db,
                        'tp_romaneio':tp_romaneio
                     }
            logger.info('PUT {0} {1} '.format(url,dados))
            r = requests.put(url,data=dados)
            self.update_state(state='EXECUTANDO',
                              meta={'current': i, 'total': total,
                                    'status':'Importando Notas Fiscais'})
            i = i + 1
    else:
        return self.update_state(state='Importacao Pendente',
                            meta={'current': total, 'total': total,
                                'status':'Servidor nao respondendo'})

    logger.info('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
    return {'current': i, 'total': total, 'status': 'Tarefa Concluida',
            'result': 'Documentos Importados'}





