import peewee as pw
from services.connect import db
from datetime import datetime
from models.LivroModel import LivroModel as Livro
from models.UsuarioModel import UsuarioModel as Usuario
from models.ClienteModel import ClienteModel as Cliente
                
class ReservaModel(pw.Model):
    cliente = pw.ForeignKeyField(Cliente, backref='reservas')
    usuario = pw.ForeignKeyField(Usuario, backref='reservas')
    livro = pw.ForeignKeyField(Livro, backref='reservas')
    data_reserva = pw.DateField(default=datetime.now())
    
    class Meta:
        database = db