import numpy as np


#EJERCICIO 1
    #Usando el array que encontráis a continuación.
        #- ¿Hay algún valor múltiplo de 7?
        #- Devuelve un array con todos los nº menores de 40 o que sean múltiplos de 7

#- ¿Hay algún valor múltiplo de 7?
a = np.array([2, 5, 4, 2, 49, 34, 59, 21, 45, 6, 105])
b = np.any(a % 7 == 0)
print(a)

#- Devuelve un array con todos los nº menores de 40 o que sean múltiplos d
print(b)
d = np.logical_or(a<40, a % 7 == 0)
print(d)
res = a[d]
print(res)

#EJERCICIO 2
    #Usando el array resultado del ejercicio anterior, calcula:   
        # - El producto de todos sus valores
        # - Convierte el array el una matriz 3x3 y realiza la suma por filas
        # - Calcula el log10 de cada elemento de la matriz que acabas de crear

# - El producto de todos sus valores
producto = np.prod(res)
print(producto)

# - Convierte el array el una matriz 3x3 y realiza la suma por filas
matriz = np.asmatrix(res)
m = matriz.reshape((3,3))
print(m)
suma_filas = np.sum(m, axis = 1)
print(suma_filas)

# - Calcula el log10 de cada elemento de la matriz que acabas de crear
logaritmo_m = (np.log10(m))
print(logaritmo_m)

#EJERCICIO 3
    #Haciendo uso de la matriz 3x3 creada en el ejercicio anterior y del siguiente array a, calcule:
        #- La suma de la matriz más el vector
        #- La división de ambos. ¿qué ocurre? Modifique el valor extraño por 0.
        #- El valor máximo de la matriz resultado de la división. ¿y por filas? ¿y por columnas?
        
vector = np.array([0,3,5])

#- La suma de la matriz más el vector
suma_m_vector = np.add(m,vector)
print(suma_m_vector)

#- La división de ambos. ¿qué ocurre? Modifique el valor extraño por 0.
division_m_vector = np.divide(m,vector)
print(division_m_vector)
division_m_vector[np.isinf(division_m_vector)] = 0
print(division_m_vector)

#- El valor máximo de la matriz resultado de la división. ¿y por filas? ¿y por columnas?
print("Max", np.max(division_m_vector))
print("Max", np.max(division_m_vector, axis=0))
print("Max", np.max(division_m_vector, axis=1))
        
        
#EJERCICIO 4
array = np.array([44, 28,  8, 34, 34, 26, 32, 12, 28,  6, 19, 12, 46, 20, 20, 49, 18,
    19, 15, 15, 43,  3, 17, 33, 27, 10, 18,  2,  3,  3, 35, 35, 21, 17,
    36, 31, 16, 27,  6, 46, 29, 25, 26, 48, 30, 19, 18,  1, 43, 10, 32,
    15, 32, 30, 40, 41, 11, 46, 39,  5, 40,  1, 26, 10, 18, 26, 25, 25,
    21, 30, 12, 46,  1, 43,  1,  3, 26, 24,  0, 36, 34,  7, 26, 25, 41,
    22,  1, 16, 43,  1, 46, 14, 17, 39, 12,  9, 42, 48,  9, 45, 47, 32,
    15,  6, 40, 18,  6, 13, 35,  8, 46, 48, 26, 23, 12, 29, 21,  6,  3,
    22, 27, 16, 27, 10, 28, 23,  5, 24, 17, 43, 25, 11, 38, 40, 32, 42,
    27, 32,  6, 16, 18, 10, 18, 34, 34,  3,  4,  5,  4,  0, 35, 30,  9,
    16, 32, 46,  7, 10, 20, 13, 48,  8, 27, 27, 27, 16, 17, 12, 35, 31,
    21, 29, 15, 49, 14, 22, 18,  0, 13, 14, 39, 30,  4, 48,  1, 19, 33,
    39,  9,  0, 24,  6, 12, 24, 29, 16, 11, 12, 13, 11])

#Considerando el array de números que podéis encontrar justo arriba, calcula:

#- Valor medio y mediano
medio = np.mean(array)
print(medio)
mediano = np.median(array)
print(mediano)

#- ¿Qué valor se encuentra en el tercer cuártil?
np.quantile(array, 0.75)

#- ¿Qué valor se encuentra en el percentil 25? ¿y en el 50? ¿con qué valor coincide este último?
print(np.percentile(array, q = 25))
print(np.percentile(array, q = 50))

#- ¿Cuál es la desviación estándar y la varianza del conjunto de datos?
print(np.std(array))
print(np.var(array))


a = np.arange(10)
a.reshape((2,5))
print(a)
