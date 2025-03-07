import peewee as pw
from connect import db
from datetime import datetime

class Cliente(pw.Model):
    nome = pw.CharField()
    cpf = pw.CharField()
    telefone = pw.CharField()
    email = pw.CharField()
    
    class Meta:
        database = db

class Autor(pw.Model):
    nome = pw.CharField()
    data_nasc = pw.DateField()
    nacionalidade = pw.CharField()
    
    class Meta:
        database = db

class Genero(pw.Model):
    nome = pw.CharField(unique=True)
    
    class Meta:
        database = db

class Livro(pw.Model):
    titulo = pw.CharField()
    autor = pw.ForeignKeyField(Autor, backref='livros')
    isbn = pw.CharField(unique=True)
    ano_publicacao = pw.IntegerField()
    genero = pw.ForeignKeyField(Genero, backref='livros')
    total_copias = pw.IntegerField()
    copias_disponiveis = pw.IntegerField()
    
    class Meta:
        database = db
        
class Usuario(pw.Model):
    nome = pw.CharField()
    usuario = pw.CharField()
    senha = pw.CharField()
    
    class Meta:
        database = db
        
class Emprestimo(pw.Model):
    cliente = pw.ForeignKeyField(Cliente, backref='emprestimos')
    usuario = pw.ForeignKeyField(Usuario, backref='emprestimos')
    livro = pw.ForeignKeyField(Livro, backref='emprestimos')
    data_emprestimo = pw.DateField(default=datetime.now())
    data_devolucao = pw.DateField(null=True)
    
    class Meta:
        database = db
        
class Reserva(pw.Model):
    cliente = pw.ForeignKeyField(Cliente, backref='reservas')
    usuario = pw.ForeignKeyField(Usuario, backref='reservas')
    livro = pw.ForeignKeyField(Livro, backref='reservas')
    data_reserva = pw.DateField(default=datetime.now())
    
    class Meta:
        database = db
        
