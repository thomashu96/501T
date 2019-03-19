from tabulate import tabulate


class Row(object):
    def __init__(self, tag):
        self.reset(tag)

    def isBusy(self):
        return self.busy

    def reset(self, tag):
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
        return -1, ""

    def loadInstruction(self, Qj, valueJ, Qk, valueK, position, type_op, ins_pc, cpi):
        row = self.reservation[position]
        row.Qj = Qj
        row.valueJ = valueJ
        row.Qk = Qk
        row.valueK = valueK
        row.op = type_op
        row.ins_pc = ins_pc
        row.time = cpi
        row.busy = True

    def updateValueByTag(self, tag, value): 
        for i in range(self.size):
            row = self.reservation[i] 
            if(row.Qj == tag):
                row.Qj = ""
                row.valueJ = value
            if(row.Qk == tag):
                row.Qk = ""
                row.valueK = value

    def time_Left(self, position):
        return self.reservation[position].time

    def update_clock(self):
        for i in range(self.size):
            if(self.reservation[i].isBusy() and self.reservation[i].Qj == "" and self.reservation[i].Qk == "" and self.reservation[i].time >= 1):
                self.reservation[i].time -= 1

    def finish(self):
        finished_list = []
        for i in range(self.size):
            row = self.reservation[i]
            if row.time == 0:
                if row.op == "ADD":
                    tag, value = row.tag, row.valueJ + row.valueK
                elif row.op == "SUB":
                    tag, value = row.tag, row.valueJ - row.valueK
                elif row.op == "MUL":
                    tag, value = row.tag, row.valueJ * row.valueK
                elif row.op == "DIV":
                    tag, value = row.tag, row.valueJ / row.valueK
                finished_list.append([tag, value, row.ins_pc])
        return finished_list

    def reset(self,position):
        self.reservation[position].reset()

    def iteraterow(self):
        arr = []
        for i in range(self.size):
            temp = []
            row = self.reservation[i]
            temp.append(row.time)
            temp.append(row.name)
            temp.append(row.busy)
            temp.append(row.op)
            temp.append(row.valueJ)
            temp.append(row.valueK)
            temp.append(row.Qj)
            temp.append(row.Qk)
            arr.append(temp)
        return arr

    def printRows(self):
        arr = self.iteraterow()
        print(tabulate(arr, headers = ['Time','Name', 'Busy', 'valueJ','valueK','Qj', 'Qk',], tablefmt='fancy_grid'))

    
class Add_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "Add")


class Mul_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "Mult")
