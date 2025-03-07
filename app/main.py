from guis.MainGUI import MainGUI
from connect import db
from models import *

db.create_tables([Usuario, Cliente, Autor, Genero, Livro, Reserva, Emprestimo], safe=True)
MainGUI()