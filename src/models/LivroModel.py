import peewee as pw
from services.connect import db
from models.GeneroModel import GeneroModel as Genero
from models.AutorModel import AutorModel as Autor
 
class LivroModel(pw.Model):
    titulo = pw.CharField()
    autor = pw.ForeignKeyField(Autor, backref='livros')
    isbn = pw.CharField(unique=True)
    ano_publicacao = pw.IntegerField()
    genero = pw.ForeignKeyField(Genero, backref='livros')
    total_copias = pw.IntegerField()
    copias_disponiveis = pw.IntegerField()
    
    class Meta:
        database = db