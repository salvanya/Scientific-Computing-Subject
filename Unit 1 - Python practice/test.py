import numpy as np

matrix = np.array([[1,2],[3,4]])

row, col = matrix.shape

for j in range(col):
    for i in range(row):
        print(matrix[i,j])

