from curses.ascii import isdigit
import numpy as np 


def FileRead(filePath):
    file = open(filePath, 'r')
   
    dimension = int(file.readline())
   
    fileElemenList = file.read().split()
   
    file.close()

    matrixElementList = []

    for element in fileElemenList:
        
        elementParted = element.split('.')

        if elementParted[0].isdigit():    
            
            if fileElemenList.index(element) > 0 and \
            fileElemenList[fileElemenList.index(element)-1] == '-':            
                if len(elementParted) == 2:   
                    matrixElement = - float( elementParted[0] + '.' + elementParted[1])

                else:
                    matrixElement = - float(elementParted[0])
            else:
                if len(elementParted) == 2:     
                    matrixElement = float(elementParted[0] + '.' + elementParted[1])

                else:
                    matrixElement = float(elementParted[0])

            matrixElementList.append(matrixElement)

    matrix = np.array(matrixElementList).reshape(dimension, dimension + 1)
    
    matrixCoeficient = []
    
    for column in range(dimension):
        matrixCoeficient.append(matrix[ : , column ]) 

    matrixCoeficient = np.column_stack(matrixCoeficient)
    matrixIndependentTerm = matrix[:, dimension]


    return matrixCoeficient, matrixIndependentTerm

def TransformToDiagonallyDominant(coefMatrix):
#    print(f'Matriz: \n {coeficientMatrix}\n')
    dimension = coefMatrix.shape[0]
#    print(f'Dimensión: \n{dimension}\n')
    dominantElements = []

    for row in range(dimension):
        currentRow = coefMatrix[row,:]
        maxRow = currentRow.max()
        maxIndex = np.where(currentRow == maxRow)
#        print(maxIndex)

        if maxIndex not in dominantElements:
            dominantElements.append(maxIndex)
        else:
            print('Error, the matrix is no transformable to a diagonally dominant one.')
            return np.NaN

    diagonalDominantMatrix = np.zeros((dimension,dimension))

    for index, place in enumerate(dominantElements):
        diagonalDominantMatrix[place, :] = coefMatrix[index,:] 

    return diagonalDominantMatrix  



filePath = 'equation.txt'

coeficientMatrix, independetTermVector = FileRead(filePath)

print(f'The coeficient matrix is: \n{coeficientMatrix} \n')
print(f'The intependent term vector is: \n{independetTermVector} \n')

diagonallyDominant = TransformToDiagonallyDominant(coeficientMatrix)

print(f'The diagonally dominant matrix is: \n{diagonallyDominant} \n')
