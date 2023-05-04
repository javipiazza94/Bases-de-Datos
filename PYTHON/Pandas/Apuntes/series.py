import numpy as np
import pandas as pd

#Se guia por series, que son matrices unidimensionales

valores = np.array([1,2,3,4,5,6])
serie = pd.Series(valores)
print(serie) #imprimimos serie
print(serie.dtype)#imprimimos tipo
print(serie.index) #imprimimos indice

serie2 = pd.Series(valores, index=['a','b','c','d','e','f'])
print(serie2) #creamos serie con otro indice

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
serie3 = pd.Series(d) #creamos serie a partir de un diccionario
print(serie3)

#Integracion con Numpy
#Funciones numpy
np.sum(serie)
np.max(serie)
serie*2
serie2+serie3

#Conversiones
serie4 = pd.Series(np.random.randint(0,10,6), index = ['b', 'c', 'a', 'e', 'd', 'f'])
print(serie4)
array = serie.to_numpy()
print(array)
type(array)

#consulta de datos
#serie['b']
serie['z'] = 56
print(serie)
serie[0]
'e' in serie
serie.keys()
serie.values
