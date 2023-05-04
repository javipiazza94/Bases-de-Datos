import numpy as np

# all - Comprueba si todos los elementos de una matriz o array cumplen una condicion

a = np.array([2,3,4,5])
np.all(a < 10)

# any - Comprueba si algún elemento de una matriz o array cumplen una condicion

a = np.array([2,3,4,5])
np.any(a < 0)

# logical_and : Función lógica and. Devuelve True si todas las comprobaciones son ciertas
np.logical_and(a > 2, a < 4)

# logical_or : Función lógica or. Devuelve True si alguna de las comprobaciones son ciertas
np.logical_or(a > 2, a < 4)

# Devuelve True si todas las diferencia en valor absoluto es menor a la tolerancia.
np.allclose([1e10,1e-7], [1.00001e10,1.000001e-7], rtol=0.00001)

#isclose - Igual, pero valor a valor
np.isclose([1e10,1e-7], [1.001e10,1.000001e-7], rtol=0.00001)

#equal - Verdadero si dos arrays o matrices son iguales en cuanto a dimensiones y valores
np.array_equal(np.array([1,2,3]), np.array([1,2,3]))
np.array_equal(np.array([1,2,3]), np.array([1,2,3,4]))

# greater - Devuelve True si el valor es mayor.
np.greater(np.array([1,2,3]), np.array([3,2,1]))
np.greater_equal(np.array([1,2,3]), np.array([3,2,1]))

# less y less_equal funcionan igual.
np.less(np.array([1,2,3]), np.array([3,2,1]))
np.less_equal(np.array([1,2,3]), np.array([3,2,1]))