import numpy as np

datos = np.loadtxt ('matriz.dat', comments ='#',skiprows = 1 )

shape_datos = np.shape ( datos )

print(datos)
print(shape_datos)

def FilasMasCeros(datos):
    shape_datos = np.shape ( datos )    
    ceros_por_fila = {}
    for fila in range(shape_datos[0]):
        cant_ceros = 0
        
        for elemento in datos[fila,:]:
            if elemento == 0:
                cant_ceros += 1
        
        ceros_por_fila[fila] = cant_ceros

    mas_ceros = max(ceros_por_fila.values())

    filas_mas_ceros = []

    for fila in ceros_por_fila.keys():
        if ceros_por_fila[fila] == mas_ceros:
            filas_mas_ceros.append(fila)
    return filas_mas_ceros

print(f'La/s fila/s con más ceros es/son {FilasMasCeros(datos)}')
        

def determ(matriz, det_ant=0):
    if matriz == np.array([]):
        return 0
    fila_mas_ceros = FilasMasCeros(matriz)[0]
    det = det_ant

    for columna in range(np.shape(matriz)[1]):
        a = matriz[fila_mas_ceros, columna]
        menor = np.delete(matriz, fila_mas_ceros, columna)
        det += a * ((-1)^( fila_mas_ceros + columna)) * determ(menor, det)

    return det

determinante = determ(datos)

print(f'El determinante es {determinante}')



    # determinante = 0
    # menor = matriz
    # while menor.shape() != (2, 2): 
    #     for columna in range(menor.shape()[1]):
    #         a = datos[fila_mas_ceros, columna]
        
    #         if a == 0:
    #             continue
        

