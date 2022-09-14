import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from function import f

x_0 = 0
x_end = 4
h = 0.1
y_0 = 1

def heun(Y, x, h):
    return Y + h * ( 0.5 * f(x,Y) + 0.5 * f(x+h, Y + h*f(x,Y)))

x = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))
method_data = [x, [y_0]]    
Y_i = y_0
x = np.nditer(x, flags=['f_index'])
x.iternext()

for x_i in x:
    Y_i = heun(Y_i, x_i, h)
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
plt.title("ODE solving by heun's Method")

plt.legend(loc='upper right')

plt.show()