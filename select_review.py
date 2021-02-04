import json
import ast 
import csv

business=[]
comments=[]
target_cate=[]
with open('business_final_data.csv','r',encoding='utf-8') as f:
	b=csv.reader(f)
	for row in b:
		business.append(row[1])
# print(business[:10])

with open('selected_comments.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		comments.append(row)
# print(comments[:10])

with open('target_cate.csv','r',encoding='utf-8') as f:
	c=csv.reader(f)
	for row in c:
		target_cate.append(row[0])
print(target_cate[:10])

business=business[1:]    #Drop the titles
comments=comments[1:]
for i in range(len(comments)):
	if comments[i][3]!='':
		comments[i][3]=ast.literal_eval(comments[i][3])
print(comments[:10])

def add_c(dict,c_l,flag):
	for c in c_l:
		if c in dict:
			dict[c][0]=dict[c][0]+flag
			dict[c][1]=dict[c][1]+1
		else:
			dict[c]=[1,1]

results=[]
category={}
for i in range(len(comments)):
	if comments[i][1] in business:
		results.append(1)
		add_c(category,comments[i][3],1)
	elif len(set(comments[i][3]) & set(target_cate))>0:
		results.append(1)
		add_c(category,comments[i][3],0)
	else:
		results.append(0)
		add_c(category,comments[i][3],0)
print(results[:30])
print(category)

# with open('results.csv','w',newline='') as f:
# 	f_csv=csv.writer(f)
# 	for i in results:
# 		f_csv.writerow([i])
# f.close()
# with open('category.csv','w',newline='') as f1:
# 	f_csv=csv.writer(f1)
# 	for c in category:
# 		f_csv.writerow([c,category[c][0],category[c][1],category[c][0]/category[c][1]])
# f1.close()
with open('n_results.csv','w',newline='') as f:
	f_csv=csv.writer(f)
	for i in results:
		f_csv.writerow([i])
f.close()