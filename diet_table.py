import requests
import json
from bs4 import BeautifulSoup as BS

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
req = requests.get(url)
src = req.text

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)


with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BS(src, 'lxml')
all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = 'https://health-diet.ru'+item.get('href')
    all_categories_dict[item_text]=item_href 


# with open('all_categories.json', 'w', encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


with open('all_categories.json', encoding='utf-8') as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():
    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    req = requests.get(category_href)
    src = req.text
    with open(f'data/{category_name}.html', 'w', encoding='utf-8') as file:
        file.write(src)