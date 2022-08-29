from bs4 import BeautifulSoup
with open('index.html', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'lxml')

# title = soup.title
# #print(title)
#
# page_h1 = soup.find("h1")
# print(page_h1.text)
#
# page_h1_all = soup.find_all('h1')
# print(page_h1_all)