"""Скапинг сайта бундестага с сбором ссылок на членов"""

import requests
from bs4 import BeautifulSoup
import json

"""Соберу ссылки на страницы людей и сохраню их в файл"""

"""Создам цикл for для сбора всех limit(кол-во единовременных показов при нажатии на слайдер (в Network) 
 и создам список для ссылок"""

# persons_url_list = []
#
# for i in range(0, 740, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158/h_a45203fd0f1592191f1bda63b5d86d72?limit=20&noFilterSet=true{i}'
#
#     """Генерирую get-запрос на странички и забираю ссылки"""
#
#     a = requests.get(url)
#     result = a.content
#
#     soup = BeautifulSoup(result, 'lxml')
#     persons = soup.find_all(class_='bt-slide-content')
#
#     for person in persons:
#         person_page_url = person.find('a').get('href')
#         persons_url_list.append(person_page_url)
#
# with open('persons_url_list.txt', 'a', encoding='utf-8') as file:
#      for line in persons_url_list:
#          file.write(f'{line}\n')

"""Далее прохожусь по каждой ссылке и забираю имя, партию"""
with open('persons_url_list.txt', encoding='utf-8') as file:

     lines = [line.strip() for line in file.readlines()]

     """Создаю цикл for и пробегаюсь по ссылкам,забирая по одной. Данные Буду добавлять
     в список data_list_person"""

     data_list_person = []
     for line in lines:
         q = requests.get(line)
         result = q.content

         soup = BeautifulSoup(result, 'lxml')
         person = soup.find(class_='bt-biografie-name').find('h3').text
         person_name_partie = person.strip().split(',')
         person_name = person_name_partie[0]
         person_partie = person_name_partie[1].strip()

         data = {
             'person_name': person_name,
             'person_partie': person_partie,
         }

         data_list_person.append(data)

         with open('final_data.json', 'w', encoding='utf-8') as file:
             json.dump(data_list_person, file, indent=4, ensure_ascii=False)

