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
    'ХО ЩИ МИХН': 'ХО ШИ МИНЬ',
}.items()


def replace(addr, r):
    if addr is None:
        return None
    for item in r:
        addr = addr.replace(item[0], item[1])
    return addr
