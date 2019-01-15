# Новогодний контест Boosters от Росбанка

Happy Data Year - новогодний чемпионат по анализу данных от Росбанка.

В обучающей выборке находятся данные о геопозиции шести тысяч банкоматов Росбанка и его партнеров, а также целевая переменная — индекс популярности банкомата. В тестовой выборке еще две с половиной тысячи банкоматов, разделенных поровну на публичную и приватную часть.

https://boosters.pro/champ_21

В данных, очевидно, есть пропуски. Часть из этих пропусков восстановлена при помощи YandexMapsApi, с использованием геокодера. В данном репозитории находится бенчмарк, предложенный организаторами boosters. Отличие от предложенного состоит в том, что часть адресов получена при помощи геокодера Yandex.

Восстановление адресов происходит с валидацией. Для этого используется транслитерация (ответ геокодера с и без транслитерации должны совпадать). Проверяется наличие домов. Если валидация по данным критериям не проходит, тогда координаты заполняются нулями

## Описание файлов

* banki.ru/ -- данные о банкоматах, полученные с портала banki.ru с помощью скрытого API
* baseline.ipynb -- ноутбук, выполнение которого позволяет получить data/submit.csv. Здесь также есть небольшой ресерч + CV
* baseline_boosters.ipynb -- исходный бейзлайн от boosters.pro
* data/ -- исходные данные от boosters.pro + пропущенные координаты, полученные в рамках ноутбука get_bad_addresses.ipynb. Здесь также находится файл с информацией о городах и населении в них, который выложила участница Александра Журавская.
* best_baseline.ipynb -- лучшее решение
* get_bad_addresses.ipynb -- получение координат с помощью геокодера яндекса (обкачка + подготовка). Сохраняет результаты работы в missed_coords.csv Реализация парсера лежит в ratings/
* get_yandex_ratings.ipynb -- получение рейтингов с помощью скрытого API яндекса. Реализация парсера лежит в yandex/. Здесь же лежат и данные с Яндекса.
* 1.png -- важность фичей по lgbm
* Happy Data Year.rar -- решение Александры Журавской

## Yandex геокодер

## Banki.ru parser

На сайте banki.ru нет открытого API. Но как заверяют администраторы, есть скрытое API. Об этом говорят на форумах. Его легко ракопать. Оно доступно без ключей и дургих перлестей. Достаточно лишь создать сессию с помощью браузера и скопипастить хедер этой сессии в качестве заголовка для запросов. Это API можно выследить, если начать загружать различные регионы с банкоматами [здесь](https://www.banki.ru/banks/). 

Банкоматы можно выгружать по-разному:

* по регионам (краткое описание). Требуется задавать регион (все регионы можно получить соответствующим запросом), после чего для каждого региона следует запросить все банкоматы. В ряде регионов их много, поэтому запрашивать все сразу не получается. Это следует делать частями. Детали можно увидеть в banki.ru/get_banks.py. 
* по регионам (детальное описание). banki.ru/get_desc.py. Для построения признаков использовались данные, полученные при помощи этого скрипта.

В полученных данных есть время работы банкоматов, координаты (можно валидировать дополнительно координаты), логотипы, ссылки, активность банкомата и многое другое. Детальнее можно посмотреть сами данные в banki.ru/data/. Спешу отметить, что на этом api не исчерпывается и оттуда можно вытаскивать дополнительную информацию.

## Yandex hidden API parser

Карты яндекса также имеют скрытое API, помимо публичного. C его помощью можно вытаскивать различную информацию: рейтинги, типы зданий и т.п. Для того, чтобы это сделать сначала требуется геокодировать адрес. А после этого специальным запросом отправить его с параметром *type=biz*. В таком случае, будет получена ценная информация о текущем здании. Исследуя запросы, которые отправляются во время навигации по странице https://yandex.ru/maps/ наверняка можно вытащить и дополнительные запросы, которые также окажутся полезными. Важно, что помимо параметров запроса, на выдачу влияют и сниппеты, которые указываются в заголовке. Детали можно увидеть в коде yandex/get_yandex_ratings.py. Здесь же лежат и данные. Каждый файл описывает соответствующую точку из набора предоставленных банкоматов в соответсвующем порядке.

Важно. Скорее всего, для того, чтобы парсер работал, Вам понадобится csrf-token и открытый браузер. csrf-token можно получить, если сделать запрос какого-нибудь адреса на странице яндекс карт. В заголовке Вы его увидите.

## Требования

Внимание! Требуется установка пакета [libpostal](https://github.com/openvenues/libpostal) (ставится из исходников) и [транслитератора](https://github.com/barseghyanartur/transliterate), помимо стандартных вещей sklearn, numpy, xgboost, lightgbm и т.п.

# New Year Contest Boosters from Rosbank

Happy Data Year - New Year's data analysis championship from Rosbank.

The training sample contains data on the geo-location of six thousand ATMs of Rosbank and its partners, as well as the target variable - the ATM popularity index. In the test sample, there are another two and a half thousand ATMs, equally divided into public and private parts.

https://boosters.pro/champ_21

There are obviously gaps in the data. Some of these permits were restored using YandexMapsApi, using a geocoder. In this repository is a benchmark, proposed by the organizers of boosters. The difference from the proposed one is that some of the addresses were obtained using the Yandex geocoder.

Restoration of addresses occurs with validation. For this, transliteration is used (the response of the geocoder with and without transliteration must be the same). Checks for availability of homes. If the validation of these criteria does not pass, then the coordinates are filled with zeros

Attention! Package installation is required [libpostal](https://github.com/openvenues/libpostal) (installed from source) and [transliterator](https://github.com/barseghyanartur/transliterate).
