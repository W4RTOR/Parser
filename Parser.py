import requests
from bs4 import BeautifulSoup

url = 'https://policies.google.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
print("1")
# Вы можете искать конкретные теги и атрибуты
title = soup.find('title').text
print(title)
print("2")
# Или искать все элементы с определенным классом
all_paragraphs = soup.find_all('p', class_='text-class')
for p in all_paragraphs:
    print(p.text)



print("Hello Parser")
