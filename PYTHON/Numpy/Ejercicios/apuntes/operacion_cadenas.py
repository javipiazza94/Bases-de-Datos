import numpy as np

# add - Devuelve la concatenación de cadenas de elementos para dos matrices de str o unicode.
a = np.array(['A', 'B', 'C'], dtype = str)
b = np.array(['D', 'E', 'F'], dtype = str)
print(np.char.add(a,b))

# multiply - Devuelve (a * i), es decir, concatenación múltiple de cadenas, por elementos.
print(np.char.multiply(a, [2,3,4]))

# capitalize - Devuelve una copia de a con solo el primer carácter de cada elemento en mayúscula.
nombres = np.array(['maria', 'antonio', 'francisco'], dtype = str)
print(np.char.capitalize(nombres))

# replace - Devuelve un array después de reemplazar los caracteres
print(np.char.replace(nombres, 'mar', 'sof'))

# split - Para cada elemento de a, devuelve una lista de las palabras de la cadena, utilizando sep como cadena delimitadora.
nombre = np.array(['Mi nombre es Abraham Requena'])
print(np.char.split(nombre, sep=' '))

#Strip - elimina espacios entre cadenas
c = np.array(['  Hola  ', '  Adios '])
print(np.char.strip(c))

#COMPARACION
# equal - Valores iguales
a = np.array(['A', 'B', 'C'], dtype = str)
b = np.array(['D', 'B', 'F'], dtype = str)
print(np.char.equal(a,b))
print(np.char.not_equal(a,b))

# greater_equal . Compara el mayor o igual a nivel cadena. A < B, o F > C
print(np.char.greater_equal(a,b))

# less_equal
print(np.char.less_equal(a,b))

#iNFO CADENA
# endswith - Devuelve True si la palabra acaba en el char que definimos
c = np.array(['Hola', 'Adios'])
print(np.char.endswith(c, suffix='ios'))

# startswith - Devuelve True si la palabra comienza en el char que definimos
print(np.char.startswith(c, prefix='Ad'))

# islower - Devuelve True si todos los caracteres están en minusculas
c = np.array(['HOLA', 'adios'])
print(np.char.islower(c))

# isupper - Devuelve True si todos los caracteres están en mayusculas
c = np.array(['HOLA', 'adios'])
print(np.char.isupper(c))

# isdigit - Devuelve True si todos los elementos son numericos
c = np.array(['HOLA', 'adios', '123'])
print(np.char.isdigit(c))