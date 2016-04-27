# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:37:50 2016

@author: marisarivera
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline

import csv
%cd ~/Desktop

!head -n 5 allstate.csv

pd.set_option('max_columns', 50)
from_csv = pd.read_csv('allstate.csv')
from_csv.head()

cols = ['customer_ID','shopping_pt','record_type','day','time','state',
'location','group_size','homeowner','car_age','car_value','risk_factor','age_oldest',
'age_youngest','married_couple','C_previous','duration_previous','A','B','C','D','E',
'F','G','cost']

#1.¿Qué características tienen los grupos a los que se les cotiza los seguros más baratos?
minimo = from_csv['cost'].quantile(0.25)
minimo
respuesta = from_csv[from_csv['cost']<minimo]
respuesta.describe()

#2.¿Qué tan probable es que se compre un seguro después de la k-ésima cotización?
n=3;
x=n+1;
total= sum (from_csv["shopping_pt"]==1)
compran=total-(sum(from_csv["shopping_pt"]==x))
probabilidad=((compran/1.0)/(total/1.0))*100
print("la probabilidad de comprar despues de la " + str(n) + " cotizacion es: "+ str(probabilidad)[0:4] + "%")

#3.Basados en la edad del más joven. ¿Que grupo tiene mayor probabilidad de comprar un seguro?
young = from_csv[from_csv['age_youngest'] < from_csv.age_youngest.quantile(0.25)]
young
x = from_csv[['group_size','risk_factor']]
x
y = x[x['risk_factor']==1]
y.describe()
y.group_size.quantile(0.75)

#4.¿Que edad promedio tienen las personas dueñas de carros viejos y carros nuevos?
edad = from_csv[['car_age','age_oldest']]  
carro_viejo = edad[edad.car_age == edad.car_age.max()] 
promedio_ageoldest = carro_viejo.age_oldest.mean()
#print(promedio_ageoldest)

edad = from_csv[['car_age','age_youngest']]  
carro_viejo = edad[edad.car_age == edad.car_age.max()] 
promedio_ageyoungest = carro_viejo.age_youngest.mean()
#print(promedio_ageyoungest)

edad = from_csv[['car_age','age_oldest']]  
carro_nuevo = edad[edad.car_age == edad.car_age.min()] 
promedio_ageoldest = carro_nuevo.age_oldest.mean()
print(promedio_ageoldest)

edad = from_csv[['car_age','age_youngest']]  
carro_nuevo = edad[edad.car_age == edad.car_age.min()] 
promedio_ageyoungest = carro_nuevo.age_youngest.mean()
print(promedio_ageyoungest)

#5.¿Probabilidad de que alguien de edad k compre un seguro?
edad=20;
age1=from_csv[from_csv['age_oldest']==edad]
totales=sum(from_csv['record_type']==1)
compra1=sum(age1['record_type']==1)
probabilidad1=((compra1/1.0)/(totales/1.0))*100

age2=from_csv[from_csv['age_youngest']==edad]
compra2=sum(age2['record_type']==1)
probabilidad2=((compra2/1.0)/(totales/1.0))*100

probabilidad=probabilidad1+probabilidad2;

print("La probabilidad que alguien de "+ str(edad) +" años compre un seguro es de: "+ str(probabilidad)[0:4] + "%")

#6.¿Que estado, en promedio, necesita menos cotizaciones?
state = from_csv[from_csv.record_type==1].groupby("state")
state.shopping_pt.mean()
state.shopping_pt.mean().min()
state.shopping_pt.mean()

#7.¿Cuántas cotizaciones, previo la compra, realizan los consumidores del estado de Florida?
a = (from_csv.state == "FL") & (from_csv.shopping_pt == 1)
b = (from_csv.state == "FL") & (from_csv.shopping_pt == 2)
print(a.sum()- b.sum())

c = (from_csv.state == "FL") & (from_csv.shopping_pt == 3)
d = (from_csv.state == "FL") & (from_csv.shopping_pt == 4)
print(c.sum()-d.sum())

e = (from_csv.state == "FL") & (from_csv.shopping_pt == 5)
print(d.sum()-e.sum())

f = (from_csv.state == "FL") & (from_csv.shopping_pt == 6)
print(e.sum()-f.sum())

g = (from_csv.state == "FL") & (from_csv.shopping_pt == 7)
print(f.sum()-g.sum())

h = (from_csv.state == "FL") & (from_csv.shopping_pt == 8)
print(g.sum()-h.sum())

i = (from_csv.state == "FL") & (from_csv.shopping_pt == 9)
print(h.sum()-i.sum())

j = (from_csv.state == "FL") & (from_csv.shopping_pt == 10)
print(i.sum()-j.sum())

k = (from_csv.state == "FL") & (from_csv.shopping_pt == 11)
print(j.sum()-k.sum())

l = (from_csv.state == "FL") & (from_csv.shopping_pt == 12)
print(k.sum()-l.sum())

m = (from_csv.state == "FL") & (from_csv.shopping_pt == 13)
print(l.sum()-m.sum())

#8.¿En qué tiempo prudente se realizan las cotizaciones?
ventas = from_csv[(from_csv.record_type == 1)]
ventas.count()
ventas.time.mode()

#9.¿Del total de carros que porcentaje tiene menos de k años?
dataFrame = from_csv[['car_age']]

def underCarAge(edad):
    x = from_csv[['car_age']]
    temp = x[x.car_age < edad]
    respuesta = (temp.count() / x.count())*100
    return respuesta

max_value = dataFrame.max()
min_value = dataFrame.min()
lista = []
for i in range(min_value,max_value+1):
    j = [int(i), str(str(float(underCarAge(i)))+'%')]
    listaDeValores.append(j)

nombre = pd.Series((v[0] for v in lista))
nombreDeSerie = pd.Series((v[1] for v in lista))
newDataFrame = pd.concat([nombre,nombreDeSerie], axis = 1)
newDataFrame.columns = ('Edad','Porcentaje')

print(newDataFrame)

#10.¿Que edad necesita menos cotizaciones para comprar un seguro?
datos = from_csv[['record_type','shopping_pt','age_youngest']]
seguro = datos[datos.record_type == 1]
cot_min = min(seguro.shopping_pt)
cot_cantidad = seguro[seguro.shopping_pt == cot_min]
respuesta = cot_cantidad.mode()
print('Para comprar la edad que menos cotiza es: ' + str(int(respuesta.age_youngest)))