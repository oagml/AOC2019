#Calculate the fule required for each module based on its mass


def fuel(mass):
    subfuel = 0

    while((mass//3-2) > 0):
        mass = mass//3 -2 
        subfuel += mass
            
    return subfuel


with open('mass.txt') as f:
    lines = f.readlines()

mass=[]
for i in lines:
    i = i.replace("\n","")
    mass.append(int(i))
   
totalfuel = 0
for i in mass:
   totalfuel = totalfuel + fuel(i) 


print(totalfuel)
