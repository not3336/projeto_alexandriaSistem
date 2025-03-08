import peewee as pw
from services.connect import db

class AutorModel(pw.Model):
    nome = pw.CharField()
    data_nasc = pw.DateField()
    nacionalidade = pw.CharField()
    
    class Meta:
        database = db