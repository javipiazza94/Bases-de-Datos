import numpy as np

# Orden: año - mes - dia
d = np.datetime64('2020-09-01')
print(d)

# Orden: año - mes - dia - hora
dh = np.datetime64('2020-09-01T14:30')
print(dh)

#array de fechas
fechas = np.array(['2020-07-01', '2020-08-01', '2020-09-01'], dtype='datetime64')
rango_fechas = np.arange('2020-08', '2020-09', dtype='datetime64[D]')
print(fechas)
print(rango_fechas)

#comparaciones
dcom= np.datetime64('2020') == np.datetime64('2020-01-01')

#operaciones
a = np.timedelta64(10, 'h')
b = np.timedelta64(8, 'D')
print(np.timedelta64(b, 'W'))
c = np.datetime64('2020-08-01') + np.timedelta64(10, 'D')
print(c)
d = np.datetime64('2020-08-01') - np.timedelta64(1, 'W')
print(d)
print(a+b)

#Dias laborables
# 2020-09-03 --> Jueves
festivo = np.busday_offset('2020-12-25', 0)
print(festivo)
# Sabado
print(np.is_busday(np.datetime64('2020-09-05')))
rango_laborales = np.busday_count(np.datetime64('2020-09-01'), np.datetime64('2020-09-30'))
print(rango_laborales)




