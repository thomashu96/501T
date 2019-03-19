### IMPORTATING STATION ### 
from instruction_queue import *
from reservation_station import * 


### IMPORTING MODULES ###
from tabulate import tabulate
from time import sleep
import numpy as np
import os



### PARAMETERS ###
memory_file_name = "memory.txt"
input_file_name = "input2.txt"

nb_add =3
nb_mult = 2
nb_load = 6
nb_store = 6
nb_register = 11
nb_registerint = 11

cpi_add = 2
cpi_sub = 2
cpi_mul = 10
cpi_div = 40
cpi_load = 3
cpi_store = 3



### INITIAL REGISTERS ###

val_reg = np.zeros(nb_register)
val_regInt = np.zeros(nb_registerint)

reg_init = [6.0,2,3.5,4,10.0,6,7.8,8,9]
regInt_init = [10,20,30,40,50,60,70]

for i in range(len(reg_init)):
    val_reg[i]=reg_init[i]
for j in range(len(regInt_init)):
    val_regInt[j]=regInt_init[j]
    
    
### MAIN FUNCTION ###

def main():
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
    return
    

### SIDE FUNCTIONS ### 

def input_file_decoder(in_file):
    input_file = open(in_file, 'r')
    instruction_buffer = []
    for line_not_split in input_file:
        if(line_not_split != ""):
            line_not_split = line_not_split.split("\n")[0]
            instruction_buffer.append(line_not_split)
    return instruction_buffer


if __name__ == '__main__':
    input("Press Enter to Start")
    print("Input_file : "+ input_file_name)
    print("Memory_file : "+ memory_file_name)
    if len(input_file_name) > 1:
        print ("Importing "+ input_file_name)
        instructions = input_file_decoder(input_file_name)
        main()
    else:
        print ("Please specify input file!")
        exit(1)
        
        