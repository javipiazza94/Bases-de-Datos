import numpy as np
import pandas as pd
from pathlib import Path

# Creamos un objeto de la clase Path para acceder a nuestro archivo de datos
data_path = Path('C:/Users/javier.puente.ext/Documents/PYTHON/Pandas/Material/Seccion-2-Estructuras_de_datos/data')

# Leemos nuestro archivo CSV usando pandas y el objeto Path creado anteriormente
dataset = pd.read_csv(data_path / 'dataset.csv', sep = ',')

# Creamos una serie de pandas con valores del 0 al 11 y mostramos sus índices
s = pd.Series(np.arange(12))
s.index.values

# Creamos un array con una lista de listas
array = [['a','a','a','a','b','b','b','b','c','c','c','c'],
        ['a','b','c','d','a','b','c','d','a','b','c','d']]

# Usamos la función zip para crear una lista de tuplas y la usamos para crear un MultiIndex
t = list(zip(array[0],array[1]))
mi = pd.MultiIndex.from_tuples(t, names=['primero','segundo'])

# Creamos una nueva serie de pandas usando el MultiIndex creado anteriormente
s = pd.Series(np.arange(12), index = mi)

# Accedemos a un valor específico del MultiIndex
s.loc[('a','b')]

# Accedemos a todos los valores de un nivel del MultiIndex
s.loc['a']
s.loc[:,'a']

# Creamos una lista de tuplas para usarla como MultiIndex para nuestras columnas del DataFrame
tuples = [('Columnas_no_importantes', 'Number'),
        ('Columnas_importantes', 'City'),
        ('Columnas_no_importantes', 'Gender'),
        ('Columnas_importantes', 'Age'),
        ('Columnas_importantes', 'Income'),
        ('Columnas_no_importantes', 'Illness')
        ]

# Creamos un nuevo MultiIndex con la lista de tuplas creada anteriormente y se lo asignamos a las columnas del DataFrame
multiindex = pd.MultiIndex.from_tuples(tuples)
dataset.columns = multiindex

# Accedemos a las columnas importantes del DataFrame
dataset['Columnas_importantes'].head()

# Mostramos los niveles de nuestro MultiIndex de las columnas
dataset.columns.levels

# Mostramos los valores del nivel 1 del MultiIndex de las columnas
multiindex.get_level_values(1)

# Accedemos a todas las filas y sólo a las columnas 'City' y 'Age' del DataFrame usando MultiIndex
dataset.loc[:,('Columnas_importantes','City')]
dataset.loc[:,[('Columnas_importantes','City'),('Columnas_importantes','Age')]]

# Creamos un objeto transpuesto de nuestro DataFrame y mostramos los índices
_ = dataset.head(5).T
_.index

# Ordenamos el DataFrame por el nivel 0 de nuestro MultiIndex de las columnas
dataset.sort_index(level=0, axis = 1).head()

# Ordenamos el DataFrame por el nivel 1 de nuestro MultiIndex de las columnas
dataset.sort_index(level=1, axis = 1).head()
