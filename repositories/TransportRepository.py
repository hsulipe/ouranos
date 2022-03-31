from .RepositoryBase import RepositoryBase

class TransportRepository(RepositoryBase):
    def __init__(self, data = []):
        super().__init__(data)
    
    def FindIndex(self, plate: str, document: str):
        for i in range(len(self.data)):
            if self.data[i].passenger_document == document and self.data[i].plate == plate:
                return i
        return -1