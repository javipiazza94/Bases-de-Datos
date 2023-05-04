import numpy as np

a = np.array([[3, 2], [1, 3]])
b = np.array([[2, 2], [1, 2]])

# Producto matricial de dos matrices
    #Metodo = Dos matrices A y B son multiplicables si el número de columnas de A coincide con el número de filas de B. 
    #El elemento cij de la matriz producto se obtiene multiplicando cada elemento de la fila i de la matriz A por cada elemento de la columna j de la matriz B y sumándolos.
print(np.dot(a, b))

# vdot - Devuelve el producto escalar de dos vectores.
    #Metodo = es el resultado de multiplicar las coordenadas de la misma dimensión de los vectores y sumarlas. Se llama producto escalar porque el resultado de la multiplicación siempre será un escalar.
print(np.vdot(a,b))

# inner - Producto interno de dos matrices.
    #Es una matriz de dimensiones (fila de A, columna de B), donde cada elemento en la posición (i,j) es el producto interno entre la i-ésima fila de A y la j-ésima columna de B. 
    #Es importante asegurarse de que el número de columnas de la matriz A sea igual al número de filas de la matriz B para que el producto interno pueda realizarse.
a = np.arange(6).reshape((2,3))
b = np.arange(3)
print(np.inner(a, b))

# matrix_power - Eleve una matriz cuadrada a la potencia (entera) n.
    #La función "np.linalg.matrix_power(m, n)" eleva una matriz cuadrada "m" a la potencia "n", produciendo una nueva matriz del mismo tamaño. 
    #Es equivalente a multiplicar "m" consigo misma "n" veces, lo cual también se puede hacer con la operación "np.dot(m, m)".
m = np.array([[2,3], [1,4]])
print(np.linalg.matrix_power(m, 2))
print(np.dot(m,m)) #es lo mismo porque si la elevo al cuadrado se esta multiplicando por si misma

# eig - Calcula los valores propios y los vectores propios rectos de una matriz cuadrada
    #El resultado es una tupla con dos elementos: el primer elemento es un vector con los valores propios de "m",
    #y el segundo elemento es una matriz donde cada columna representa un vector propio recto correspondiente a los valores propios
m = np.diag([4,3,2,1])
print(np.linalg.eig(m))

# det - Calcula el determinante de una matriz.
print(np.linalg.det(m))
    #El determinante es una función que se aplica a una matriz cuadrada y que se utiliza en muchos aspectos de las matemáticas y la física. 
    #Geométricamente, el determinante de una matriz de 2x2 representa el área de un paralelogramo, y el determinante de una matriz de 3x3 representa el volumen de un paralelepípedo con las dimensiones correspondientes a las columnas de la matriz.
    #Matemáticamente, el determinante se utiliza para determinar si una matriz tiene inversa y para calcular esa inversa. Una matriz tiene inversa si y solo si su determinante no es cero.
    
# solve - Resuelve una ecuación con matrices
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
print(x = np.linalg.solve(a, b))
