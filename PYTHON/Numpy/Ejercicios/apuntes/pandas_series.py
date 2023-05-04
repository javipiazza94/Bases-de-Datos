import pandas as pd
import numpy as np

#DATOS
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

prinera_serie = pd.Series(data = my_data, index = labels) # Creando una serie con array
print(prinera_serie)

segunda_serie = pd.Series(d) # Creando una serie con un diccionario
print(segunda_serie)

tercera_serie = pd.Series(arr, labels) #creando una serie con un array y una lista
print(tercera_serie)

pd.Series(data = labels)

ser1 = pd.Series([1,2,3,4],['USA', 'GERMANY', 'USSR', 'JAPAN']) #Metemos dos listas en una serie
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','GERMANY', 'ITALY', 'JAPAN']) #creamos una segunda con un ligero cambio
print(ser2)

print(ser1+ser2) #hacemos combinaciones de serie con sus elementos comunes