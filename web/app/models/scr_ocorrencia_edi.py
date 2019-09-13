from sqlalchemy import Table, Column, Integer, String, ForeignKey,Date, Text, Numeric, DateTime, Sequence
from sqlalchemy.sql import func
from sqlalchemy.orm import synonym
from app.sqla import Model, Base

from app import db, app

class ScrOcorrenciaEdi(Model):
    __tablename__ = 'scr_ocorrencia_edi'
    
    id_scr_ocorrencia_edi = Column(Integer,Sequence('scr_ocorrencia_edi_id_scr_ocorrencia_edi_seq'), primary_key=True )
    id = synonym('id_scr_ocorrencia_edi')
    codigo_edi = Column(Integer)     
    ocorrencia = Column(String(150))



