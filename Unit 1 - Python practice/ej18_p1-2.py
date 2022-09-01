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
                projections += (-1)* ( ( np.dot(vector,orthogonalVector) / np.dot(orthogonalVector,orthogonalVector)) * orthogonalVector)
                
                # print(f'u = {vector}\
                #     \nv = {orthogonalVector}\
                #     \n<u,v> = {np.dot(vector,orthogonalVector)}\
                #     \n<u,u> = {np.dot(orthogonalVector,orthogonalVector)}\
                #     \n<u,v>/<u,u> = {np.dot(vector,orthogonalVector) / np.dot(orthogonalVector,orthogonalVector)}\
                #     \n<u,v>/<u,u>*v = {( ( np.dot(vector,orthogonalVector) / np.dot(orthogonalVector,orthogonalVector)) * orthogonalVector)}\
                #     \nProjection for {orthogonalVector} = {projections}\n')
                 

#            print(f'Vector: {vector}')
            
#            print(f'Projection: {projections}')

            newOrthogonalVector = vector + projections
            
#            print(f'Orthogonal vector: {newOrthogonalVector}')
            
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

# nDimension = 2
# vectorList = np.array([[1,2],[2,1]])
# print(f'Vecors:\n {vectorList[0]}\n {vectorList[1]}\n')

print(f'The orthogonal basis for the {nDimension}-dimensional space are: ')

orthogonalVectorList = GramSchmidt(vectorList, nDimension)

for orthogonalVector in orthogonalVectorList:
    print(orthogonalVector)

