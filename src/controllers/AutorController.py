from models.AutorModel import AutorModel
from datetime import datetime

class AutorController:

	@staticmethod
	def createAutor(nome: str, dataNascimento: str, nacionalidade: str):
		warnings = []
		if not(nome and dataNascimento and nacionalidade):
			warnings.append('Alguns dos campos obrigatórios estão vazíos!')
		if nome and len(nome) < 8:
			warnings.append('O campo nome precisa conter no mínimo 8 caracteres.')
		if nacionalidade and len(nacionalidade) < 5:
			warnings.append('O campo nacionalidade precisa conter no mínimo 8 caracteres.')
		if dataNascimento:
			try:
				datetime.strptime(dataNascimento, '%d/%m/%Y')
			except Exception as e:
				warnings.append('A data de nascimento informada é inválida.')

		if warnings:
			return {
				'type':'Warning',
				'title':'Houve alguns problemas ao cadastrar.',
				'message': "\n".join(warnings)
			}
		
		try:
			newAutor = AutorModel(nome=nome, data_nasc=dataNascimento,nacionalidade=nacionalidade)
			newAutor.save()
			return {
				'type':'Success',
				'title':'Autor cadastrado com sucesso',
				'message': f'O Autor {newAutor.nome} foi criado com sucesso',
				'autor': newAutor
			}
		except Exception as e:
			return {
				'type':'Error',
				'title':'Erro ao inserir autor', 
				'message': str(e)
			}

	@staticmethod
	def getAllAutores():
		try:
			autores = AutorModel.select()
			return {
				'type':'Success', 
				'autores':autores
			}
		except Exception as e:
			return {
				'type':'Error',
				'title':'Erro ao buscar autores',
				'message': str(e)
			}

	@staticmethod
	def getAutorById(id: int):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}

		try:
			autor = AutorModel.get_or_none(AutorModel.id == id)
			if autor == None:
				return {
					'type':'Warning',
					'title':'Autor não existe',
					'message':'Nenhum Autor associada ao ID informado'
				}
			return {
				'type':'Success', 
				'autor':autor
			}
		except Exception as e:
			return {
				'type':'Error', 
				'title':'Ocorreu um erro ao consultar autor',
				'message': str(e)
			}
	@staticmethod
	def deleteAutor(id: int):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}
		try:
			response = AutorController.getAutorById(id)
			if response['type'] == 'Error' or response['type'] == 'Warning':
				return response
			autor = response['autor']
			autor.delete_instance()
			return {
				'type':'Success', 
				'title':'Sucesso ao excluir autor',
				'message':'Autor deletado com sucesso'
			}
		except Exception as e:
			return {
				'type':'Error', 
				'title':'Ocorrreu um erro ao deletar autor',
				'message': str(e)
			}

	@staticmethod
	def updateAutor(id: int, autorUpdate: AutorModel):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}
		
		if not isinstance(autorUpdate, AutorModel):
				return {
					'type':'Warning',
					'title':'Ocorreu uma incosistência nos dados',
					'message':'Os dados enviados são inválidos ou estão inconsistentes'
				}
		try:
			response = AutorController.getAutorById(id)
			if response['type'] == 'Error' or response['type'] == 'Warning':
				return response
			autor = response['autor']
			if autorUpdate.nome != autor.nome and AutorModel.select().where(AutorModel.nome == autorUpdate.nome):
				return {
					'type':'Warning',
					'title':'Nome de autor já existe',
					'message':'Já existe um autor com esse mesmo nome.'
				}
			autorUpdate.save()
			return {
				'type':'Success',
				'title':'Autor alterado com sucesso',
				'message':'Os dados do autor foram atualizados.'
			}
		except Exception as e:
			return {
				'type':'Error',
				'title':'Ocorrreu um erro ao atualizar informações do autor',
				'message': str(e)
			}

