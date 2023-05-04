# Importamos las librerías necesarias
import numpy as np
import pandas as pd
from pathlib import Path

# Definimos la ruta del archivo de datos
data_path = Path('C:/Users/javier.puente.ext/Documents/PYTHON/Pandas/Material/Seccion-2-Estructuras_de_datos/data')

# Cargamos los datos desde el archivo .csv en un DataFrame
dataset = pd.read_csv(data_path / 'dataset.csv', sep=',')

# Obtenemos la cantidad de registros por ciudad usando value_counts() y lo guardamos en la variable contador_ciudades
contador_ciudades = dataset['City'].value_counts()

# Creamos una serie booleana que indica True si la ciudad es 'Dallas' y False en caso contrario
dallas = dataset['City'] == 'Dallas'

# Filtramos el DataFrame para obtener únicamente los registros cuya ciudad sea 'Dallas' y lo guardamos en dallas_city
dallas_city = dataset[dataset['City'] == 'Dallas']

# Contamos la cantidad de registros que hay en dallas_city y lo mostramos en pantalla
dallas_city['City'].value_counts()

#CONSULTAS POR POSICION
# Seleccionamos la fila 1 del DataFrame mediante su posición
dataset.loc[1]

# Creamos un nuevo DataFrame llamado dataset1 a partir de dataset, donde el índice empieza en 10 y aumenta en 1 para cada registro
dataset1 = dataset.set_index(np.arange(10, len(dataset)+10))

#Devuelve la posicion (no nombres) 1 del nuevo rango
dataset1.iloc[1]

# Mostramos las primeras filas del DataFrame dataset1
dataset1.head()

# Seleccionamos la ciudad y la edad de la fila con índice 10
dataset1.loc[10, 'City']

# Seleccionamos la ciudad y la edad de la fila con índice 10
dataset1.loc[10, ['City', 'Age']]

# Seleccionamos la ciudad y la edad de todas las filas
dataset1.loc[:, ['City','Age']]

# Seleccionamos la primera fila del DataFrame dataset1 mediante su posición
dataset1.iloc[0]

# Seleccionamos todas las columnas de la fila con índice 10
dataset1.loc[10]

# Seleccionamos el valor de la primera fila y segunda columna del DataFrame mediante su posición. Da fila y columna
dataset.iat[0,1]

# Seleccionamos la ciudad de la primera fila del DataFrame mediante su etiqueta
dataset.loc[0, 'City']

# Seleccionamos la ciudad de la primera fila del DataFrame mediante su etiqueta (con at)
dataset.at[0, 'City']

#CONSULTAS POR FILTROS (SLICING)
# Seleccionamos las filas 1 a 3 del DataFrame
dataset.loc[1:3]

# Seleccionamos todas las filas a partir de la fila 4
dataset.loc[4:]

# Seleccionamos las primeras tres filas del DataFrame
dataset.loc[:3]

# El método sample() recuperar una selección aleatoria de filas o columnas de una serie o DataFrame. 
# tomara muestras de filas de forma predeterminada y acepta un número específico de filas / columnas para devolver, o una fracción de filas.

# Seleccionamos una muestra aleatoria del 10% del dataset y la almacenamos en la variable r
r = dataset.sample(frac=0.1)

# Mostramos el tamaño de la muestra seleccionada. Muestra el numero de filas y de columnas
r.shape

# Seleccionamos las filas del DataFrame que tengan valores de edad iguales a 41 o 42
dataset[dataset['Age'].isin([41,42])]

#Usamos la funcion where para filtrar
# Usamos la función "where" para seleccionar los valores de la columna 'Age' donde se cumple que la edad es igual a 41. Los que no te devuelve un Nan
dataset['Age'].where(dataset['Age'] == 41)

# Usamos la función "where" para seleccionar los valores de la columna 'Age' donde se cumple que la edad es igual a 41, en caso contrario, se reemplaza por el valor -1
dataset['Age'].where(dataset['Age'] == 41, -1)

#Usamos la funcion Query para filtrar datos con expresiones en formato cadena
# Seleccionamos las filas del DataFrame donde la edad es igual a 41 usando la función "query"
dataset.query('Age == 41')

# Seleccionamos las filas del DataFrame donde la ciudad es Dallas y la edad es 41 usando la función "query". Hay que tener cuidado con las comillas, se deben de diferenciar
dataset.query('City == "Dallas" and Age == 41')

# Seleccionamos las filas del DataFrame donde el índice es menor que 4 usando la función "query"
dataset.query('index < 4')

# Seleccionamos las filas del DataFrame donde la edad es 41 o 42 usando la función "query"
dataset.query('Age in (41,42)')

#Usamos valores de variables dentro de la expresion
# Creamos una variable "ciudad_buscada" que contiene el valor "Dallas"
ciudad_buscada = "Dallas"
# Seleccionamos las filas del DataFrame donde la ciudad es igual a la variable "ciudad_buscada" usando la función "query"
dataset.query(f'City == "{ciudad_buscada}"')

# Creamos un filtro para eliminar filas duplicadas basado en la columna 'City' y lo almacenamos en una nueva variable, sin afectar al DataFrame original. 
dataset.drop_duplicates('City', inplace=False, keep='first') #El inplace devuelve una copia pero no modifica el original. 












