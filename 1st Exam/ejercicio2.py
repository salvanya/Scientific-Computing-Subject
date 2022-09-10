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

    mas_ceros = max(ceros_por_fila.values(),default=0)

    filas_mas_ceros = []

    for fila in ceros_por_fila.keys():
        if ceros_por_fila[fila] == mas_ceros:
            filas_mas_ceros.append(fila)
    if len(filas_mas_ceros) == 0:
        return [0]
    return filas_mas_ceros

print(f'La/s fila/s con más ceros es/son {FilasMasCeros(datos)}')
    

def determinante(matriz, total=0):

    indices = np.shape(matriz)
     

    if indices[0] == 2 and indices[1] == 2:
        valor = matriz[0,0] * matriz[1,1] - matriz[1,0] * matriz[0,1]
        return valor
 

    fila = FilasMasCeros(matriz)[0]

    for columna in range(indices[1]):
        menor = np.delete(matriz, fila, 0 )
        menor = np.delete(menor,columna,1)
        
        signo = (-1)**(columna + fila) 

        sub_det = determinante(menor)

        total += signo * matriz[fila,columna] * sub_det 
 
    return total

print(f'El determinante de la matriz con mi método {determinante(datos)}')
print(f'El determinante de la matriz con numpy {np.linalg.det(datos)}')
