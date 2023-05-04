import numpy as np

# shape - Recuperas la dimension
a = np.array([[1,2,3,4], [4,3,2,1]])
print(a)
print(a.shape)
print(a[:,1:]) #imprime las columnas desde la 1 hasta el final
print(a[0:1,:]) #imprime las fila desde la 1, y columnas desde la 1 hasta el final


# reshape - Modificar la dimension
print(a.reshape((4,2)))

# ravel - Aplana un array de más de 1D
print(a.ravel())

# T - Transpone filas y columnas
print(a.T)

#Tipos de arrays
# asarray - Convierte una lista python en numpy array
listaArray = np.asarray([1,2,3,4], dtype = np.int8)
print(listaArray)

# asfarray - Igual, pero devuelve el array de tipo float
listaFloatArray = np.asfarray([1,2,3,4])
print(listaFloatArray)

# repeat - Genera un array de números iguales
b = np.repeat(a = 99, repeats=10).reshape(5,2)
print(b)

# asarray_chkfinite - Convierte la entrada en un array, verificando NaN o Infs.
c = [1,2,3,4, np.nan]
# print(np.asarray_chkfinite(c)) Comprueba si hay un nulo o inf


#union de arrays
# concatenate - Une un conjunto de arrays por filas o columnas
a = np.array([[1,2,3,4], [1,2,3,4]])
b = np.array([[4,3,2,1]])
print(a.shape)
print(b.shape)
concatenar_filas = np.concatenate((a,b), axis = 0)
print(concatenar_filas)
concatenar_col = np.concatenate((a.T,b.T), axis = 1)
print(concatenar_col)

# stack - Parecido a join, pero genera un nuevo indice
a = np.array([1,2,3,4])
b = np.array([4,3,2,1])
stack = np.stack(arrays=(a,b), axis = 1)
print(stack)


#Division de arrays
# split - Divide un array en varios 
a = np.arange(0, 20)
print(a)
print(np.split(a, indices_or_sections=4))
print(np.split(a, [3, 5, 10, 16]))


#Añadir o eliminar elementos
# insert - Inserta elementos en una posicion del array
a = np.array([1,2,3,4])
np.insert(a, obj=4, values=[5,6])
print(a)
np.insert(a, obj=1, values=[5,6])
print(a)

# append - Inserta elementos al final del array
print(np.append(a, [5,6]))

# delete - Elimina un elemento del array
print(np.delete(a, obj = 3))

# unique - Deja los elementos unicos del array
a = np.array([1,1,1,1,2,2,2,2,3,3,3,3])
print(np.unique(a))
