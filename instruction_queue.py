from tabulate import tabulate

## Instruction queue object
class Time(object): 
    def __init__(self, pc ,ins):
        self.pc = pc
        self.ins = ins,
        self.issue = "-"
        self.start = "-"
        self.finish = "-"
        self.isFinished = False
        self.wb = "-"

class Timing(object):
    def __init__(self, instructions):
        self.instructionList = []
        self.size = len(instructions)
        for i in range(self.size):
            time = Time(i,instructions[i])
            self.instructionList.append(time)

    def timing_update_issue(self, pc, clock):
        self.instructionList[pc].issue = clock

    def timing_update_start(self, pc, clock):
        self.instructionList[pc].start = clock

    def timing_update_finish(self, pc, clock):
        if not self.instructionList[pc].isFinished:
            self.instructionList[pc].finish = clock
            self.instructionList[pc].isFinished = True

    def timing_update_wb(self, pc, clock):
        if pc>=0:
            self.instructionList[pc].wb = clock

    def getList(self):
        return self.instructionList

    def printList(self):
        print ("############################################################################################################################")
        print ("{:^120}".format("TIMING TABLE"))
        print ("############################################################################################################################")   
        column_names = [ "PC", "INSTRUCTION", "ISSUE", "EX Start", "EX Finish", "WB"]
        row_format = "{!s:^20}" * len(column_names)
        print (row_format.format(*column_names))
        for tt_entry in self.instructionList:
            tt_entry_list = [tt_entry.pc , tt_entry.ins[0], tt_entry.issue, tt_entry.start, tt_entry.finish, tt_entry.wb]
            print(row_format.format(*tt_entry_list))
        print
        print("\n")
