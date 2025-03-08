from models.ClienteModel import ClienteModel
class ClienteController:
	@staticmethod
	def createCliente(nome, cpf, telefone, email):
		warnings = []
		errors = []
		if nome and cpf and telefone:
			warnings.apend("Alguns dos campos obrigatórios está vazío!")
		if len(nome) < 8:
			warnings.apend("O campo nome precisa conter no mínimo 8 caracteres.")
		if len(cpf)<11:
			warnings.apend("O CPF precisa conter 11 números.")
		if len(telefone) < 11:
			warnings.apend("O Telefone precisa conter 11 números.")

		if len(warnings) > 0:
			return {'type':'warning', 'warnings': warnings }
		else:
			try:
				newCliente = ClienteModel(nome, cpf, telefone, email)
				newCliente = ClienteModel.save()
				return {'type':'success', 'cliente': newCliente}
			except Exception as e:
				error.append(str(e))
				return {'type':'error', 'errors': errors }

	@staticmethod
	def getAllClientes():
		try:
			clientes = ClienteModel.select()
			return clientes
		except Exception as e:
			pass
