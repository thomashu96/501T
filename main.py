from reservation_station import * 
from instruction_queue import *

INSCONFIG = {
    'ADDD': {
        'time': 2,
        'resv': 'ADD'
    },
    'SUBD': {
        'time': 2,
        'resv': 'ADD'
    },
    'MULTD': {
        'time': 10,
        'resv': 'MUL'
    },
    'DIVD': {
        'time': 40,
        'resv': 'MUL'
    },
    'LD': {
        'time': 3,
        'resv': 'LOAD'
    },
    'ST': {
        'time': 3,
        'resv': 'STORE'
    },
}

RESVNUMCONFIG = {
    'Add': 3,
    'Mult': 2,
    'Load': 3,
    'Store': 3
}

Register_size = 10
Memory_size = 10

Add = Add_RS(RESVNUMCONFIG)
Mult = Mul_RS(RESVNUMCONFIG)

print(Add.getFreePosition())
print(Mult.getFreePosition())


