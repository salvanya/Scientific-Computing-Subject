import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def calculateSine(x):
    return np.sin(2*x)

x1 = np.linspace(0, 2*pi, 51)
#print("x1 = ", x1)
x2 = np.arange(pi/2, 3*pi, pi/10)
#print("x2 = ", x2)

y1 = []
for number in x1:
    y1.append(calculateSine(number))
#print("y1 = ", y1)
     
y2 = []
for number in x2:
    y2.append(calculateSine(number))
#print("y2 = ", y2)

plt.plot(x1, y1)
plt.plot(x2, y2)

plt.title("Sine of the double angle")
plt.xlabel("Angle")
plt.ylabel("Sine of the angle")
plt.show()

