# Importing Packages
import numpy as np
import matplotlib.pyplot as plt

# Defining Equation and Derivative
def f(x):
    res = np.cos(x)-2*x**3
    return res
 
def dfdx(x):
    res = -np.sin(x)-6*x**2
    return res



def Newton_Raphson(x0, tol, max_iter):
    # Newton-Raphson Algorithm
    xi_1 = x0
    i = 0  # Iteration counter
    while i < max_iter:
        i += 1
        xi = xi_1-f(xi_1)/dfdx(xi_1)  # Newton-Raphson equation

        if abs(f(xi_1)) < tol:
            return xi

        print(f'xi : {xi}')

        xi_1 = xi
    
    print('Max iteration reached')
    
    return None


max_iter = 20  # Max iterations
tol = 1E-15  # Tolerance
x0 = 1  # Initial guess



print(f'The solution is: {Newton_Raphson(x0, tol, max_iter)}')

