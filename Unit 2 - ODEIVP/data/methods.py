from data.function import f
def euler(Y, x, h):
    return Y + h * f(x,Y)


def midpoint(Y, x, h):
    return Y + h * f( x+(h/2), Y+(h/2)*f(x, Y) )

def heun(Y, x, h):
    return Y + h * ( 0.5 * f(x,Y) + 0.5 * f(x+h, Y + h*f(x,Y)))

def rk4(Y, x, h):
    k1 = f(x, Y)
    k2 = f(x + h / 2, Y + h * (0.5 * k1) )
    k3 = f(x + h / 2, Y + h * (0.5 * k2) )
    k4 = f(x + h, Y + h * (1 * k3) )
    return Y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

