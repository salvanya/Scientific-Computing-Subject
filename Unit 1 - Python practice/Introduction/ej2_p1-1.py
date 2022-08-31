import numpy as np
from numpy import pi

iterator = 1
list = [1]
while iterator <= 20:
    iterator += 0.5
    list.append(iterator)

print(list)

print("List with arange")
array = np.arange(pi, 2*pi, pi/15)

print(array)

print("List with linspace")
array = np.linspace( pi, 2*pi, 15 )
print(array)
