import numpy as np
import pandas as pd

#LECTURA
#Leemos un archivo csv
from pathlib import Path
data_path = Path('C:/Users/javier.puente.ext/Documents/PYTHON/Pandas/Material/Seccion-2-Estructuras_de_datos/data')
dataset = pd.read_csv(data_path / 'dataset.csv', sep = ',')

#filtramos 
filtro = dataset.head() #5 primeras opciones
filtro2 = pd.read_csv(data_path / 'dataset.csv', sep = ',', usecols=['Gender','Age']).head() #por edad y sexo

#leemos un JSON
dataset.head(100).to_json(data_path / 'dataset_records.json', orient='records')
ds = pd.read_json(data_path / 'dataset_index.json', orient='index') #convertimos en dataset
ds.head()

#read fwf
widths = [1, 6, 4, 2, 7, 2]
ds_fijo = pd.read_fwf(data_path / 'dataset_fijo', widths=widths, header = None)
ds_fijo.columns = ['Number', 'City', 'Gender', 'Age', 'Income', 'Illness']

#read parquet
ds_parquet = pd.read_parquet(data_path / 'dataset.parquet', engine='pyarrow')
parquet = ds_parquet.head() #ocupa menos megas que csv
print(parquet)

#ESCRITURA

df_to_write = dataset.head(100)
#to_cs
df_to_write.to_csv(data_path / 'df_to_write.csv', index = False, sep = '#', header = False)
#to_json
df_to_write.to_json(data_path / 'df_to_write.json', orient = 'split')
#to_parquet
df_to_write.to_parquet(data_path / 'df_to_write.parquet', engine = 'pyarrow')


