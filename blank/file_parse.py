import re

from bs4 import BeautifulSoup
with open('index.html', encoding='utf-8') as file:
    content = file.read()
"""Создание экземпляра класса для последующей работы с методами BS"""
soup = BeautifulSoup(content, 'lxml')

# title = soup.title
# #print(title)

"""Отображает первый найденный элемент"""
# page_h1 = soup.find("h1")
# print(page_h1.text)

"""Отображает все элементы по критерию"""
# page_h1_all = soup.find_all('h1')
# print(page_h1_all)

"""Поиск в определенном теге по атрибуту"""
# user_name = soup.find('div', 'user__name')
# print(user_name.text)

"""Благодаря связке методов мы можем идти 'вглубь' кода и уже в объекте BS можем найти тег <span>.
Стоит иметь в виду,что,если в коде несколько похожих по названию классов, то парситься будет
первый попавшийся класс, следовательно, лучше первым аргументом указывать нужный блок"""
# user_name = soup.find('div', class_="user__name").find("span").text
# print(user_name)

"""Вторым способом задания атрибутов для фильтрации поиска яв-ся задание словаря, в котором в 
качестве пары ключ-значение указываем параметры отбора.Удобно, если есть какая-то жесткая фильтрация
(по нескольким критериям)"""
# user_name = soup.find('div', {'class': 'user__name'}).find('span').text
# print(user_name)

"""Парсим соц.сети 1 способ"""
# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(social_links)

"""Парсим соц.сети 2 способ(минус в наличии еще доп. ссылок, может не стыковаться с условием отбора,
поэтому 1 способ точнее)."""
# all_a = soup.find_all('a')
# print(all_a)

"""Ссылки всегда лежат в href. Достать сслыки из этого тега мы можем при помощи метода get().
Работает с любыми атрибутами(не только ссылки).Здесь парсить можно и без get(), можно просто
обратиться к атрибуту в списке--item['href']"""
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")

"""Для перемещения по DOM-дереву есть также еще полезные методы.Например find_parent() и 
find_parents().Они ищут родителя или родителей эл-ов,т.е.,поднимаются по структуре html-
дерева (снизу-вверх), а их работа аналогична find и find_all с поправкой, что используются,
когда нужно подниматься вверх. Это полезно,когда нет определенного класса у блока, но
есть класс у нужного эл-та,за который можно зацепиться и вытаскивать аналогичные эл-ты.
В этом примере забирается не все,а только эл-ты до первого родителя"""

# post_div = soup.find(class_='post__text').find_parent()
# print(post_div)

"""Если в find_parent мы ничего не указываем, то парсим до первого попавшегося родителя,
а,если указать, то парсится все до него"""

# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_div)

"""find_parent отрабатывает так,что поднимается до самого верха, включая даже body и
html-тег"""

# post_divs = soup.find(class_='post__text').find_parents()
# print(post_divs)

"""Следующими полезными эл-ми яв-ся next_element и previous_element.
next_element работает достаточно дотошно и выдает все(даже переносы строки,
что озночает,что на выходе можем получить пустой ответ, соответственно, next_element
нужно будет вызвать несколько раз.previous_element()-полная противоположность и работает
снизу-вверх"""

# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

"""Есть похожий метод find_next(), который сразу вернет след. эл-т"""
# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)

""".find_next_sibling(), .find_previous_sibling(). Ищут и возвращают следующий
и предыдущий эл-ты внутри искомого тега.find_previous_sibling()- протипоположный метод"""

# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

"""Также можно парсить по тексту(text), но есть одна загвоздка. Через text можем распарсить 
только введя текст блока полностью (а,если текст большой?). ЗДесь на помощь приходит re c методом compile()"""

find_text = soup.find('a', text=re.compile('супер'))
print(find_text)