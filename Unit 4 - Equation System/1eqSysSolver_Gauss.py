import numpy as np 

matrix = np.loadtxt('matrix.txt', comments = '#')

print(matrix)

def elim_gauss(matrix):
    dim = matrix.shape[0]
    
    col = 0
    for i in range(dim-1):
        # print(matrix [i,col])
        if matrix [i,col] == 0:
            print ('Error, null header')
            return 

        for j in range(i+1,dim):
            matrix[j, :] -= matrix[i, :] * ( matrix[j,col] / matrix[i,col] )

        col += 1

    solution = np.zeros(dim)

    solution[dim-1] = matrix[dim-1,dim] / matrix [dim-1,dim-1]

    i = dim-2
    while i >= 0:
        j = dim-1
        while j > i:
            matrix[i,dim] -= matrix[i,j] * solution[j] 
            j -= 1

        matrix[i,dim] /= matrix[i,i]

        solution[i] = matrix[i,dim]

        i -= 1

    return solution


print(f'The solution vector is: {elim_gauss(matrix)}')

