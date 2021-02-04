import csv 
import numpy as np 
import pandas as pd

neighbors,business={},[]
with open('eaters_frequency.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		neighbors[row[0]]=row[1:]
print(neighbors)
with open('business_final_data_neighborhood.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		business.append(row)
print(business[:10])
for i in range(1,len(business)):
	business[i]=business[i]+neighbors[business[i][28]]
print(business[1:5])

with open('X_frequency.csv','w',newline='',encoding='utf-8') as f:
	f_csv=csv.writer(f)
	for i in business:
		f_csv.writerow(i)
f.close()