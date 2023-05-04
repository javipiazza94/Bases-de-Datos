import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#importamos datos
data = sns.load_dataset('titanic')
print(data.head())

#representacion predeterminada = puntos
sns.catplot(x = 'pclass', y = 'age', data = data, height=7, kind = 'swarm',hue = 'sex')

#representacion por boxplot = Este tipo de gráfico muestra los valores de los tres cuartiles de la distribución junto con los valores extremos. Estos gráficos son muy usados para detectar valores anómalos u outliers
fig, ax = plt.subplots(figsize = (15, 6))
sns.boxplot(x = 'pclass', y = 'age', data = data, hue = 'sex', ax = ax)
sns.catplot(x = 'pclass', y = 'age', data = data, kind = 'box', height = 6)
sns.boxplot(x = 'age', y = 'pclass', data = data, hue = 'sex', ax = ax, orient='h')
sns.catplot(x = 'pclass', y = 'age', data = data, hue = 'sex', kind = 'violin', height=8)

#representacion por Bar Plots = Un gráfico muy tipico a la hora de representar variables categóricas es el barplot o0 catplot
sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = data, kind = 'bar', estimator=np.count_nonzero)

#mostramos graficos
plt.show()