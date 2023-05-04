import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

data = sns.load_dataset('titanic')
#data['sex'] = data['sex'].replace({'male': 0, 'female': 1})

print(data.head())

#mostramos graficos
#Temas 
sns.set_style('whitegrid') #Los estilos posibles son: darkgrid, whitegrid, dark, white y ticks
sns.boxplot(x = 'pclass', y = 'age', data = data)
sns.set_theme() #volver al tema original

#Contexto =  posibles valores son: paper, notebook, talk y poster
sns.set_context('notebook', font_scale=1.4, rc={"lines.linewidth": 3.5})
sns.boxplot(x = 'pclass', y = 'age', data = data)

#Paleta de colores = Seaborn nos permite seleccionar entre una amplia gama de colores. Podemos elegir entre distintas paletas de colores.sns.boxplot(x = 'pclass', y = 'age', data = data)
sns.boxplot(x = 'pclass', y = 'age', data = data, palette=sns.color_palette("husl", 8))
# Paired
sns.boxplot(x = 'pclass', y = 'age', data = data, palette=sns.color_palette("Set2", 8))
# CMAP
#sns.heatmap(data.corr(), cmap=sns.color_palette('Accent', as_cmap=True))
#sns.heatmap(data.corr(), cmap=sns.color_palette('Blues', as_cmap=True))

#mostramos graficos
plt.show()

