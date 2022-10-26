import numpy as np
import matplotlib.pyplot as plt
from auxiliar.exp_data_simulator import exp_data_simulator

def func(x):
    return 0.1 + 0.2*((0.9*x)**2)

def Z_der(x,a):
    '''Z_der(x,a)
       x[numpy array]: Vector of X values from data
       a[numpy array]: Vector of parameters'''
    first_der = []
    second_der = []
    third_der = []

    for x_i in x:
        first_der.append(1)
        second_der.append((a[2]*x_i)**2)
        third_der.append(2*(a[2]*x)*x)

    return np.array([first_der,second_der,third_der]).transpose() 

def Gauss_Newton(x, y, func, Z, guess ,err, maxiter):
    '''Gauss_Newton(x, y, func, parameter_num ,err, maxiter)
       x[list]: X values of the data points
       Y[list]: Y values of the data points
       func[function y=f(x)]: Function to fit
       Z[function] = Derivative matrix evaluator.
       guess[list[float]]: List of initial guess for parameters
       err[float]: Acceptable error to interrupt
       maxiter[int]: Iterations before interrupting'''



    iter = 0
    a_i = np.array(guess)

    while iter < maxiter:
        iter += 1
        z_der = Z_der(x, a_i)        
        


x, y = exp_data_simulator(-10, 10, func, 2)
z_der = Z_der(x,[3,4,5])

print (f'z_der = {z_der} \n z_der shape = {z_der.shape}')

# fit_x, fit_y = linear_least_square(x,y)


plt.scatter(x,y, color = 'black', label = 'Experimental Data')
# plt.plot(fit_x, fit_y, color = 'red', label = 'Linear Fit')

plt.legend()
