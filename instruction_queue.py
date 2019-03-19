from tabulate import tabulate

## Instruction queue object
class Timing(object):
    #empty timing table
    timing_table=[]

    def timing_table_add(self, pc, ins):
        timing_table_entry = {
            "PC" : pc,
            "instruction" : ins,
            "ISSUE" : "-",
            "EX_FINISH" : "-",    
            "WB" : "-",
        }
        self.timing_table.append(timing_table_entry.copy())

    def timing_table_update(self, tt_entry_index, issue_clock, ex_clock, wb_clock):
        self.timing_table[tt_entry_index]["ISSUE"] = issue_clock
        self.timing_table[tt_entry_index]["EX_FINISH"] = ex_clock
        self.timing_table[tt_entry_index]["WB"] = wb_clock

    def getList(self):
        return self.timing_table

    def iteraterow(self):
        arr = []
        for i in range(len(self.timing_table)):
            temp = []
            row = self.timing_table[i]
            temp.append(row['PC'])
            temp.append(row['instruction'])
            temp.append(row["ISSUE"])
            temp.append(row["EX_FINISH"])
            temp.append(row["WB"])
            arr.append(temp)
        return arr

    def printList(self):
        arr = self.iteraterow()
        print tabulate(arr, headers = ['PC','instruction', 'ISSUE', 'EX_FINISH', "WB"], tablefmt='fancy_grid')


## Example
timing_table = Timing()

instructions = ['LD F6,32(R2)', 
                'LD F3,44(R2)',              
                'MULTD F0,F3,F6',
                'MULTD F3,F6,F6',  
                'DIVD F9,F0,F6',
                'SUBD F8,F3,F6',
                'SUBD F8,F2,F6',
                'SUBD F7,F3,F6',
                'SUBD F6,F0,F5',                 
                'ADDD F6,F8,F3'
                ]

for i in range(len(instructions)):
    instruction = instructions[i].replace(",", " ")
    timing_table.timing_table_add(i,instruction)
timing_table.timing_table_update(1,1,2,5)
timing_table.timing_table_update(2,5,8,9)
timing_table.timing_table_update(3,5,8,11)
timing_table.printList()

