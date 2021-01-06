from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

item_url_list = []

def get_urls_from(page):
    try:
        header = {
            'cookie': '',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'referer': 'https://www.tripadvisor.com.sg/Restaurants-g60763-New_York_City_New_York.html',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-fetch-dest': 'empty',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors'
        }
        page_view = 'https://www.tripadvisor.com.sg/RestaurantSearch-g60763-oa{}-a_geobroaden.false-New_York_City_New_York.html#EATERY_LIST_CONTENTS'.format(str(30*page))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" + str(page+1))
        wb_data = requests.get(page_view, headers=header)
        time.sleep(random.randint(15,30))
        soup = BeautifulSoup(wb_data.text,'lxml')
        if soup.find_all(class_='no-search'):
            pass
        else:
            for url in soup.select('div.wQjYiB7z > span > a'):
                item_url = url.get('href')
                item_url_list.append(item_url)
    except:
        print("ERROR" + str(page+1))

for page in range(375):
    get_urls_from(page)

url_df = pd.DataFrame(item_url_list)
url_df.to_csv('item_urls.csv')

