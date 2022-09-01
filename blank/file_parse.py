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
all_a = soup.find_all('a')
print(all_a)

"""Ссылки всегда лежат в href. Достать сслыки из этого тега мы можем при помощи метода get()"""
for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")
