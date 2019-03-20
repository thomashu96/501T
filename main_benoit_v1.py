### IMPORTATING STATION ###
from instruction_queue import *
from reservation_station import *
from load_station import *
from register import Registers

### IMPORTING MODULES ###
from tabulate import tabulate
from time import sleep
import numpy as np
import os


### PARAMETERS ###
memory_file_name = "memory.txt"
input_file_name = "input3.txt"

nb_add = 3
nb_mult = 2
nb_load = 6
nb_store = 6
nb_register = 11

cpi_latency = 1

cpi_add = 2 
cpi_sub = 2 
cpi_mul = 10
cpi_div = 40
cpi_load = 3
cpi_store = 3
 

max_iter = 100

### INITIAL REGISTERS ###

cpi_add += cpi_latency
cpi_sub += cpi_latency
cpi_mul += cpi_latency
cpi_div += cpi_latency
cpi_load += cpi_latency
cpi_store += cpi_latency

val_reg = np.zeros(nb_register)

reg_init = [6.0, 2, 3.5, 4, 10.0, 6, 7.8, 8, 9]

for i in range(len(reg_init)):
    val_reg[i] = reg_init[i]

clock = 0
pc = 0

RESVNUMCONFIG = {
    'Add': nb_add,
    'Mult': nb_mult,
    'Load': nb_load,
    'Store': nb_store
}

Add = Add_RS(RESVNUMCONFIG)
Mult = Mul_RS(RESVNUMCONFIG)
Load = Load_Station(RESVNUMCONFIG, memory_file_name)
Store = Store_Station(RESVNUMCONFIG, memory_file_name)
Register = Registers(nb_register, val_reg)

### MAIN FUNCTION ###


def main():
    global pc
    global clock

    cdb_in_use = 0 # will be 1 or 0
    cdb_buffer = [] # treated as a priority queue, older buffer entries are at the top (smaller index)

    for i in range(max_iter):
        input("Press enter to simulate a clock")
        clock+=1
        load_instruction(instructions)
        cdb_buffer = is_finished()
        if len(cdb_buffer)>0:
            cdb_pc_list = [x[2] for x in cdb_buffer]
            pc_min = cdb_pc_list.index(min(cdb_pc_list))
            tag_cdb,value_cdb,pc_cdb = cdb_buffer[pc_min]
            cdb_update(tag_cdb,value_cdb)
            
        update()
        print("============================================================================================================================================")
        print("Clock cycle :", clock, "\n")
        print("PC :", pc, "\n")
        Add.printList()
        Mult.printList()
        Load.printList()
        Register.printList()
        
        
        
    return


    
### LOAD FUNCTIONS ###

def load_instruction(instructions):
    global pc
    global clock
    if (pc >= len(instructions)):
        print("No instruction issued")
    else:
        instruction = instructions[pc].split(" ")
        type_op = instruction[0]
        dest = instruction[1]        
        print("INPUT INSTRUCTIONS: ", instruction)
        if (type_op == "ADD"):
            FetchInstruction(Add,instruction,cpi_add)
            
        if (type_op == "SUBD"):
            FetchInstruction(Add,instruction,cpi_sub)
            
        if (type_op == "MULTD"):
            FetchInstruction(Mult,instruction,cpi_mul)
            
        if (type_op == "DIVD"):
            FetchInstruction(Mult,instruction,cpi_div)
            
        if (type_op == "LD"):
            Fetchload(Load,instruction,cpi_load)
            
        pc += 1
 
def FetchInstruction(station,regs,cpi):
    global pc
    global clock
    type_op = regs[0]
    dest = regs[1]
    reg_valueI = regs[2]
    reg_valuek = regs[3]
    result = station.getFreePosition()
    if result[0]>=0 and (not Register.isBusy(dest)):
        Register.updateRegisterTag(result[1],dest)
        operand1 = Register.getRegister(reg_valueI)
        operand2 = Register.getRegister(reg_valuek)
        station.loadInstruction(operand1[1], operand1[0], operand2[1], operand2[0], result[0], type_op, pc, cpi)
        return True
    else :
        pc-=1
        return False
        
def Fetchload(station,regs,cpi):
    global pc
    global clock
    type_op = regs[0]
    dest = regs[1]
    operand = regs[2]
    result = station.getFreePosition()
    if result[0]>=0 and (not Register.isBusy(dest)):
        Register.updateRegisterTag(result[1],dest)
        offset = extract_offset_reg(operand)[0]
        reg_value = extract_offset_reg(operand)[1]
        Load.loadInstruction(reg_value,offset, result[0], type_op, pc, cpi)
        return True
    else :
        pc-=1
        return False        
        
    
def extract_offset_reg(instruction_text):
    inst_split = instruction_text.replace(')', '(').split('(')
    offset = inst_split[0]
    #print("offset : ", offset)
    reg_value = inst_split[1][1]
    #print("reg_value : ", reg_value)
    return (offset, reg_value)


### UPDATE FUNCTIONS ###
    
def is_finished():
    list_add = Add.finish()
    list_mult = Mult.finish()
    list_load = Load.finish()
    list_finished = list_add+list_mult+list_load 
    return list_finished

    
def update():
    Add.update_clock()
    Mult.update_clock()
    Load.update_clock()
    
       
def cdb_update(tag, value):
    # when value is ready in RS -> broadcast values to Register, RS
    
    # check and update rs
    Add.updateValueByTag(tag, value)
    Mult.updateValueByTag(tag, value)

    # check and update register
    Register.updateRegisterByTag(tag,value)
    
### PRINT FUNCTIONS ###

def initial_table(instructions):
    timing_table = Timing(instructions)
    print("============================================================================================================================================")
    print("Clock cycle :", clock, "\n")
    timing_table.printList()
    Add.printList()
    Mult.printList()
    Load.printList()
    Register.printList()

def input_file_decoder(in_file):
    input_file = open(in_file, 'r')
    instructions = []
    for line_not_split in input_file:
        if(line_not_split != ""):
            line_not_split = line_not_split.split("\n")[0]
            instructions.append(line_not_split.replace(",", " "))
    return instructions





if __name__ == '__main__':
    # input("Press Enter to Start")
    print("Input_file : " + input_file_name)
    print("Memory_file : " + memory_file_name)
    if len(input_file_name) > 1:
        print("Importing " + input_file_name)
        instructions = input_file_decoder(input_file_name)
        #initial_table(instructions)
        main()
    else:
        print("Please specify input file!")
        exit(1)
