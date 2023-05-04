import pandas as pd

# Crear dataframe
df = pd.DataFrame({'a': [0, 4, 8, 12],
                'b': [1, 5, 9, 13],
                'c': [2, 6, 10, 14],
                'd': [3, 7, 11, 15]})

# Especificar ruta completa del archivo
ruta_archivo = r'C:\Users\javier.puente.ext\Documents\PYTHON\Numpy\Ejercicios\apuntes\my_dataframe.csv'

# Exportar dataframe a CSV en la ruta especificada
#df.to_csv(ruta_archivo, index=False)

#Leemos el archivo
lectura = pd.read_csv('C:/Users/javier.puente.ext/Documents/PYTHON/Numpy/Ejercicios/apuntes/my_dataframe.csv')
#print(lectura)

#Añadimos una columna
df ['e'] = df ['a'] + df ['b']
print(df)

#Leemos un Excel
excel= pd.read_excel('C:/Users/javier.puente.ext/Documents/PYTHON/Numpy/Ejercicios/apuntes/Artículos.xlsx')
print(excel)

#leemos un HTML
#data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.html')
#print(data)
#data[5].head()
#data.info()

#leemos una base de datos
# SQL
from sqlalchemy import create_engine
# mini bbdd
engine = create_engine('sqlite:///:memory:')#creamos instancia en memoria
df.to_sql('my_table', engine)#pasamos el dataframe a bbdd, lo almacenamos en la instancia y le nombramos
sqldf = pd.read_sql('my_table',  con = engine) #lo leemos
print(sqldf)

