"""Скапинг сайта бундестага с сбором ссылок на членов"""

import requests
from bs4 import BeautifulSoup
import json

"""Соберу ссылки на страницы людей и сохраню их в файл"""

"""Создам цикл for для сбора всех limit(кол-во единовременных показов при нажатии на слайдер (в Network) """

for i in range (0, 740, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true{i}'
    print(url)