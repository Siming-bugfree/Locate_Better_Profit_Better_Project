from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

item_url_list = []

def get_urls_from(page):
    try:
        header = {
            'cookie': 'TAUnique=%1%enc%3AQdV7w8ASnEYlbsNlpj00H4OtKHxkST%2BtW53sTMVh2FQ%3D; TASSK=enc%3AAJ%2FZJdH9Gu7MTpiOEuewPckZEDmerA1ZCAcqcPcd2qx6Q4Ogm6WsEKH6YSY2foQ4xcGIZ1pTZq4G0BdNWduNuiKaDNtzsCAaK9PIxWqRZsm2C5mTaw42LQwfckNRjNp3kA%3D%3D; ServerPool=B; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; TADCID=XktfiuCmb6hfNb2lABQCjnFE8vTET66GHuEzPi7KfWGdnt__oBNhgFWcWAGfahGrXQKXqMx0q_kGnYaTmubnRFFDv3WrFwy6sbs; TAAUTHEAT=5cgSnvUZun9U6Lw8ABQC5pMD6MhQQX22iUWVeLafiSF0nmeBGdlABB7tXIxBG5I7dae6roH2tSjn2nXxIPxSRdvlvg2QX2MaXdJNv9Aq-7Nw-gX3Z5X25JR0zfZ-aRIt3kTF2ElUobBRM8BRoymxq6piwsSl3oE8EidR0JhooJjE2Q0pPgI3jFbNLo644NjFKR7eC1VUfrylGx_UCATCSy7WR2Rdww2oKMNwOeMq; PAC=AE2ra4s3BZzP_DfR97reEP6TxpvwjUBXZlN-L3TuDFWrSkuDeoTpeZzqWiqt2uahMu43nCwKlaiaKYzyWUFOjhINvnsv21XxITrU9zGpUIkx61YaUYM-F9eKQuCIeYjuyofibx6AqL5tS0a-PjKyo9S-Tsgc6DV169iW-D01wVI3P9sn_G_5yLltlAAq2u7G76o5H2ePXEgKlLPtcnBFTV60SxMJ6PrR4kEtoZbj69kW; PMC=V2*MS.32*MD.20201113*LD.20201120; TART=%1%enc%3AJW7DZaY9NB%2BWJXLSWenHLsbEhG9aR0Hqx5Gvqt6atM0mZ6JsJDQ%2BuUNnHrmvTMzGNox8JbUSTxk%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1*RY.2020*RM.11*RD.20*RH.20*RG.2; TAReturnTo=%1%%2FRestaurant_Review-g60763-d5937621-Reviews-Obao-New_York_City_New_York.html; roybatty=TNI1625!AMJTBaNiattvI6pGH89iIBzBm7p3xsynyivf%2FWd04wyM3iWiNxa4TxgB0%2F7SjVvds1siP7cGz2Ik5ngXbrJUPbLX9XxGFAaUK2gwY%2FuIlntdiQ7xKBtSAiIQA1jDswsHNrYItjFkPu5b6Po0PKrdWCvMUPSDujEhnJuC7Y%2F8RFN3%2C1; SRT=%1%enc%3AJW7DZaY9NB%2BWJXLSWenHLsbEhG9aR0Hqx5Gvqt6atM0mZ6JsJDQ%2BuUNnHrmvTMzGNox8JbUSTxk%3D; CM=%1%sesstch15%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CCYLPUSess%2C%2C-1%7Ctvsess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7C%24%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csesshours%2C%2C-1%7CCOVIDMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7CSPACMCSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csesslaf%2C%2C-1%7CCYLPUPers%2C%2C-1%7Cperslaf%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Cperswifi%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CSPACMCPers%2C%2C-1%7CTrayssess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7Cbooksticks%2C%2C-1%7Cbookstickp%2C%2C-1%7CListMCPers%2C%2C-1%7Csesswifi%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CCrisisSess%2C%2C-1%7CTBPers%2C%2C-1%7Cperstch15%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7Cpershours%2C%2C-1%7CPremiumORSess%2C%2C-1%7CRestAdsPers%2C%2C-1%7CTrayspers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CMCPPers%2C%2C-1%7CListMCSess%2C%2C-1%7CSPMCSess%2C%2C-1%7Cmdpers%2C%2C-1%7Cpers_rev%2C%2C-1%7Cmds%2C1605857579664%2C1605943979%7CRBAPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CRCSess%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Cpssamex%2C%2C-1%7CCYLPers%2C%2C-1%7Ctvpers%2C%2C-1%7CTBSess%2C%2C-1%7CTSMCSess%2C%2C-1%7CAdsRetSess%2C%2C-1%7CCOVIDMCPers%2C%2C-1%7CMCPSess%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cmdsess%2C%2C-1%7C; TASession=%1%V2ID.1590FCC829B9D057AA39169EFDF6CC5A*SQ.65*PR.40185%7C*LS.DemandLoadAjax*GR.77*TCPAR.97*TBR.47*EXEX.36*ABTR.71*PHTB.9*FS.61*CPU.45*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.A1556ED3B603A3395E2D968DD0C34799*LF.en*FA.1*DF.0*TRA.false*LD.5937621*EAU.J; TAUD=LA-1605325974315-1*RDD-1-2020_11_14*RD-531605346-2020_11_20.5937621*LG-531608163-2.1.F.*LD-531608164-.....; __vt=u4NCism5HfAlAIdKABQCq4R_VSrMTACwWFvfTfL3vxF7eH3w_yA-irqM7IatTe8pooldBuLqx7lQN8cmDgiGcXPRbUy2lftK3OnnbphepJ7oOd3AVMOnC5aPp0Zc99R7N_dK1WpVRx4v3xYCqsDQyy0S9iFq7NZ3HCpOcVa_JL2l8BfLEIDCgtUtw8o5qtOlHrJb4CJZGAPU4-0',
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

