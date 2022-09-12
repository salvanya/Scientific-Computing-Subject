import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from euler import euler
from midpoint import midpoint
from heun import heun

def f(x, y=0):
    func = - 2*x**3 + 12*x**2 - 20*x + 8.5
    return func

def rk4(f, x0, x_end, h, y0):
    x = np.linspace(x0, x_end, int(((x_end - x0)/h)))
    rk4_method = [x, [y0]]    
    yi = y0
    x = np.nditer(x, flags=['f_index'])
    x.iternext()

    for xi in x:
        k1 = f(xi, yi)
        k2 = f(xi + h / 2, yi + h * (0.5 * k1) )
        k3 = f(xi + h / 2, yi + h * (0.5 * k2) )
        k4 = f(xi + h, yi + h * (1 * k3) )
        yip1 = yi + h/6 * (k1 + 2*k2 + 2*k3 + k4)      
        rk4_method[1].append(yip1)
        yi = yip1

    return rk4_method

rk4_data = rk4(f, 0 , 4, 0.1, 1)
euler_data = euler(f, 0 , 4, 0.1, 1)
midpoint_data = midpoint(f, 0 , 4, 0.1, 1)
heun_data = heun(f, 0 , 4, 0.1, 1)


def compare_function(x):
    func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    return func

function_to_compare = [rk4_data[0], []]

for x in rk4_data[0]:
    function_to_compare[1].append(compare_function(x))

plt.plot(function_to_compare[0],function_to_compare[1], label = 'Analitic function')
plt.plot(euler_data[0], euler_data[1], label = "Euler's method")
plt.plot(midpoint_data[0], midpoint_data[1], label = "Midpoint's method")
plt.plot(heun_data[0], heun_data[1], label = "Heun's method")
plt.plot(rk4_data[0],rk4_data[1], label = "RK4's method")

sns.set()


plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title("ODE solving by RK4's Method compared to analitic and other methods")

plt.legend(loc='upper right')

plt.show()
