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

matrix = [[],[]]

for row  in data:
    for j in range(xlength):
        matrix.append(row[j])

print(matrix)
print(type(matrix))

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


#Determine the asteroid with the highest number of visible asteroids

