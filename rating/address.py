from rating import utils
from rating.enums import Languages
from rating.utils import extract_struct_resp_addr_, extract_full_resp_addr_, extract_query_, extract_point_


class Address:
    def __init__(self, item_en=None, item_ru=None):
        if item_en.index != item_ru.index:
            raise Exception("Indexies not equal. Index_en=%d. Index_ru=%d" % (item_en.index, item_ru.index))
        self.index = item_en.index

        resp_en, resp_ru = item_en.resp, item_ru.resp
        if resp_en is None or resp_ru is None:
            self.is_valid = False
            return

        if resp_en.status_code != 200 or resp_ru.status_code != 200:
            raise Exception("Parsing error %d" % self.index)

        j_en, j_ru = resp_en.json(), resp_ru.json()
        self.is_valid = True
        self.sturct_en = extract_struct_resp_addr_(j_en)
        self.sturct_ru = extract_struct_resp_addr_(j_ru)
        self.full_addr_en = extract_full_resp_addr_(j_en)
        self.full_addr_ru = extract_full_resp_addr_(j_ru)
        self.query_en = extract_query_(j_en)
        self.query_ru = extract_query_(j_ru)
        self.point_en = extract_point_(j_en)
        self.point_ru = extract_point_(j_ru)

        self.best_lang = Languages.NULL

    def get_best_coords(self):
        return utils.str_to_point(self.point_en) if self.best_lang == Languages.EN else utils.str_to_point(self.point_ru)
