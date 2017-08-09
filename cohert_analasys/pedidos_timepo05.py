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
# for i in range(4747):
good_ids=[]
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
            # print gastos_total_per_client,num_of_transaction_per_client,week_when_client_start,i
            # print a4
            if  gastos_total_per_client>30:
                gg.append(gastos_total_per_client)
                nn.append(num_of_transaction_per_client)
                ww.append(week_when_client_start)
                good_ids.append(i)
    except:
        pass
        # print id_client, bd.iloc[id_client, 0]
bd=bd.iloc[good_ids,:]
bd.index=range(bd.shape[0])
ind=range(0,30)

wo_all=list(4+np.array((ind))*2)  #gast this week
fo_all=list(5+np.array((ind))*2) # gives me actibe week

print wo_all
print fo_all
print np.ones(30)
mat=np.ones(30)
mmat=np.ones((30,30))-1
print mmat.shape
#
print "retation"
for j in range(1,31):
    for i in range(1,31):
        # j=30
        st1="fo"+str(j)
        st2="w"+str(i)
        # print bd[(bd.loc[:,st1]==1) & (bd.loc[:,st2]!=0)].shape[0],st1,st2
        # print bd[(bd.loc[:, st1] == 1) & (bd.loc[:, st2] != 0)], st1, st2
        bdg=bd[(bd.loc[:, st1] == 1) & (bd.loc[:, st2] != 0)]
        # print bdg.iloc[:,wo_all]

        mmat[j-1,i-1]=np.sum(bdg.iloc[:,wo_all].values)
            # bd[(bd.loc[:,st1]==1) & (bd.loc[:,st2]!=0)].shape[0]
print mmat
#
mata=pd.DataFrame(mmat)
mata.to_csv("mata1.csv")
mmatR=np.ones((30,30))-1
i=2
l=30-i
print i,l
print mmat[i,i:l+i]
print mmat[i,i:l+i].shape
print mmatR[i,:l]
print mmatR[i,:l].shape

for i in range(mmat.shape[0]):
    l=30-i
    # print i,l
    print mmatR[i,:l].shape, mmat[i,i:l+1].shape,i,l
    mmatR[i,:l]= mmat[i,i:l+i]
    # mmatR[i, :l] =mmatR[i, :l]/mmatR[i, 0]*100


for i in range(mmatR.shape[0]):
    for j in range(mmatR.shape[0]):
        mmatR[i,j]=format(mmatR[i,j], '.2f')



mataR=pd.DataFrame(mmatR)
mataR.to_csv("mata2.csv")
import seaborn as sns;
week=[]
for i in range(1,31):
    week.append("w"+str(i))
mataR.columns=week
sns.heatmap(mataR,cmap="YlGnBu")#,annot=True)
plt.show()


# if ret==1:
# elif ret==2:
# elif ret == 3:
# elif ret == 4:
# elif ret == 5:
# elif ret == 6:
# elif ret == 7:
# elif ret == 8:
# elif ret == 9:
# elif ret == 10:
# elif ret == 11:
# elif ret == 12:
# elif ret == 13:
# elif ret == 14:
# elif ret == 15:
# elif ret == 16:
# elif ret == 17:
# elif ret == 18:
# elif ret == 19:
# elif ret == 20:
# elif ret == 21:
# elif ret == 22:
# elif ret == 23:
# elif ret == 24:
# elif ret == 25:
# elif ret == 26:
# elif ret == 27:
# elif ret == 28:
# elif ret == 29:
# elif ret == 30:
# else:
#     print "algo raro"
# #
st1 = "fo1" + str(j)
st2 = "w1" + str(i)
#
# print np.sum(bdg.iloc[:,wo_all].values)
# bdg=bd[(bd.loc[:, st1] == 1) & (bd.loc[:, st2] != 0)]