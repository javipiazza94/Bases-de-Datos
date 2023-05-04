import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)#Creamos una semilla para los mismos numeros aleatorios
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) #creamos un dataframe
print(df)
print(df['W'])
print(type(df))
print(df[['W','X']]) #imprimimos 2 columnas

df['new'] = df['W'] + df['Y'] #creamos columna nueva
#print(df)

df.drop('new', axis = 1, inplace=True) # borramos con axis = 1 para las columnas
print(df)

df.drop('E', axis = 0, inplace=True) #borramos fila
print(df)

# Truco para recordar
# Posiciones 0 y 1
# axis = 0 (filas) y axis = 1 (columnas)

print(df.shape)
## ¿como podemos seleccionar filas?
# 2 maneras
# seleccionar por el index

print(df.loc['A'])
# 2 maneras
# indice numérico

df.iloc[0]
# seleccionar la posición de una fila x columa

print(df.loc['B','Y'])

df.loc[['A','B'],['W','Y']]

df > 0 
df[df>0]
bool_df = df > 0
## filtros en función de una columna

df[df['W']>0]

# utilizando varios pasos
# Quiero todos las filas en las que la columna W sea positiva y obtener los valores de la columna X
# Imaginemos que queremos las variaciones positivas de la empresa W y obtener esos mismos valores para la empresa X

resultdf = df[df['W']>0]

# Un paso
df[df['W']>0]['X']

# multiple conditions
df[ (df['W']>0) & (df['Y']<1) ]

# multiple conditions
df[ (df['W']>0) | (df['Y']<0) ]