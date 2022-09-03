"""CБор калорийности продукта с сайта"""

"""Для начала нужно собрать все ссылки по продуктам,а потом уже пройтись циклом по каждой
и собрать информацию"""

import requests
from bs4 import BeautifulSoup
import json
import csv

"""Сохранение индексной страницы, на которой нах-ся ссылки на категории продуктов"""

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

"""Возврат работы метода get() из requests.В headers прописываю Accept и user_agent (берется из network браузера).
Делается для того, чтобы система не думала,что я бот(параметр этот необязательный!)"""

headers = {
    'Accept': '*/*',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.104'
}
# req = requests.get(url,headers=headers)
# src = req.text
#print(src)

"""Сохраняю полученный html в файл.Это обязательная практика, так как большинство сайтов не любят, когда их парсят и
могут забанить, поэтому информацию лучше искать в отдельном файле с соответствующим кодом"""

# with open('cal.html', 'w', encoding='utf-8') as file:
#     file.write(src)

"""Открываю полученный файл в режиме чтения и сохраняю в переменную для дальнейшего парсинга"""
# with open('cal.html', encoding='utf-8') as file:
#      src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')

"""Собираем ссылки на категории c добавлением доменного имени и конкантенацией. После отбора данных,сохраню их в словарь."""

# all_products_dict = {}
# all_products = soup.find_all(class_='mzr-tc-group-item-href')
# for item in all_products:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#
#     all_products_dict[item_text] = [item_href]

"""Сохраню полученный словарь в json-файл. Сохранение в json удобен и сокращает время поиска
информации в интернете"""

# with open('all_products_dict.json', 'w', encoding='utf-8') as file:
#     json.dump(all_products_dict,file, indent=4, ensure_ascii=False)

"""ЗАгрузка файла в переменную"""

with open('calorie//all_products_dict.json', encoding='utf-8') as file:
    all_categories = json.load(file)

"""Создам цикл, на каждой итерации которого я буду заходить на новую страницу категории,
собирать данные и записывать их в файл"""

#iteration_count = int(len(all_categories))-1
count = 0
for category_name, category_href in all_categories.items():

    rep = [',', ' ', '-']
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')

    """Запросы на страницы"""

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    """Сохраню страницы под именем категории"""

    with open(f'calorie/data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open(f'calorie/data/{count}_{category_name}.html', encoding='utf-8') as file:
        code = file.read()

    """Создаю объект BS"""

    soup = BeautifulSoup(code, 'lxml')

    """Проверка страницы на наличие таблицы с продуктами. Если есть пустые страницы, то
    в коде страницы должен присутствовать alert. Ищу его и прописываю следующее условие"""

    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    """Cобираю заголовки таблицы"""

    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    """открываю файл для записи данных таблицы"""

    with open(f'calorie/data/{count}_{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

        """Указываю writer, что конкретно нужно записывать в файл. Для этого 
            использую writerow(). Он принимает один аргумент, а, если, нужно больше,
                    то прописываю следующим образом"""

        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates,
            )
        )

    """Собираю данные о продуктах"""
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    for item in products_data:
        product_tds = item.find_all('td')
        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        with open(f'calorie/data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            """Так как нужно до записать файл, то вместо w использую а"""

            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates,
                )
            )
    count += 1
