from .RepositoryBase import RepositoryBase
class UsersRepository(RepositoryBase):
    def __init__(self, data = []):
        super.__init__(data)

    def FindIndex(self, cpf):
        return self.data.index(lambda x: x.cpf == cpf)

    def GetItem(self, document):
        for i in range(len(self.data)):
            if self.data[i].document == self.data[i].document:
                return self.data[i]
        return None