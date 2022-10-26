import numpy as np
import matplotlib.pyplot as plt
from auxiliar.exp_data_simulator import exp_data_simulator

def func(x):
    return 3 + 5*x

x, y = exp_data_simulator(0, 20, func, 10)

def linear_least_square(x, y):
    '''linear_least_square(x, y)'''
    
    # Create Z matrix transpose
    first_column = np.ones(len(x))
    Z_transpose = np.array([first_column, x])
    #print(f'Z_transpose = {Z_transpose}')
    
    # Create Y vector
    Y = np.array(y)
    #print(f'Y = {Y}')

    # Create Z
    Z = Z_transpose.transpose()
    #print(f'Z = {Z}')
    
    # Create a
    a = np.linalg.inv(Z_transpose.dot(Z)).dot(Z_transpose.dot(Y))
    #print(a)

    # Create linear fit y's
    linear_y = []
    print(a)
    for x_i in x:
        linear_y.append(a[0]+a[1]*x_i)
    
    return (x, linear_y)


fit_x, fit_y = linear_least_square(x,y)

plt.scatter(x,y, color = 'black', label = 'Experimental Data')
plt.plot(fit_x, fit_y, color = 'red', label = 'Linear Fit')

plt.legend()
