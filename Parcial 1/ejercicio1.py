import numpy as np
from numpy import pi

def sen(constante,angulo):
    return np.sin(constante*angulo)

x = np.linspace(-pi, pi, 101)

file = open("resultados_funcion.dat", "a")

for angle in x:
    file.write(str(angle)+" ")

file.write('\n')

for numero in range(2,11):
    if numero%2 == 0:
        for angle in x:
            file.write(str(sen(numero, angle))+ " ")
        file.write('\n')

file.close