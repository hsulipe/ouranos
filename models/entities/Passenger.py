from .User import User

class Passenger(User):
    def __init__ (
        self, 
        name, 
        birthdate, 
        document, 
        address, 
        city, 
        state
    ):
        super().__init__(
            name, 
            birthdate, 
            document, 
            address
        )
        
        self.city = city
        self.state = state
        