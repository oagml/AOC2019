'''
Part 2 of the Day 10
From the position of the monitoring station, destroy asteroids with a laser, the laser can only
destroy one asteroid at a time, destroy one and then rotate clockwise to destroy the next asteroid.
Repeat the process until all asteroids are destroyed. Find the position of the 200th asteroid
destroyed.
'''

import numpy as np

data = open('inputdata.txt', 'r').read().splitlines()


xlength = len(data[0]) #Get the length of one line (All lines have the same length)
ylength = len(data) #Get the length of the list

matrix = np.chararray((36,36))

rowcount = 0
for row  in data:
    for column in range(xlength):
        matrix[rowcount,column] = row[column]
    rowcount += 1

print(matrix)

stationx = 29 #Monitoring station at x coordinates
stationy = 26 #Monitoring station at y coordinates

'''
This function determines the slope and quadrant of a given point in a matrix relative to
the origin, it returns a tuple with the calculated slope and quadrant
'''
def determineSlopeQuadrant(xOrigin, yOrigin, xTarget, yTarget):

    if ((yOrigin - yTarget) == 0): #Avoid division by zero
        slope = -999

    else:
        slope = (xOrigin-xTarget)/(yOrigin-yTarget)

    if (xTarget>=xOrigin and yTarget>yOrigin):
        quadrant = "I"

    elif (xTarget<xOrigin and yTarget>=yOrigin):
        quadrant = "II"

    elif (xTarget<=xOrigin and yTarget<yOrigin):
        quadrant = "III"

    elif (xTarget>xOrigin and yTarget<=yOrigin):
        quadrant = "IV"

    else:
        quadrant = "NA"

    return(slope,quadrant)

#From the monitoring station, examine all other asteroids that are visible and store them in
#"groups" of the same slope, each entry is going to contain the x and y position and the distance
#to the monitoring station  (manhattan distance)
groups = dict()

for i in range(xlength):        #columns
    for j in range(ylength):    #rows
        currentSlope = determineSlopeQuadrant(stationx, stationy, i, j)
        

#Once you have the groups,sort them from the smallest to the greatest distance 

#Sort the groups in a clockwise order, starting from straight up.

#Make a loop to knock off asteroids the smallest of each group and count until you reach the 
#200th asteroid
