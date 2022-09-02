import numpy as np
from numpy import pi
import matplotlib.pyplot as plt


def Reach(initialVelocity, angle):
    reach = ((initialVelocity**2)*np.sin(2*angle))/9.8067

    x = np.linspace(0, reach, 101)

    y = []

    for xi in x:
        time = xi / ( initialVelocity * np.cos(angle) )
        
        yi = initialVelocity * np.sin(angle) * time - (1/2) * 9.8067 * (time**2)

        y.append(yi)

    return x, y

def CreateAngleList():
    angleList = []
    
    angle = 5
    
    while angle <= 85:
        angleList.append((angle*pi)/180)
        angle += 5

    return angleList

initialVelocity = 35

angleList = CreateAngleList()

angleLabel = 5

for angle in CreateAngleList():
    x, globals()[f'y{angle}'] = Reach(initialVelocity, angle)
    plt.plot(x, globals()[f'y{angle}'], label=f'{angleLabel}°')
    angleLabel += 5

plt.xlabel('X distance [m]')
plt.ylabel("Y distance [m]")
plt.title("Projectile motion at different angles")

plt.legend(bbox_to_anchor=(1.01, 1))

plt.show()