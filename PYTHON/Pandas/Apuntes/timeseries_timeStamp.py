import pandas as pd
import numpy as np
import datetime

#El tipo de datos "Timestamp" es el tipo más básico asociado a series de tiempo. Su constructor nos permite varios inputs.
ts = pd.Timestamp(2020, 1, 1)

ts = pd.Timestamp('2020-01-01')

#Podemos crear una serie de tiempo, añadiendo varios Timestamps
dt = pd.to_datetime(['01/01/2020', np.datetime64('2020-01-02'), datetime.datetime(2020, 1, 3)])

#intervalos de tiempo
#El parámetro freq puede tener valores:
    #D: Dias
    #M: Meses
    #Y: Años
    #W: Semanas
    #H: Horas
dt_int = pd.date_range('2020-01-01', periods=5, freq='D')

#Podemos usar estas series de tiempo como indices de las series o dataframes
s = pd.Series(np.arange(10), index = dt_int)

#Y podemos hacer operaciones agrupando cada X dias.
s.resample('2D').mean()
s.resample('1M').mean()

#Para convertir otros tipos de datos a 'timestamp', podemos usar el método to_datetime
pd.to_datetime(pd.Series(['Aug 01, 2020', '2020-01-02']))

#¿Qué ocurre cuando hay una fecha "ambigua"? Por ejemplo, el "04/08/2020". ¿Nos referimos al 4 de Agosto o al 8 de Abril? Para ello tenemos el parámetro day_first
_ = pd.to_datetime('04/08/2020')
_ = pd.to_datetime('04/08/2020', dayfirst=True)
_ = pd.to_datetime('04/08/2020', format='%d/%m/%Y')
_ = pd.to_datetime('04/08/2020', format='%m/%d/%Y')

#Dara Not a Time
pd.to_datetime('30/02/2020', format='%d/%m/%Y', errors = 'coerce')

#EPOCH
#Las fechas 'epoch' representan el número de segundos que han transcurrido desde el 1 de enero de 1970. Podemos convertir ese valor en una fecha pandas.
pd.to_datetime([1349720105, 1349806505, 1349892905, 1349979305, 1350065705], unit='s')

#Hasta ahora hemos visto como generar rangos de fechas con date_range, pero podemos generar dichos rangos aplicando unas máscaras si usamos bdate_range.
week_mask = 'Mon Tue Wed'
_ = pd.bdate_range('2020-01-01', '2020-01-30', freq='C', weekmask=week_mask)
pd.to_datetime('2020-01-01').day_name()

#Componentes de los timestamp
# isocalendar: Separa cada componente de la fecha
dr = pd.bdate_range('2020-01-01', '2020-01-30', freq='C', weekmask=week_mask)
ywd = dr.isocalendar()
dr.year
dr.month
dr.hour
dr.day
dr.dayofyear
dr.weekday
dr.day_name()






