from .SingletonMeta import SingletonMeta

class RepositoryBase(SingletonMeta):
    def __init__(self, data = []):
        self.data = data

    def Exists(self, id):
        return self.FindIndex(id) < 0 
    
    def FindIndex(self, id):
        return self.data.index(lambda x: x.id == id)

    def Put(self, item):
        self.data.append(item)

    def Get(self, delegate=lambda item: item):
        for i in range(len(self.data)):
            if delegate(self.data[i]):
                return self.data[i]
        return None

    def Query(self, delegate=lambda Item: Item):
        arr = []
        for i in range(len(self.data)):
            if delegate(self.data[i]):
                arr.append(self.data[i])
        return arr

    def Remove(self, id):
        index = self.FindIndex(id)
        self.data.pop(index)