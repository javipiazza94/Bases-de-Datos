import numpy as np
from sys import getsizeof

#Tipos mas comunes
#entero
a = np.array([1,2,3,4], dtype=np.int8)
print("A", getsizeof(a)) #averiguamos tamaño
b = a.dtype is np.int16 #averiguamos si es int16
print(b)

#booleano
bool_array = np.array([[1,0,0,1], [0,1,1,0]], dtype = bool)
print(bool_array)
print(bool_array.dtype)#averiguamos tipo

#char
char_array = np.array(['a','b','c'], dtype = np.chararray)
print(char_array)

#nam
variable_nulo = np.nan
comnprobacion_nulo = np.isnan(variable_nulo)
print(comnprobacion_nulo)

#matrix
matrix = np.matrix('1 2 3 ; 4 5 6', dtype=np.float32)
print(matrix)