from rating.address import Address
from rating.enums import Languages
from rating.utils import is_contain_number_, get_house_, is_valid_country_, is_valid_city_, is_valid_house_, \
    is_valid_street_, get_city_
from postal.parser import parse_address as libpostal_parser_address


class StructValidator:
    def __init__(self):
        self.invalid_addresses = []
        self.valid_addresses = []

    def __set_parsed_resp(self, valid, invalid):
        self.valid_addresses.append(valid)
        self.invalid_addresses.append(invalid)

    def __match_ru_en(self, addr):
        is_one_substr_other = addr.full_addr_en.find(addr.full_addr_ru) != -1 or addr.full_addr_ru.find(
            addr.full_addr_en) != -1
        # AND
        is_valid_country = is_valid_country_(addr.sturct_ru) and is_valid_country_(addr.sturct_en)
        is_valid_city = is_valid_city_(addr.sturct_ru) and is_valid_city_(addr.sturct_en)
        # OR
        is_valid_street = is_valid_street_(addr.sturct_ru) or is_valid_street_(addr.sturct_en)
        is_valid_house = is_valid_house_(addr.sturct_ru) or is_valid_house_(addr.sturct_en)

        is_valid_structs = is_valid_country and is_valid_city and is_valid_street and is_valid_house
        return is_one_substr_other and is_valid_structs

    def __get_lang(self, addr):
        is_matched = self.__match_ru_en(addr)
        if is_matched and addr.full_addr_en.find(addr.full_addr_ru) != -1:
            return Languages.EN
        if is_matched and addr.full_addr_ru.find(addr.full_addr_en) != -1:
            return Languages.RU
        return Languages.NULL

    def __validate(self, addr):
        addr.best_lang = self.__get_lang(addr)
        if len(addr.full_addr_en) == 0 and len(addr.full_addr_ru) == 0:
            self.__set_parsed_resp(None, addr)
            return
        if addr.best_lang == Languages.NULL:
            self.__set_parsed_resp(None, addr)
            return
        self.__set_parsed_resp(addr, None)

    def validate(self, addrs):
        for i, addr in enumerate(addrs):
            if addr is None or not addr.is_valid:
                self.__set_parsed_resp(None, None)
                continue
            self.__validate(addr)


class HouseValidator:
    def __init__(self):
        self.invalid_addresses = []
        self.valid_addresses = []

    def __set_parsed_resp(self, valid, invalid):
        self.valid_addresses.append(valid)
        self.invalid_addresses.append(invalid)

    def __validate_houses(self, houses):
        house_en, house_ru, house_query_en, house_query_ru = houses
        if len(house_en) == 1 and len(house_ru) == 0 and (
                house_en == house_query_en or house_en == house_query_ru):
            return Languages.EN
        if len(house_en) == 0 and len(house_ru) == 1 and (
                house_ru == house_query_en or house_ru == house_query_ru):
            return Languages.RU
        if house_en == house_ru == house_query_en or house_en == house_ru == house_query_ru:
            return Languages.BOTH
        return Languages.NULL

    def __get_lang(self, addr):
        house_query_en = get_house_(libpostal_parser_address(addr.query_en))
        house_query_ru = get_house_(libpostal_parser_address(addr.query_ru))
        house_en = get_house_(libpostal_parser_address(addr.full_addr_en))
        house_ru = get_house_(libpostal_parser_address(addr.full_addr_ru))
        city_en = get_city_(addr.sturct_en)
        city_ru = get_city_(addr.sturct_ru)

        is_valid_city = city_en == city_ru
        is_multi_houses = len(house_en) > 1 or len(house_ru) > 1
        is_empty_req_house = len(house_query_en) == 0

        if is_multi_houses or is_empty_req_house or not is_valid_city:
            return Languages.NULL

        houses = (house_en, house_ru, house_query_en, house_query_ru)
        lang = self.__validate_houses(houses)

        return lang

    def __validate(self, addr):
        en_contain_num = is_contain_number_(addr.full_addr_en)
        ru_contain_num = is_contain_number_(addr.full_addr_ru)
        if not (en_contain_num or ru_contain_num):
            self.__set_parsed_resp(None, addr)
            return
        addr.best_lang = self.__get_lang(addr)
        if addr.best_lang != Languages.NULL:
            self.__set_parsed_resp(addr, None)
            return
        self.__set_parsed_resp(None, addr)

    def validate(self, addrs):
        for i, addr in enumerate(addrs):
            if addr is None or not addr.is_valid:
                self.__set_parsed_resp(None, None)
                continue
            self.__validate(addr)


def union_addresses(addrs1, addrs2):
    addrs = []
    for i, addr in enumerate(zip(addrs1, addrs2)):
        addr1, addr2 = addr[0], addr[1]
        if addr1 is not None and addr2 is not None:
            raise Exception("Both addr is NOT None" % i)
        if addr1 is not None:
            addrs.append(addr1)
            continue
        if addr2 is not None:
            addrs.append(addr2)
            continue
        addrs.append(None)
    return addrs


def extract_addresses(resps_en, resps_ru, is_log=True):
    addrs = [Address(item[0], item[1]) for item in zip(resps_en, resps_ru)]

    struct_validator = StructValidator()
    struct_validator.validate(addrs)

    house_validator = HouseValidator()
    house_validator.validate(struct_validator.invalid_addresses)

    valid_addresses = union_addresses(house_validator.valid_addresses, struct_validator.valid_addresses)
    invalid_addresses = house_validator.invalid_addresses

    if is_log:
        valid = len([el for el in valid_addresses if el is not None])
        invalid = len([el for el in invalid_addresses if el is not None])
        print('Valid: %d. Invalid: %d.' % (valid, invalid))
    return valid_addresses, invalid_addresses
