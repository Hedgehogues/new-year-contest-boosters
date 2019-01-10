import time
import json
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
import requests


def get_objects_list(id_list):
    data = '{"jsonrpc":"2.0","method":"bank/getBankObjectsData","params":{"id_list":[%s]},"id":"3"}' % ','.join(map(str, id_list))
    url = 'https://www.banki.ru/api/'
    params = {'content-length': len(data)}
    objs_list = requests.post(url, data=data, params=params)
    return objs_list.json()


path = 'data/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

ids = []
for file in onlyfiles:
    j = json.load(open(path + file))
    for item in j:
        ids.append(item['id'])


path_to_data = './data/'
step = 500
for j, i in tqdm(enumerate(range(0, len(ids), step)), total=len(ids)//step+1):
    cur_ids = ids[i:i+step]
    if j < 277:
        continue
    desc = get_objects_list(cur_ids)
    desc = desc['result']['data']

    with open('desc/%d.json' % j, 'w') as outfile:
        json.dump(desc, outfile)
    time.sleep(1.5)

