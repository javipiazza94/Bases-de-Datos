import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

#cargamos datos
data = sns.load_dataset('tips')
data.head()

#grafico de regresion
fig,ax = plt.subplots(figsize = (10, 5))
sns.regplot(x = 'tip', y = 'total_bill', data = data, ax=ax, ci = True, line_kws={'color':'red'}, color = 'green')
    #tips
        #ci: Intervalo de confianza
        #line_kws: Diccionario para personalización de la linea
    #inplot
sns.lmplot(x = 'tip', y= 'total_bill', data = data, height = 6)
    #separamos por variables
sns.lmplot(x = 'tip', y= 'total_bill', data = data, height = 6, hue = 'smoker')

#joinplot = Por último, vamos a conocer el jointplot. Este gráfico combina la regresión con la distribución.
sns.jointplot(x='tip', y='total_bill', data=data, kind = 'reg')

# Mostramos graficos
plt.show()

