import csv
import xlrd
import xlwt
from xlutils.copy import copy
from bs4 import BeautifulSoup
import requests
import json
import time 
import random
import os


#Read urls
urls=[]
with open('item_urls.csv','r') as data:
    items=csv.reader(data)
    for item in items:
        urls.append('http://www.tripadvisor.com.sg'+item[0])

#Prepare output
exist_urls=[]   
if os.path.exists('result.xls'):
    result=xlrd.open_workbook('result.xls')
    wb=copy(result)
    ws=wb.get_sheet(0)
    result=result.sheet_by_index(0)
    for i in range(1,result.nrows):
        exist_urls.append(result.cell(i,11).value)
else:
    wb = xlwt.Workbook()
    ws = wb.add_sheet('result')
    col_names=['name','geo','lat','lng','avg_rating','review_count','det_rating','cuisine','meal','pricerange','url']
    for i in range(len(col_names)):
        ws.write(0, i, col_names[i])
    wb.save('result.xls')

#Start 
start_index=1 #skip the title of list urls
end_index=7000 
for url_index in range(start_index,end_index):
    if urls[url_index] in exist_urls:
        continue
    time.sleep(random.randint(5,15))
    print(url_index)
    print(urls[url_index])
    response=requests.get(urls[url_index])
    html=response.text
    # print(html)
    soup=BeautifulSoup(html,'lxml')
    exp=soup.select('script')
    for e in exp:
        if 'WEB_CONTEXT' in e.text:
            txt=e.text
            start=7+txt.find('"data":{"name"')
            end=7+txt.find('html"}},"error":null},')
    data=txt[start:end]
    if data=='': continue
    data=json.loads(data)
    ws.write(url_index, 0, data['name'])
    ws.write(url_index, 1, data['geo'])
    loc=data['location']    
    ws.write(url_index, 2, loc['latitude'])
    ws.write(url_index, 3, loc['longitude'])
    rating=data['rating']
    ws.write(url_index, 4, rating['primaryRating'])
    ws.write(url_index, 5, rating['reviewCount'])
    det_rating={}
    detailed_rating_list=rating['ratingQuestions']
    for item in detailed_rating_list:
        det_rating[item['name']]=item['rating']
    ws.write(url_index, 6, str(det_rating))
    detail=data['detailCard']['tagTexts']
    cuisine=[]
    cuisine_list=detail['cuisines']['tags']
    for item in cuisine_list:
        cuisine.append(item['tagValue'])
    ws.write(url_index, 7, str(cuisine))
    meal_list=detail['meals']['tags']
    meal=[]
    for item in meal_list:
        meal.append(item['tagValue'])
    ws.write(url_index, 8, str(meal))
    ws.write(url_index, 9, detail['priceRange']['tags'][0]['tagValue'])
    ws.write(url_index, 10, data['detailCard']['numericalPrice'])
    ws.write(url_index, 11, urls[url_index])
    wb.save('result.xls')

wb.save('result.xls')
