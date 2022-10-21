import numpy as np

def g(x0):
    x = x0[0]
    y = x0[1]
    g1 = (x**2 - y + 0.5) / 2
    g2 = (-(x**2) - 4*(y**2) + 8*y + 4) / 8
    g = np.array([g1, g2])

    return g

def Fixed_Point(x_0, tol, maxiter):
    iteration = 0

    while iteration < maxiter:
        x_i = g(x_0)

        print(f'x_0 = {x_0}')
        print(f'x_i = {x_i}')

        error = abs(np.max(x_i - x_0))
        print(f'Error = {error}')
        if  error < tol and iteration > 1:
            return x_i

        x_0 = np.copy(x_i)

        iteration += 1
        print(f'iteration: {iteration}')
        print('------------------')

    print("The seed does not converge")
    return None

x_0 = np.array([0, 1])
tol = 1e-10
maxiter = 100

print(f'The solution is: {Fixed_Point(x_0, tol, maxiter)}')
