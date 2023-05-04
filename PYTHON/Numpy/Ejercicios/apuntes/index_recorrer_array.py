import numpy as np

#consulta mediante corchetes a una posicion
a = np.array([0,1,2,3,4,5,6,7,8,9])
print(a[0])
print(a[9])
print(a.shape) #numero de elementos
#print(a[10]) #da error

#consulta mediante SLICING en varias posiciones
print(a[0:9:2])
print(a[0:8:3])
print(a[-2:10]) #ultimos 2 elementos
print(a[9::-1]) #Decreciente
print(a[:5]) #todos los numeros hasta el 5
print(a[5:]) #del 5 hacia delante
a[1:5] = 69
print(a)
b = a[6:10].copy()
print(b)

#consulta en array multidimensionales
b = np.array([[1,2,3], [3,4,5]], dtype = np.int8)
print(b[0][1])
print(b[0, 0:2])
print(b[0:2, 0:2])

#consulta en tipo nam
x = np.array([[4, 3], [np.nan, 2.], [np.nan, np.nan]])
print(x[np.isnan(x)])
print(x[~np.isnan(x)])

#indexado booleano
c = np.array([0,1,2,3,4,5,6,7,8,9])
print(c>5)
print(c[c>4])
print(c[c%2==0])

char_array = np.array(['Openwebinars', 'Machine Learning', 'Numpy'])
print(char_array[char_array == 'Numpy'])

#Recorrido con for
d = np.array([0,1,2,3,4,5,6,7,8,9])

for valor in d:
    print(valor)
    
print()
    
for valor in np.nditer(d):
    print(valor)