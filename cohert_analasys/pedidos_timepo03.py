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
gg=[]
nn=[]
ww=[]
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
            gg.append(gastos_total_per_client)
            nn.append(num_of_transaction_per_client)
            ww.append(week_when_client_start)
    except:
        pass
        # print id_client, bd.iloc[id_client, 0]

plt.hist(gg,bins=300)
plt.xlim((0,300))
plt.title("Gastos per client")
plt.show()
#
# plt.hist(nn,bins=30)
# plt.title("Num of transaction per client")
# plt.show()
# print ww
# ww=map(lambda x: int(x),ww)
# plt.hist(ww,bins=30)
# plt.title("Week when client starts")
# plt.show()
id_client=655
total_per_week=[]
new_per_week=[]
for i in list(4+np.array((ind))*2):
    total_per_week.append(np.sum(bd.iloc[:,i]))
    new_per_week.append((np.sum(bd.iloc[:,i+1])))
    print np.sum(bd.iloc[:,i]),bd.columns[i],np.sum(bd.iloc[:,i+1])
plt.plot(total_per_week,"o-")
plt.title("Total money per week")
plt.show()
plt.plot(new_per_week,"o-")
plt.title("Num of new ppl per week")
plt.show()

print np.sum(bd.iloc[:,4])