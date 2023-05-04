import numpy as np

#orden
# min y max devuelven los valores minimos y maximos de un array
a = np.array([2,5,6,10])
print("Min", np.min(a))
print("Max", np.max(a))
print(a.argmax()) #devuelve la posicion del maximo
print(a.argmin()) #devuelve la posicion del minimo
b = np.arange(12).reshape(3,4)

print(np.min(b, axis = 1)) # Axis 1 por fila
print(np.min(b, axis = 0)) # Axis 0 por columnas

# percentile - Calcule el percentil q-ésimo de los datos a lo largo del eje especificado.
b = np.arange(0, 101)
print(np.percentile(b, q = 11))

# Idem para el quantil. 
print(np.quantile(b, q = 0.25))

#MEDIAS Y COVARIANZAS
# median - Calcula la mediana (valor central)
print(np.median(b))
print(np.median(np.array([1,2,0,100,200,300,50])))

# average o media (con pesos)
a = np.array([1,2,3,4])
print(np.average(a))
print(np.average(a, weights=[2,2,1,1]))

# mean - Practicamente idéntico
b = np.arange(12).reshape(4,3)

print(np.mean(b, axis = 0)) # Media por columnas
print(np.mean(b, axis = 1)) # Media por filas

# std - Desviacion estándar
print(np.std(b, axis = 0))
print(np.std(b))

# var - Varianza
np.var(b, axis = 1)
std = np.std(b, axis = 0)
print(std)
var = np.var(b, axis = 0)
print(var)
print(np.sqrt(var))


