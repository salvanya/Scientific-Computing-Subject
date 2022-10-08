from function import f
import numpy as np

def bisection(a, b, tol, maxiter=10000):   
    c = (a + b) / 2
    f_c = f(c)
    f_a = f(a)
    f_b = f(b)
    error = abs(a-b)/2

    iteration = 1

    while (error) > tol and abs(f_c) > tol and iteration < maxiter:
        if np.sign(f_a) != np.sign(f_c):
            b = c
        elif np.sign(f_b) != np.sign(f_c):
            a = c

        c = (a + b) / 2
        f_a = f(a)
        f_b = f(b)
        f_c = f(c)
        iteration += 1
        error = abs(a-b)/2
    

    return c, error, iteration

def false_position(a, b, tol, maxiter=10000):       
    f_a = f(a)
    f_b = f(b)
    c = b - (f_b * ( b - a ))/(f_b-f_a)
    c_prev = c+100
    f_c = f(c)
    iteration = 1
    error = abs(c - c_prev)

    while abs(c - c_prev) > tol and abs(f_c) > tol and iteration < maxiter:
        if np.sign(f_a) != np.sign(f_c):
            b = c
        elif np.sign(f_b) != np.sign(f_c):
            a = c

        f_a = f(a)
        f_b = f(b)
        c_prev = c
        c = b - (f_b * ( b - a ))/(f_b-f_a)
        f_c = f(c)
        iteration += 1
        error = abs(c - c_prev)
    
    return c, error, iteration

bis, bis_err, iter = bisection(-9,0,0.001)
print(f'The root is {bis} with an error of {bis_err} in {iter} iterations')

false_pos, false_pos_err, iter = false_position(-9,0,0.001)
print(f'The root is {false_pos} with an error of {false_pos_err} in {iter} iterations')    

