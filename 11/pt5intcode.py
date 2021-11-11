#Create an intcode computer that can read and excute simple programs. For more information 
#See the advent of code 2019, Day 11

import itertools
import intcode
import numpy as np

data = open('inputdata', 'r').read().split(',')

listcopy = []

for i in data:
    listcopy.append(int(i)) #Copy original list

for i in range(10000000): #What is this
    listcopy.append(0)

def rotate (currdir, direction):
    if (direction == 0 and currdir == "Up"): #Turn left
        return "Left"
    elif (direction == 0 and currdir == "Left"): #Turn down
        return "Down"
    elif (direction == 0 and currdir == "Right"): #Turn up
        return "Up"
    elif (direction == 0 and currdir == "Down"): #Turn right
        return "Right"

    elif (direction == 1 and currdir == "Up"): #Turn right
        return "Right"
    elif (direction == 1 and currdir == "Left"): #Turn Up
        return "Up"
    elif (direction == 1 and currdir == "Right"): #Turn down
        return "Down"
    elif  (direction == 1 and currdir == "Down"): #Turn left
        return "Left"

    else:
        print("Error: Reached an invalid input")


giveninput = 0
output = 0
relativeBase = 0
halt = 0
pos = 0
outputOrder = 1
orientation = ["Left","Up","Right","Down"]
paint = ["Black", "White"]
currentDirection = "Up"
currentColor = "Black"
currentRow = 500 #Start from the middle of the matrix
currentCol = 500 #Start from the middle of the matrix

matrix = np.full((1000,1000), '.')

positionsReached = set()

while (halt != 99):

    instruction = intcode.instruction_decoder(listcopy[pos])

    if instruction == False:
        break

    elif instruction[3] == 1: #Add
        #print("Adding...")
        intcode.addition(listcopy, pos, instruction, relativeBase)
        pos += 4
    elif instruction[3] == 2: #Multiply
        #print("Multiplying...")
        intcode.multiplication(listcopy, pos, instruction, relativeBase)
        pos += 4

    elif instruction[3] == 3: #Input
        #print("Input...")
        if matrix[currentRow][currentCol] == '.': #If the robot is over a black panel
            print("Painting black")
            giveninput = 0
        else: #If the robot is over a white panel
            print("Painting white")
            giveninput = 1
        intcode.programinput(listcopy, pos, giveninput, instruction, relativeBase)
        pos += 2

    elif instruction[3] == 4: #Output
        output = intcode.programoutput(listcopy, pos, instruction, relativeBase)
        #outputlist.append(output)
        print("Output................................................................")
        print(output)

        if (outputOrder%2): #If the output is odd, it's a paint instruction
            if(output == 0): #Paint the panel black
                matrix[currentRow][currentCol] = '.'
                positionsReached.add((currentRow,currentCol))
            else: #Paint the panel white
                matrix[currentRow][currentCol] = '#'
                positionsReached.add((currentRow,currentCol))

        else: #If the ouput is even, it's a direction instruction
            if(rotate(currentDirection, output) == "Up"):
                currentDirection = "Up"
                currentRow -= 1
            elif (rotate(currentDirection, output) == "Down"):
                currentDirection = "Down"
                currentRow += 1
            elif (rotate(currentDirection, output) == "Right"):
                currentDirection = "Right"
                currentCol += 1
            elif (rotate(currentDirection, output) == "Left"):
                currentDirection = "Left"
                currentCol -= 1

        pos += 2
        outputOrder += 1

    elif instruction[3] == 5: #Jump If True
        #print("Jump If True...")
        pos = intcode.jump_if_true(listcopy, pos, instruction, relativeBase) #This function returns  pointer value

    elif instruction[3] == 6: #Jump If False
        #print("Jump If False...")
        pos = intcode.jump_if_false(listcopy, pos, instruction, relativeBase) #This function returns  pointer value

    elif instruction[3] == 7: #Less Than
        #print("Less Than...")
        intcode.less_than(listcopy, pos, instruction, relativeBase)
        pos += 4

    elif instruction[3] == 8: #Equals
        #print("Equals...")
        intcode.equals_func(listcopy, pos, instruction, relativeBase)
        pos += 4

    elif instruction[3] == 9: #Adjust Relative Base
        #print("Adjusting Base...")
        relativeBase = intcode.adjust_base(listcopy, pos, instruction, relativeBase)
        pos += 2

    elif instruction[3] == 99: #Halt
        halt = 99
        print("Halt condition has been reached")
    else:
        halt = 99
        print("Error: Unexpected Opcode")


    #print(f'New position: {pos}')

print(positionsReached)
print(len(positionsReached))

'''
for i in range(0, len(outputlist), 2):
    if (outputlist[i] == 0 and matrix[currentRow][currentCol] == '#'):
        matrix[currentRow][currentCol] = '.'
        positionsReached.add((currentRow,currentCol))
    elif (outputlist[i] == 1 and matrix[currentRow][currentCol] == '.'):
        matrix[currentRow][currentCol] = '#'
        positionsReached.add((currentRow,currentCol))

    if (rotate(currentDirection, outputlist[i + 1]) == "Up"):
        currentDirection = "Up"
        currentRow -= 1

    elif (rotate(currentDirection, outputlist[i + 1]) == "Down"):
        currentDirection = "Down"
        currentRow += 1

    elif (rotate(currentDirection, outputlist[i + 1]) == "Right"):
        currentDirection = "Right"
        currentCol += 1

    elif (rotate(currentDirection, outputlist[i + 1]) == "Left"):
        currentDirection = "Left"
        currentCol -= 1
'''
