import peewee as pw
from services.connect import db
from datetime import datetime
from models.LivroModel import LivroModel as Livro
from models.UsuarioModel import UsuarioModel as Usuario
from models.ClienteModel import ClienteModel as Cliente
                
class EmprestimoModel(pw.Model):
    cliente = pw.ForeignKeyField(Cliente, backref='emprestimos')
    usuario = pw.ForeignKeyField(Usuario, backref='emprestimos')
    livro = pw.ForeignKeyField(Livro, backref='emprestimos')
    data_emprestimo = pw.DateField(default=datetime.now())
    data_devolucao = pw.DateField(null=True)
    
    class Meta:
        database = db