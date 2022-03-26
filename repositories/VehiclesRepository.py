from .SingletonMeta import SingletonMeta

class VehiclesRepository(metaclass=SingletonMeta):
    def __init__(self, data = []):
        self.data = data
    
    