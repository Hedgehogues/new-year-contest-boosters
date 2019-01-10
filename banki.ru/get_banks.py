import json
import time

import tqdm

import requests


def get_regions_list():
    params = {
        'cookie': 'PHPSESSID=23f57bf601dffa5868d06586ed01f458; BANKI_RU_USER_IDENTITY_UID=3213121084713848811; user-region-id=4; aff_sub3=%2Fbanks%2Fmap%2Fmoskva_i_oblast%7E%2Fdolgoprudnyiy%2F; uid=uQo9b1wf114dE0DLMoNVAg==; __utmc=241422353; __utmz=241422353.1545590623.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=241422353.|1=siteDesign=new=1; _ga=GA1.2.172985365.1545590623; _gid=GA1.2.444194788.1545590624; _ym_uid=1545590624847364883; _ym_d=1545590624; scs=%7B%22t%22%3A1%7D; ga_client_id=172985365.1545590623; BANKI_RU_GUEST_ID=604738954; _ym_isad=2; flocktory-uuid=05e5408a-1759-44a5-bfb8-a60ac5990fbf-3; ins-mig-done=1; spUID=15455906245263c4ed73e3e.560b79a7; _fbp=fb.1.1545590624654.204411224; __gads=ID=160ee29e8534ca40:T=1545590625:S=ALNI_MZgeW4ox5e8hyvgH7zgNxhFl9AEvQ; FullScreenZenit=true; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2018-12-23%2021%3A44%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.banki.ru%2Fbanks%2Fmap%2Fmoskva_i_oblast%7E%2Fdolgoprudnyiy%2F%23%2F%21b1%3Aall%21s3%3Aoffice%21s4%3Alist%21m4%3A1%21p1%3A1%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2018-12-23%2021%3A44%3A00%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.banki.ru%2Fbanks%2Fmap%2Fmoskva_i_oblast%7E%2Fdolgoprudnyiy%2F%23%2F%21b1%3Aall%21s3%3Aoffice%21s4%3Alist%21m4%3A1%21p1%3A1%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; lp_vid=1e1902bf-84da-4873-29db-fd8772fe752f; lp_abtests=[]; decid_png=1259851644; decid_etag=1259851644; decid_cache=1259851644; DEC_ID=1259851644; __utma=241422353.172985365.1545590623.1545590623.1545597861.2; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F70.0.3538.77%20Safari%2F537.36; BANKI_RU_LAST_VISIT=23.12.2018+23%3A44%3A21; insdrSV=3; BANKI_RU_BANNERS=318_22844_1_24122018%2C106_797_1_24122018%2C106_809_2_24122018; bank_geo_link=#/!b1:all!s3:office!s4:list!m1:12!m2:55.9385709999935!m3:37.510142999999964!p1:1; tmr_detect=0%7C1545597863814; NonRobot=1545600494b0cfa72d161ee0169dd6b1d4ad2ead51581+50ce993fbaddab32f67e334b4f8978be',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'cache-control': 'max-age=0',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    url = 'https://www.banki.ru/bitrix/components/banks/universal.select.region/ajax.php?type=city'
    region_list = requests.get(url, params=params)
    return region_list.json()


def get_objects_list(region_id, limit, offset=0):
    data = '{"jsonrpc":"2.0","method":"bankGeo/getObjectsByFilter","params":{"with_empty_coordinates":true,"offset":%d , "limit":%d,"type":["office","branch","atm","cash","self_office"],"region_id":[%d]},"id":"2"}' % (offset, limit, region_id)
    url = 'https://www.banki.ru/api/'
    params = {'content-length': len(data)}
    objs_list = requests.post(url, data=data, params=params)
    return objs_list.json()


path_to_data = './data/'
limit = 3000
resp_regions = get_regions_list()
for i, region in tqdm.tqdm(enumerate(resp_regions['data']), total=len(resp_regions['data'])):
    if i < 8882:
        continue

    json_path = '%s%d-%s.json' % (path_to_data, i, region['region_name'])
    offset_step = 0
    resps = []
    while True:
        resp_objs = get_objects_list(region['id'], limit, offset_step)
        offset_step += limit
        resps += resp_objs['result']['data']
        if resp_objs['result']['limit'] + resp_objs['result']['offset'] > resp_objs['result']['total']:
            break
    with open(json_path, 'w') as outfile:
        json.dump(resps, outfile)
    time.sleep(1)

