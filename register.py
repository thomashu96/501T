from tabulate import tabulate

class Register(object):
    def __init__(self, name, Qi, value):
        self.name = name
        self.Qi = Qi
        self.value = value

class Registers(object):
    def __init__(self, size, values):
        self.registerList = []
        self.size = size
        for i in range(size):
            register = Register("F"+str(i),"", values[i])
            self.registerList.append(register)

    def getRegister(self, name):
        return self.registerList[int(name[1:])]

    def editRegister(self, register, name):
        """
        edit Register F'n' for updating
        """
        self.registerList[int(name[1:])] = register

    def updateRegisterTag(self,tag, name):
        self.registerList[int(name[1:])].Qi = tag

    def updateRegisterByTag(self, tag, value): 
        for i in range(self.size):
            if(self.registerList[i].Qi == tag):
                reg = Register(self.registerList[i].name,"", value)
                self.editRegister(reg, i)

    def iterateRegister(self):
        arr = []
        for i in range(self.size):
            temp = []
            register = self.registerList[i]
            temp.append(register.name)
            temp.append(register.Qi)
            temp.append(register.value)
            arr.append(temp)
        return arr

    def printRows(self):
        arr = self.iterateRegister()
        print(tabulate(arr, headers = ['Register','Qi','Value'], tablefmt='fancy_grid'))


