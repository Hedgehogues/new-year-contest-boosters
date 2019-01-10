import re
from copy import deepcopy

import numpy as np
import requests


header = {
    'Cookie': 'yandexuid=295134901546943449; i=jeiDQItMxS3EPevhuUK9goGrpF5PNnDqQLrWnKzpJSOH95J73PxPkm1BKQgDy2Cql4n8uNtu0qB9NPAu/4njumXI4ek=',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept-Encoding': 'gzip',
    'Cache-Control': "no-cache",
}
query_string = {
    "origin": "maps-location",
    "results": "200",
}
url = "https://yandex.ru/maps/api/search"


def get_biz(lat, long, query_string):
    sep = ','
    q = query_string
    q["ll"] = str(lat) + sep + str(long)
    q["type"] = "biz"
    q["mode"] = "reverse"
    q["snippets"] = 'masstransit/2.x,businessrating/1.x,'
    q['business_show_closed'] = 0
    region_list = requests.request('GET', url, headers=header, params=q)
    return region_list.json()


def get_latlong(text, url, query_string):
    q = deepcopy(query_string)
    q["text"] = text
    region_list = requests.request('GET', url, headers=header, params=q)
    return region_list.json()


def extract_data(items):
    metros = []
    stops = []
    scores = []
    counts = []
    categories = []
    for item in items:
        if 'rating' in item and 'score' in item['rating']:
            scores.append(item['rating']['score'])
        else:
            scores.append(0)
        if 'rating' in item and 'count' in item['rating']:
            counts.append(item['rating']['count'])
        else:
            counts.append(0)
        if 'metro' in item and len(item['metro']) != 0:
            metros.append(int(re.findall('\d+', item['metro'][0]['distance'])[0]))
        else:
            metros.append(0)
        if 'stops' in item and len(item['stops']) != 0:
            stops.append(int(re.findall('\d+', item['stops'][0]['distance'])[0]))
        else:
            stops.append(0)
        if 'categories' in item and len(item['categories']) != 0:
            if 'class' in item['categories'][0]:
                categories.append(item['categories'][0]['class'])
            else:
                categories.append('None')
        else:
            categories.append('None')
    return np.mean(metros), np.mean(stops), list(zip(scores, counts, categories))


def get_items(text, csfr_token="286ae639798f7d0adc9d7a1f496f83fa57a9612e:1547121538604"):
    q = deepcopy(query_string)
    q['csrfToken'] = csfr_token
    resp = get_latlong(text, url, q)
    lat, long = resp['data']['items'][0]['coordinates']
    resp = get_biz(lat, long, q)
    return extract_data(resp['data']['items'])


# print(get_items(''))
# print(get_items('Гвардейская площадь, 2, Норильск, Красноярский край, Россия, 663302'))
