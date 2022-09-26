import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.icd10data.com/ICD10CM/Codes'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user__agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100'
}

# req = requests.get(url, headers=headers)
# src = req.text

# with open('codes.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('codes.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_codes_dict = {}
all_codes = soup.find('div', class_='body-content').find('ul').find_all(class_='identifier')
for item in all_codes:
    item_text = item.text
    item_href = 'https://www.icd10data.com' + item.get('href')
    all_codes_dict[item_text] = [item_href]
print(all_codes_dict)



