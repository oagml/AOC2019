"""
This is an orchard tree problem. Some ideas to solve this puzzle:
    Use a matrix to store the positions of asteroids and empty spaces
    Linear algebra could be useful
    Move the origin to each asteroid to analyze that position
"""

import numpy as np

#Import the data and convert into a matrix

data = open('inputdata.txt', 'r').read().splitlines()

xlength = len(data[0]) #Get the length of one line (All lines have the same length)
ylength = len(data) #Get the length of the list

matrix = np.chararray((36,36))
matrixOfsights = np.zeros((36,36))

rowcount = 0
for row  in data:
    for column in range(xlength):
        matrix[rowcount,column] = row[column]
    rowcount += 1

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


for i in range(xlength):
    for j in range(ylength):
        if(matrix[i][j] == b'#'): #Asteroid to be analyzed found
            xOrigin = i
            yOrigin = j
            slopesNquads = set()
            for k in range(xlength):
                for l in range (ylength):
                    if (k == i and l == j): #Ignore the asteroid being analyzed
                        pass
                    else:
                        print(f"Comparing asteroid in {i},{j} with asteroid in {k},{l}")
                        if(matrix[k][l] == b'#'): #Asteroid to be compared to found
                            currentSlopeQuad = determineSlopeQuadrant(i,j,k,l)
                            print(currentSlopeQuad)
                            if(currentSlopeQuad in slopesNquads):
                                pass
                            else:
                                slopesNquads.add(currentSlopeQuad)
                                matrixOfsights[i][j] = matrixOfsights[i][j] + 1

print(matrixOfsights)

print(np.amax(matrixOfsights))

#Once you have the matrix loop through every position in the matrix and analyse how many asteroids
#they can see

#As you loop through each asteroid in the matrix, identify every line of sight with other asteroids
#and store every slope you find in a set of slopes, also identify the distance of to each asteroid
#if you find an asteroid with a slope previously found, compare the distance and the one with the lesser distance
#is the one in the actual sight
#Make matrix where you store the number of asteroids each asteroid is seeing like this:
'''
.7..7
.....
67775
....7
...87

'''
#Another possible solution is to just count the slopes, if you find an asteroid, store the slope,
#if you then find another asteroid with the same slope, just ignore it.


#Determine the asteroid with the highest number of visible asteroids

