import numpy as np

# Eye - Devuelve una matriz 2-D con unos en la diagonal y ceros en el resto. Son cuadradas
matriz_diagonal =np.eye(4)
print(matriz_diagonal)

#desplazar la diagonal con parametro k
k = np.eye(4, k=1)
print(k)

# identity - Devuelve un array identidad
array_id = np.identity(4, dtype = 'int8')
print(array_id)

# ones - Devuelve un array de unos. Podemos definir su dimension
array_uno = np.ones(shape=(2,3))
print(array_uno)

# zeros - Devuelve un array de zeros. Podemos definir su dimension
array_zero = np.zeros(shape=(2,3))
print(array_zero)

# full - Devuelve una nueva matriz de forma y tipo dados, rellena con fill_value.
array_cifra = np.full(shape=(4,4), fill_value=99)
print(array_cifra)
array_relleno_lista= np.full(shape=(4,4), fill_value=[10,20,30,40])
print(array_relleno_lista)

#Random --> Crea valores aleatorios
aleatorio = np.random.rand(2,3)
print(aleatorio)
aleatorio_distribucion_normal = np.random.randn(3)
print(aleatorio_distribucion_normal)
aleatorio_enteros = np.random.randint(low=1, high=100, size=25)
print(aleatorio_enteros)

#Creacion desde datos existentes
# fromstring - Una nueva matriz 1-D inicializada a partir de datos de texto en una cadena.
array_cadenas = np.fromstring('1 2 3 4' , sep = ' ')
print(array_cadenas)

datos = np.loadtxt(r'C:\Users\javier.puente.ext\Documents\PYTHON\Numpy\Material\Seccion 3 - Operaciones con Numpy\Leccion 1 - Rutinas de creación de arrays\datos.txt', delimiter=' ')
print(datos)

#rangos numericos
# arange - Devuelve un array de los valores existentes en un invervalo definido. Podemos 
# configurar el tamaño del paso
array_rangos = np.arange(1, 10, 2)
print(array_rangos)

# linspace - Devuelve un número de valores entre un intervalo
linspace = np.linspace(start=1, stop=10, num = 5, endpoint=False, retstep=True)
print(linspace)
linspace2 = np.linspace(start=2, stop= 3.5, num = 10)
print(linspace2)

# logspace - Igual, pero aplicando una escala logaritmica
logspace = np.logspace(start=2, stop= 3.5, num = 10)
print(logspace)

#matrices
# diag - Extrae la diagonal de una matriz o array de dos dimensiones
a = np.eye(N = 4)
a = np.diag(a, k = 1)
print(a)

# diagflat - Crea una matriz bidimensional con la entrada usada como diagonal.
diagflat =np.diagflat(v = [1,2,3,4], k = 0)
print(diagflat)

# tri - Una matriz con unos en la diagonal y debajo de ella, y ceros en cualquier otro lugar.
tri = np.tri(N = 5, M = 5)
print(tri)

# asmatrix - Crea un tipo matrix a partir de un array
b = np.array([[1,2,3,4], [4,3,2,1]])
print(np.asmatrix(b))
