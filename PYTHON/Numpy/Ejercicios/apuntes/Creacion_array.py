import numpy as np

#tipo de array
array1 = np.array([1,2,3,4,5,6], dtype = 'int')
print(type(array1))

#tipo de dimensiones
array2 = np.array([[1,2,3],[4,5,6]], dtype = 'int', ndmin=2 )
print(array2)

#array complejo
array3 = np.array([1,2,3], dtype = 'complex')
print(array3)

#Funciones de array
#np.zeros --> array de ceros
array_ceros = np.zeros(15)
print(array_ceros)

#np.arange --> aporta un rango
array_arange = np.arange(15)
print(array_arange)
array_arange_par = np.arange(0,12,2)
print(array_arange_par)
array_arange.reshape((5,3))
print(array_arange)

#np.ones --> array de unos
array_ones = np.ones(15)
array_one_multi = np.ones((6,3))
print(array_ones)
print(array_one_multi)

#shape --> da el tamaño del array
array = np.arange(1, 200, 3)
print(array)
print(array.shape)

