from function import f, f_1

def newton(x_0, tol, maxiter=10000):
    x_1 = x_0 - ( f(x_0) / f_1(x_0) )
    iteration = 1
    error_x = abs(x_1 - x_0)
    error_y = abs(f(x_1))

    while error_x > tol and error_y > tol and iteration < maxiter:
        x_0 = x_1
        x_1 = x_0 - ( f(x_0) / f_1(x_0) )
        iteration += 1
        error_x = abs(x_1 - x_0)
        error_y = abs(f(x_1))

    return x_1, error_x, error_y, iteration


def secant(x_0, x_1, tol, maxiter=10000):
    x_2 = x_1 - ( f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0) ) )
    iteration = 1
    error_x = abs(x_2 - x_1)
    error_y = abs(f(x_2))

    while error_x > tol and error_y > tol and iteration < maxiter:
        x_0 = x_1
        x_1 = x_2
        x_2 = x_1 - ( f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0) ) )
        iteration += 1
        error_x = abs(x_2 - x_1)
        error_y = abs(f(x_2))

    return x_2, error_x, error_y, iteration


root, x_error, y_error, iterations = newton(10, 0.0001)
print(f'The root is: {root} \n\
        The x error is: {x_error}\n\
        The y error is: {y_error}\n\
        The iterations were: {iterations}\n')

root, x_error, y_error, iterations = secant(4, 10, 0.0001)
print(f'The root is: {root} \n\
        The x error is: {x_error}\n\
        The y error is: {y_error}\n\
        The iterations were: {iterations}\n')



