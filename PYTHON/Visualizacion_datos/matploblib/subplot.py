import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from pathlib import Path

#IMPRIMIMOS TABLA
data_path = Path('C:/Users/javier.puente.ext/Documents/PYTHON/Visualizacion_datos/Datos')
data = pd.read_csv(data_path / 'house.csv')
print(data.head())
print(data['city'].value_counts())

agrup = data.groupby('condition').agg({
    'sqft_living' : 'mean',
    'sqft_lot' : 'mean'
})
print(agrup)


#DOS GRAFICAS DISTINTAS
fig, ax = plt.subplots(figsize = (8,7))

ax.plot(agrup['sqft_living'], label = 'sqft_living')
ax.plot(agrup['sqft_lot'], label = 'sqft_lot')

ax.legend()

#DUPLICAR EJES

import matplotlib.patches as mpatches
fig, ax = plt.subplots(figsize = (8,7))

ax.plot(agrup['sqft_living'], label = 'sqft_living', color = 'blue')

ax1 = ax.twinx()
ax1.plot(agrup['sqft_lot'], label = 'sqft_lot', color = 'orange')
sqft_living = mpatches.Patch(color='blue', label='Variable sqft_living')
sqft_lot = mpatches.Patch(color='orange', label='Variable sqft_lot')
plt.legend(handles=[sqft_living, sqft_lot], title = 'Leyenda')

#MISMO GRAFICO CON 6 DATOS
cities = data.query('city in ("Seattle", "Renton", "Bellevue", "Redmond", "Issaquah")')
agr = cities.groupby(['city', 'condition'])['price'].mean().unstack().T
agr.fillna(0, inplace = True)
print(agr)

cities = ["Seattle", "Renton", "Bellevue", "Redmond", "Issaquah"]

fig, ax = plt.subplots(nrows=3, ncols = 2, figsize = (20,20))

i,j = 0,0

for c in cities:
    ax[i,j].bar(x = agr.index, height = agr[c].values)
    ax[i,j].set_title(c)
    ax[i,j].set_xlabel('Condition')
    ax[i,j].set_ylabel('Precio medio')
    j+=1
    if j == 2:
        i+=1
        j=0

print(plt.show())