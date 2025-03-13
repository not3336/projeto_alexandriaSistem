from models.GeneroModel import GeneroModel

class GeneroController:
    @staticmethod
    def createGenero(nome: str):
        if not isinstance(nome, str) or not nome:
            return {
                'type':'Warning',
                'title':'Nome inválidos',
                'message':'O nome repassado é inválido ou está vazio.'
            }

        try:
            newGenero = GeneroModel(nome=nome)
            newGenero.save()
            return {
                'type':'Success',
                'title':'Novo gênero cadastrado',
                'message':f'O gênero {newGenero.nom} foi cadastrado com sucesso.'
            }
        except Exception as e:
            return {
                'type':'Error',
                'title':'Erro ao inserir genero',
                'message': f'Ocorreu o seguinte erro:\n{e}'
            }
    
    @staticmethod
    def getAllGeneros():
        try:
            generos = GeneroModel.select()
            return {
                'type':'Success',
                'generos': generos
            }
        except Exception as e:
            return {
                'type':'Error',
                'title':'Erro ao consultar Generos',
                'message':f'Ocorreu o seguinte erro:\n{e}'
            }

    @staticmethod
    def getGeneroById(id: int):
        if not isinstance(id, int) or id < 0:
            return {
                'type':'Warning',
                'title':'Id inválido',
                'message': 'O id informado não é um número ou é negativo'
            }
        try:
            genero = GeneroModel.get_or_none(GeneroModel.id == id)
            if isinstance(genero, None):
                return {
                    'type':'Warning',
                    'title':'Genero inexistênte',
                    'message':'Não existe nenhum genero com o id informado.'
                }
            return {
                'type':'Success',
                'genero': genero
            }
        except Exception as e:
            return {
                'type':'Error',
                'title':'Ocorreu um erro ao consultar genero',
                'message': str(e)
            }
        
    @staticmethod
    def deleteGeneroById(id: int):
        if not isinstance(id, int) or id < 0:
            return {
                'type':'Warning',
                'title':'Id inválido',
                'message': 'O id informado não é um número ou é negativo'
            }
        
        try:
            response = GeneroModel.getGeneroById(id)
            if response['type'] == 'Warning' or response['type'] == "Error":
                return response
            genero = response['genero']
            nome = genero.nome
            genero.delete_instance()
            return {
                'type':'Success',
                'title':'Genero excluido com sucesso',
                'message':f'O genero {nome} foi exluido com sucesso.'
            }
        except Exception as e:
            return {
                'type':'Error', 
                'title':'Ocorreu um erro ao excluir genero',
                'message': str(e)
            }
	
    @staticmethod
    def updateGenero(id: int, updateGenero: GeneroModel):
        if not isinstance(id, int) or id < 0:
            return {
                'type':'Warning',
                'title':'Id inválido',
                'message': 'O id informado não é um número ou é negativo'
            }
        
        if not isinstance(updateGenero, GeneroModel):
                return {
                    'type':'Warning',
                    'title':'Ocorreu uma incosistência nos dados',
                    'message':'Os dados enviados são inválidos ou estão inconsistentes'
                }

        try:
            response = GeneroModel.getGeneroById(id)
            if response['type'] == 'Warning' or response['type'] == "Error":
                return response
            genero = response['genero']

            if genero.nome != updateGenero.nome and GeneroModel.select().where(GeneroModel.nome == updateGenero.nome):
                return {
                    'type':'Warning', 
                    'title':'Genero já existente', 
                    'message':'Já existe um gênero com o nome informado.'
                }
            updateGenero.save()
            return {
                'type':'Success',
                'updateGenero': updateGenero
            }
        except Exception as e:
            return {
                'type':'Error', 
                'title':'Ocorreu um erro ao atualizar informações do gênero', 
                'message': str(e)
            }