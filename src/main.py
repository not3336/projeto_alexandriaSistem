from gui.MainGUI import MainGUI
from services.connect import db
from models.UsuarioModel import UsuarioModel
from models.ClienteModel import ClienteModel
from models.AutorModel import AutorModel
from models.GeneroModel import GeneroModel
from models.LivroModel import LivroModel
from models.ReservaModel import ReservaModel
from models.EmprestimoModel import EmprestimoModel

#Criar tabelas do banco de dados
#As tabelas são criadas apenas se não existirem
db.create_tables([UsuarioModel, ClienteModel, AutorModel, GeneroModel, LivroModel, ReservaModel, EmprestimoModel], safe=True)

MainGUI()