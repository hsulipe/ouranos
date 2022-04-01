from .User import User
from datetime import date
class Driver(User):
    def __init__ (
        self, 
        name: str, 
        birthdate: date, 
        document: str, 
        address: str
    ):
        super().__init__(
            name, 
            birthdate, 
            document, 
            address
        )
        self.type = "Admin"
        