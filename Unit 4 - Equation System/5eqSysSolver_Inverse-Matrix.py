import numpy as np 

matrix = np.loadtxt('matrix_to_invert.txt', comments = '#')

print(matrix)

def inverse(matrix):
    dim = matrix.shape[0]
    col = 0

    identity = np.zeros(matrix.shape)
    for i in range(dim):
        identity[i,i] = 1

    matrix = np.concatenate((matrix, identity), axis=1)     

    print(matrix)

    for i in range(dim):
        if (matrix[i] == np.zeros(dim*2)).all():
            print('This system is Indeterminated')
            return

        incompatible = np.zeros(dim*2)
        incompatible[4] = matrix[i,dim]
        
        if (matrix[i] == incompatible).all():
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
                    break 

        for j in range(dim):
            if j != i:
                matrix[j, :] -= matrix[i, :] * ( matrix[j,col] / matrix[i,col] )

        matrix[i,:] = matrix[i,:] / matrix[i,col] 

        col += 1

    print(matrix)
    
    solution =  np.array_split(matrix, 2, axis = 1)

    return solution[1]


print(f'The solution vector is: {inverse(matrix)}')
