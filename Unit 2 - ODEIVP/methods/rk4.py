import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from function import f

x_0 = 0
x_end = 4
h = 0.1
y_0 = 1

def rk4(Y, x, h):
    k1 = f(x, Y)
    k2 = f(x + h / 2, Y + h * (0.5 * k1) )
    k3 = f(x + h / 2, Y + h * (0.5 * k2) )
    k4 = f(x + h, Y + h * (1 * k3) )
    return Y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

x = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))
method_data = [x, [y_0]]    
Y_i = y_0 
x = np.nditer(x, flags=['f_index'])
x.iternext()

for x_i in x:
    Y_i = rk4(Y_i, x_i, h)
    method_data[1].append(Y_i)

def compare_function(x,y=1):
    func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    return func

function_to_compare = [method_data[0], []]

for x in method_data[0]:
    function_to_compare[1].append(compare_function(x))

plt.plot(function_to_compare[0],function_to_compare[1], label = 'Analitic Function')
plt.plot(method_data[0],method_data[1], label = 'Predicted Function')
sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by rk4's Method")

plt.legend(loc='upper right')

plt.show()