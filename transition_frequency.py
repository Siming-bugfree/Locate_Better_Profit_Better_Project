import csv 
import numpy as np 
import pandas as pd

T,D=[],[]
with open('extended_collaborative.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		T.append(row)
T=T[1:]
with open('Demagraphic_Toronto - Demagraphic_Toronto.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		D.append(row)
neighbors=D[0][1:]
D=D[1:]
variables=[]
for i in range(len(D)):
	variables.append(D[i][0])
	D[i]=D[i][1:]
D=np.array(D,dtype='float32')
T=np.array(T,dtype='float32')
D=pd.DataFrame(D, index=variables, columns=neighbors)
T=pd.DataFrame(T, index=neighbors, columns=neighbors)
D=D.T
p=D['Population, 2016']
print(D)
for j in range(1,D.shape[1]):
	for i in range(len(p)):
		D.iloc[i,j]=D.iloc[i,j]*p[i]
print(D)
D=D.T
E=D.dot(T)
# print(E.T)

E.T.to_csv('eaters_collaborative.csv',index=True)
