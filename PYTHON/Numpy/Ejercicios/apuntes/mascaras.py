import numpy.ma as ma
import numpy as np

#MASCARAS --> Anulan datos erroneos e incompletos
x = np.array([1,2,3,-1,4])

# Definimos el valor negativo como invalido --> el 1 (true) es el dato enmascarado
mask_array = ma.masked_array(x, mask = [0,0,0,1,0])
print(mask_array)
print(mask_array.min())
print(x.min())
print(x[0] is ma.masked)
print(mask_array[3] is ma.masked)
print(ma.masked_not_equal(x, 2))
print(ma.masked_where(x<2, x))
print(ma.masked_less_equal(x, 2))
print(ma.masked_inside(x, 1, 3))



