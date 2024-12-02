import requests
from bs4 import BeautifulSoup

link = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/'
site = requests.get(link)
html = BeautifulSoup(site.content, 'html.parser')
main_api = 'https://globus-online.kg'

names = html.find_all('div', class_='list-showcase__name')
sales = html.find_all('span', class_='c-prices__value')
links = html.find_all('div', class_='list-showcase__name')

link_list = [main_api + i.find('a').get('href') for i in links]
sales_list = [i.text for i in sales]
names_list = [i.text for i in names]
new = list(zip(names_list, sales_list, link_list))

with open('meats.txt', 'a', encoding='utf-8') as file:
    for i in new:
        file.write(f"{i[0]} - {i[1]} - {i[2]} \n")


# задача

main_api = 'https://globus-online.kg/catalog/napitki/kola_limonady_kvas/'

names = html.find_all('div', class_='list-showcase__name')
sales = html.find_all('span', class_='c-prices__value')
links = html.find_all('div', class_='list-showcase__name')

link_list = [main_api + i.find('a').get('href') for i in links]
sales_list = [i.text for i in sales]
names_list = [i.text for i in names]
new = list(zip(names_list, sales_list, link_list))

with open('drinks.txt', 'a', encoding='utf-8') as file:
    for i in new:
        file.write(f"{i[0]} - {i[1]} - {i[2]} \n")