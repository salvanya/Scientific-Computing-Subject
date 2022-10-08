import numpy as np
import matplotlib.pyplot as plt

def f(x, Y):
    func = np.zeros(2)
    func[0] = Y[1]    
    func[1] = -Y[0]
    
    return func
    
x_0 = 0
x_end = 10
h = 0.1
x_i = x_0
Y_i = np.zeros(2)
Y_i[0] = 1
Y_i[1] = 0

def rk4(x, Y, h):
    k1 = f(x, Y)
    k2 = f(x + h / 2, Y + h * (0.5 * k1) )
    k3 = f(x + h / 2, Y + h * (0.5 * k2) )
    k4 = f(x + h, Y + h * (1 * k3) )
    return Y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

data = [[x_0],[1],[0]]

while x_i <= x_end:
    Y_i= rk4(x_i, Y_i, h)
    data[1].append(Y_i[0])
    data[2].append(Y_i[1])
    
    x_i += h
    data[0].append(x_i)

#print( data )

plt.plot(data[0], data[1], label = 'u')
plt.plot(data[0], data[2], label = 'v')

plt.legend()

plt.show()