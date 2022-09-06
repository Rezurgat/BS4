"""Разобью ссылку по слешу и заберу его имя"""

url = 'http://www.edutainme.ru/edindex/edindex/project/01math' #ссылка из products_data

url = url.split('/')[-2] #можно распечатать полученный список, посмотреть расположение имени и взять индекс

