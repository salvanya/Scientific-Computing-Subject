import numpy as np

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