import numpy as np
import matplotlib.pyplot as plt

# Equations:
#u[0] is x and u[1] is x dot , u[2] is y and u[3] is y dot

w=1
b=0.2

def F(y,x):
    fx=y[1]
    ax=-w**2 * y[0]-b * fx
    fy=y[3]
    ay=-(w+0.2)**2 * y[2]-(b+0.1) * fy
    return np.array([fx,ax,fy,ay])

def rk4(f, y0,x0, xm , n):
    x = np.linspace(x0, xm, n+1)
    y = np.array((n+1)*[y0])
    h = x[1]-x[0] 

    for i in range(n): 
        k1 = h * f(y[i], x[i]) 
        k2 = h * f(y[i] + 0.5 * k1, x[i] + 0.5*h) 
        k3 = h * f(y[i] + 0.5 * k2, x[i] + 0.5*h) 
        k4 = h * f(y[i] + k3, x[i] + h) 
        y[i+1] = y[i] + (k1 + 2*(k2 + k3) + k4) / 6 
    
    return y, x 
        
u, t = rk4(F, np.array([10.,20.,10.,20.]) , 0. , 100. , 1000) 

x,vx,y,vy= u.T 
 
plt.plot(t, x, t, y) 
plt.grid('on') 
plt.legend(['x(t)','y(t)']) 
plt.show()
