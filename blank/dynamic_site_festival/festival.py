"""Динамический сайт с фестивалями. Нужно пройтись по каждому фестивалю, забрать название,
дату проведения, а затем погрузиться глубже,кликнув по адресу, а там забрать всю контактную инфу,
которая может отличаться (количеством полей) с json-файлом на выходе """

import requests
from bs4 import BeautifulSoup
import json

"""Так как сайт меняется динамически, то нужно сделать еще один get-запрос и посмотреть, что
выдаст в ответ (через Network) при попытке открыть больше ссылок. В данном случае в headers в
конце есть параметр '0=24', который яв-ся offset'ом (смещением).Конечное значение равняется 168"""

"""Создам словарь заголовков"""

headers = {
    'user__agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
}

"""Список под ссылки"""

fests_urls_list = []
for i in range(0, 192, 24):

    """вместо offset подставлю i"""

    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=24%20Jan%202021&to_date=&where%5B%5D=2&where%5B%5D=3&where%5B%5D=4&where%5B%5D=6&where%5B%5D=7&where%5B%5D=8&where%5B%5D=9&where%5B%5D=10&maxprice=500&o={i}&bannertitle=May"
    # print(url)

    req = requests.get(url=url, headers=headers)

    """Так как ответом в данном случае будет словарь,то передам данный сразу в json"""

    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'data/index_{i}.html', 'w', encoding='utf-8') as file:
        file.write(html_response)

    """Собираю ссылки"""

    with open(f'data/index_{i}.html', encoding='utf-8') as file:
        src = file.read()


    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-details-link')

    for item in cards:
        fest_url ='https://www.skiddle.com' + item.get('href')
        fests_urls_list.append(fest_url)

"""После получения ссылок собираю с них информацию"""

for url in fests_urls_list:
    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_info = soup.find('div', class_='top-info-cont')

        """Имя фестиваля"""

        fest_name = fest_info.find('h1').text.strip()

        """Дата фестиваля"""

        fest_date = fest_info.find('h3').text.strip()

        """Ссылка на локацию, при переходе на которую нужно будет собрать всю 
        необходимую информацию"""

        fest_location = 'https://www.skiddle.com' + fest_info.find('a', class_='tc-white').get('href')

    except Exception as ex:
        print('Some error')
