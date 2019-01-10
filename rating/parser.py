from rating.repl import repl_not_valid_city_and_country, replace, repl_en, repl_shorts_en
from rating.ya_maps_client import Request
from postal.parser import parse_address as libpostal_parser_address
from rating.utils import get_city_


class InvalidAddressCityParser:
    def parse(self, addrs):
        reqs = []
        for addr in addrs:
            if addr is not None:
                reqs.append(Request('Россия, ' + get_city_(addr.sturct_en), addr.index))
                continue
            reqs.append(Request(None, None))
        return reqs


class InvalidAddressesLibpostalParser:
    __tags_for_sort = dict([
        ('state_district', -300),
        ('country', -200),
        ('city_district', -100),
        ('city', 0),
        ('state', 100),
        ('suburb', 200),
        ('road', 300),
        ('postcode', 400),
        ('house', 500),
        ('house_number', 600),
        ('unit', 700),
    ])

    def __sort(self, items):
        n = len(items)
        for i, item in enumerate(items):
            items[i] = (item[0], self.__tags_for_sort[item[1]] + n - i - 1)
        return items

    def __build_address_by_tags(self, struct_addrs):
        reqs = []
        for i, items in enumerate(struct_addrs):
            if items is None:
                reqs.append(None)
                continue
            self.__sort(items)
            req = [item[0] for item in sorted(items, key=lambda el: el[1])]
            if len(req) == 0:
                reqs.append('fake_address_aisud88zux89cua0skdpkapookcpozkxc90iais09i')
                return
            reqs.append(', '.join(req))
        return reqs

    def __apply_replaces_shorts(self, addr):
        addr = ' ' + addr + ' '
        addr = replace(addr, repl_en)
        addr = replace(addr, repl_shorts_en)
        return addr

    def __get_struct_addrs(self, addrs):
        struct_addrs = []
        inds = []
        for addr in addrs:
            if addr is None:
                struct_addrs.append(None)
                inds.append(None)
                continue
            new_addr = self.__apply_replaces_shorts(addr.query_en)
            new_addr = new_addr.upper()
            answ = libpostal_parser_address(new_addr)
            struct_addrs.append(answ)
            inds.append(addr.index)
        return struct_addrs, inds

    def parse(self, addrs):
        struct_addrs, inds = self.__get_struct_addrs(addrs)
        addrs = self.__build_address_by_tags(struct_addrs)
        reqs = []
        for addr, ind in zip(addrs, inds):
            addr = addr.upper() if addr is not None else addr
            new_addr = replace(addr, repl_not_valid_city_and_country)
            reqs.append(Request(new_addr, ind))
        return reqs
