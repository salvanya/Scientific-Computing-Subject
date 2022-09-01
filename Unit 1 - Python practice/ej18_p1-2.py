import random as rnd
import numpy as np

def CreateRandomVector(dimension):
    vector = []
    for i in range(dimension):
        vector.append(rnd.randrange(-9 ,10))
    
    return np.array(vector)

def GramSchmidt(vectorList, dimension):

    zero = np.zeros(dimension)

    orthogonalVectorList = []

    while len(orthogonalVectorList) < len(vectorList):
        for vector in vectorList:    
            projections = zero
            
            for orthogonalVector in orthogonalVectorList:
                projections += -( np.dot((np.dot(vector,orthogonalVector)) \
                    / (np.dot(orthogonalVector,orthogonalVector)), orthogonalVector) )     

            newOrthogonalVector = vector-projections

            if (newOrthogonalVector == zero).all():
                print(f'These vectors does not form a basis for R{dimension}')
                return 0

            orthogonalVectorList.append(newOrthogonalVector)

    return orthogonalVectorList

def GenerateAndPrintVectorSet(dimension):
    print(f'The random generated {dimension}-dimensional vectors are: ')

    vectorList = []

    for i in range(dimension):
        globals()[f'vector{i}'] = CreateRandomVector(dimension)    
        
        vectorList.append(globals()[f'vector{i}'])

        print( globals()[f'vector{i}'] )

    return vectorList


nDimension = int(input("Enter de vector dimension: "))

vectorList = GenerateAndPrintVectorSet(nDimension)

print(f'The orthogonal basis for the {nDimension}-dimensional space are')

orthogonalVectorList = GramSchmidt(vectorList, nDimension)

for orthogonalVector in orthogonalVectorList:
    print(orthogonalVector)

