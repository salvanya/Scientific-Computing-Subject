import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from euler import euler
from midpoint import midpoint

def f(x, y=0):
    func = - 2*x**3 + 12*x**2 - 20*x + 8.5
    return func

def heun(f, x0, x_end, h, y0):
    x = np.linspace(x0, x_end, int(((x_end - x0)/h)))
    heun_method = [x, [y0]]    
    yi = y0
    x = np.nditer(x, flags=['f_index'])
    x.iternext()

    for xi in x:
        yip1 = yi + h * ( 0.5 * f(xi,yi) + 0.5 * f(xi+h, yi + h*f(xi,yi)))      
        heun_method[1].append(yip1)
        yi = yip1

    return heun_method

heun_data = heun(f, 0 , 4, 0.1, 1)
euler_data = euler(f, 0 , 4, 0.1, 1)
midpoint_data = midpoint(f, 0 , 4, 0.1, 1)

def compare_function(x):
    func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    return func

function_to_compare = [heun_data[0], []]

for x in heun_data[0]:
    function_to_compare[1].append(compare_function(x))

plt.plot(function_to_compare[0],function_to_compare[1], label = 'Analitic function')
plt.plot(heun_data[0],heun_data[1], label = "Heun's method")
plt.plot(euler_data[0], euler_data[1], label = "Euler's method")
plt.plot(midpoint_data[0], midpoint_data[1], label = "Midpoint's method")

sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by Heun's Method compared to analitic and other methods")

plt.legend(loc='upper right')

plt.show()
