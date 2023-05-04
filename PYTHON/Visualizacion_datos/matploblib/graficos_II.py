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


#GRAFICO DE LINEAS
fig, ax = plt.subplots(figsize = (10,6))

x = np.arange(5)
y = np.cos(x)

ax.plot(x, y)
ax.set(xlabel = 'Valores X', ylabel = 'Cos(x)', title = 'Cos de valores')


#GRAFICO DE BARRAS
num_by_bathrooms = data.groupby('bedrooms')['price'].count()
fig, ax = plt.subplots(figsize = (20, 6))

ax.bar(x = num_by_bathrooms.index.values, height=num_by_bathrooms.values, width = 0.5, align='center')
ax.axhline(num_by_bathrooms.mean(), color = 'blue', alpha = .5)

ax.set_xticks(num_by_bathrooms.index.values)
ax.set_yscale('log') # linear

ax.set_xlabel('Numero de baños')
ax.set_ylabel('Numero de filas')


#HISTOGRAMA
price = data.query('price > 0 and price < 1_500_000')['price']

fig, ax = plt.subplots(figsize = (15, 7))

ax.hist(price, bins=10, density=True)
ax.set_title('Histograma de precio')


#GRAFICO DE PUNTOS
data['condition'].unique()
fig, ax = plt.subplots(figsize = (15, 7))

x = data['bathrooms']
y = data['sqft_living']

vol = np.sqrt(data['price'])/10

colors = ["", "green", "yellow", "blue", "gray", "red"]

ax.scatter(x = x, y = y, s = vol, c = data['condition'].apply(lambda x: colors[x]))

ax.set_xlabel('Bathrooms', fontsize = 15)
ax.set_ylabel('sqft_living', c = 'blue', fontsize = 15)


#GRAFICO DE TARTAS
cities = data.query('city in ("Seattle", "Renton", "Bellevue", "Redmond", "Issaquah")')
vc = cities['city'].value_counts(normalize = True)
fig, ax = plt.subplots(figsize = (15, 7))

explode = [0.1, 0, 0, 0.2, 0]
ax.pie(vc, labels=vc.index, explode=explode, shadow = True, autopct='%1.1f%%', startangle=0, );

#GRAFICO DE TABLAS
df = data.query('condition in (2,3,4) and bedrooms in (1,2,3)')
_ = df.pivot_table(index = 'condition', columns = 'bedrooms', values = 'price', aggfunc=np.count_nonzero)
price_mean = df.groupby('bedrooms')['price'].mean()
fig, ax = plt.subplots(figsize = (10, 7))

ax.bar(x = price_mean.index, height=price_mean.values)
ax.table(_.values, loc='bottom', rowLabels=_.index.values, colLabels=_.columns.values)

plt.subplots_adjust(left=0, bottom=-.2)
plt.xticks([])

plt.ylabel('Precio medio segun nº baños')
print(plt.show())

#MAPA DE CALOR
fig, ax = plt.subplots(figsize = (8,6))

ax.pcolormesh(np.arange(13), np.arange(13), data.corr().values, cmap = 'Blues')

plt.xticks(np.arange(13), data.columns, rotation = 'vertical');
plt.yticks(np.arange(13), data.columns, rotation = 'horizontal');


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (7,7))
ax = fig.gca(projection='3d')

# Generamos los datos
X = np.arange(-2, 2, 0.25)
Y = np.arange(-2, 2, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

surf = ax.plot_surface(X, Y, Z, cmap='Blues')