import numpy as np
import random as rnd
import timeit

matrixSize = int(input('Enter "n" for an nxn matrix: '))


def creatRandomMatrix(n):
    matrix = []

    for i in range(n*n):
        matrix.append(rnd.randrange(0,10))

    return np.array(matrix).reshape(n,n)
     

matrix1 = creatRandomMatrix(matrixSize)
matrix2 = creatRandomMatrix(matrixSize)


def matrixMultiplication(matrix1, matrix2):
    row1, col1 = matrix1.shape 
    row2, col2 = matrix2.shape

    if col1 != row2:
        print("Matrix dimension error")
        return

    m = col1

    multMatrixList = []
    
    for i in range(row1):
        for j in range (col2):
            multipliedElement = 0
            
            for k in range(m):
                multipliedElement += matrix1[i,k]*matrix2[k,j]

            multMatrixList.append(multipliedElement)

    return np.array(multMatrixList).reshape(row1,col2) 

starttime = timeit.default_timer()

matC = matrixMultiplication(matrix1, matrix2)

endtime = timeit.default_timer()

print('Tiempo algoritmo propio {} s'.format(endtime - starttime))

starttime = timeit.default_timer()

matC = np.matmul(matrix1, matrix2)

endtime = timeit . default_timer()

print ('Tiempo algoritmo numpy {} s'.format(endtime - starttime))
