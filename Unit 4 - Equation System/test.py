from pprint import pprint
import numpy as np

matrix = np.loadtxt('matrix.txt')

dim = len(matrix[0])

a = matrix[0:,0:dim-1]

b = matrix[:,dim-1]

print("Matrix:")
pprint(matrix)


print("A:")
pprint(a)

print("b:")
pprint(b)
