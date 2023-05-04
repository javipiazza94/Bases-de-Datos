import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Cargamos los datos
data = sns.load_dataset('mpg')
print(data.head())

#Creamos los graficos
sns.set_theme(style="darkgrid")
g = sns.relplot(x = 'weight', y = 'horsepower', data = data, height=7, hue= 'origin', style='cylinders')
L = sns.relplot(x = 'weight', y = 'horsepower', data = data, height=7, hue= 'origin', kind= 'line')
#En 3D
hp_mean = data.groupby('cylinders')['horsepower'].mean()
sns.relplot(x = 'cylinders', y = 'horsepower', data = data, height=7, kind = 'line', hue = 'origin', ci = 'sd')
#Por fechas
df = pd.DataFrame(dict(time=pd.date_range("2020-01-01", periods=200),
                    value=np.random.randn(200).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df, height = 8)

#Mostramos graficos
plt.show()