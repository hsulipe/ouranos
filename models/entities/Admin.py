from .User import User
from datetime import date
class Admin(User):
    def __init__(
        self, 
        name: str, 
        birthdate: date, 
        document: str, 
        address: str, 
        login: str = None, 
        password: str = None
    ):
        super().__init__(
            name, 
            birthdate, 
            document, 
            address
        )
        self.type = "Admin"
        self.login = login
        self.password = password
