# -*- coding: latin-1 -*-
#!/usr/bin/env python
import json 
from flask import Blueprint, request, jsonify, make_response, current_app
from flask_restful import Api, Resource, reqparse, marshal, abort
from psycopg2.extras import DictCursor
from app import query_db, get_db 
from app.api.model import filial_schema
from app.util import calcula_hash
#from app import mail
from flask_mail import Message
import traceback

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.utils import formatdate, make_msgid
from email import generator
from time import localtime, strftime
import smtplib
import re
from datetime import datetime
import time



from app.api.logistica.documentos import Usuarios, Romaneios, Imagens, Trackings
from app.api.logistica.model.ocorrencias import Ocorrencias
from app.api.logistica.model.notas_fiscais import NotasFiscaisModel
from app.api.logistica.model.veiculos import VeiculosModel
from app.api.logistica.model.motoristas import MotoristaModel
from app.api.logistica.model.protocolos import ProtocolosModel
from app.api.logistica.model.romaneios_app import RomaneiosAppModel
from app.api.logistica.model.regiao_cidades import RegiaoCidadesModel
from app.api.logistica.model.vuupt import VuuptModel

#from app import get_db, close_conection 

from marshmallow import ValidationError

softlog = Blueprint('softlog',__name__)

api = Api(softlog)


class SendMail(Resource):

    def post(self):

        a = request.args
        print(a)
        parser = reqparse.RequestParser()
        
        parser.add_argument('sender',type=str,help='O sender do email')
        parser.add_argument('titulo',type=str,help='O titulo do email')
        parser.add_argument('mensagem',type=str,help='Mensagem a ser enviada')
        parser.add_argument('email',type=str,help='O email para envio')
        
        args = parser.parse_args()

        sender = args.get("sender")
        titulo = args.get("titulo")
        mensagem = args.get('mensagem')
        email = args.get('email')

        #print(mensagem)
        #print(args.get('conferencias'))

        r = send_mail_anexo_sendgrid(sender, email,"",titulo, mensagem, None, None, None)
        
        #print("Resposta ",r)
        #r = 1
        if r == 0:
            operacao = 'ok'
        else:
            operacao = ''

        response = jsonify(operacao)

        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8088')

        return response







class Hello(Resource):

    def get(self):                    
        """Retorna Hello World"""
       
        return "Hello World" 

class Usuario(Resource):

    def get(self, codigo_acesso, login):                    
        """Retorna Dados do Usuario"""       
        #parser = reqparse.RequestParser()
        #parser.add_argument('codigo_acesso',type=int,help='Codigo de acesso obrigatório')
        #parser.add_argument('login',type=str,help='Login do usuário obrigatório')

        #args = parser.parse_args()
        
        r = Usuarios.get_user(login,codigo_acesso)

        if r is None:
            abort(404, message="Usuário {} não existe".format(login))
        else:
            return r, 200

class Usuario2(Resource):
    def get(self, codigo_acesso, cpf):
        r = Usuarios.get_user_fornecedor(cpf,codigo_acesso)

        if r is None:
            abort(404, message="Usuário {} não existe".format(cpf))
        else:
            return r, 200

class Protocolo(Resource):

    def get(self,codigo_acesso,data_expedicao,id_nf_protocolo):
        """Retorna lista de protocolos"""

        o = ProtocolosModel()

        r = o.get_protocolo(data_expedicao,id_nf_protocolo,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de protocolos")
        else:
            return r, 200


class Protocolo2(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('conferencias',type=str,help='O parâmetro conferências é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        conferencias = args.get('conferencias')
        #print(args.get('conferencias'))

        o = ProtocolosModel()
        r = o.setConferenciaProtocolo(codigo_acesso,conferencias)

        if r is None:
            abort(404, message="Não há documentos disponíveis.")

        return {"resultado":"Ok"}


class NotasFiscais(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

        parser.add_argument('tipo_busca',
                                type=int,
                                required=True, 
                                help='O parâmetro tipo_busca é inválido.')

        parser.add_argument('id_protocolo',
                                type=int,
                                help='O parâmetro id_protocolo é inválido.')

        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        id_protocolo = args.get('id_protocolo')
        tipo_busca = args.get('tipo_busca')
        #print(args.get('conferencias'))

        o = NotasFiscaisModel()
        if tipo_busca == 1:
            r = o.get_nota_fiscal_by_protocolo(id_protocolo,codigo_acesso)
        else:
            abort(404,'Tipo de Busca inexistente.')

        if r is None:
            abort(404, message="Não há documentos disponíveis.")
    
        return r,200

class Veiculos(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = VeiculosModel()
        r = o.get_veiculos(codigo_acesso)

        if r is None:
            abort(404, message="Não há veiculos registrados.")
    
        return r,200

class RegiaoCidades(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = RegiaoCidadesModel()
        r = o.get(codigo_acesso)

        if r is None:
            abort(404, message="Não há cidades com regiao na base de dados.")

        resposta = json.loads(r)

        h = calcula_hash(r)
        d = {
                    'data':resposta,
                    'ETag':h
            }

        h1 = request.headers.get('ETag')
        print(h1)
        if (h==h1):
            d = {
                'data':{'cidades':[], 'regioes':[]},
                'ETag':h
            }
                 
        return d,200
  
class Motoristas(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',
                                type=int,
                                required=True, 
                                help='O parâmetro codigo_acesso é inválido.')

       
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        
        #print(args.get('conferencias'))

        o = MotoristaModel()
        r = o.get_motoristas(codigo_acesso)

        if r is None:
            abort(404, message="Não há motoristas registrados.")
    
        return r,200

class RomaneiosApp(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('romaneios',type=str,help='O parâmetro romaneios é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        romaneios = args.get('romaneios')
        #print(args.get('conferencias'))

        o = RomaneiosAppModel()
        r = o.set(codigo_acesso,romaneios)
        
        if r is None:
            abort(404, message="Nao foi possivel gravar documentos")
        else:
            return {"resultado":"Ok"}, 200


class Romaneio(Resource):

    def get(self,codigo_acesso,data,cpf_motorista):
        """Retorna lista de protocolos"""      
                
        r = Romaneios.get_romaneios2(cpf_motorista,data,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de romaneios")
        else:
            return r, 200

class Romaneio2(Resource):

    def get(self,codigo_acesso,data,cpf_motorista):
        """Retorna lista de protocolos"""      
                
        r = Romaneios.get_romaneios2(cpf_motorista,data,codigo_acesso)

        if r is None:
            abort(404, message="Nao há registro de romaneios")
        else:
            return r, 200


class Ocorrencia(Resource):

    def get(self,codigo_acesso):
        """Retorna lista de ocorrências"""      
                
        r = Ocorrencias.getOcorrencias(codigo_acesso)

        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return r, 200


class Ocorrencias2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('ocorrencias',type=str,help='O parâmetro ocorrencias é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        ocorrencias = args.get('ocorrencias')
        #print(args.get('conferencias'))

        r = Ocorrencias.setOcorrencias(codigo_acesso,ocorrencias)
        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return {"resultado":"Ok"}, 200
        

class Imagem(Resource):
        
    def get(self,codigo_acesso,imagem):
        
        r = Imagens.getImagem(codigo_acesso,imagem)

        if r is None:
            abort(404, message="Nao há ocorrências")
        else:
            return r, 200

class Imagem2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('imagens',type=str,help='O parâmetro imagens é inválido.')
        
        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        imagens = args.get('imagens')
        #print(args.get('conferencias'))

        r = Imagens.setImagens(codigo_acesso,imagens)

        if r is None:
            abort(404, message="Ocorreu um erro ao persistir informacoes")

        return {"resultado":"Ok"}

class Tracking(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('codigo_acesso',type=int,help='O parâmetro codigo_acesso é inválido.')
        parser.add_argument('tracking',type=str,help='O parâmetro tracking é inválido.')

        args = parser.parse_args()

        codigo_acesso = args.get('codigo_acesso')
        tracking = args.get('tracking')
        #print(args.get('conferencias'))

        r = Trackings.setTracking(codigo_acesso,tracking)

        if r is None:
            abort(404, message="Ocorreu um erro ao persistir informacoes")
        
        return {"resultado":"Ok"}

class VuuptOcorrencia(Resource):
    def post(self):
        
        # data in string format and you have to parse into dictionary
        data = request.data.decode()
        #dataDict = json.loads(data)
        print(data)
        
        
        VuuptModel.set_vuupt_ocorrencias(self,53, data)
        return {"resultado":"Ok"}



def send_mail_anexo_sendgrid(p_sender,p_recipients,p_cc,p_subject,p_message,p_filename_anexo,p_stream_anexo, p_nome_msg):

    # Date: 26/04/2006
	# Retorno: 	0 - Envio Ok.
	#		1 - Nao foi possivel conectar ao servidor de email
	#		2 - Falha de autenticao
	#		3 - Falha de envio.

    
    vSender         = p_sender
    vRecipients     = p_recipients
    vRecipients     = vRecipients.replace(';',',')
    #vRecipients     = 'paulo.sergio@softlog.eti.br,nilton.paulino@softlog.eti.br,paulo.sergio.softlog@gmail.com'
    vCc             = p_cc
    vSubject        = p_subject
    vMessage        = p_message
    vNomeAnexo      = p_filename_anexo
    vConteudoAnexo  = p_stream_anexo


    smtpserver = 'smtp.sendgrid.net'
    AUTHREQUIRED = 1 			  # if you need to use SMTP AUTH set to 1
    smtpuser = 'softlogtecnologia'  	  # for SMTP AUTH, set SMTP username here
    smtppass = 'softrans321@foxtotal'  		  # for SMTP AUTH, set SMTP password here
    try:
        server = smtplib.SMTP(smtpserver, port=587)
    except:
        #print(traceback.format_exc())
        return 1

    msg = MIMEMultipart('related')
    msg['Subject'] = vSubject
    msg['Date'] = strftime("%a, %d %b %Y %H:%M:%S -0300", localtime())
    msg['Cc'] = vCc
    msg['From'] = vSender
    msg['To'] = vRecipients

    msg.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    # Expressao regular de http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/440481

    t = re.sub("< */? *\w+ */?\ *>", "", vMessage)
    msgText = MIMEText(t)
    msgAlternative.attach(msgText)

    msgText = MIMEText(vMessage,'html','utf-8')
    msgAlternative.attach(msgText)

    if vNomeAnexo is not None and vConteudoAnexo is not None:
        header = 'Content-Disposition', 'attachment; filename="%s"' % vNomeAnexo
        anexo = MIMEBase('application',"octet-stream")
        anexo.set_payload(bytes(vConteudoAnexo,'utf-8'))
        encode_base64(anexo)
        anexo.add_header(*header)
        msg.attach(anexo)

    if vNomeAnexo is not None and vConteudoAnexo is None:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(vNomeAnexo, "rb").read())
        encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'%vNomeAnexo)
        msg.attach(part)


    vRetorno = ''

    if AUTHREQUIRED:
        try:
            server.login(smtpuser, smtppass)
        except socket.error as erro:
            print(traceback.format_exc())
            vRetorno = 2

        listaR = vRecipients.split(',')
        listaR = [ x.strip() for x in listaR]
        try:
            smtpresult = server.sendmail(vSender, listaR, msg.as_string())
        except Exception as e:
            print(traceback.format_exc())
            #print('Falha de envio')
            return 3
##            for recipient in listaR:
##                smtpresult = server.sendmail(vSender, recipient.strip(), msg.as_string())
##                print ("Enviando email para ",recipient.strip())
##                vRetorno = 0


    server.quit()
    return 0


api.add_resource(Hello,'/hello')
api.add_resource(Usuario,'/usuario/<int:codigo_acesso>/<login>')
api.add_resource(Usuario2,'/usuario2/<int:codigo_acesso>/<cpf>')
api.add_resource(Protocolo,'/protocolo/<int:codigo_acesso>/<data_expedicao>/<int:id_nf_protocolo>')
api.add_resource(Protocolo2,'/protocolo')
##api.add_resource(NotasFiscais,'/notasromaneio/<int:codigo_acesso>/<int:id_protocolo>')
api.add_resource(NotasFiscais,'/notasromaneio')
api.add_resource(Veiculos,'/veiculos')
api.add_resource(RegiaoCidades,'/regiao_cidades')
api.add_resource(Motoristas,'/motoristas')
api.add_resource(RomaneiosApp,'/romaneiosapp')
api.add_resource(Romaneio,'/romaneio/<int:codigo_acesso>/<data>/<cpf_motorista>')
api.add_resource(Romaneio2,'/romaneio2/<int:codigo_acesso>/<data>/<cpf_motorista>')
api.add_resource(Ocorrencia,'/ocorrencia/<int:codigo_acesso>')
api.add_resource(Ocorrencias2,'/ocorrencia')
api.add_resource(Imagem2,'/imagem')
api.add_resource(Tracking,'/tracking')
api.add_resource(VuuptOcorrencia,'/vuupt/ocorrencias')
api.add_resource(SendMail,'/send_mail')
