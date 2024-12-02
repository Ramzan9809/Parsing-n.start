import requests

link = 'https://icanhazip.com/'
result = requests.get(link).text
print(result)

