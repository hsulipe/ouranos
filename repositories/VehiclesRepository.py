from .RepositoryBase import RepositoryBase
class VehiclesRepository(RepositoryBase):
    def __init__(self, data = []):
        super.__init__(data)
    
    def FindIndex(self, plate: str):
        return self.data.index(lambda x: x.plate == plate)