import UsersRepository

class User:
    def __init__(self, name, birthdate, document, address, login, password):
        self.name = name
        self.birthdate = birthdate
        self.document = document
        self.address = address
        self.login = login
        self.password = password

    def register(self):
        repo = UsersRepository()
        self.repo.Insert(self)
