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

for url in fests_urls_list[0:1]:
    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_info = soup.find("div", class_="MuiContainer-root MuiContainer-maxWidthFalse css-1krljt2")

        """Имя фестиваля"""

        fest_name = fest_info.find('h1').text.strip()


        """Дата фестиваля"""

        fest_date = soup.find('div', class_='MuiGrid-root MuiGrid-container css-f3i3nk').find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text


        """Ссылка на локацию, при переходе на которую нужно будет собрать всю 
        необходимую информацию"""

        fest_location = soup.find('div', class_='MuiBox-root css-107d1jv').find('div', class_='MuiBox-root css-zzbvj8').find_all('iframe')
        print(fest_location)
        """Соберу данные контактов и запишу все в файл"""

        q = requests.get(url=fest_location, headers=headers)
        soup = BeautifulSoup(q.text, 'lxml')

        contact_details = soup.find('h2', string="Venue contact details and info").find_next()

        """Собираю информацию из <p>"""

        items = [item.text for item in contact_details.find_all('p')]

        """Далее нужно разбить нужную информацию в строках, так как изначально получаю их слитыми"""

        for contact_detail in items:
            print(contact_detail)
    except Exception as ex:
        print('Some error')




