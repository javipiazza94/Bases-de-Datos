import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

data = sns.load_dataset('titanic')
data.head()

#FacetGrid = La clase FacetGrid es útil cuando desea visualizar la distribución de una variable o la relación entre múltiples variables por separado dentro de subconjuntos de su conjunto de dato
g = sns.FacetGrid(data = data, col = 'pclass', hue = 'sex') #columnas por clase y divididas por sexo
g.map(sns.scatterplot, 'age', 'fare') #dibuja la grafica en ambos ejes, x e y
g.add_legend()

#PairGrid
g = sns.PairGrid(data = data, vars = ['pclass', 'age', 'fare'], hue = 'sex')
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot)
g.map_upper(sns.kdeplot)

#mostramos graficos
plt.show()