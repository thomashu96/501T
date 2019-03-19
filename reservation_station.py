from tabulate import tabulate

class Row(object):
    def __init__(self, tag):
        self.reset(tag)
    
    def isBusy(self):
        return self.busy

    def reset(self,tag):
        self.tag = tag
        self.op = ""
        self.Qj = ""
        self.valueJ = 0
        self.Qk = ""
        self.valueK = 0
        self.busy = False
        self.time = -1 
        self.ins_pc = ""

    def isFinished(self):
        if self.time == 0:
            return True
        else:
            return False

class RS(object):
    def __init__(self, RESVNUMCONFIG, name):
        self.reservation = []
        self.size = RESVNUMCONFIG[name]
        for t in range(self.size):
            row = Row(name+str(t))
            self.reservation.append(row)

    def getFreePosition(self):
        for i in range(self.size):
            if(not self.reservation[i].isBusy()):
                return i, self.reservation[i].tag
        return -1,""

    def loadInstruction(self, Qj, valueJ, Qk, valueK, position,type_op, ins_pc, cpi): 
        row = self.reservation[position]
        row.Qj = Qj
        row.valueJ = valueJ
        row.Qk = Qk
        row.valueK = valueK
        row.op = type_op
        row.ins_pc = ins_pc
        row.time = cpi
        row.busy = True

    def Time_Left(self,position):
        return self.reservation[position].time
    
    def is_Operating(self):
        

    
class Add_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "ADD")

class Mul_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "MUL")


        
