import numpy as np 

matrix = np.loadtxt('matrix.txt', comments = '#')

print(matrix)

def elim_gauss_jordan(matrix):
    dim = matrix.shape[0]
    col = 0

    for i in range(dim):
        print(f'i = {i}')

#        if (matrix[i] == np.zeros(5)).all():
        if matrix[i] == np.zeros(5):
            print('This system is Indeterminated')
            return
        incompatible = np.zeros(5)
        incompatible[4] = matrix[i,dim]
        # if (matrix[i] == incompatible).all():
        if matrix[i] == incompatible:
            print('This system is Incompatible')
            return 

        if i != dim-1:
            abs_column = abs(matrix[:, col][i:dim-1])
            max_index = i + np.argmax(abs_column)
            matrix[[i, max_index]] = matrix[[max_index, i]] 

        if matrix [i,col] == 0:
            for k in range(i,dim-1):
                if matrix[k,col] != 0:
                    matrix[[i,k]] = matrix[[k,i]]
                    print(matrix)
                    break 

        for j in range(dim):
            if j != i:
                matrix[j, :] -= matrix[i, :] * ( matrix[j,col] / matrix[i,col] )

        matrix[i,:] = matrix[i,:] / matrix[i,col] 

        #print(matrix)
        #print(f'columna = {col}')
        col += 1

    #print(matrix)

    solution = matrix[:, dim]

    return solution

sol = elim_gauss_jordan(matrix)
print(f'The solution vector is: {sol}')
print(f'El tipo de la solución es: {type(sol)}')
