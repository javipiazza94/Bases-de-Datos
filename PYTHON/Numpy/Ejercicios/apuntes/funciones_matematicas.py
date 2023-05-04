import numpy as np

# round - Redonde un número a las cifras que definamos
a = 2.49264
print(np.round(a, 1))
array = np.array([1.435, 13.1435, 4.916])
print(np.round(array, 2))

# floor - Devuelve el suelo - el número entero pequeño más cercano
print(np.floor(array))

# Devuelve el techo - el siguiente número entero
print(np.ceil(array))


#SUMAS Y PRODUCTOS
# prod - Devuelve el producto de los elementos de la matriz sobre un eje dado
b = np.array([2,3,4])
print(np.prod(b))
b = np.array([[2,3,4],[2,2,2]])
print(np.prod(b, axis = 0))
print(np.prod(b, axis = 1))

# sum - Mismo funcionamiento que prod, pero en este caso realizando la suma
print(np.sum(b))
print(np.sum(b, axis = 0))
print(np.sum(b, axis = 1))


#EXPONENTES Y LOGARITMOS
#exp - Calcula el exponencial de todos los elementos en la matriz de entrada.
print(np.exp(b))
print(np.power(np.e, b)) #elevar el numero e
p = np.power(np.e, b)
print(np.log(p))
print(np.log10(b))
print(np.power(10, np.log10(b)))
print(np.log2(b))
print(np.power(2, np.log2(b)))

#OPERACIONES ARITMETICAS
a = np.array([[1,2,3,4], [4,3,2,1]])
b = np.array([4,3,2,1])

# Suma
print(np.add(a,b))
print(a+a)
# Resta
print(np.subtract(a,b))
print(a-7)
# Multiplicacion
print(np.multiply(a,b))
print(b*3)
# Division
print(np.divide(a,b))
print(b/2)