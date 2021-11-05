#Create an intcode computer that can read and excute simple programs. For more information 
#See the advent of code 2019, Day 5

from programinput import program

listcopy = program

giveninput = 5

def get_parameters(inputlist, position,  instruction):
    if instruction[2] == 0: #Position Mode
        print(inputlist[position+2])
        parameter1 = inputlist[inputlist[position+1]]
    else:                   #Immediate Mode
        parameter1 = inputlist[position+1]
                                                  
    if instruction[1] == 0: #Position Mode
        parameter2 = inputlist[inputlist[position+2]]
    else:                   #Immediate Mode
        parameter2 = inputlist[position+2]

    return parameter1, parameter2


def addition (inputlist, position, instruction):
    
    parameter1, parameter2 = get_parameters(inputlist, position, instruction)

    inputlist[inputlist[position + 3]] = parameter1 + parameter2
    
    print(f'{parameter1} + {parameter2} = {parameter1 + parameter2}')


def multiplication (inputlist, position, instruction):

    parameter1, parameter2 = get_parameters(inputlist, position, instruction)

    inputlist[inputlist[position + 3]] = parameter1 * parameter2
    
    print(f'{parameter1} * {parameter2} = {parameter1 + parameter2}')

def programinput (inputlist, position, inputparam):
    inputlist[inputlist[position + 1]] = inputparam

def programoutput (inputlist, position, instruction):
    if(instruction[2] == 0): #Position Mode
        return inputlist[inputlist[position+1]]
    else:
        return inputlist[position+1]

def jump_if_true(inputlist, position, instruction):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction)
    if parameter1 != 0:
        return parameter2
    else:
        return (position + 3)

def jump_if_false(inputlist, position, instruction):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction)
    if parameter1 == 0:
        return parameter2
    else:
        return (position + 3)

def less_than(inputlist, position, instruction):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction)
    if parameter1 < parameter2:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 1
        else:                   #Immediate Mode
            inputlist[position + 3] = 1
    else:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 0
        else:                   #Immediate Mode
            inputlist[position + 3] = 0

def equals_func(inputlist, position, instruction):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction)
    if parameter1 == parameter2:
        if (instruction[0] == 0): #Position Mode 
            inputlist[inputlist[position + 3]] = 1
        else:                   #Immediate Mode
            inputlist[position + 3] = 1
    else:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 0
        else:                   #Immediate Mode
            inputlist[position + 3] = 0

def instruction_decoder (instruction):

    opcode = instruction % 100 #Use modulus operation to get the last two digits of a number
    valid_opcodes = {1,2,3,4,5,6,7,8,99}
    
    if opcode in valid_opcodes:
        print(f'Valid instruction: {instruction}')
        instruction_string = str(instruction)

        output_list = [0,0,0,0]
        output_list[3] = opcode 
        output_list[2] = (instruction%1000)//100 #Use modulus and  rounded division to get hundreds value
        output_list[1] = (instruction%10000)//1000
        output_list[0] = (instruction%100000)//10000

        print(output_list) 
        return output_list

    else:
        print(f'Instruction not valid: {instruction}')
        return False


#instruction_decoder(11003)

#instruction_decoder(123)

halt = 0

pos = 0

output = 19690720

#print(listcopy)

while (halt != 99):
   
    instruction = instruction_decoder(listcopy[pos])
    
    if instruction == False:
        break

    elif instruction[3] == 1: #Add
        print("Adding...")
        addition(listcopy, pos, instruction)
        pos += 4
    elif instruction[3] == 2: #Multiply
        print("Multiplying...")
        multiplication(listcopy, pos, instruction)
        pos += 4

    elif instruction[3] == 3: #Input
        print("Input...")
        programinput(listcopy, pos, giveninput)
        pos += 2

    elif instruction[3] == 4: #Output
        print("Output................................................................")
        print(programoutput(listcopy, pos, instruction))
        pos += 2

    elif instruction[3] == 5: #Jump If True
        print("Jump If True...")
        pos = jump_if_true(listcopy, pos, instruction) #This function returns  pointer value

    elif instruction[3] == 6: #Jump If False
        print("Jump If False...")
        pos = jump_if_false(listcopy, pos, instruction) #This function returns  pointer value

    elif instruction[3] == 7: #Less Than
        print("Less Than...")
        less_than(listcopy, pos, instruction)
        pos += 4

    elif instruction[3] == 8: #Equals
        print("Equals...")
        equals_func(listcopy, pos, instruction)
        pos += 4

    elif instruction[3] == 99: #Halt
        halt = 99
        print("Halt condition has been reached")
    else:
        halt = 99
        print("Error: Unexpected Opcode")

    #print(listcopy)

    print(f'New position: {pos}')

#multiplication(junklist, 0)

#print(listcopy)
    
