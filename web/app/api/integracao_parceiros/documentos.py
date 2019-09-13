from app import query_db, execute_db
from app.api.integracao_parceiros.model import qry_db, qry_participantes,\
            qry_qt_docs, qry_lst_participantes, qry_nf, qry_nf2, qry_lst_participantes_2, \
            qry_cte, qry_upd_baixa_nfe 

class Documentos(object):


    def get_docs_disponiveis(id_db,cnpj,data,acesso):
        qry_parceiros = """
            SELECT 
                string_agg('''' || trim(cnpj_cpf) || '''',',') as lst_cnpj
            FROM 
                fornecedores
            WHERE 
                tipo_parceiro = 1
        """
                
        parceiros = query_db(int(id_db),qry_parceiros)
        
        parceiro = parceiros[0]
               
        if len(parceiro) == 0:
            return None
        
        bds = query_db(1,qry_db % (parceiro['lst_cnpj']))

        movimentos = []
        id = 0
        for bd in bds:            
            d = {}
            ## Recupera a lista de clientes envolvidos
            dados = {'data':data,'cnpj':cnpj}            
            d['id_bd']          = bd['id_bd']
            d['cnpj']           = bd['cnpj_cpf']
            d['razao_social']   = bd['razao_social']
            d['id_db_main']     = id_db 
            d['acesso']         = acesso


            ## Recupera a quantidade e a lista de documentos disponiveis
            row = query_db(bd['id_bd'],qry_qt_docs % ({'data':data,'cnpj':cnpj}),None,True)
            id = id + 1;
            if len(row) == 0:
                d['qt_docs']        = 0
                d['lst_notas']      = '0'
                d['tp_romaneio']    = 0
            else:
                d['qt_docs']        = row['qt']
                if row['lst_notas'] is None:
                    d['lst_notas']      = '0'
                else:
                    d['lst_notas']      = row['lst_notas']

                d['tp_romaneio']    = row['tp_romaneio']

            ## Obtem lista de participantes (clientes)            
            if d['tp_romaneio'] == 1:
                row_cli = query_db(bd['id_bd'],qry_lst_participantes % dados,None,True)                                
            else:
                row_cli = query_db(bd['id_bd'],qry_lst_participantes_2 % dados,None,True)
                
            if row_cli['lst_clientes'] is None:
                d['lst_clientes'] = '0'
            else:
                d['lst_clientes'] = row_cli['lst_clientes']
            
            movimentos.append(d)

        resultado = {'documentos_disponiveis':movimentos}
        return resultado

    def get_json_clientes(id_db,lst_clientes):
        cmd = qry_participantes%({'lst_clientes':lst_clientes})

        #print(cmd)
        clientes = query_db(id_db,cmd)

        if len(clientes) == 0:
            return None
        else:
            resultado = clientes
            return resultado

    def get_json_notas(id_db,lst_notas,tp_romaneio=1):

        if tp_romaneio == 1:
            cmd = qry_nf % (lst_notas)
        else:
            cmd = qry_nf2 % (lst_notas)

        #print(cmd)        
        nfes = query_db(id_db,cmd)

        if len(nfes) == 0:
            return None
        else:
            resultado = nfes
            return resultado


    def insere_clientes(id_db,dados):
        import json 

        clientes = json.loads(dados)
        resultado = []        
        for cliente in clientes:
            #print('###############################',str(cliente))
            cmd = """
                    BEGIN;
                    SELECT f_insere_cliente('%s'::json) as cliente;
                    COMMIT;
                """ % (json.dumps(cliente[0]))

            try:
                r = execute_db(id_db,cmd)
            except Exception as e:
                r = None
                            
            resultado.append(r)

        return resultado


    def insere_nf(id_db,dados,id_usuario,empresa,filial, id_db_origem,tp_romaneio):
        import json 
        nfes = json.loads(dados)
        resultado = []                
        for nfe in nfes:
            #print(str(nfe[0]))
            try:
                r = execute_db(id_db,'BEGIN')            
                cmd = """                    
                        SELECT f_insere_nf_parceiros('%s'::json,%s,'%s','%s') as nf;                    
                    """ % (json.dumps(nfe[0]),id_usuario,empresa,filial)

                r = query_db(id_db,cmd)
                
                nova_nf = r[0]['nf']
                nf_origem = nfe[0]['id_nota_fiscal_imp']
                if nf_origem != '0':
                    if tp_romaneio == 1:
                        cmd_conf = """
                                        BEGIN;
                                        UPDATE scr_notas_fiscais_imp 
                                                SET id_nota_fiscal_redespachador = %s
                                        WHERE id_nota_fiscal_imp = %s;
                                    """ % (str(nova_nf), str(nf_origem))
                    else:
                        cmd_conf = """
                                        BEGIN;
                                        UPDATE scr_conhecimento_notas_fiscais 
                                                SET id_nota_fiscal_redespachador = %s
                                        WHERE id_conhecimento_notas_fiscais = %s;
                                    """ % (str(nova_nf), str(nf_origem))

                #print('COMANDO EMITIDO',cmd_conf)
                r = execute_db(id_db_origem,cmd_conf)
                r = execute_db(id_db_origem,'COMMIT')
                r = execute_db(id_db,'COMMIT')                

            except Exception as e:
                r = execute_db(id_db,'ROLLBACK')
                r = execute_db(id_db_origem,'ROLLBACK')            
            
            resultado.append(r)

        return resultado
    
    def get_chaves_cte(lst_id_nfs, parceiro_cnpj, redespachador_cnpj):        
        #Identifica o id do banco de dados do parceiro

        cmd = qry_db % ("'" + parceiro_cnpj.strip() + "'")
                
        r = query_db(1,cmd)       

        if len(r) > 0:
            id_db_parceiro = r[0]['id_bd']            
        else:            
            return ''

        cmd = qry_cte % (lst_id_nfs,redespachador_cnpj)
        nfes = query_db(id_db_parceiro,cmd)

        
        if len(nfes) == 0:
            return ''

        
        lista_chaves = []        
        for nf in nfes:      
            print(nf['chave_cte'])
            lista_chaves.append(str(nf['id_nota_fiscal_imp']) + '_' + nf['chave_cte'])

        #print('Lista Chaves', str(lista_chaves))

        return ','.join(lista_chaves)
    
    def set_baixa_entrega_nfe(args):
        """Realiza Baixa de Entregas"""
        cmd = qry_db % ("'" + parceiro_cnpj.strip() + "'")
                        
        r = query_db(1,cmd)

        if len(r) > 0:
            id_db = r[0]['id_bd']
        else:            
            return ''

        cmd_upd = qry_upd_baixa_nfe % (args)
        r = query_db(id_db,cmd_upd)
        
        if r is not None:
            pass

        return r['numero_nota_fiscal']
