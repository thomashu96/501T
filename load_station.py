from tabulate import tabulate


class Load_Store(object):
    def __init__(self, RESVNUMCONFIG, name,memory):
        self.reservation = []
        self.size = RESVNUMCONFIG[name]
        self.memory = memory
        for t in range(self.size):
            row = Row(name+str(t))
            self.reservation.append(row)


    def getFreePosition(self):
        for i in range(self.size):
            if(not self.reservation[i].isBusy()):
                return i, self.reservation[i].tag
        return -1, ""

    def loadInstruction(self, reg_value,offset, position, type_op, ins_pc, cpi):
        row = self.reservation[position]
        row.reg_value = reg_value
        row.offset = offset
        row.address = str(offset) +'+R'+str(reg_value)
        row.op = type_op
        row.ins_pc = ins_pc
        row.time = cpi
        row.busy = True
        row.cpi_init = cpi

    def updateValueByTag(self, tag, value): 
        for i in range(self.size):
            row = self.reservation[i] 
            if(row.value == tag):
                row.value = value

    def time_Left(self, position):
        return self.reservation[position].time

    def update_clock(self):
        for i in range(self.size):
            if (self.reservation[i].isBusy() and self.reservation[i].time == self.reservation[i].cpi_init):
                self.reservation[i].fuState = 1 
                break
            
        for i in range(self.size):
            if self.reservation[i].isBusy() and self.reservation[i].fuState == 1 :
                self.reservation[i].time -= 1

    def finish(self):
        finished_list = []
        for i in range(self.size):
            row = self.reservation[i]
            if row.time == 0:
                
                if row.op == "LD":
                    
                    file_object  = open(self.memory, "r") 
                    count = 0
                    while count <= int(row.reg_value):
                            ret = file_object.readline()
                            count = count + 1
                    file_object.close()
                    row.value = float(ret) + float(row.offset)
                    tag, value = row.tag, row.value
                    
                finished_list.append([tag, value, row.ins_pc])
        return finished_list

    def reset(self,position):
        self.reservation[position].reset()

class Load_Station(Load_Store,):
    def __init__(self, RESVNUMCONFIG,memory):
        super().__init__(RESVNUMCONFIG, "Load",memory)

    def printList(self):
        print("###########################################################")
        print("{:^65}".format("Load Station"))
        print("###########################################################")
        column_names = ["Time", "Name", "Busy", "Address"]
        row_format = "{!s:^15}" * len(column_names)
        print(row_format.format(*column_names))
        for entry in self.reservation:
            entry_list = [entry.time, entry.tag, entry.busy, entry.address]
            print(row_format.format(*entry_list))
        print
        print("\n")
    
class Store_Station(Load_Store):
    def __init__(self, RESVNUMCONFIG,memory):
        super().__init__(RESVNUMCONFIG, "Store",memory)


class Row(object):
    def __init__(self, tag):
        self.tag = tag
        self.reset()

    def isBusy(self):
        return self.busy

    def reset(self):
        self.op = ""
        self.reg_value = -1
        self.offset = 0
        self.value = -1
        self.address = ""
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