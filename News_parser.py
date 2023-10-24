import requests
from bs4 import BeautifulSoup

url = "https://itc.ua/ua/tag/it-v-ukrayini-ua/"


def connection_try(link):
    try:
        response = requests.get(link)
        return response
    except ConnectionError:
        return f'Connection Error: {ConnectionError}'


def parsing_news(response_object):
    soup = BeautifulSoup(response_object.text, 'html.parser')

    news_headlines = soup.find_all('div', class_='col-sm-12')
    news_count = 0
    news_data = {}
    for headline in news_headlines:

        news_data[f'{news_count}'] = {
            'Header': headline.find('h2').text.replace('\n', ''),
            'Link': headline.find('h2').find('a')['href']
        }
        news_count += 1
        if news_count >= 5:
            break
    return news_data


def return_news():
    if connection_try(url).status_code == 200:
        news = parsing_news(connection_try(url))
        return news

    else:
        print("Помилка при отриманні сторінки. Код відповіді:", connection_try(url).status_code)
