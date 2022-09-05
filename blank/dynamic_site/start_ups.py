"""Сайт по парсингу динамического сайта онлайн-стартапов с записью в json"""

import requests
from bs4 import BeautifulSoup
import json

"""Создам ф-ю, которая будет принимать в себя url-адрес"""

def get_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104'
    }

    """req и with лучше комментировать, чтобы постоянно не стучаться на сайт"""

    # req = requests.get(url, headers=headers)

    # with open('projects.html', 'w', encoding='utf-8') as file:
    #     file.write(req.text)

    """ЧИтаю файл с последующим сохранением в переменную"""
    with open('projects.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    """Нахожу все ссылки стартапов"""

    articles = soup.find_all('article', class_='ib19')

    """Забираю ссылки из карточек и конкантенирую с доменом"""

    products_data = []
    for article in articles:
        project_url ='http://www.edutainme.ru/edindex/' + article.find('div', class_='txtBlock').find('a').get('href')
        products_data.append(project_url)

    """Далее мне нужно перейти по каждой ссылке, собрать названия, ссылки на логотип, краткое описание, 
     полное описание"""

    for project_url in products_data:
        req =requests.get(project_url, headers=headers)




get_url('http://www.edutainme.ru/edindex/')