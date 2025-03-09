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
	def getAutorById(id):
		try:
			autor = AutorModel.get_or_none(AutorModel.id == id)
			if autor == None:
				return {'type':"Warning", 'title':"Autor não existe", 'message':"Nenhum Autor associada ao ID informado"}
			return {'type':"Success", 'autor':autor}
		except Exception as e:
			return {'type':"Error", 'title':"Ocorreu um erro ao consultar autor", 'message': [str(e)]}
	@staticmethod
	def deleteAutor(id):
		try:
			autor = AutorModel.get_or_none(AutorModel.id == id)
			if autor == None:
				return {'type':"Warning", 'title':"Autor não existe", 'message':"Nenhum Autor associada ao ID informado"}
			autor.delete_instance()
			return {'type':"Success", 'title':"Sucesso ao excluir autor", 'message':"Autor deletado com sucesso"}
		except Exception as e:
			return {'type':"Error", 'title':"Ocorrreu um erro ao deletar autor", 'message': [str(e)]}

	@staticmethod
	def updateAutor(id, autorUpdate):
		try:
			autor = AutorModel.get_or_none(AutorModel.id == id)
			if autor == None:
				return {'type':"Warning", 'title':"Autor não existe", 'message':"Nenhum Autor associada ao ID informado"}
			if not isinstance(autorUpdate, AutorModel):
				return {'type':"Warning", 'title':"Ocorreu uma incosistência nos dados", 'message':"Não foram informados todos os dados do autor"}
			if len(AutorModel.select().where(AutorModel.nome == autorUpdate.nome)) > 0:
				return {'type':"Warning", 'title':"Nome de autor já existe", 'message':"Já existe um autor com esse mesmo nome."}
			autorUpdate.save()
			return {'type':"Success", 'title':"Autor alterado com sucesso", 'message':"Os dados do autor foram atualizados."}
		except Exception as e:
			return {'type':"Error", 'title':"Ocorrreu um erro ao atualizar informações do autor", 'message': [str(e)]}

