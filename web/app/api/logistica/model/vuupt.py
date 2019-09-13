from app import query_db, execute_db
import socket

class VuuptModel(object):

    def set_vuupt_ocorrencias(self,id_acesso, data):
        
        sql_ins = """INSERT INTO vuupt_tmp (dados) VALUES ('%s')""" % data.replace("'","'")

        if isOpen('187.72.51.13','5432'):
            execute_db(id_acesso,"begin")
            execute_db(id_acesso,sql_ins)
            execute_db(id_acesso,"commit")


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.settimeout(4)
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

