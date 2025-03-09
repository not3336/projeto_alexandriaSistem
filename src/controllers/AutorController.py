from models.AutorModel import AutorModel
from datetime import datetime

class AutorController:

	@staticmethod
	def createAutor(nome, dataNascimento, nacionalidade):
		warnings = []
		errors = []
		if not(nome and dataNascimento and nacionalidade):
			warnings.append("Alguns dos campos obrigatórios estão vazíos!")
		if len(nome) < 8:
			warnings.append("O campo nome precisa conter no mínimo 8 caracteres.")
		if len(nacionalidade) < 5:
			warnings.append("O campo nacionalidade precisa conter no mínimo 8 caracteres.")
		if dataNascimento:
			try:
				datetime.strptime(dataNascimento, "%d/%m/%Y")
			except Exception as e:
				warnings.append("A data de nascimento informada é inválida.")

		if len(warnings) > 0:
			return {'type':'Warning',"title":"Houve alguns problemas ao cadastrar.", 'message': warnings }
		else:
			try:
				newAutor = AutorModel(nome=nome, data_nasc=dataNascimento,nacionalidade=nacionalidade)
				newAutor.save()
				return {'type':'Success', 'title':"Autor cadastrado com sucesso",'message': [f"O Autor {newAutor.nome} foi criado com sucesso"],
					'autor': newAutor}
			except Exception as e:
				errors.append(str(e))
				return {'type':'Error', 'title':"Erro ao inserir autor", 'message': errors }

	@staticmethod
	def getAllAutores():
		try:
			autores = AutorModel.select()
			return {'type':"Success", 'autores':autores}
		except Exception as e:
			return {'type':"Error", 'title':"Erro ao buscar autores", 'message': [str(e)]}

	@staticmethod
	def deleteAutor(id):
		try:
			autor = AutorModel.get(AutorModel.id == id)
			autor.delete_instance()
			return True
		except Exception as e:
			return False
