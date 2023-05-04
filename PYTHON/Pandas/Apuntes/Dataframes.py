import numpy as np
import pandas as pd

#Son datos bidimensionales, con filas y columnas (tablas)
#Usando un diccionario de series
d = {'col1': pd.Series([1., 2., 3., 4.]),
    'col2': pd.Series([4., 3., 2., 1.])}
df = pd.DataFrame(d)

#Usando un diccionario de valores
d2 = {'col1': [1., 2., 3., 4.],
    'col2': [4., 3., 2., 1.]}
df2 = pd.DataFrame(d2, index = ['a','b','c','e'])

#Usando una lista de diccionarios
l = [{'col1': 1, 'col2' : 4}, {'col1': 2, 'col2' : 3},  
    {'col1': 3, 'col2' : 2}, {'col1': 4, 'col2' : 1, 'col3' : 3}]
df3 = pd.DataFrame(l, index = ['a','b','c','e'])

# Recupero la columna con [] y creamos una nueva
df3['col2']
type(df3['col2'])
df3['col4'] = df3['col1'] + df3['col2']

# Elimino columnas con del
del df3['col3']

#insertamos una nueva columna
df3.insert(0, 'col0', df3['col4'] + df3['col2'])
print(df3)

#metodo assign para crear nueva columna en el dataframe
df = df.assign(col3 = 3)
print(df)
