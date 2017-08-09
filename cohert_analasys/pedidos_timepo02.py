import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re
from unidecode import unidecode
from sklearn import preprocessing

# -*- coding: utf-8 -*
import datetime
import re

fila="Prueba Vitaly.xlsx"
bd=pd.read_excel(fila,sheetname="pedidos_tiempo 2017",encoding='utf-8')
print bd.head(10)
print bd.columns
print bd.shape
columns=["id","sexo","zip","age"]
# columns+=["id2","sexo2","zip2","age2"]
print columns
for i in range(1,31):
    st1="w"+str(i)
    st2 = "fo"+str(i)
    print st1,st2
    columns +=[st1,st2]
print columns
bd.columns=columns
print bd.head(10)
ind=range(0,30)
print list(4+np.array((ind))*2)
# plt.plot(bd.iloc)
print sum(bd.iloc[0,list(4+np.array((ind))*2)])
id_client=4747 #last
id_client=105

print bd.iloc[id_client,:]
def get_info(id_client,bd):
    gastos_total_per_client= sum(bd.iloc[id_client,list(4+np.array((ind))*2)])
    # print "gastos total",gastos_total_per_client
    when_start=bd.iloc[id_client,4:]
    bool=bd.iloc[id_client,list(5+np.array((ind))*2)]==1
    pattern=u"\d+"
    week_when_client_start=re.findall(pattern,bool.index[bool.values].values[0])[0]
    # print  "when client start", week_when_client_start
    num_of_transaction_per_client=np.sum([bd.iloc[id_client,list(4+np.array((ind))*2)]!=0])
    # print "num of transaction per client",num_of_transaction_per_client
    logika= bd.iloc[id_client,list(4+np.array((ind))*2)]!=0
    active_weeks= map(lambda  x: re.findall(pattern,x)[0],logika.index[logika.values].values)
    # print "active weeks",active_weeks
    wactive_weeks=map(lambda x: "w"+x,active_weeks)
    gastos_per_week_per_client=bd.loc[id_client,wactive_weeks].values
    # print "gastos per week per client",gastos_per_week_per_client
    return gastos_total_per_client,week_when_client_start,num_of_transaction_per_client,active_weeks,gastos_per_week_per_client
z=1
CAC=30
for i in range(4747):
    id_client=i

    try:
        a1,a2,a3,a4,a5=get_info(id_client,bd)
        gastos_total_per_client=a1
        week_when_client_start=a2
        num_of_transaction_per_client=a3
        active_weeks=a4
        gastos_per_week_per_client=a5

        # print gastos_total_per_client,num_of_transaction_per_client,week_when_client_start,i
        if gastos_total_per_client==0:
            # print id_client, bd.iloc[id_client, 0],z
            z=z+1
        else:
            print gastos_total_per_client,num_of_transaction_per_client,week_when_client_start,i
    except:
        pass
        # print id_client, bd.iloc[id_client, 0]



#
# zips=[1, 2, 3,  4,  5,  6,  7,  8,  9,
#     10, 11, 12,13, 14, 15, 16, 17, 18, 19,20,  21,  22,  23,  24,  25,  26,  27,  28,  29,   30,
#     31, 32,  33, 34, 35, 36, 37,38,  39,  40, 41, 42, 43, 44, 45, 46, 47, 48,  49, 50,  51,   52]
# cities=[ "Araba", "Albacete", "Alicante","Almeria", "Avila", "Badajoz",  "Balearic     Islands", "Barcelona",  "Burgos",
#      "Caceres", "Cadiz", "Castellon",  "Ciudad     Real", "Cordoba", "A     Coruna", "Cuenca", "Girona", "Granada",
#     "Guadalajara",    "Gipuzkoa", "Huelva",    "Huesca",    "Jaen", "Leon", "Lleida", "La     Rioja(formerly     Logrono)",
#      "Lugo",    "Madrid","Malaga",    "Murcia", "Navarre",  "Ourense",  "Asturias(formerly     Oviedo)",  "Palencia",
#         "Las     Palmas",    "Pontevedra", "Salamanca",    "Santa     Cruz     de     Tenerife",    "Cantabria(formerly Santander)",
#         "Segovia", "Seville",    "Soria", "Tarragona", "Teruel", "Toledo", "Valencia",    "Valladolid",
#         "Bizkaia",    "Zamora",    "Zaragoza",    "Ceuta",    "Melilla"]
#
# bdg=pd.DataFrame(zip(zips,cities))
# bdg.columns=["zips","cities"]
# print bdg.head(20)
#
#
# print bd.zip
# cc=[]
# for i in range(4747):
#     zips=bd.zip[i]
#     zips=str(int(zips))
#     if len(zips)==4:
#         zz=zips[0]
#     else:
#         zz=zips[:2]
#     print zz,zips,bdg.cities[bdg.zips==int(zz)].values[0]
#     cc.append(bdg.cities[bdg.zips==int(zz)].values[0])
# a,b=np.unique(cc,return_counts=True)
# print zip(a,b)
# print b
# sort_index = np.argsort(b)
# for a1,a2 in  zip(a[sort_index[::-1]],b[sort_index[::-1]]):
#     print a1,a2
print np.unique(bd.sexo.loc[:566].values,return_counts=True)
bd= bd[bd.age!=2017]
bd= bd[bd.age>80]
print bd.head(20)
