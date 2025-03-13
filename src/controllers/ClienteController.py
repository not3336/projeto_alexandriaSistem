from models.ClienteModel import ClienteModel
class ClienteController:
	@staticmethod
	def createCliente(nome: str, cpf: str, telefone: str, email: str):
		warnings = []
		if not(nome and cpf and telefone):
			warnings.apend("Alguns dos campos obrigatórios está vazío!")
		if nome and len(nome) < 8:
			warnings.apend("O campo nome precisa conter no mínimo 8 caracteres.")
		if cpf and len(cpf)<11:
			warnings.apend("O CPF precisa conter 11 números.")
		if telefone and len(telefone) < 11:
			warnings.apend("O Telefone precisa conter 11 números.")

		if warnings:
			return {
				'type':'Warning', 
				'title':"Ocorreu algum(ns) problema(s)", 
				'message': '\n'.join(warnings) 
			}
		
		try:
			newCliente = ClienteModel(nome, cpf, telefone, email)
			newCliente = ClienteModel.save()
			return {
				'type':'success',
				'cliente': newCliente
			}
		except Exception as e:
			return {
				'type':'Error', 
				'title': "Ocorreu um erro ao inserir cliente",
				'message':str(e)
			}

	@staticmethod
	def getAllClientes():
		try:
			clientes = ClienteModel.select()
			return {
				'type':'Success',
				'clientes': clientes
			}
		except Exception as e:
			return {
				'type':"Error",
				'title':'Ocorreu um erro ao consultar clientes',
				'message': str(e)
			}
	
	@staticmethod
	def getClientesById(id: int):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}
		try:
			cliente = ClienteModel.get_or_none(ClienteModel.id == id)
			if isinstance(cliente, None):
				return {
					'type':'Warning',
					'title':'Cliente inexistênte',
					'message':'Não existe nenhum cliente com o id informado.'
				}
			return {
				'type':'Success',
				'cliente': cliente
			}
		except Exception as e:
			return {
				'type':'Error',
				'title':'Ocorreu um erro ao consultar cliente',
				'message': str(e)
			}
		
	@staticmethod
	def deleteClienteById(id: int):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}
		
		try:
			response = ClienteController.getClientesById(id)
			if response['type'] == 'Warning' or response['type'] == "Error":
				return response
			cliente = response['cliente']
			nome = cliente.nome
			cliente.delete_instance()
			return {
				'type':'Success',
				'title':'Cliente excluido com sucesso',
				'message':f'O cliente {nome} foi exluido com sucesso.'
			}
		except Exception as e:
			return {
				'type':'Error', 
				'title':'Ocorreu um erro ao excluir cliente',
				'message': str(e)
			}
	
	@staticmethod
	def updateCliente(id: int, updateCliente: ClienteModel):
		if not isinstance(id, int) or id < 0:
			return {
				'type':'Warning',
				'title':'Id inválido',
				'message': 'O id informado não é um número ou é negativo'
			}
		
		if not isinstance(updateCliente, ClienteModel):
				return {
					'type':'Warning',
					'title':'Ocorreu uma incosistência nos dados',
					'message':'Os dados enviados são inválidos ou estão inconsistentes'
				}

		try:
			response = ClienteController.getClientesById(id)
			if response['type'] == 'Warning' or response['type'] == "Error":
				return response
			cliente = response['cliente']

			if cliente.nome != updateCliente.nome and ClienteModel.select().where(ClienteModel.nome == updateCliente.nome):
				return {
					'type':'Warning', 
					'title':'Nome de Cliente existente', 
					'message':'Já existe um cliente com o nome informado.'
				}
			updateCliente.save()
			return {
				'type':'Success',
				'updateCliente': updateCliente
			}
		except Exception as e:
			return {
				'type':'Error', 
				'title':'Ocorreu um erro ao atualizar informações do cliente', 
				'message': str(e)
			}
