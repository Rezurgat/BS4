import requests
from bs4 import BeautifulSoup
import json

"""Сохранение индексной страницы, на которой нах-ся ссылки на основные коды"""

url = 'https://www.icd10data.com/ICD10CM/Codes'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user__agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100'
}

# req = requests.get(url, headers=headers)
# src = req.text

"""Сохраняю полученный html в файл."""

# with open('codes.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('codes.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

"""Собираю ссылки на категории кодов"""

base_codes_dict = {}
sub_pages_dict = {}
base_codes = soup.find('div', class_='body-content').find('ul').find_all(class_='identifier')
for item in base_codes:
    item_text = item.text
    item_href = 'https://www.icd10data.com' + item.get('href')
    base_codes_dict[item_text] = [item_href]

"""Сохраняю ссылки и наименования в json для удобства работы"""
# with open('json/all_codes.json', 'w', encoding='utf-8') as file:
#     json.dump(base_codes_dict, file, indent=4, ensure_ascii=False)
#
with open('json/all_codes.json', encoding='utf-8') as file:
    codes_categories_json = json.load(file)

"""Прохожу циклом по ссылкам и записываю полученный html страниц в файлы"""
for code_category_name, code_category_href in codes_categories_json.items():

    req = requests.get(url=code_category_href, headers=headers)
    src = req.text

    # with open(f'data/{code_category_name}.html', 'w', encoding='utf-8') as file:
    #     file.write(src)

    with open(f'data/{code_category_name}.html', encoding='utf-8') as file:
        base = file.read()

    """ Создаю объект BS для углубления в сборе информации """

    soup_sub = BeautifulSoup(base, 'lxml')

    """ Собираю код, содержащий название и ссылки подстраниц """

    sub_pages = soup_sub.find('div', class_='body-content').find('ul', class_='i51').find_all(class_='identifier')
    for sub_item in sub_pages:
        sub_item_text = sub_item.text
        sub_item_href = 'https://www.icd10data.com' + sub_item.get('href')
        sub_pages_dict[sub_item_text] = [sub_item_href]

"""Сохраняю ссылки и наименования подстраниц в json для удобства работы"""
with open('json/sub_pages.json', 'w', encoding='utf-8') as file:
    json.dump(sub_pages_dict, file, indent=4, ensure_ascii=False)

with open('json/sub_pages.json', encoding='utf-8') as file:
    sub_pages_json = json.load(file)






















    # group_code = soup.find('div', class_='body-content').find('h1', class_='pageHeading').find('span', class_='identifier').text
    # group_desc = soup.find('h1', class_='pageHeading').text.replace(group_code, '')
    # code = soup.find('ul', class_='i51').find('li').find_all(class_='identifier')
    # print(code)
