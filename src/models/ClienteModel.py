import peewee as pw
from services.connect import db

class ClienteModel(pw.Model):
    nome = pw.CharField()
    cpf = pw.CharField()
    telefone = pw.CharField()
    email = pw.CharField()
    
    class Meta:
        database = db