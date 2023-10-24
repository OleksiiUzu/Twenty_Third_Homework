from bs4 import BeautifulSoup

with open('practice.xml', 'r', encoding='utf-8') as file:
    xml_data = file.read()

soup = BeautifulSoup(xml_data, 'xml')

num = 0

for entry in soup.find_all('entry'):

    title = entry.find('title').text
    link = entry.find('link')['href']
    updated = entry.find('updated').text
    summary = entry.find('summary').text

    num += 1
    print(f'{num})')

    print(f"Заголовок: {title}")
    print(f"Посилання: {link}")
    print(f"Оновлено: {updated}")
    print(f"Сумарний текст: {summary}\n")

