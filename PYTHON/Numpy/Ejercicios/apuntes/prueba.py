import numpy as np

#Creamos una lista
lista = [1,2,3,4]
print(lista)

#Tratamos de multiplicarla por 2, pero lo que hace Python es añadir valores
valor = 2
lista_duplicada = lista*valor
print(lista_duplicada)

#Para multiplicarla tenemos que generar una lista aparte en la cual añadimos los valores mediante un for de la lista anterior
res = []
Valor_2 = 3
for v in lista_duplicada:
    res.append(v*Valor_2)
    
print(res)

#En cambio, si lo hacemos abriendo el objeto array desde numpy se hace mas facilmente
array = np.array(lista_duplicada)
print(array*4)
