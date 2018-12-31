def is_contain_number_(s):
    return any(c.isnumeric() for c in s)


def get_house_(struct):
    # libpostal
    houses = []
    for item in struct:
        if item[1] == 'house' or item[1] == 'house_number':
            houses.append(item[0])
    return houses


def get_city_(struct):
    # yandex api
    for item in struct:
        if item['kind'] == 'locality':
            return item['name']
    return ''


def is_valid_country_(struct):
    # yandex api
    for item in struct:
        if item['kind'] == 'country' and item['name'] != 'Россия':
            return False
    return True


def is_valid_city_(struct):
    # yandex api
    for item in struct:
        if item['kind'] == 'locality' or item['kind'] == 'province' and item['name'] == 'Москва':
            return True
    return False


def is_valid_street_(struct):
    # yandex api
    for item in struct:
        if item['kind'] == 'street':
            return True
    return False


def is_valid_house_(struct):
    # yandex api
    for item in struct:
        if item['kind'] == 'house' or item['kind'] == 'house_number':
            return True
    return False


def extract_struct_resp_addr_(resp):
    # GeoJson
    components = []
    data = resp['response']['GeoObjectCollection']['featureMember']
    if len(data) != 0:
        components = data[0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    return components


def extract_full_resp_addr_(resp):
    # GeoJson
    full_addr = ''
    data = resp['response']['GeoObjectCollection']['featureMember']
    if len(data) != 0:
        full_addr = data[0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    return full_addr


def extract_point_(resp):
    # GeoJson
    point = None
    data = resp['response']['GeoObjectCollection']['featureMember']
    if len(data) != 0:
        point = data[0]['GeoObject']['Point']['pos']
    return point


def extract_query_(resp):
    # GeoJson
    return resp['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['request']


def str_to_point(s):
    l = s.split(' ')
    return {'long': l[0], 'lat': l[1]}
