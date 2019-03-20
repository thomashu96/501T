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
        return self.registerList[int(name[1:])].value,self.registerList[int(name[1:])].Qi
    
    def isBusy(self,name):
        if self.registerList[int(name[1:])].Qi == "":
            return False
        else :
            return True
        

    def editRegister(self, register, number):
        """
        edit Register F'n' for updating
        """
        self.registerList[number] = register

    def updateRegisterTag(self,tag, name):
        self.registerList[int(name[1:])].Qi = tag

    def updateRegisterByTag(self, tag, value): 
        for i in range(self.size):
            if(self.registerList[i].Qi == tag):
                reg = Register(self.registerList[i].name,"", value)
                self.editRegister(reg, i)

    def printList(self):
        print("############################################################################################################################")
        print("{:^120}".format("Register"))
        print("############################################################################################################################")
        List = self.registerList.copy()
        List.insert(0,Register("Name","Qi","Value"))
        column_names = [List[i].name for i in range(self.size)]
        column_Qi = [List[i].Qi for i in range(self.size)]
        column_value = [List[i].value for i in range(self.size)]
        row_format = "{!s:^10}" * (len(column_names))
        print(row_format.format(*column_names))
        print(row_format.format(*column_Qi))
        print(row_format.format(*column_value))
        print


