import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def f(x, y=0):
    func = np.zeros(2)
    
    func[0] = y[1]
    func[1] = x*(y[0]**2)
    
    return func

x_0 = 0
x_end = 100
h = 0.1
y_0 = np.zeros(2)
y_0[0] = 1
y_0[1] = 0

print(y_0)

def euler(Y, x, h):
    return Y + h * f(x,Y) 

x = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))
method_data = [ x, [y_0[0]], [y_0[1]] ]    
Y_i = y_0
x = np.nditer(x, flags=['f_index'])
x.iternext()

print (method_data)

for x_i in x:
    Y_i = euler(Y_i, x_i, h)
    method_data[1].append(Y_i[0])
    method_data[2].append(Y_i[1])
    
print(method_data)


for i in range( len(method_data) - 1 ):
    plt.plot(method_data[0],method_data[i+1], label = f'y{i+1}')

sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by Euler's Method")

plt.legend(loc='upper right')

plt.show()

