#What is the Manhattan distance from the central port to the closest intersection?

from programinput import wire1, wire2

wire1_copy = wire1 #Copy strings of raw data
wire2_copy = wire2 #Copy strings of raw data
wire1_list = wire1_copy.split(",") #Split raw data and create a list of strings
wire2_list = wire2_copy.split(",") #Split raw data and create a list of strings


def getInstruction (rawstr): 
    return(rawstr[0], int(rawstr[1:]))

def storetravel (travel_instructions):
    x = 0
    y = 0
    wireset = set()
    for i in range(len(travel_instructions)):
        current_instruction = getInstruction(travel_instructions[i])
        for j in range(current_instruction[1]):
            if current_instruction[0] == 'R':
                x += 1
                wireset.add((x,y))
            elif current_instruction[0] == 'L':
                x -= 1
                wireset.add((x,y))
            elif current_instruction[0] == 'U':
                y += 1
                wireset.add((x,y))
            elif current_instruction[0] == 'D':
                y -= 1
                wireset.add((x,y))

    return wireset


wire1_travel = storetravel(wire1_list)
wire2_travel = storetravel(wire2_list)

#print(wire1_travel)
print(len(wire1_travel))
print(len(wire2_travel))
both = wire1_travel&wire2_travel
total = list()
for i in both:
   total.append(abs(i[0]) + abs(i[1])) 


print(both)
print(min(total))


def intersection_steps(travel_instructions, intersections):
    x = 0
    y = 0
    step = 0
    intersec_steps = dict()
    for i in range(len(travel_instructions)):
        current_instruction = getInstruction(travel_instructions[i])
        for j in range(current_instruction[1]):
            if current_instruction[0] == 'R':
                x += 1
                step += 1
            elif current_instruction[0] == 'L':
                x -= 1
                step += 1
            elif current_instruction[0] == 'U':
                y += 1
                step += 1
            elif current_instruction[0] == 'D':
                y -= 1
                step += 1
            if (x,y) in intersections:
                intersec_steps.update({(x,y):step})

    return intersec_steps


steps_wire1 = intersection_steps(wire1_list, both)
steps_wire2 = intersection_steps(wire2_list, both)
print(f'Length of steps_wire1 is: {len(steps_wire1)}')
print(steps_wire1)
print(f'Length of steps_wire2 is: {len(steps_wire2)}')
print(steps_wire2)

listofsteps = list()
for key1 in steps_wire1:
    for key2 in steps_wire2:
        if key2 == key1:
            listofsteps.append(steps_wire1[key1] + steps_wire2[key2])


print(listofsteps)
print(min(listofsteps))


