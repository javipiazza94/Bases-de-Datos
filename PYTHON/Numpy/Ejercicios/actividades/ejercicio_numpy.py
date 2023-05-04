
import numpy as np


#Crea un array con 10 ceros
a = np.zeros(10)
#print(a)

#Crea un array con 10 unos
b = np.ones(10)
#print(b)

#Crea un array de 10 cincos
c = np.full(10, fill_value=5)
#print(c)

#Crea un array de enteros que empiece en 10 y acabe en 50
d = np.random.randint(low=10, high=50, size=20)
#print(d)

#Crea un array de enteros pares que empiece en 10 y acabe en 50
par = np.arange(10, 51, 2)
#print(par)

#Crea una matriz 3x3 con los valores desde el 0 hasta el 8
matriz = np.arange(0,9).reshape(3,3)
#print(matriz)

#Crea la matriz identidad 2x2
identidad =np.identity(2, dtype = 'int8')
#print(identidad)

#Genera un número aleatorio utilizando Numpy
num_aleatorio = np.random.randint(647438)
#print(num_aleatorio)

#Genera un array de 25 números aleatorios que sigan una distribución normal estandar
aleatorio_normal = np.random.randn(25)
#print(aleatorio_normal)

#Crea la siguiente matriz:
m = np.arange(1,101).reshape(10,10)/100
#print(m)

#Crea un array de 20 elementos entre 0 y 1
linspace = np.linspace(start=0, stop=1, num = 20)
#rint(linspace)

#Indexa
mat = np.arange(1,26).reshape(5,5)
#print(mat)

#Obten la siguientes matrices con la matriz mat
mat[3,4]
mat[0:3,1:2]
mat[4,:]
mat[3:,:]

#Obtén la suma de todos los valores de mat
print(mat.sum())

#Obtén todos la desviación típica de los valores
print(mat.std())
