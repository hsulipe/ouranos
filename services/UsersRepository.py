class UsersRepository:
    def __init__(self, data = []):
        self.data = data
    
    def Insert(self, user):
        user.type = type(user)
        self.data.append(user)

    def FindIndex(self, cpf):
        return self.data.index(lambda x: x.cpf == cpf)
    
    def Delete(self, cpf):
        userIndex = self.FindIndex(cpf)
        self.data.pop(userIndex)

UsersRepository