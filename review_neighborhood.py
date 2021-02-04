import json
import ast 
import csv

comments=[]
business={}
user={}
with open('selected_comments.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		comments.append(row)
comments=comments[1:]
print(comments[:10])
with open('matched_yelp_business_neighborhood.csv','r',encoding='utf-8') as f:
	b=csv.reader(f)
	for row in b:
		business[row[1]]=row[2]
print(business)
with open('User_Location.csv','r',encoding='utf-8') as f:
	u=csv.reader(f)
	for row in u:
		user[row[0]]=row[1]
print(user)

for i in range(len(comments)):
	comments[i].append(business[comments[i][1]])
for i in range(len(comments)):
	comments[i].append(user[comments[i][2]])

import pandas as pd
import numpy as np
df = pd.read_csv('longitude_latitude.csv')

lis = []
for i in range(df.shape[0]):
    li = []
    li.append(df.iloc[i][1])
    li.append(df.iloc[i][2])
    lis.append(li)
mat = np.zeros([df.shape[0],df.shape[0]])
for i in range(len(lis)):
    for j in range(len(lis)):
        mat[i][j] = np.sqrt((lis[i][0]-lis[j][0])**2 + (lis[i][1]-lis[j][1])**2)

n={}
with open('longitude_latitude.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	i=-1
	for row in c:
		n[row[0]]=i
		i+=1
print(n)

print(comments[:10])
for i in range(len(comments)):
	comments[i].append(mat[n[comments[i][5]]][n[comments[i][6]]])

with open('combined_for_tm.csv','w',newline='') as f:
	f_csv=csv.writer(f)
	for i in comments:
		f_csv.writerow(i)
f.close()
