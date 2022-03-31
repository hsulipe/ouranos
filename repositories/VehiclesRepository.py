from .RepositoryBase import RepositoryBase
class VehiclesRepository(RepositoryBase):
    def __init__(self, data = []):
        super().__init__(data)
    
    def FindIndex(self, plate: str):
        for i in range(len(self.data)):
            if self.data[i].plate == plate:
                return i
        return -1