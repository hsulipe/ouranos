from datetime import date
from ...repositories.UsersRepository import UsersRepository
class User:
    def __init__(
        self, name: str, 
        birthdate: date, 
        document: str, 
        address: str 
    ):
        self.name = name
        self.birthdate = birthdate
        self.document = document
        self.address = address

    def Register(
        self, 
        repo: UsersRepository
    ):
        self.type = type(self)
        if repo == None or repo.exists(self.cpf):
            return False
        
        repo.Insert(self)
        return self