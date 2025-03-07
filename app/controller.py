from models import *

def getAllUsuarios():
    users = Usuario.select()
    return users

def insertUsuario(user):
    newUser = Usuario.create(**user)
    newUser.save()
    return newUser
