#Create an intcode computer that can read and excute simple programs. For more information 
#See the advent of code 2019, Day 2

from programinput import program

listcopy = list.copy(program) #Make a copy of the original program

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


halt = 0 #flag for indicating wether a halt opcode is in the current instruction

pos = 0 #instruction pointer

    
print(listcopy)

noun = 1 #noun is the first parameter of the first instruction
verb = 2 #verb is the second parameter of the first instruction

for i in range(100):
    
    for j in range(100): 
        listcopy = list.copy(program) #Reset the original values of the list
        pos = 0 #Reset the instruction pointer 
        halt = 0
        listcopy[noun], listcopy[verb] = i, j #Set the increased of of i and j to the positions 1 and 2 
        while (halt != 99): #Execute the entire program until a halt opcode or invalid opcode is reached

            if listcopy[pos] == 1: #Add                  
                #print("Adding...")
                addition(listcopy, pos)
                pos += 4
            elif listcopy[pos] == 2: #Multiply
                 #print("Multiplying...")
                 multiplication(listcopy, pos)
                 pos += 4
            elif listcopy[pos] == 99:
                 halt = 99
                 #print("Halt condition has been reached")
            else:
                 halt = 99
                 print("Error: Unexpected Opcode")
        if listcopy[0] == 19690720:
            print('We found the expected number!. The combination of numbers is:')
            print(listcopy[noun], listcopy[verb])
            break
        #else:
            #print('Expected number not reached yet. The current combination of numbers is:')  
            #print(listcopy[noun], listcopy[verb])
            #print(listcopy[0])
