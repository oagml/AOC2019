#Day 12 of AOC2019
#You start tracking the four largest moons of Jupiter: Io, Europa, Ganymede and Callisto
#You calculate the position of each mon (your puzzle input)
#You need to simulate their motion
#The x, y and z velocity of each moon starts at 0
#Simulate the motion of the moons in time steps.
#Update the velocity of every moon by applying gravity.
#Then, once all moons' velocities have been updated, update the position of every mooon by applying velocity
#To apply gravity, consider every pair of moons
#On each axis, the velocity of the moon changes by +1 or -1 to pull the moons together.

#Velocity
#Update the velocity by applying gravity
#There are 6 possible pairs that can be calculated for the 4 moons

#axisDV: Calculate the change in velocity for 2 moons on a single axis given their positions on that axis
def axisDV (pos1, pos2):
    if(pos1 == pos2):
        dv1= 0
        dv2 = 0
        return dv1, dv2

    elif(pos1 > pos2):
        dv1 = -1
        dv2 = 1
        return dv1, dv2

    else:
        dv1 = 1
        dv2 = -1
        return dv1, dv2

#moonVelocity: Calculate the velocity of 2 moons given their position and velocity on 3 axis
def moonVelocity (x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2):
    dvx1, dvx2 = axisDV(x1,x2)
    dvy1, dvy2 = axisDV(y1, y2)
    dvz1, dvz2 = axisDV(z1, z2)

    velx1 = vx1 + dvx1
    velx2 = vx2 + dvx2
    vely1 = vy1 + dvy1
    vely2 = vy2 + dvy2
    velz1 = vz1 + dvz1
    velz2 = vz2 + dvz2

    return velx1, vely1, velz1, velx2, vely2, velz2

#moonPosition: Calulate the new position of 2 moons given their position and updated velocity on 3 axis
def moonPosition (x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2):
    posx1 = x1 + vx1
    posy1 = y1 + vy1
    posz1 = z1 + vz1

    posx2 = x2 + vx2
    posy2 = y2 + vy2
    posz2 = z2 + vz2

    return posx1, posy1, posz1, posx2, posy2, posz2

#Timesteps
timesteps = 1000

#3 axis values for each of the 4 moons
pos = [[-9, -1, -1], [2, 9, 5], [10, 18, -12], [-6, 15, -7]]
vel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


#Cycles for 1 step:
#Update the velocities

for i in range(timesteps):
    for i in range(len(pos)):
        for j in range(i, len(pos)):
            if (i == j):
                continue
            print(f"Pair of moons: {i}, {j}")
            x1, y1, z1 = pos[i]
            x2, y2, z2 = pos[j]
            vx1, vy1, vz1 = vel[i]
            vx2, vy2, vz2 = vel[j]

            vx1,vy1,vz1,vx2,vy2,vz2= moonVelocity(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2)
            vel[i] = [vx1, vy1, vz1]
            vel[j] = [vx2, vy2, vz2]

        #x1,y1,z1,x2,y2,z2 = moonPosition(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2)
        #pos[i] = [x1, y1, z1]
        #pos[j] = [x2, y2, z2]

    #Update the positions:
    for i in range(len(pos)):
        pos[i] = [x + y for x, y in zip(pos[i], vel[i])]


for i in pos:
    print(i)

for i in vel:
    print(i)


#Calculate the total energy

#Potential energy
def potEn (pos):
    pot = 0
    for i in pos:
        pot = pot + abs(i)

    return pot


#Kinetic Energy
def kinEn (vel):
    kin = 0
    for i in vel:
        kin += abs(i)

    return kin

#Total Energy
def totEn (pot, kin):
    totalEnergy = pot*kin
    return (totalEnergy)

totalSumEnergy = 0

for i in range(len(pos)):
    pot = potEn(pos[i])
    print(f"The potential energy is: {pot}")
    kin = kinEn(vel[i])
    moonTotal = totEn(pot, kin)

    totalSumEnergy += moonTotal

print(totalSumEnergy)


