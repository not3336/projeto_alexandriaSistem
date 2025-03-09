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
	response = AutorController.getAllAutores()
	autores = response['autores']
	for autor in autores:
		print(f"ID: {autor.id}, Nome:{autor.nome}, Data_Nasc: {autor.data_nasc}, Nacionalidade: {autor.nacionalidade}.")
def deleteAutorTest():
	response = AutorController.deleteAutor(8)
	print(response)

def updateAutorTest():
	response = AutorController.getAutorById(1)
	autorUpdate = response['autor']
	autorUpdate.nome = "Nieli de Jesus Mota Neres"

	response = AutorController.updateAutor(2, autorUpdate)
	print(response)

getAllAutoresTest()
#updateAutorTest()