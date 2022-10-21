import numpy as np

def jacobi(A,B, X0, tol, maxiter = 1000):
    # PROCEDIMIENTO

    # Gauss-Seidel
    tamano = np.shape(A)

    n = tamano[0]
    m = tamano[1]
    X = np.copy(X0)

    for i in range(0,n,1):
        columna=abs(A[i:,i])
        dondemax=np.argmax(columna)
        if(dondemax!=0):
            #intercambio filas
            temporal=np.copy(A[i,:])
            A[i,:]=A[dondemax+i,:]
            A[dondemax+i,:]=temporal

    diferencia = np.ones(n, dtype=float)
    iteraciones=1

    while iteraciones < maxiter:
        Xi = np.zeros(X0.shape[0])
        
        for i in range(0,n,1):
            suma = 0
            for j in range(0,m,1):
                if(i!=j):
                    suma = suma-A[i,j]*X0[j]
            nuevo = (B[i]+suma)/A[i,i]
            diferencia[i] = np.abs(nuevo-X0[i])
            norma = np.max(diferencia)
            Xi[i] = nuevo

        X0 = np.copy(Xi)

        if norma < tol:
            return X0

        iteraciones+=1

    return None

# INGRESO
A = np.array([[3. , -0.1, -0.2],
              [0.1,  7  , -0.3],
              [0.3, -0.2, 10  ]])

B = np.array([7.85,-19.3,71.4])

X0  = np.array([0.,0.,0.])

tolera = 0.00001

print(jacobi(A,B,X0,tolera))