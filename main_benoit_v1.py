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
input_file_name = "input2.txt"

nb_add = 3
nb_mult = 2
nb_load = 6
nb_store = 6
nb_register = 11

cpi_add = 2
cpi_sub = 2
cpi_mul = 10
cpi_div = 40
cpi_load = 3
cpi_store = 3

max_iter = 100

### INITIAL REGISTERS ###

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

    for i in range(max_iter):
        phase_one()
    return


def phase_one():
    instruction = instructions[pc]
    regs = instruction.replace(",", " ").split(" ")

### SIDE FUNCTIONS ###


def extract_offset_reg(instruction_text):
    inst_split = instruction_text.regs[2].replace(')', '(').split('(')
    offset = inst_split[0]
    print("offset : ", offset)
    reg_value = inst_split[1][1]
    print("reg_value : ", reg_value)
    return (offset, reg_value)


def input_file_decoder(in_file):
    input_file = open(in_file, 'r')
    instruction_buffer = []
    instructions = []
    for line_not_split in input_file:
        if(line_not_split != ""):
            line_not_split = line_not_split.split("\n")[0]
            instruction_buffer.append(line_not_split)
            instructions.append(line_not_split.replace(",", " "))
    return instruction_buffer, instructions


if __name__ == '__main__':
    # input("Press Enter to Start")
    print("Input_file : " + input_file_name)
    print("Memory_file : " + memory_file_name)
    if len(input_file_name) > 1:
        print("Importing " + input_file_name)
        instructions_buffer, instructions = input_file_decoder(input_file_name)
        timing_table = Timing(instructions)
        print("Clock cycle :", clock, "\n")
        timing_table.printList()
        Add.printList()
        Mult.printList()
        Register.printList()
        # main()
    else:
        print("Please specify input file!")
        exit(1)
