import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Cargamos los datos
data = sns.load_dataset('titanic')
print(data.head())
print(data.columns)

# Representamos histogramas
fig, ax = plt.subplots(figsize = (10, 5))
sns.distplot(a = data['age'], bins = 10, hist = True, kde = False, norm_hist=True, ax = ax)

# Histograma por categorías
print(data['pclass'].value_counts())
fig, ax = plt.subplots(figsize = (10, 5))
sns.distplot(a = data['pclass'], bins = 3, hist = True, kde = False, norm_hist=False, ax = ax)

# Usando distintos elementos
sns.displot(data, x="age", hue = 'sex', height=7, element = 'step')
sns.displot(data, x="age", hue = 'sex', height=7, multiple = "stack")
sns.displot(data, x="age", hue = 'sex', height=7, multiple = "dodge")

# Distintos graficos
sns.displot(data, x="age", col = 'sex', height=7, stat = 'density')

# Kernel gaussiano
fig, ax = plt.subplots(figsize = (10, 5))
sns.distplot(a = data['age'], bins = 10, hist = False, kde = True, ax = ax)
sns.displot(data, x="age", height=7, kind = 'kde', bw_adjust = .25) #tamaño de banda ajustado
sns.displot(data, x="age", height=7, kind = 'kde', hue = 'sex', bw_adjust = .25) #varias variables en el mismo resultado

# Distribucion acumulativa empirica
sns.displot(data, x="age", kind='ecdf')
sns.displot(data, x="age", kind='ecdf', hue = 'sex') #por sexo

# Mostramos graficos
plt.show()
