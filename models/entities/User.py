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
        if repo == None or repo.Exists(self.document):
            return False
        
        repo.Put(self)
        return self