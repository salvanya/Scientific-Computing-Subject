import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def f(x, y=0):
    func = - 2*x**3 + 12*x**2 - 20*x + 8.5
    return func

def euler(f, x0, x_end, h, y0):
    x = np.linspace(x0, x_end, int(((x_end - x0)/h)))
    euler_method = [x, [y0]]    
    yi = y0
    x = np.nditer(x, flags=['f_index'])
    x.iternext()

    for xi in x:
        yip1 = yi + h * f(xi,yi)           
        euler_method[1].append(yip1)
        yi = yip1

    return euler_method

euler_data = euler(f, 0 , 4, 0.1, 1)

def compare_function(x,y=1):
    func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    return func

function_to_compare = [euler_data[0], []]

for x in euler_data[0]:
    function_to_compare[1].append(compare_function(x))

plt.plot(function_to_compare[0],function_to_compare[1], label = 'Analitic Function')
plt.plot(euler_data[0],euler_data[1], label = 'Predicted Function')
sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by Euler's Method")

plt.legend(loc='upper right')

plt.show()
