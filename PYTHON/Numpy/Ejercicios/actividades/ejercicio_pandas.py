import pandas as pd
import numpy as np

#Ejercicios
#Pueden haber diferentes formas de resolver las siguientes cuestiones plantedas, nunca existe una única forma de hacer las cosas, ¿cúal es la tuya? 

ruta = 'C:/Users/javier.puente.ext/Documents/PYTHON/Numpy/Ejercicios/actividades/Salaries.csv'
df_sal = pd.read_csv(ruta)
print(df_sal)

# Muestra las primeras líneas del dataframe
print(df_sal.head(5))

#Obten info variables+
print(df_sal.info())

# ¿Cual es la media de TotalPayBenefits?
print(df_sal['TotalPayBenefits'].mean())

# ¿Cual es el máximo del TotalPay?
print(df_sal['TotalPay'].max())

# De las agency de San Francisco, ¿cual es el promedio de TotalPay?
print(df_sal[df_sal['Agency']=='San Francisco']['TotalPay'].mean())

#¿Cual es el empleo de Joanne Hayes-White?
print(df_sal[df_sal['EmployeeName']=='Joanne Hayes-White']['JobTitle'])

#¿Quien es el empleado mejor pagado (incluyendo beneficios)?
print(df_sal[df_sal['TotalPayBenefits'] == df_sal['TotalPayBenefits'].max()])

#¿Cuántos empleados hay?
print(df_sal['Id'].nunique())