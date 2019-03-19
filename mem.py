from tabulate import tabulate

class mem(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Memory(object):
    def __init__(self, size, values):
        self.memoryList = []
        self.size = size
        for i in range(size):
            mem = mem("R"+str(i), values[i])
            self.memoryList.append(mem)

    def load_in_memory_ByName(self, name):
        return self.memoryList[int(name[1:])]

    def store_in_memory(self, name, value):
        self.memoryList[int(name[1:])] = value

