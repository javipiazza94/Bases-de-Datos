import pandas as pd
import numpy as np
from pathlib import Path

#Ejercicio 1:
#Lee los datos del fichero 'house.csv' en un dataframe.   
data = pd.read_csv('C:/Users/javier.puente.ext/Documents/PYTHON/Pandas/Material/Seccion-2-Estructuras_de_datos/Leccion 8 - Ejercicios/house.csv')
data2 = pd.read_csv('C:/Users/javier.puente.ext/Documents/PYTHON/Pandas/Material/Seccion-2-Estructuras_de_datos/Leccion 8 - Ejercicios/house.csv')

    #¿Hay alguna habitación con 8 habitaciones?
habitaciones = data['bedrooms']
8 in habitaciones
data.query('bedrooms == 8').shape
habitaciones.value_counts()
    #¿Cual es el número mínimo y máximo de habitaciones en el DF?
minimo = habitaciones.min()
maximo = habitaciones.max()
    #Crea una nueva columna que sea la relación de precio por planta.
data['precio_planta'] = data['price']/data['floors']


#Ejercicio 2
    #El precio de la casa que se encuentra en la fila número 256
data.loc[256, 'price']
    #El número de habitaciones de las filas 215 a 222
data.loc[215:222, 'bedrooms']
    #Recupera una selección aleatoria del 15% del DF
r = data.sample(frac=0.15)
    #De ese 15% aleatorio, filtra aquellos registros con 3 o 4 habitaciones y precio menor a 300_000 euros
consulta = r.query('bedrooms in (3,4) and price <300000')


#Ejercicio 3
    #Genera un índice multiple con las columnas "street", "city", "statezip" y "country" bajo el nombre "localizacion", y el resto de columnas bajo el nombre "caracteristicas". 
col_indexada = [['caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas',
    'caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas','caracteristicas',
    'caracteristicas','caracteristicas', 'localizacion', 'localizacion', 'localizacion', 'localizacion', 
    'caracteristicas'],
    ['date', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
    'floors', 'waterfront', 'view', 'condition', 'sqft_above',
    'sqft_basement', 'yr_built', 'yr_renovated', 'street', 'city',
    'statezip', 'country', 'precio_planta']]
tuplas = list(zip(*col_indexada))
multiindex = pd.MultiIndex.from_tuples(tuplas)
data.columns = multiindex
    #Ordena dichas columnas y genera un nuevo DF que contenga solo las columnas de "localizacion".
data['localizacion'].head()


#Ejercicio 4
    # Convierte la columna 'date' en un tipo fecha.
data2['date'] = pd.to_datetime(data2['date'], yearfirst=True)
    # Genera 3 nuevas columnas fruto de extraer el año, mes y día.
data2['año'] = data2['date'].dt.year
data2['mes'] = data2['date'].dt.month
data2['dia'] = data2['date'].dt.day
# Encuentra el precio medio por mes.
precio_medio_por_mes = data2.groupby(data2['date'].dt.month)['price'].mean()
print(precio_medio_por_mes)
    # una nueva columna fruto de sumar 20 días a la columna fecha.
td = pd.Timedelta('20 days')
data2['fecha_extra'] = pd.to_datetime(data2['date']+td)
print(data2.head())

