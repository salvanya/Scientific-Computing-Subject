import random as rnd
import numpy as np

nDimension = int(imput("Enter de vector dimension: "))

def CreateRandomVector(dimension):
    vector = []
    for i in range(dimension):
        vector.append(rnd.randrange(-9 ,10))
    
    return np.array(vector)

def WriteArrayFile(dimension):
    file = open('array.txt', 'x')
    for i in range(dimension):
        vector = CreateRandomVector(dimension)
        lineVector = ""
        for element in vector:
            
        file.write()

        

    file.close()