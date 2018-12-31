# Новогодний контест Boosters от Росбанка

Happy Data Year - новогодний чемпионат по анализу данных от Росбанка.

В обучающей выборке находятся данные о геопозиции шести тысяч банкоматов Росбанка и его партнеров, а также целевая переменная — индекс популярности банкомата. В тестовой выборке еще две с половиной тысячи банкоматов, разделенных поровну на публичную и приватную часть.

https://boosters.pro/champ_21

В данных, очевидно, есть пропуски. Часть из этих пропусков восстановлена при помощи YandexMapsApi, с использованием геокодера. В данном репозитории находится бенчмарк, предложенный организаторами boosters. Отличие от предложенного состоит в том, что часть адресов получена при помощи геокодера Yandex.

Восстановление адресов происходит с валидацией. Для этого используется транслитерация (ответ геокодера с и без транслитерации должны совпадать). Проверяется наличие домов. Если валидация по данным критериям не проходит, тогда координаты заполняются нулями

Внимание! Требуется установка пакета [libpostal](https://github.com/openvenues/libpostal) (ставится из исходников) и [транслитератора](https://github.com/barseghyanartur/transliterate).

# New Year Contest Boosters from Rosbank

Happy Data Year - New Year's data analysis championship from Rosbank.

The training sample contains data on the geo-location of six thousand ATMs of Rosbank and its partners, as well as the target variable - the ATM popularity index. In the test sample, there are another two and a half thousand ATMs, equally divided into public and private parts.

https://boosters.pro/champ_21

There are obviously gaps in the data. Some of these permits were restored using YandexMapsApi, using a geocoder. In this repository is a benchmark, proposed by the organizers of boosters. The difference from the proposed one is that some of the addresses were obtained using the Yandex geocoder.

Restoration of addresses occurs with validation. For this, transliteration is used (the response of the geocoder with and without transliteration must be the same). Checks for availability of homes. If the validation of these criteria does not pass, then the coordinates are filled with zeros

Attention! Package installation is required [libpostal](https://github.com/openvenues/libpostal) (installed from source) and [transliterator](https://github.com/barseghyanartur/transliterate).
