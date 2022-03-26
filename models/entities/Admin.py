from .User import User

class Admin(User):
    def __init__(
        self, 
        name, 
        birthdate, 
        document, 
        address, 
        login=None, 
        password=None
    ):
        super().__init__(
            name, 
            birthdate, 
            document, 
            address
        )
        self.login = login
        self.password = password
