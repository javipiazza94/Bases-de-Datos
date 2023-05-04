import numpy as np
import numpy.ma as ma
"""
### Ejercicio 1

Crea 3 nuevos arrays. 
- Array de tipo entero, que contenga solo los números impares del 1 al 100. 
- Array de tipo cadena con tu nombre y apellidos
- Array de tipo fechas, que contenga todos los días desde el 01Enero2020 al 04Febrero2020

"""
array_impares = np.arange(1, 100, 2)
array_cadena = np.array(["Javier", "Puente", "Piazza"])
array_fechas = np.arange('2020-01-01', '2020-02-04', dtype='datetime64[D]')
print(array_cadena)
print(array_fechas)
print(array_impares)

"""
### Ejercicio 2
    Recupera los últimos 10 elementos del array de impares
"""
print(array_impares[-10:100])

"""
### Ejercicio 3

Recorre el array de fechas, y genera un nuevo numpy array que contenga unicamente los días laborales
    
"""
laborables = []
for fecha in array_fechas:
    if np.is_busday(fecha):
        laborables.append(fecha)
laborables_array = np.array(laborables, dtype = 'datetime64')
print(laborables_array)

print(array_fechas[np.is_busday(array_fechas)])

"""
### Ejercicio 4

Genera la siguiente matriz. 

$A = \begin{pmatrix}
10 & 1 & 8 & 4 \\
3 & 7 & 2 & 1 \\
0 & 2 & 20 & 12 \\
\end{pmatrix}$

¿De qué tipo es?
Luego, implementa una máscara a todos los números de la matriz mayores o iguales a 10
    
"""
matrix = np.matrix('10 1 8 4 ; 3 7 2 1; 0 2 20 12', dtype=np.int16)
print(ma.masked_greater_equal(matrix, 10))

"""
### EJERCICO 5
   Crea dos fechas, la primera de ellas será tu fecha de nacimiento, y la segunda, la de un familiar o amigo tuyo. 

- ¿Qué diferencia en horas hay entre las dos fechas?
- ¿Cual sería tu fecha de nacimiento si hubieras nacido 236 horas antes?
"""

fecha_javi = np.datetime64('1994-08-25')
fecha_vega = np.datetime64('2018-03-27')

d1 = fecha_javi - np.timedelta64(236, 'h')
print(d1)

d2 = fecha_javi - fecha_vega

print(f"Mi sobrina es {str(np.timedelta64(d2, 'h'))} horas menor que yo")
print(d2)

