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

    def timing_table_update_issue(self, tt_entry_index, issue_clock):
        self.timing_table[tt_entry_index]["ISSUE"] = issue_clock

    def timing_table_update_ex_finish(self, tt_entry_index, ex_clock):
        self.timing_table[tt_entry_index]["EX_FINISH"] = ex_clock

    def timing_table_update_wb(self, tt_entry_index, wb_clock):
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
        print(tabulate(arr, headers = ['PC','instruction', 'ISSUE', 'EX_FINISH', "WB"], tablefmt='fancy_grid'))
