import numpy as np

#EJERCICIO 1
#Genera un array que contenga 25 elementos entre 0 y 99 siguiendo una distribución lineal. 
#Luego, transforma ese array en una matriz de 5 x 5. ¿Cuál es la diagonal de la matriz? ¿Y la diagonal justo superior?

a = np.arange(0,100,4)
print(a)
m = a.reshape((5,5))
print(m)
diagonal = a = np.diag(m)
print(diagonal)
diagonal_SUP = a = np.diag(m, k=1)
print(diagonal_SUP)

#EJERCICIO 2
#Crea un de 5 x 4 con el valor repetido 10. Une esa matriz a la matriz del ejercicio anterior para conseguir dos nuevas matrices, una de  5 x 9, y otra de 9 x 5.
b = np.full(shape=(4, 5), fill_value=10)
print(b)

concatenar_fil = np.concatenate((m,b), axis = 0)
print(concatenar_fil)
contatenar_col = np.concatenate((m, b.T), axis = 1)
print(contatenar_col)

#EJERCICIO 3
#Teniendo el array inicial que podéis ver justo abajo, debéis realizar las operaciones necesarias para obtener el array: 
# ¿Qué elementos del array comienzan por 'E'?

cadenas_arr = np.array(['     este es un curso de openwebinars    '], str)
print(cadenas_arr)
cadenas_arr2 = np.char.strip(cadenas_arr)
print(cadenas_arr2)
cadenas_arr3 = np.char.split(cadenas_arr2, sep=' ')
cadenas_arr3 = np.array(cadenas_arr3[0])
print(cadenas_arr3)
cadenas_arr4 = np.char.capitalize(cadenas_arr3)  # Capitalizamos la primera letra
print(cadenas_arr4)
cadenas_arr5 = np.char.startswith(cadenas_arr4, prefix='E')  # Filtramos por palabras que empiezan con E
print(cadenas_arr4[cadenas_arr5])

#EJERCICIO 4

"""
Considerando las matrices A y B. 
- Realiza la multiplicación matricial de AxB y BxA. ¿Son iguales?
- Realiza la multiplicación de la matriz A x 2
- ¿Cúanto es la multiplicación escalar de AxB? ¿y de BxA?
"""

a = np.array([[3,1,2], [4,1,3], [2,0,1]])
b = np.array([[2,0,3], [1,1,1], [0,2,4]])

print(a)
print(b)

multi_1 = np.dot(a, b)
print(multi_1)
multi_2 = np.dot(b, a)
print(multi_2)
print(a*2)
print(np.vdot(a,b))
print(np.vdot(b,a))

#EJERCICIO 5

"""
A^3
El determinante de A
Resuelve la ecuación Ax = y, siendo y el array [3,2,5]
"""

a = np.array([[3,1,2], [4,1,3], [2,0,1]])
print(np.linalg.matrix_power(a, 2))
print(np.linalg.det(a))
y = np.array([3,2,5])
x = np.linalg.solve(a, y)
print(x)
