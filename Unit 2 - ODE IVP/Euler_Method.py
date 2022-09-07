import numpy as np
import matplotlib.pyplot as plt

def pend(y, t, b, c):
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

b = 0.25
c = 5.0
y0 = np.array([np.pi - 0.1, 0.0])

def rungekutta1(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        y[i+1] = y[i] + (t[i+1] - t[i]) * f(y[i], t[i], *args)
    return y

t = np.linspace(0, 10, 1001)
sol1 = rungekutta1(pend, y0, t, args=(b, c))

plt.plot(t, sol1[:, 0], label='Euler')
plt.plot(t, sol1[:, 0], label='Heun')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

