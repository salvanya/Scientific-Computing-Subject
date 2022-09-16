import numpy as np
import matplotlib.pyplot as plt

def f(x, Y):
    func = np.zeros(2)
    func[0] = Y[1]    
    func[1] = -Y[0]
    
    return func
    
x_0 = -7
x_end = 7
h = 0.1
x_i = x_0 + h
Y_i = np.zeros(2)
Y_i[0] = 1
Y_i[1] = 0

def euler(x, Y, h):
    return Y + h * f(x, Y)

data = [[x_0],[1],[0]]

while x_i <= x_end:
    data[0].append(x_i)
    Y_i= euler(x_i, Y_i, h)
    data[1].append(Y_i[0])
    data[2].append(Y_i[1])
    x_i = x_i + h

print( data )

plt.plot(data[0], data[1], label = 'u')
plt.plot(data[0], data[2], label = 'v')

plt.legend()

plt.show()