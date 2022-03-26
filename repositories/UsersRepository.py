from .SingletonMeta import SingletonMeta

class UsersRepository(metaclass=SingletonMeta):
    def __init__(self, data = []):
        self.data = data
    
    def Put(self, user):
        user.type = type(user)
        self.data.append(user)

    def FindIndex(self, cpf):
        return self.data.index(lambda x: x.cpf == cpf)

    def GetItem(self, document):
        for i in range(len(self.data)):
            if self.data[i].document == self.data[i].document:
                return self.data[i]
        return None

    def Get(self, delegate=lambda x: x):
        for i in range(len(self.data)):
            if delegate(self.data[i]):
                return self.data[i]
        return None

    def Query(self, delegate=lambda x: x):
        arr = []
        for i in range(len(self.data)):
            if delegate(self.data[i]):
                arr.append(self.data[i])
        return arr

    def Remove(self, cpf):
        userIndex = self.FindIndex(cpf)
        self.data.pop(userIndex)

UsersRepository