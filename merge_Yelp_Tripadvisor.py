# -*- coding: utf-8 -*-

import pandas as pd
import unidecode
import numpy as np
from math import *
import math

df_trip = pd.read_excel('Tripadviser_Toronto.xls')
df_trip.head()
#df_trip = df_trip[df_trip.review_count > 0]
df_trip['name'] = df_trip['name'].str.rstrip(', Canada').str.lower().str.replace(' - ','-')
df_trip['id'] = range(1,len(df_trip)+1)
df_trip['trip_coord'] = df_trip[['lat','lng']].values.tolist()
df_trip['trip_freq'] = df_trip['name'].map(df_trip['name'].value_counts())
df_trip = df_trip.reset_index(drop=True)

df_yelp = pd.read_json('yelp_academic_dataset_business.json', lines = True)
df_yelp['name'] = df_yelp['name'].apply(unidecode.unidecode).str.lower().str.replace(' - ','-')
df_yelp = df_yelp[df_yelp.city == 'Toronto']
df_yelp = df_yelp[df_yelp.is_open == 1]
df_yelp['yelp_coord'] = df_yelp[['latitude','longitude']].values.tolist()
df_yelp['yelp_freq'] = df_yelp['name'].map(df_yelp['name'].value_counts())
df_yelp = df_yelp.reset_index(drop=True)

# count the matchings of restaurants' names in yelp dataset
df_trip['store_count'] = df_trip['name'].map(df_yelp['name'].value_counts())

## compute the threshold for distance
restaurant_1to1 = pd.merge(df_trip[df_trip.store_count == 1],df_yelp[df_yelp.yelp_freq == 1],left_on='name',right_on='name')

def compute_dist(df):
    return np.sqrt((df['lat']-df['latitude'])**2 + (df['lng']-df['longitude'])**2)
restaurant_1to1['dist'] = restaurant_1to1.apply(compute_dist, axis=1)
thr = restaurant_1to1['dist'].quantile(0.89) # 89% percentile as threshold

# compute the distance of two locations
def distance_1o1(loc1,loc2):
    return np.sqrt(pow(loc1[0]-loc2[0],2)+pow(loc1[1]-loc2[1],2))

# return the index of the closest among the n yelp stores
def match_1oN(trip_id,yelp_busi_id):  # input the ids of the stores in trip and yelp
    if yelp_busi_id == []:
        return float("nan")
    elif len(yelp_busi_id) == 1:
        return yelp_busi_id[0]
    else:
        dis = [distance_1o1(
                list(df_trip.trip_coord[df_trip.id == trip_id])[0], 
                list(df_yelp.yelp_coord[df_yelp.business_id == j])[0]
                ) for j in yelp_busi_id]
        min_dis = min(dis)
        if min_dis <= thr:
            return yelp_busi_id[dis.index(min_dis)]
        else:
            return float("nan")
    

# return the index of the best match among all the trip stores
def match_No1(trip_id,yelp_busi_id):
    dis = [distance_1o1(
            list(df_trip.trip_coord[df_trip.id == i])[0],
            list(df_yelp.yelp_coord[df_yelp.business_id == yelp_busi_id])[0]
            ) for i in trip_id]
    return trip_id[dis.index(min(dis))]


# find the candidates of each store
pools = df_yelp['name'].to_list()
id_pools = df_yelp['business_id'].to_list()

def matching_id(x):
    idx_list = [i for i in range(len(pools)) if x['name'] in pools[i]]
    business_id = [id_pools[i] for i in idx_list]
    return business_id

df_trip['candidates'] = df_trip.apply(lambda x: matching_id(x), axis=1)

# find the match for all stores on tripadvisor
df_trip['match_yelp'] = [match_1oN(k,df_trip.candidates[k-1]) for k in df_trip.id]

# find the best match for all yelp stores that is the match for at least one trip store
dict_match = {}
for i in [x for x in df_trip.match_yelp if pd.isnull(x)==False]:
    dict_match[i] = match_No1(list(df_trip[df_trip.match_yelp == i].id),i)

# construct an "id key" for trip data based on dict_match
trip_id = []
for i in range(len(df_yelp)):
    if df_yelp.business_id[i] in dict_match.keys():
        trip_id.append(dict_match[df_yelp.business_id[i]])
    else:
        trip_id.append(float("nan"))
        
df_yelp['trip_id'] = trip_id



################################################
#### repeat the matching procedure on yelp data

# return the index of the closest among the n trip stores
def match_1oN_yelp(yelp_busi_id, trip_id):  # input the ids of the stores in trip and yelp
    if trip_id == []:
        return float("nan")
    elif len(trip_id) == 1:
        return trip_id[0]
    else:
        dis = [distance_1o1(
                list(df_yelp.yelp_coord[df_yelp.business_id == yelp_busi_id])[0], 
                list(df_trip.trip_coord[df_trip.id == j])[0]
                ) for j in trip_id]
        min_dis = min(dis)
        if min_dis <= thr:
            return trip_id[dis.index(min_dis)]
        else:
            return float("nan")

# find the candidates of each store
pools = df_trip['name'].to_list()
id_pools = df_trip['id'].to_list()
df_yelp['candidates'] = df_yelp.apply(lambda x: matching_id(x), axis=1)

# find the match for all stores on tripadvisor
df_yelp['match_trip'] = df_yelp.apply(lambda x: match_1oN_yelp(x['business_id'], x['candidates']), axis=1)
df_yelp.match_trip.fillna(df_yelp.trip_id, inplace=True)

def match_No1_yelp(yelp_busi_id,trip_id):
    dis = [distance_1o1(
            list(df_yelp.yelp_coord[df_yelp.business_id == i])[0],
            list(df_trip.trip_coord[df_trip.id == trip_id])[0]
            ) for i in yelp_busi_id]
    return yelp_busi_id[dis.index(min(dis))]

# find the best match for all trip stores that is the match for at least one yelp store
dict_match = {}
for i in [x for x in df_yelp.match_trip if pd.isnull(x)==False]:
    dict_match[i] = match_No1_yelp(list(df_yelp[df_yelp.match_trip == i].business_id),i)

dict_match = dict([(value, key) for key, value in dict_match.items()]) 
# construct an "id key" for trip data based on dict_match
match_trip = []
for i in range(len(df_yelp)):
    if df_yelp.business_id[i] in dict_match.keys():
        match_trip.append(dict_match[df_yelp.business_id[i]])
    else:
        match_trip.append(float("nan"))
        
df_yelp['match_trip'] = match_trip
df_yelp = df_yelp.drop(['trip_id','candidates'], axis=1)
df_trip = df_trip.drop(['candidates'], axis=1)

df_yelp.to_csv('matched_yelp_business.csv',encoding='utf_8_sig')


# merge the two dataset on id and match_trip
yelp_all = pd.read_csv('yelp_data.csv',encoding='gb18030')
yelp_all = yelp_all.merge(pd.DataFrame(df_yelp[['business_id','match_trip']]),on='business_id')
# keep only the yelp stores that have match in trip
yelp_trip = yelp_all[pd.isna(yelp_all.match_trip)==False]
# merging!
yelp_trip = yelp_trip.merge(df_trip, left_on='match_trip', right_on='id')
yelp_trip.to_csv('yelp_trip.csv', encoding='utf_8_sig')








