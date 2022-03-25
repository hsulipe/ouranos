import User

class Driver(User):
    def __init__ (
        self, 
        name, 
        birthdate, 
        document, 
        address
    ):
        super().__init__(name, birthdate, document, address)
        