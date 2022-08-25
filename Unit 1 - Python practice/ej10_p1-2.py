from email.errors import MisplacedEnvelopeHeaderDefect
import numpy as np

matA = np.loadtxt('data/matriz_A.dat',  skiprows=1)
matB = np.loadtxt('data/matriz_B.dat',  skiprows=1)
matC = np.loadtxt('data/matriz_C.dat',  skiprows=1)

print(matA, matA.shape)
print(matB, matB.shape)
#print(matC, matC.shape)

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



print(matrixMultiplication(matA, matB), matrixMultiplication(matA, matB).shape)

print(np.matmul(matA, matB), np.matmul(matA, matB).shape)