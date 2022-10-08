import numpy as np 

matrix = np.loadtxt('matrix.txt', comments = '#')

print(matrix)

def elim_gauss(matrix):
    dim = matrix.shape[0]
    col = 0

    for i in range(dim-1):
        if (matrix[i] == np.zeros(5)).all():
            print('This system is Indeterminated')
            return
        incompatible = np.zeros(5)
        incompatible[4] = matrix[i,dim]
        if (matrix[i] == incompatible).all():
            print('This system is Incompatible')
            return 

        abs_column = abs(matrix[:, col][i:dim-1])
        max_index = i + np.argmax(abs_column)
        #max_index = np.where( matrix[:, 0] == np.max(matrix[:, 0]))
        matrix[[i, max_index]] = matrix[[max_index, i]] 

        if matrix [i,col] == 0:
            for k in range(i,dim-1):
                if matrix[k,col] != 0:
                    matrix[[i,k]] = matrix[[k,i]]
                    print(matrix)
                    break 
            
        for j in range(i+1,dim):
            matrix[j, :] -= matrix[i, :] * ( matrix[j,col] / matrix[i,col] )

        col += 1

    print(matrix)

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
