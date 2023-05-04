import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#GRAFICO DE PUNTOS
# Crear la figura y los ejes
#fig, ax = plt.subplots()
# Dibujar puntos
#ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
# Guardar el gráfico en formato png
#plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
#print(plt.show())

#GRAFICO DE LINEAS
x = np.arange(5)
y = np.array([2.0, 2.5, 1.5, 3.0, 4.5])
#plt.plot(x, y)
#plt.plot(x, y, 'o')
#plt.plot(x, y, 'xr')

#pintar varios gráficos en el mismo plot.
import matplotlib.style as mplstyle

mplstyle.use('ggplot') # dark_background, fast
z = y + 1
w = np.log(y)
plt.plot(x, y, '*', label = 'y')
plt.plot(x, z, 'g-', label = 'z')
plt.plot(x, w, '--', label = 'w')
plt.legend()
plt.title('Mi primer gráfico')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()




