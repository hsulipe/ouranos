from .User import User
from datetime import date
from ..enums.StateEnum import StateEnum

class Passenger(User):
    def __init__ (
        self, 
        name: str, 
        birthdate: date, 
        document: str, 
        address: str, 
        city: str, 
        state: StateEnum
    ):
        super().__init__(
            name, 
            birthdate, 
            document, 
            address
        )
        self.type = "Passenger"
        self.city = city
        self.state = state
        