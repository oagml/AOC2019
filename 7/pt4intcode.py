#Create an intcode computer that can read and excute simple programs. For more information 
#See the advent of code 2019, Day 5

import itertools

data = open('inputdata.txt', 'r').read().split(',')

listcopy = []

for i in data:
    listcopy.append(int(i))

amplifiers = []
for i in range(5):
    amplifiers.append(listcopy.copy())

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


def intcodeprocessing(program, giveninput, phase, pos):

    halt = 0

    output = 0

    while (halt != 99):

        instruction = instruction_decoder(program[pos])

        if instruction == False:
            break

        elif instruction[3] == 1: #Add
            print("Adding...")
            addition(program, pos, instruction)
            pos += 4
        elif instruction[3] == 2: #Multiply
            print("Multiplying...")
            multiplication(program, pos, instruction)
            pos += 4

        elif instruction[3] == 3: #Input
            #print("Input...")
            #This part of the code is special for Day 7:
            if pos >= 2:
                programinput(program, pos, giveninput)
                print("Taking Input...") 
            else:
                programinput(program, pos, phase)
                print("Taking phase...")
            pos += 2

        elif instruction[3] == 4: #Output
            print("Output................................................................")
            output = programoutput(program, pos, instruction)
            print(output)
            pos += 2
            #This part of the code is special for Day 7
            break

        elif instruction[3] == 5: #Jump If True
            print("Jump If True...")
            pos = jump_if_true(program, pos, instruction) #This function returns  pointer value

        elif instruction[3] == 6: #Jump If False
            print("Jump If False...")
            pos = jump_if_false(program, pos, instruction) #This function returns  pointer value

        elif instruction[3] == 7: #Less Than
            print("Less Than...")
            less_than(program, pos, instruction)
            pos += 4

        elif instruction[3] == 8: #Equals
            print("Equals...")
            equals_func(program, pos, instruction)
            pos += 4

        elif instruction[3] == 99: #Halt
            halt = 99
            print("Halt condition has been reached")
        else:
            halt = 99
            print("Error: Unexpected Opcode")


        print(f'New position: {pos}')

    return output, pos, halt, program


giveninput = 0
outputs = []
positions = [0,0,0,0,0]
halt = 0
phases = [5,6,7,8,9]
permutedphases = []

for i in itertools.permutations(phases, 5):
    permutedphases.append(list(i))

for combination  in permutedphases:
    while halt != 99:
        print(f"Current combination: {combination}")
        for i in range(len(combination)):
            giveninput, positions[i], halt, amplifiers[i] = intcodeprocessing(amplifiers[i], giveninput, combination[i], positions[i])
            outputs.append(giveninput)
    halt = 0
    positions = [0,0,0,0,0]
    giveninput = 0

'''
testphase = [9,7,8,5,6]
positions = [0,0,0,0,0]
halt = 0
print("Amplifiers initialized:")
for i in amplifiers:
    print(i)

while halt != 99:
    for i in range(len(testphase)):
        giveninput, positions[i], halt, amplifiers[i] = intcodeprocessing(amplifiers[i], giveninput, testphase[i], positions[i])
        outputs.append(giveninput)
        print("List of positions:.......................................")
        print(positions)
        print(f"Amplifier: {i}")
        print(f"Output: {giveninput}")
        print(f"Halt: {halt}")
        print("Amplifiers:")
        for j in amplifiers:
            print(j)
'''
print("Outputs recorded:")
outputs.sort()
print(outputs)






