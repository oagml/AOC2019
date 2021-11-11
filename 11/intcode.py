#Create an intcode computer that can read and excute simple programs.

def get_parameters(inputlist, position,  instruction, relativeBase):
    if instruction[2] == 0: #Position Mode
        #print(inputlist[position + 1])
        parameter1 = inputlist[inputlist[position+1]]
    elif instruction[2] == 1:   #Immediate Mode
        parameter1 = inputlist[position+1]
    else:                   #Relative Mode
        parameter1 = inputlist[inputlist[position+1] + relativeBase]

                                                  
    if instruction[1] == 0: #Position Mode
        parameter2 = inputlist[inputlist[position+2]]
    elif instruction[1] == 1:   #Immediate Mode
        parameter2 = inputlist[position+2]
    else:                    #Relative Mode
        parameter2 = inputlist[inputlist[position+2] + relativeBase] 

    return parameter1, parameter2


def addition (inputlist, position, instruction, relativeBase):
    
    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)

    #print(f'{parameter1} + {parameter2} = {parameter1 + parameter2}')
    if (instruction[0] == 2): #Write in Relative Mode
        inputlist[inputlist[position + 3] + relativeBase] = parameter1 + parameter2
    else:                   #Write in Position Mode 
        inputlist[inputlist[position + 3]] = parameter1 + parameter2
    

def multiplication (inputlist, position, instruction, relativeBase):

    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)

    #print(f'{parameter1} * {parameter2} = {parameter1 *  parameter2}')

    if (instruction[0] == 2): #Write in Relative Mode
        inputlist[inputlist[position + 3] + relativeBase] = parameter1 * parameter2
    else:                   #Write in Position Mode
        inputlist[inputlist[position + 3]] = parameter1 * parameter2
    

def programinput (inputlist, position, inputparam, instruction, relativeBase):
    if (instruction[2] == 2):   #Relative Mode
        inputlist[inputlist[position + 1] + relativeBase] = inputparam
    else:                       #Position Mode
        inputlist[inputlist[position + 1]] = inputparam


def programoutput (inputlist, position, instruction, relativeBase):
    if(instruction[2] == 0): #Position Mode
        return inputlist[inputlist[position+1]]
    elif(instruction[2] == 1): #Immediate Mode
            return inputlist[position + 1]
    elif (instruction[2] == 2): #Relative Mode
        return inputlist[inputlist[position + 1] + relativeBase]

def jump_if_true(inputlist, position, instruction, relativeBase):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)
    if parameter1 != 0:
        return parameter2
    else:
        return (position + 3)

def jump_if_false(inputlist, position, instruction, relativeBase):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)
    if parameter1 == 0:
        return parameter2
    else:
        return (position + 3)

def less_than(inputlist, position, instruction, relativeBase):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)
    if parameter1 < parameter2:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 1
        elif (instruction[0] == 1): #Immediate Mode
            inputlist[position + 3] = 1
        else:                   #Relative Mode
            inputlist[inputlist[position + 3] + relativeBase] = 1
    else:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 0
        elif (instruction[0] == 1):  #Immediate Mode
            inputlist[position + 3] = 0
        else:                       #Relative Mode
            inputlist[inputlist[position + 3] + relativeBase] = 0


def equals_func(inputlist, position, instruction, relativeBase):
    parameter1, parameter2 = get_parameters(inputlist, position, instruction, relativeBase)
    if parameter1 == parameter2:
        if (instruction[0] == 0): #Position Mode 
            inputlist[inputlist[position + 3]] = 1
        elif (instruction[0] == 1):                   #Immediate Mode
            inputlist[position + 3] = 1
        else:                   #Relative Mode 
            inputlist[inputlist[position + 3] + relativeBase] = 1
    else:
        if (instruction[0] == 0): #Position Mode
            inputlist[inputlist[position + 3]] = 0
        elif (instruction[0] == 1): #Immediate Mode
            inputlist[position + 3] = 0
        else:                       #Relative Mode
            inputlist[inputlist[position + 3] + relativeBase] = 0

def adjust_base(inputlist, position, instruction, relativeBase): 

    if instruction[2] == 2:         #Relative Mode
        return (inputlist[inputlist[position + 1] + relativeBase] + relativeBase)
    elif instruction[2] == 0:       #Postion Mode
        return (inputlist[inputlist[position + 1]] + relativeBase)
    else:                           #Immediate Mode
        return (inputlist[position + 1] + relativeBase)


def instruction_decoder (instruction):

    opcode = instruction % 100 #Use modulus operation to get the last two digits of a number
    valid_opcodes = {1,2,3,4,5,6,7,8,9,99}
    
    if opcode in valid_opcodes:
        #print(f'Valid instruction: .....{instruction}')
        instruction_string = str(instruction)

        output_list = [0,0,0,0]
        output_list[3] = opcode 
        output_list[2] = (instruction%1000)//100 #Use modulus and  rounded division to get hundreds value
        output_list[1] = (instruction%10000)//1000
        output_list[0] = (instruction%100000)//10000

        #print(output_list) 
        return output_list

    else:
        print(f'Instruction not valid: {instruction}')
        return False

'''

def intcodeprocessing(program, giveninput, pos, relativeBase, outputlist):

    halt = 0

    output = 0

    while (halt != 99):

        instruction = instruction_decoder(program[pos])

        if instruction == False:
            break

        elif instruction[3] == 1: #Add
            #print("Adding...")
            addition(program, pos, instruction, relativeBase)
            pos += 4
        elif instruction[3] == 2: #Multiply
            #print("Multiplying...")
            multiplication(program, pos, instruction, relativeBase)
            pos += 4

        elif instruction[3] == 3: #Input
            #print("Input...")
            programinput(program, pos, giveninput, instruction, relativeBase)
            pos += 2

        elif instruction[3] == 4: #Output
            output = programoutput(program, pos, instruction, relativeBase)
            outputlist.append(output)
            #print("Output................................................................")
            #print(output)
            pos += 2

        elif instruction[3] == 5: #Jump If True
            #print("Jump If True...")
            pos = jump_if_true(program, pos, instruction, relativeBase) #This function returns  pointer value

        elif instruction[3] == 6: #Jump If False
            #print("Jump If False...")
            pos = jump_if_false(program, pos, instruction, relativeBase) #This function returns  pointer value

        elif instruction[3] == 7: #Less Than
            #print("Less Than...")
            less_than(program, pos, instruction, relativeBase)
            pos += 4

        elif instruction[3] == 8: #Equals
            #print("Equals...")
            equals_func(program, pos, instruction, relativeBase)
            pos += 4

        elif instruction[3] == 9: #Adjust Relative Base
            #print("Adjusting Base...")
            relativeBase = adjust_base(program, pos, instruction, relativeBase)
            pos += 2

        elif instruction[3] == 99: #Halt
            halt = 99
            #print("Halt condition has been reached")
        else:
            halt = 99
            #print("Error: Unexpected Opcode")


        #print(f'New position: {pos}')

    return output, pos, halt, program
'''
