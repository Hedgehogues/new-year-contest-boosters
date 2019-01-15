# Новогодний контест Boosters от Росбанка

Happy Data Year - новогодний чемпионат по анализу данных от Росбанка.

В обучающей выборке находятся данные о геопозиции шести тысяч банкоматов Росбанка и его партнеров, а также целевая переменная — индекс популярности банкомата. В тестовой выборке еще две с половиной тысячи банкоматов, разделенных поровну на публичную и приватную часть.

[Happy Data Year](https://boosters.pro/champ_21)

## Описание файлов

* [banki.ru/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/banki.ru) -- данные о банкоматах, полученные с портала [banki.ru](https://banki.ru) с помощью скрытого API
* [baseline.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/baseline.ipynb) -- ноутбук, выполнение которого позволяет получить [data/submit.csv](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/data/submit.csv). Здесь также есть небольшой ресерч + CV
* [baseline_boosters.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/baseline_boosters.ipynb) -- исходный бейзлайн от boosters.pro
* [data/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/data) -- исходные данные от boosters.pro + пропущенные координаты, полученные в рамках ноутбука [get_bad_addresses.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb). Здесь также находится файл с информацией о городах и населении в них, который выложила участница Александра Журавская.
* [best_baseline.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/best_baseline.ipynb) -- лучшее решение
* [get_bad_addresses.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb) -- получение координат с помощью геокодера яндекса (обкачка + подготовка). Сохраняет результаты работы в [missed_coords.csv](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/missed_coords.json) Реализация парсера лежит в [rating/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/rating)
* [get_yandex_ratings.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_yandex_ratings.ipynb) -- получение рейтингов с помощью скрытого API яндекса. Реализация парсера лежит в [yandex/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/yandex). Здесь же лежат и данные с Яндекса.
* [1.png](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/1.png) -- важность фичей по lgbm
* Happy Data Year.rar -- решение Александры Журавской

## Yandex геокодер

Геокодирование производилось двумя способами, которые матчатся друг с другом. Будем различать геокодирование 2х видов: на английском и на русском. 

Этап 1. Два вида геокодинга будем матчить. При транслитерации на русский будем заменять токены и даже слова. 
Этап 2. Валидация по стране, городу, улице и дому. И отдельно по дому. Если удалось произвести матчинг для русского и английского варианта геокодирования, то добавляем к ответу данный адресс.
Этап 3. С помощью libpostal восстанавливаем структуру тех адресов, которые не удалось распарсить на предыдущем шаге (дом, страна, улица и т.д.). Распологаем их в хронологическом порядке: страна, область, город, улица, дом.
Этап 4. Повторно отправляем запросы к геокодеру для адресов предыдущего шага.
Этап 5. Валидация по стране, городу, улице и дому. И отдельно по дому. Если удалось произвести матчинг для русского и английского варианта геокодирования, то добавляем к ответу данный адресс. (Повтор этапа 2)
Этап 6. Отбираем те адреса, у которых распознаны города хотя бы в одном случае и распознана страна как Россия

Детальнее можно посмотреть ноутбук [get_bad_addresses.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb), а также, реализацию парсеров [rating/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/rating).

## Banki.ru parser

На сайте banki.ru нет открытого API. Но как заверяют администраторы, есть скрытое API. Об этом говорят на форумах. Его легко ракопать. Оно доступно без ключей и дургих перлестей. Достаточно лишь создать сессию с помощью браузера и скопипастить хедер этой сессии в качестве заголовка для запросов. Это API можно выследить, если начать загружать различные регионы с банкоматами [здесь](https://www.banki.ru/banks/). 

Банкоматы можно выгружать по-разному:

* по регионам (краткое описание). Требуется задавать регион (все регионы можно получить соответствующим запросом), после чего для каждого региона следует запросить все банкоматы. В ряде регионов их много, поэтому запрашивать все сразу не получается. Это следует делать частями. Детали можно увидеть в [banki.ru/get_banks.py](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/banki.ru/get_banks.py). 
* по регионам (детальное описание). [banki.ru/get_desc.py](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/banki.ru/get_desc.py). Для построения признаков использовались данные, полученные при помощи этого скрипта.

В полученных данных есть время работы банкоматов, координаты (можно валидировать дополнительно координаты), логотипы, ссылки, активность банкомата и многое другое. Детальнее можно посмотреть сами данные в [banki.ru/data/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/banki.ru). Спешу отметить, что на этом api не исчерпывается и оттуда можно вытаскивать дополнительную информацию.

## Yandex hidden API parser

Карты яндекса также имеют скрытое API, помимо публичного. C его помощью можно вытаскивать различную информацию: рейтинги, типы зданий и т.п. Для того, чтобы это сделать сначала требуется геокодировать адрес. А после этого специальным запросом отправить его с параметром *type=biz*. В таком случае, будет получена ценная информация о текущем здании. Исследуя запросы, которые отправляются во время навигации по странице [Ya.Maps](https://yandex.ru/maps/) наверняка можно вытащить и дополнительные запросы, которые также окажутся полезными. Важно, что помимо параметров запроса, на выдачу влияют и сниппеты, которые указываются в заголовке. Детали можно увидеть в коде [yandex/get_yandex_ratings.py](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_yandex_ratings.ipynb). Здесь же лежат и данные. Каждый файл описывает соответствующую точку из набора предоставленных банкоматов в соответсвующем порядке.

Важно. Скорее всего, для того, чтобы парсер работал, Вам понадобится csrf-token и открытый браузер. csrf-token можно получить, если сделать запрос какого-нибудь адреса на странице яндекс карт. В заголовке Вы его увидите.

## Требования

Внимание! Требуется установка пакета [libpostal](https://github.com/openvenues/libpostal) (ставится из исходников) и [транслитератора](https://github.com/barseghyanartur/transliterate), помимо стандартных вещей sklearn, numpy, xgboost, lightgbm и т.п.

# New Year Contest Boosters from Rosbank

Happy Data Year - New Year's data analysis championship from Rosbank.

The training sample contains data on the geo-location of six thousand ATMs of Rosbank and its partners, as well as the target variable - the ATM popularity index. In the test sample, there are another two and a half thousand ATMs, equally divided into public and private parts.

[Happy Data Year](https://boosters.pro/champ_21)

## File Description

* [banki.ru/](http://hithub.com/Hedgehogues/new_year_contest_boosters/tree/master/banki.ru) - ATM data obtained from the [banki.ru](https://banki.ru) portal using a hidden API
* [baseline.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/baseline.ipynb) - a laptop that allows you to get [data/submit.csv](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/data/submit.csv). There is also a small survey + CV
* [baseline_boosters.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/baseline_boosters.ipynb) - source baseline from boosters.pro
* [data/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/data) - source data from boosters.pro + missing coordinates received within the notebook [get_bad_addresses.ipynb](https:// github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb). There is also a file with information about cities and the population in them, which is posted by the participant Alexandra Zhuravskaya.
* [best_baseline.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/best_baseline.ipynb) - the best solution
* [get_bad_addresses.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb) - obtaining coordinates using Yandex geocoder (rolling + preparation). Saves work results to [missed_coords.csv](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/missed_coords.json) The implementation of the parser lies in [rating/](https://github.com/Hedgehogues/new_year_contest_bo/tree/master/rating)
* [get_yandex_ratings.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_yandex_ratings.ipynb) - getting ratings using the hidden API of Yandex. The implementation of the parser is in [yandex/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/yandex). Here are the data from Yandex.
* [1.png](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/1.png) - the importance of features by lgbm
* Happy Data Year.rar - the decision of Alexandra Zhuravskaya

## Yandex geocoder

Geocoding was done in two ways, which are matched with each other. We will distinguish 2 types of geocoding: in English and in Russian.

Step 1. Two types of geocoding will match. When transliterating into Russian, we will replace tokens and even words.
Step 2. Validation of the country, city, street and house. And separately at home. If it was possible to make a match for the Russian and English versions of geocoding, then we add this address to the answer.
Step 3. Using libpostal, we restore the structure of those addresses that we could not parse in the previous step (house, country, street, etc.). We arrange them in chronological order: country, region, city, street, house.
Step 4. Resend requests to the geocoder for the addresses of the previous step.
Step 5. Validation of the country, city, street and house. And separately at home. If it was possible to make a match for the Russian and English versions of geocoding, then we add this address to the answer. (Repeat Stage 2)
Step 6. We select those addresses in which cities were recognized at least in one case and the country is recognized as Russia

You can see the laptop [get_bad_addresses.ipynb](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/get_bad_addresses.ipynb) for details, as well as the implementation of parsers [rating/](https://github.com/Hedgehogues/new_year_contest_boosters/tree/master/rating).

## Banki.ru parser

The site banki.ru no open API. But as administrators assure, there is a hidden API. This is said on the forums. It is easy to dig. It is available without keys and durgy perlestey. It is enough to create a session using a browser and copy the header of this session as a header for requests. This API can be tracked down if you start downloading different regions with ATMs [here](https://www.banki.ru/banks/).

ATMs can be unloaded in different ways:

* by region (short description). You need to specify a region (all regions can be obtained by a corresponding request), after which all ATMs should be requested for each region. In a number of regions there are a lot of them, so it’s impossible to request everything at once. This should be done in parts. Details can be seen in [banki.ru/get_banks.py](http://hithub.com/Hedgehogues/new_year_contest_boosters/blob/master/banki.ru/get_banks.py]).
* by region (detailed description). [banki.ru/get_desc.py](https://github.com/Hedgehogues/new_year_contest_boosters/blob/master/banki.ru/get_desc.py). For the construction of signs used data obtained using this script.

In the data obtained there is an operating time of ATMs, coordinates (you can validate additional coordinates), logos, links, ATM activity and much more. You can see the data themselves in [banki.ru/data/](http://hithub.com/Hedgehogues/new_year_contest_boosters/tree/master/banki.ru) for more details. I hasten to note that this api is not exhausted, and from there you can pull out additional information.

## Requirements

Attention! Requires installation of the [libpostal package](https://github.com/openvenues/libpostal) (supplied from source) and [transliterator](https://github.com/barseghyanartur/transliterate), in addition to standard sklearn, numpy, xgboost things , lightgbm, etc.
