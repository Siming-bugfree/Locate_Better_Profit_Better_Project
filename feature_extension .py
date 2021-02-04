import csv

b={}
with open('business_preprocessed.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		b[row[0]]=row[1:]
print(b)
X=[]
with open('X_cuisine.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		X.append(row)
print(X[:10])

X[0]=X[0]+b['business_id']
for i in range(1,len(X)):
	X[i]=X[i]+b[X[i][1]]
print(X[:10])

with open('X_combined.csv','w',newline='',encoding='utf-8') as f:
	f_csv=csv.writer(f)
	for i in X:
		f_csv.writerow(i)
f.close()