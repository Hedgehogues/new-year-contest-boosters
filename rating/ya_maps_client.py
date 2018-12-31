import requests
from transliterate import translit

from rating.repl import replace, repl_en, repl_space_en, repl_lemmatics_en, repl_ru, repl_lemmatics_ru
from tqdm import tqdm


class Request:
    def __init__(self, addr, index):
        self.addr = addr
        self.index = index


class Response:
    def __init__(self, resp, index):
        self.resp = resp
        self.index = index


class YandexApiClient:

    def __init__(self, token=''):
        self.__token = token

    def __request(self, addr):
        return requests.get(
            'https://geocode-maps.yandex.ru/1.x/?format=json&apikey=%s&geocode=%s' % (self.__token, addr))

    def translit_geocode_i(self, addr):
        if addr is None:
            return None
        addr = ' ' + addr + ' '
        addr = replace(addr, repl_en)
        addr = replace(addr, repl_space_en)
        addr = replace(addr, repl_lemmatics_en)
        addr = translit(addr, 'ru')
        addr = replace(addr, repl_ru)
        addr = replace(addr, repl_lemmatics_ru)
        addr = replace(addr, repl_ru)
        return self.__request(addr)

    def geocode_i(self, addr):
        if addr is None:
            return None
        return self.__request(addr.upper())

    def translit_geocode(self, reqs):
        resps = []
        for req in tqdm(reqs, total=len(reqs)):
            resp = self.translit_geocode_i(req.addr)
            resps.append(Response(resp, req.index))
        return resps

    def geocode(self, reqs):
        resps = []
        for req in tqdm(reqs, total=len(reqs)):
            resp = self.geocode_i(req.addr)
            resps.append(Response(resp, req.index))
        return resps
