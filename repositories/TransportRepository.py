from .RepositoryBase import RepositoryBase

class TransportRepository(RepositoryBase):
    def __init__(self, data = []):
        super.__init__(data)
    
    def FindIndex(self, plate: str, cpf):
        return self.data.index(lambda x: x.cpf == cpf and x.plate == plate)