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
        project_url ='http://www.edutainme.ru/' + article.find('div', class_='txtBlock').find('a').get('href')
        products_data.append(project_url)

    """Далее мне нужно перейти по каждой ссылке, собрать названия, ссылки на логотип, краткое описание, 
     полное описание, сайт стартапа"""

    for project_url in products_data:
        req =requests.get(project_url, headers=headers)

        """Cохраню страницу стартапа по его именем, а имя возьму из ссылки"""

        project_name = project_url.split('/')[-2]

        """Сохраняю файл под именем стартапа"""

        with open(f"dynamic_site/data/{project_name}.html", 'w', encoding='utf-8') as file:
            file.write(req.text)

        with open(f"dynamic_site/data/{project_name}.html", encoding='utf-8') as file:
            src = file.read()

        """Извлекаю данные"""

        soup = BeautifulSoup(src, 'lxml')

        """Нахожу в полученном html-файле нужный div (первым извлеку логотип стартапа)
        и извлекаю инфу из него. Также заверну блок в обработчик исключений, чтобы в случае
        отсутствия лого, имени и тд., не выбрасывало ошибку"""

        try:
            project_data = soup.find('div', class_='inside')
            project_logo = 'http://www.edutainme.ru/edindex/' + soup.find('div', class_='Img logo').find('img').get('src')

        """Далее на очереди имя стартапа"""

        except Exception:
            project_logo = "No logo"

        try:
            project_name = soup.find('div', class_='txt').find('h1').text
        except Exception:
            project_name = 'No project name'

        """далее извлекаю короткое описание"""

        try:
            project_short_description = project_data.find('div', class_='txt').find('h4', class_='head').text
        except Exception:
            project_short_description = "No short description"

        """Извлекаю ссылку на сайт стартапа"""

        try:
            project_link = project_data.find('div', class_='txt').find('p').find('a').get('href')
        except Exception:
            project_link = 'No project link'

        """Извлекаю описание проекта"""

        try:
            project_full_description = project_data.find('div', class_='textWrap').find('div', class_='rBlock').text
        except Exception:
            project_full_description = "No project full description"







get_url('http://www.edutainme.ru/edindex/')