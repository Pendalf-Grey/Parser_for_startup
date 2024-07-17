import json
import sqlite3
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# print('Start parser')
#
# BASE_DIR = Path(__file__).resolve().parent
#
# db_path = BASE_DIR / 'db.sqlite3'
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# domain = 'https://prodoctorov.ru/moskva/top/chastnaya-stomatologiya/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

# '''сымитируем запросы от пользователя с помощью headers'''
# req = requests.get(url=domain, headers=headers)
# src = req.text
# print(src)

# '''сохраним HTML-разметку в файл'''
# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)

# '''откроем файл, прочитаем и сохраним в переменную'''
# with open('index.html', encoding='utf-8') as file:
#     src = file.read()

# '''создадим объект BS, передадим внутрь переменную с HTML, подключим парсер lxml'''
# soup = BeautifulSoup(src, 'lxml')

# ''' достаём названия клиник'''
# '''записываем в names_list'''
# names_of_the_clinic = soup.find_all('a', {'class': 'b-link b-link_underline_hover b-link_color_primary-blue d-inline'})
# names_list = list()
# for name in names_of_the_clinic:
#     names = name.text.strip()
#     names_list.append(names)

# '''достаём ссылки на цены'''
# '''записываем в links_list'''
# links_to_prices = soup.find_all('a', {'class': 'b-contacts-list__item b-contacts-list__item_link'})
# links_list = list()
# for link in links_to_prices:
#     links = link.get('href')
#     links_list.append(links)

# '''попробуем цикл while для создания первичного data_set'''
# all_names_and_links = dict()
# counter = 0
# while counter < len(links_list):
#     key = names_list[counter]
#     val = links_list[counter]
#     all_names_and_links[key] = 'https://prodoctorov.ru' + val
#
#     counter += 1

'''сохраним data_set в файл'''
# with open('all_names_and_links.json', 'w', encoding='utf-8') as file:
#     json.dump(all_names_and_links, fp=file, ensure_ascii=False, indent=4)

# '''откроем файл, прочитаем, сохраним в переменную'''
# with open('all_names_and_links.json', encoding='utf-8') as file:
#     all_names_and_links = json.load(file)

# '''создаём цикл, пробегаемся по ссылкам, собираем все цены, записываем в файл'''
# for names_clinic, links_price in all_names_and_links.items():
#
#     '''заменили один или несколько символов names_clinic на _'''
#     symbol = [' ']
#     for i in symbol:
#         if i in names_clinic:
#             names_clinic = names_clinic.replace(i, '_')
#             print(names_clinic)
#
#     '''достаём новую HTML-разметку'''
#     '''переопределяем req и src'''
#     req = requests.get(url=links_price, headers=headers)
#     src = req.text


# '''записываем в новый файл'''
# with open('index_2.html', 'w', encoding='utf-8') as file:
#     file.write(src)

'''откроем, прочитаем, сохраним в переменную src'''
with open('index_2.html', encoding='utf-8') as file:
    src = file.read()

'''переопределим объект BS'''
soup = BeautifulSoup(src, 'lxml')

'''достаём названия операций'''
'''записываем в operace_list'''
names_operace = soup.find_all('div', {'class': 'b-lpu-services__service-name ui-text ui-text_body-1'})
operace_name_list = list()
for name in names_operace:
    names = name.text.strip()
    operace_name_list.append(names)
print(operace_name_list)

'''достаём цены операций'''
'''записываем в operace_price_list'''
prices_operace = soup.find_all('div', {'class': 'ui-text ui-text_subtitle-1 ui-kit-color-text'})
operace_price_list = list()
for price in prices_operace:
    prices = price.text.strip()
    operace_price_list.append(prices)
print(operace_price_list)

'''попробуем while для создания {}'''
all_operace_and_price = dict()
counter = 0
while counter < len(operace_price_list):
    key = operace_name_list[counter]
    val = operace_price_list[counter]

    all_operace_and_price[key] = val

    counter += 1

print(all_operace_and_price)

'''сохраним data_set в файл'''
with open('all_operace_and_price.json', 'w', encoding='utf-8') as file:
    json.dump(all_operace_and_price, fp=file, ensure_ascii=False, indent=4)