from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

item_url_list = []

def get_urls_from(page):
    try:
        header = {
            'cookie': 'TAUnique=%1%enc%3AQdV7w8ASnEYlbsNlpj00H4OtKHxkST%2BtW53sTMVh2FQ%3D; TASSK=enc%3AAJ%2FZJdH9Gu7MTpiOEuewPckZEDmerA1ZCAcqcPcd2qx6Q4Ogm6WsEKH6YSY2foQ4xcGIZ1pTZq4G0BdNWduNuiKaDNtzsCAaK9PIxWqRZsm2C5mTaw42LQwfckNRjNp3kA%3D%3D; ServerPool=B; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; CM=%1%sesstch15%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CCYLPUSess%2C%2C-1%7Ctvsess%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CUVOwnersSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CRepTarMCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7C%24%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CTSMCPers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csesshours%2C%2C-1%7CCOVIDMCSess%2C%2C-1%7CTARSWBPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7CSPACMCSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csesslaf%2C%2C-1%7CCYLPUPers%2C%2C-1%7Cperslaf%2C%2C-1%7CRevHubRMPers%2C%2C-1%7CUVOwnersPers%2C%2C-1%7Csh%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCrisisPers%2C%2C-1%7CCCPers%2C%2C-1%7CRepTarMCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Cperswifi%2C%2C-1%7CSPMCPers%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CSPACMCPers%2C%2C-1%7CTrayssess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7Cbooksticks%2C%2C-1%7Cbookstickp%2C%2C-1%7CListMCPers%2C%2C-1%7Csesswifi%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CCrisisSess%2C%2C-1%7CTBPers%2C%2C-1%7Cperstch15%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7Cpershours%2C%2C-1%7CPremiumORSess%2C%2C-1%7CRestAdsPers%2C%2C-1%7CTrayspers%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CMCPPers%2C%2C-1%7CListMCSess%2C%2C-1%7CSPMCSess%2C%2C-1%7Cmdpers%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBAPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CRCSess%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Cpssamex%2C%2C-1%7CCYLPers%2C%2C-1%7Ctvpers%2C%2C-1%7CTBSess%2C%2C-1%7CTSMCSess%2C%2C-1%7CAdsRetSess%2C%2C-1%7CCOVIDMCPers%2C%2C-1%7CMCPSess%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cmdsess%2C%2C-1%7C; TART=%1%enc%3AJW7DZaY9NB%2BWJXLSWenHLsbEhG9aR0Hqx5Gvqt6atM0mZ6JsJDQ%2BuUNnHrmvTMzGNox8JbUSTxk%3D; TATravelInfo=V2*AY.2020*AM.12*AD.6*DY.2020*DM.12*DD.7*A.2*MG.-1*HP.2*FL.3*DSM.1606404048753*RS.1*RY.2020*RM.11*RD.20*RH.20*RG.2; TAAUTHEAT=dlVBIAi4I05G57p3ABQC5pMD6MhQQX22iUWVeLafiSGiMePC00DrB81-z7nNuB8BLSHjKrhQgAO5kZedm1uqCAH0MP7Fn5Wfa67IwUUrIxTLzrNfAC-FtQnA1VRhUej2sH_iozSbuTpwLT88lm-01WGU5UrOLv6Q95Avo79mHBpItttFakqWJOWyNigAR-mtDANkxC-ePWXDfJpi_Ej-jx7DvTpoJlLpvUNXkxBF; TADCID=uA4G3k0loXIINvkoABQCjnFE8vTET66GHuEzPi7KfWHLMfwAT0-Vc_Hut7cMZ6zfCnfdN94OgycjDbhYsFIrREOrlCrWCQ-zQZ8; PAC=AJCblZ_zcbJYHJn5ynomu0wjXfpUGpumn0AH5ljvXIk0_sA_OnhZfPBvFyoZhl7QJXKWeKxb3qXXPuxlsTTtIucAuM9nRDeZfFqQFx9zn3EP-ly7bMdNHLSV5cOU46UqqW4CpMNj_UVLt5uZNpdV5yIjxwrshSd8SpixubBiYwTUMGgh9DWO3ZPLEGykZbZIKSKBJ_nCye-78TpfVVOVBd1EYvJIey2zz6UfiInJ-zIjw7SXpgp15z5FPBQ39YGf1Fpwy3bvGQYblbVka1laACo%3D; PMC=V2*MS.32*MD.20201113*LD.20201128; TAReturnTo=%1%%2FRestaurants-g155019-Toronto_Ontario.html; __vt=Wt8psE8oqmnvy_DCABQCq4R_VSrMTACwWFvfTfL3vxGo0lfYSmA_LcX8fhQW7sDqiPv5A95ts5L4_7rgo8_CJHQBjn0IwH8xyjiNF-JXBCyjre2_CLPCwZQhzf5lqK-hXo3ZX2t9Oc2g5dflJwEdL42hTbw; roybatty=TNI1625!ANA4VEz6Xs5Zm%2FnNsZGP0Qm7Eki1lEylTlrw0zaUKc8nu44p96K1HSVLywW3tQNlYHDtkjXFCTVJJNItzJMQ9ltHTVPAuOYlEDqYFKdubZdiMLSPCzMBRvJMWoeMRh%2FJs23qgtd3uOCtRndMY7uIInlzInp2QEiRZCjh2tuYeP6l%2C1; SRT=%1%enc%3AJW7DZaY9NB%2BWJXLSWenHLsbEhG9aR0Hqx5Gvqt6atM0mZ6JsJDQ%2BuUNnHrmvTMzGNox8JbUSTxk%3D; TASession=%1%V2ID.1590FCC829B9D057AA39169EFDF6CC5A*SQ.224*PR.40185%7C*LS.Restaurants*GR.77*TCPAR.97*TBR.47*EXEX.36*ABTR.71*PHTB.9*FS.61*CPU.45*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.A1556ED3B603A3395E2D968DD0C34799*LF.en*FA.1*DF.0*RT.0*TRA.false*LD.155019*EAU.J; TAUD=LA-1605325974315-1*RDD-1-2020_11_14*RD-533752846-2020_11_20.8319600*HDD-1078074234-2020_12_06.2020_12_07*LG-1228713658-2.1.F.*LD-1228713659-.....',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'referer': 'https://www.tripadvisor.com.sg/Restaurants-g155019-Toronto_Ontario.html',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-fetch-dest': 'empty',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors'
        }
        # page_view = 'https://www.tripadvisor.com.sg/RestaurantSearch-g155019-oa{}-a_geobroaden.false-Toronto_Ontario.html#EATERY_LIST_CONTENTS'.format(str(30*page))
        page_view = 'https://www.tripadvisor.com.sg/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=155019&itags=16556%2C9909%2C9900%2C9901%2C11776%2C16548&o=a{}'.format(str(30*page))
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

for page in range(35):
    get_urls_from(page)

url_df = pd.DataFrame(item_url_list)
url_df.to_csv('urls_TORONTO_etc1.csv')


#https://www.tripadvisor.com.sg/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=155019&itags=10591&o=a30

