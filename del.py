import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

to_json = []
is_first_passage = True
i = 24
url = f'https://www.ticketland.ru/show/jsGetPopular/?offset={i}'

ua = UserAgent()
headers = {
    'Accept': '*/*',
    'User-Agent': ua.random
}
while 1:
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    links = soup.find_all(class_='card__image-link')
    if links is []:
        break
    for link in links[0:1]:
        link = 'https://www.ticketland.ru' + link.get('href')
        req = requests.get(url=link, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        title = soup.find(class_='pr-2').text
        print(title)
        print(link)
        date_and_time_all = soup.find_all(class_='show-card__date')
        places = soup.find_all(class_='show-card__place')
        prices = soup.find_all(class_='show-card__price')
        for date_and_time, place, price in zip(date_and_time_all, places, prices):
            date_and_time = (date_and_time.text.strip().replace('				', '')
                             .replace('\n', '').replace('                        ', ' ')
                             .replace('                    •	', ' '))
            print(date_and_time)
            place = place.text.strip()
            place = (place.replace('            ', '').replace('\n', '')
                     .replace('•        ', ' ').replace('     ', ' ')
                     .replace('    ', ' ').replace('   ', ' ').replace('  ', ' '))
            print(place)
            price = (price.text.replace('\n', '').replace('                ', ''))
            print(price)
