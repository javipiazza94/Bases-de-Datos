import pandas as pd
import numpy as np
import datetime

# Los Timedeltas son diferencias de tiempo, expresadas en unidades como días, horas, minutos, segundos. 
# Pueden ser tanto positivos como negativos. Timedelta es una subclase de datetime.timedelta y se comporta de manera similar, pero permite la compatibilidad con los tipos np.timedelta64, así como una gran cantidad de atributos, análisis y representación personalizados.

# Definimos un Timedelta de 10 días.
td = pd.Timedelta('10 days')

# Definimos otro Timedelta de 10 días, especificando la unidad de medida.
td = pd.Timedelta(10, unit='d')

# Definimos un Timedelta con una duración de 10 días, 2 horas y 20 minutos.
td = pd.Timedelta('10 days 2 hours 20 minutes')

# Creamos un rango de fechas desde el 1 de enero de 2020 hasta el 10 de marzo de 2020, con una frecuencia semanal.
dt_int = pd.date_range(start='2020-01-01', end='2020-03-10', freq='W')

# Sumamos el Timedelta 'td' al rango de fechas 'dt_int'.
dt_int + td

# Creamos otro rango de fechas desde el 10 de enero de 2020 hasta el 19 de enero de 2020, con una frecuencia diaria.
dt_int2 = pd.date_range(start='2020-01-10', end='2020-01-19', freq='D')

# Calculamos la diferencia entre los dos rangos de fechas, para obtener un array de Timedeltas.
diff = dt_int - dt_int2

# Consultamos el valor mínimo de los Timedeltas en 'diff'.
diff.min()

# Consultamos la mediana de los Timedeltas en 'diff'.
diff.median()

# Consultamos el valor máximo de los Timedeltas en 'diff'.
diff.max()

# Creamos una Serie de Pandas con un índice de Timedeltas, utilizando el array de Timedeltas 'diff' como índice.
s = pd.Series(np.arange(10), index = diff)

# Consultamos el valor de la Serie 's' para el Timedelta de 7 días.
s['7 days']

# Consultamos el valor de la Serie 's' para el Timedelta de 7 días y el de 25 dias.
s['7 days':'25 days']
