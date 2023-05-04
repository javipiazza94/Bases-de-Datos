import pandas as pd
import numpy as np

arr_m = np.arange(50).reshape(5,10)
print(arr_m[1:3,1:3])

d = {'a':10, 'b':20, 'c':30}
print(pd.Series(d))

print(pd.Series([1,2,3,4],['USA', 'GERMANY', 'USSR', 'JAPAN']))

arr = np.array([1,2,3,4,5,6,7,8])
print(arr[(arr>=1) & (arr<5)])

a = np.arange(25)
a.reshape((5,5))
print(a)