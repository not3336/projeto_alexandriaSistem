import peewee as pw
from services.connect import db
        
class UsuarioModel(pw.Model):
    nome = pw.CharField()
    usuario = pw.CharField()
    senha = pw.CharField()
    
    class Meta:
        database = db