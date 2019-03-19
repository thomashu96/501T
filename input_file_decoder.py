## Text input function 

def input_file_decoder(input):
    input_file = open(input, 'r')
    instruction_buffer = []
    for line_not_split in input_file:
        if(line_not_split != ""):
            line_not_split = line_not_split.split("\n")[0]
            instruction_buffer.append(line_not_split)
    print instruction_buffer

## Example
input_file_decoder("input2.txt")