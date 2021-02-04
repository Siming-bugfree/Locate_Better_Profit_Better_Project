import csv 
import numpy as np 
import pandas as pd

neighborhoods=[]
with open('longitude_latitude.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		neighborhoods.append(row[0])
neighborhoods=neighborhoods[1:]

frequency=[]
with open('collaborative_filter_frequency.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		frequency.append(row)
print(frequency[:5])

T=np.zeros([140,140])
T=pd.DataFrame(T, index=neighborhoods, columns=neighborhoods)
for i in range(1,len(frequency)):
	for j in range(1,len(frequency[0])):
		T[frequency[0][j]][frequency[i][0]]=frequency[i][j]

T.to_csv('extended_collaborative.csv',index=False)
