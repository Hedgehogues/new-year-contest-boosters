repl_shorts_en = {
    ' PR-KT ': ' ,pr-kt. ',
    ' PR-KT.': ' ,pr-kt. ',

    ' KORP.': ' ,korp. ',
    ' KORP ': ' ,korp. ',

    ' PER.': ' ,per. ',
    ' PER ': ' ,per. ',
    ' NAB ': ' nab., ',
    ' NAB.': ' nab., ',
    ' H/W.': ' sh., ',
    ' H/W ': ' sh., ',
    ' H-W.': ' sh., ',
    ' H-W ': ' sh., ',
    ' AVE.': ' ,ul. ',
    ' AVE ': ' ,ul. ',
    ' B-R.': ' bul. ',
    ' B-R ': ' bul.',
    ' MKR.': ' mkr. ',
    ' MKR ': ' mkr. ',
    ' STR.': ' ,ul. ',
    ' STR ': ' ,ul. ',
    ' LIT.': ' ,litera ',
    ' LIT ': ' ,litera ',

    ' PR ': ' ,pr-kt. ',
    ' PR.': ' ,pr-kt. ',
    ' AV.': ' ,ul. ',
    ' AV ': ' ,ul. ',
    ' PL.': ' ,ploshad` ',
    ' PL ': ' ,ploshad` ',
    ' BR.': ' bul. ',
    ' BR ': ' bul. ',
    ' SH.': ' sh., ',
    ' SH ': ' sh., ',
    ' ST.': ' ul. ',
    ' ST ': ' ul. ',
    ' UL ': ' ul. ',
    ' UL.': ' ul. ',

    ' G.': ' ,g. ',
    ' G ': ' ,g. ',
    ' D.': ' ,dom. ',
    ' D ': ' ,dom. ',
    ' B ': ' bul. ',
    ' B.': ' bul. ',
}.items()
repl_space_en = {
    '.': ' ',
    ',': ' ',
    ' PER ': ' ',
    ' NAB ': ' ',
    ' H/W ': ' ',
    ' PR-KT ': ' ',
    'LIT': ' ',
    ' V ': ' ',
    ' ST ': ' ',
    ' D ': ' ',
    ' UL ': ' ',
    ' R ': ' ',
    ' AV ': ' ',
    ' AVE ': ' ',
    ' STR ': ' ',
    ' G ': ' ',
    ' P ': ' ',
    ' KR ': ' ',
    ' PL ': ' '
}.items()
repl_lemmatics_en = {
    'SHCH': 'Щ',

    'JA': 'Я',
    'AY': 'АЙ',
    'ZH': 'Ж',
    'IJ': 'ИЙ',
    'CH': 'Ч',
    'YU': 'Ю',
    'OY': 'ОЙ',
    'SH': 'Ш',
    'UB': 'ЮБ',

    'J': 'Ж',
}.items()
repl_en = {
    'UL. VOKZALNAJA MAGI       NOVOSIBIRSK': ",NOVOSIBIRSK, VOKZAL'NAYA MAGISTRAL', ",
    '16 B.SEMENOVSKAYA': ", BOL'SHAYA SEMENOVSKAYA, 16, ",
    '14/2 BUMAZHNIY': ',BUMAJNIY PROEZD, DOM 14/2,',
    '63A IZMAYLOVSKIY AV.': ',IZMAYLOVSKIJ BULVAR, DOM. 63А, ',
    '133A MOZHAYSKOE H/W.      MOSCOW': ',MOZAYSKOE SHOSSE, DOM. 133A, ',
    'MOSCOW': 'MOSKVA, ',
    'TOGLIATTI': "TOL'YATTI, ",
}.items()


repl_lemmatics_ru = {
    'НЫ ': 'НИЙ ',
    'ЦХ': 'Ч',
    'ИЫ': 'ИЙ',
    'ЫА': 'Я',
    'ЕЫ': 'ЕЙ',
    'KH': 'Х',
}.items()
repl_ru = {
    'БЛВД': 'БУЛЬВАР',
    'ГЮБКИН': 'ГУБКИН',
    'ФАВОРС': 'ФАВОРСКОГО',
    'КОММУНИСТИЧ': 'КОММУНИСТИЧЕСКАЯ',
    'КОРАБЛЕСТРО': 'КОРАБЛЕСТРОИТЕЛЕЙ',
    'РОСТОВ-НА-ДО': 'РОСТОВ-НА-ДОНУ',
    'АЛТЫФ': 'АЛТУФЬЕВСКОЕ',
    'НАРО': 'НАРОДОВ',
    'ЦЕМЗАВО': 'ЦЕМЗАВОДА',
    'БЕЛГОРОД. ПОЛКА-34': 'БЕЛГОРОДСКОГО ПОЛКА, 34',
    'РАБОЧЕГО ШТА': 'РАБОЧЕГО ШТАБА',
    'ИНТЕРНАТСОИН': 'ИНТЕРНАЦИОНАЛЬНЫЙ',
    'ГЕР. ТИХООКЕАН': 'ГЕРОЕВ-ТИХООКЕАНЦЕВ УЛИЦА',
    'ХО ЩИ МИХН': 'ХО ШИ МИНЬ',
}.items()


repl_not_valid_city_and_country = {
    'NAB. SEREBRYANICHE MOSKVA G., DOM. 29': 'Москва, Серебряническая набережная, д. 29',
    'MKR. PERVOMAISKII IRKUTSK G., DOM. 23': 'Иркутск, Микрорайон первомайский, д. 23',
    'UL. INTERNACIONAL TAMBOV G., DOM. 16A': 'Тамбов, ул. Интернациональная, д. 16А',
    'MKR. UBILEINYI IRKUTSK G., DOM. 19/1': 'Иркутск, Микрорайон Юбилейный, д. 19/1',
    'MKR. UBILEINYI IRKUTSK G., DOM. 13/1': 'Иркутск, Микрорайон Юбилейный, д. 19/1',
    'V PER. 4-I V PARGOLOVO P, DOM. 19, LITERA': 'ПАРГОЛОВО, дом 19',
    'PR-KT. KOMMUNISTICH YUZHNO-SAKHA, DOM. 33': 'Южно-сахалинск, Коммунистический проспект, дом. 33',
    'UL. BABUSH SANKT-PETERB, DOM. 10, LITERA A': 'Санкт-Петербург, улица Бабушкина, дом 10, литера А',
    'AVIAITSIONNAYA, KOMSOMOLSK-31, 12': 'fake_address_aisud88zux89cua0skdpkapookcpozkxc90iais09i',
    'SCHERTSA UL. BELGOROD, 64': 'Белгород, улица Щорса, дом 64',
    'UL. KRASNOARMEISK BLAGOVESHCHE, DOM. 123': 'Благовещенск, улица кросноармейская, дом 64',
    "SARAPUL G., DOM. 142V UL. RASKOL'NIKOV": 'Сарапул, улица раскольникова, дом 142В',
    'S. MAYA, SOVETSKAYA, 25': 'fake_address_aisud88zux89cua0skdpkapookcpozkxc90iais09i',
    'UL. GEROEV STALIN YOSHKAR-OLA, DOM. 35V': 'Йошкорола, улица Героев сталинистев, дом 35В',
    'KRASNOARMEI SANKT-PETERB, UL., 10, DOM. 22': 'Санкт-Петербург, 10 красноармейская улица, дом 22',
    "UL. BOL'SHAYA MORS SANKT-PETERB, DOM. 30": 'Санкт-Петербург, большая морская улица, дом 30',
    "UL. KUTUZOVA VOLOGDA, 20 N": 'Вологда-20, улица Кутозова',
    "UL. BOL'SHAYA YAROSLAVL G., DOM. 118/11": 'Большая Октябрьская улица, 118/11, Ярославль, Россия, 150014',
    "E UL. SOBINO PENZA G., KORP., DOM. 7": 'Пенза, улица Собинова, 7',
    "PR-KT. TRAKTOROSTRO CHEBOXARY G., DOM. 76": 'проспект Тракторостроителей, 76, Чебоксары, Чувашская Республика, Россия',
    "UNKNOWN DZERZHINSK G.": 'Дзержинск',
    "PR-KT. MASHINOSTROI YAROSLAVL G., DOM. 22": 'проспект Машиностроителей, 22, Ярославль, Россия, 150051'
}.items()


def replace(addr, r):
    if addr is None:
        return None
    for item in r:
        addr = addr.replace(item[0], item[1])
    return addr
