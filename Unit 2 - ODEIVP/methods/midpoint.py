import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from euler import euler

def f(x, y=0):
    func = - 2*x**3 + 12*x**2 - 20*x + 8.5
    return func

def midpoint(f, x0, x_end, h, y0):
    x = np.linspace(x0, x_end, int(((x_end - x0)/h)))
    midpoint_method = [x, [y0]]    
    yi = y0
    x = np.nditer(x, flags=['f_index'])
    x.iternext()

    for xi in x:
        yip1 = yi + h * f( xi+(h/2), yi+(h/2)*f(xi, yi) )           
        midpoint_method[1].append(yip1)
        yi = yip1

    return midpoint_method

midpoint_data = midpoint(f, 0 , 4, 0.1, 1)
euler_data = euler(f, 0 , 4, 0.1, 1)

def compare_function(x):
    func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    return func

function_to_compare = [midpoint_data[0], []]

for x in midpoint_data[0]:
    function_to_compare[1].append(compare_function(x))

plt.plot(function_to_compare[0],function_to_compare[1], label = 'Analitic function')
plt.plot(midpoint_data[0],midpoint_data[1], label = "Midpoint's method")
plt.plot(euler_data[0], euler_data[1], label = "Euler's method")
sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by Midpoint's Method compared to analitic and Euler's Method")

plt.legend(loc='upper left')

plt.show()
