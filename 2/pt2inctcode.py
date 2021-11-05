#Create an intcode computer that can read and excute simple programs. For more information 
#See the advent of code 2019, Day 2

from programinput import program

listcopy = program

#junklist = [2,3,2,0]

def addition (inputlist, position):
    if inputlist[position] == 1:
         inputlist[inputlist[position + 3]] = inputlist[inputlist[position + 1]] + inputlist[inputlist[position + 2]]
    else:
        print('Error: Current position does not correspond to addition')
    

def multiplication (inputlist, position):
    if inputlist[position] == 2:
        inputlist[inputlist[position + 3]] = inputlist[inputlist[position + 1]] * inputlist[inputlist[position + 2]]
    else:
        print('Error: Current position does not correspond to multiplication')


halt = 0

pos = 0

output = 19690720

print(listcopy)

while (halt != 99):
   
    if listcopy[pos] == 1: #Add
        print("Adding...")
        addition(listcopy, pos)
        pos += 4
    elif listcopy[pos] == 2: #Multiply
        print("Multiplying...")
        multiplication(listcopy, pos)
        pos += 4
    elif listcopy[pos] == 99:
        halt = 99
        print("Halt condition has been reached")
    else:
        halt = 99
        print("Error: Unexpected Opcode")

    print(listcopy)

    print("New position:" + str(pos))

#multiplication(junklist, 0)

print(listcopy)
    
