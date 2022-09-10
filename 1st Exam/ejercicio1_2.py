import numpy as np
import matplotlib.pyplot as plt

file = open("resultados_funcion.dat", "r")

data = []

for i in range(6):
    data.append(file.readline().split())

file.close()

print(len(data))

for i, x in enumerate(data):
    for index, element in enumerate(x):
        data[i][index] = float(element) 

plt.plot(data[0], data[1], label = r'$2.|\theta$')
plt.plot(data[0], data[2], label = r'$4.|\theta$')
plt.plot(data[0], data[3], label = r'$6.|\theta$')
plt.plot(data[0], data[4], label = r'$8.|\theta$')
plt.plot(data[0], data[5], label = r'$10.|\theta$')       

plt.xlabel (r'$theta$')
plt.ylabel (r'$sin(n.\theta)$')

plt.legend ()

plt.savefig ('plot10.pdf')