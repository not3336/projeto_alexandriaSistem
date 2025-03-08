import sys
import os

# Adiciona a pasta2 ao caminho do sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers.AutorController import AutorController
from datetime import datetime
#OK
def insertAutorTest():
	data = ["Carlos Alberto Sales", datetime.strptime("12/05/1958", "%d/%m/%Y"), "Brasileiro"]

	response = AutorController.createAutor(*data)
	print(response)
#OK
def getAllAutoresTest():
	autores = AutorController.getAllAutores()
	for autor in autores:
		print(f"Nome:{autor.nome}, Data_Nasc: {autor.data_nasc}, Nacionalidade: {autor.nacionalidade}.")

getAllAutoresTest()