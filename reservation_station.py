from tabulate import tabulate


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
        row.cpi_init = cpi

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
            if (self.reservation[i].isBusy() and self.reservation[i].Qj == "" and self.reservation[i].Qk == "" and self.reservation[i].time >= 1 and self.reservation[i].time == self.reservation[i].cpi_init):
                self.reservation[i].fuState = 1
                break
        for i in range(self.size):    
            if(self.reservation[i].isBusy() and self.reservation[i].Qj == "" and self.reservation[i].Qk == "" and self.reservation[i].time >= 1 and self.reservation[i].fuState == 1):
                self.reservation[i].time -= 1

    def finish(self):
        finished_list = []
        for i in range(self.size):
            row = self.reservation[i]
            if row.time == 0:
                if row.op == "ADDD":
                    tag, value = row.tag, row.valueJ + row.valueK
                elif row.op == "SUBD":
                    tag, value = row.tag, row.valueJ - row.valueK
                elif row.op == "MULTD":
                    tag, value = row.tag, row.valueJ * row.valueK
                elif row.op == "DIVD":
                    tag, value = row.tag, row.valueJ / row.valueK
                finished_list.append([tag, value, row.ins_pc])
        return finished_list

    def reset(self, position):
        self.reservation[position].reset()


class Add_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "Add")

    def printList(self):
        print("############################################################################################################################")
        print("{:^120}".format("Add Reservation Station"))
        print("############################################################################################################################")
        column_names = ["Time", "Name", 'op','Busy', 'valueJ', 'valueK', 'Qj', 'Qk']
        row_format = "{!s:^15}" * len(column_names)
        print(row_format.format(*column_names))
        for entry in self.reservation:
            entry_list = [entry.time, entry.tag, entry.op, entry.busy, entry.valueJ, entry.valueK, entry.Qj, entry.Qk]
            print(row_format.format(*entry_list))
        print("\n")


class Mul_RS(RS):
    def __init__(self, RESVNUMCONFIG):
        super().__init__(RESVNUMCONFIG, "Mult")

    def printList(self):
        print("############################################################################################################################")
        print("{:^120}".format("Mutl Reservation Station"))
        print("############################################################################################################################")
        column_names = ["Time", "Name", 'op','Busy', 'valueJ', 'valueK', 'Qj', 'Qk']
        row_format = "{!s:^15}" * len(column_names)
        print(row_format.format(*column_names))
        for entry in self.reservation:
            entry_list = [entry.time, entry.tag, entry.op, entry.busy, entry.valueJ, entry.valueK, entry.Qj, entry.Qk]
            print(row_format.format(*entry_list))
        print
        print("\n")

    


class Row(object):
    def __init__(self, tag):
        self.tag = tag
        self.reset()

    def isBusy(self):
        return self.busy

    def reset(self):
        self.op = ""
        self.Qj = ""
        self.valueJ = 0
        self.Qk = ""
        self.valueK = 0
        self.busy = False
        self.time = -1
        self.ins_pc = ""
        self.fuState = 0
        self.cpi_init = -1

    def isFinished(self):
        if self.time == 0:
            return True
        else:
            return False
