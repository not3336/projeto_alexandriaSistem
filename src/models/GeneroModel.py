import peewee as pw
from services.connect import db

class GeneroModel(pw.Model):
    nome = pw.CharField(unique=True)
    
    class Meta:
        database = db