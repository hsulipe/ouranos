from repositories import SingletonMeta

class UsersRepository(metaclass=SingletonMeta):
    def __init__(self, data = []):
        self.data = data
    
    def Put(self, user):
        user.type = type(user)
        self.data.append(user)

    def FindIndex(self, cpf):
        return self.data.index(lambda x: x.cpf == cpf)

    def GetItem(self, id):
        return {}
    
    def Remove(self, cpf):
        userIndex = self.FindIndex(cpf)
        self.data.pop(userIndex)

UsersRepository