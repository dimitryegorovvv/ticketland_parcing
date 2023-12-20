import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import sys
from itertools import zip_longest

to_json = []
is_first_passage = True
i = 0
correct_url = 'https://www.ticketland.ru/'

ua = UserAgent()
headers = {
    'Accept': '*/*',
    'User-Agent': ua.random
}

# number_with_city = sys.argv
# number_with_city = int(number_with_city[1])
# print(number_with_city)

number_with_city = int(input('Введите город '))

if number_with_city == 1:
    print('Выбранный регион - Москва')
elif number_with_city == 2:
    correct_url = 'https://spb.ticketland.ru/'
    print('Выбранный регион - СПб')
elif number_with_city == 3:
    correct_url = 'https://barnaul.ticketland.ru/'
    print('Выбранный регион - Алтайский край')
elif number_with_city == 4:
    correct_url = 'https://amur.ticketland.ru/'
    print('Выбранный регион - Амурская область')
elif number_with_city == 5:
    correct_url = 'https://arhan.ticketland.ru/'
    print('Выбранный регион - Архангельская область')
elif number_with_city == 6:
    correct_url = 'https://astrakhan.ticketland.ru//'
    print('Выбранный регион - Астрахань')
elif number_with_city == 7:
    correct_url = 'https://belgorod.ticketland.ru/'
    print('Выбранный регион - Белгородская область')
elif number_with_city == 8:
    correct_url = 'https://bryansk.ticketland.ru/'
    print('Выбранный регион - Брянская область')
elif number_with_city == 9:
    correct_url = 'https://vladivostok.ticketland.ru/'
    print('Выбранный регион - Владивосток и Приморский край')
elif number_with_city == 10:
    correct_url = 'https://vladimir.ticketland.ru/'
    print('Выбранный регион - Владимирская область')
elif number_with_city == 11:
    correct_url = 'https://vog.ticketland.ru/'
    print('Выбранный регион - Волгоградская область')
elif number_with_city == 12:
    correct_url = 'https://vologda.ticketland.ru/'
    print('Выбранный регион - Вологодская область')
elif number_with_city == 13:
    correct_url = 'https://voronezh.ticketland.ru/'
    print('Выбранный регион - Воронежская область')
elif number_with_city == 14:
    correct_url = 'https://ekb.ticketland.ru/'
    print('Выбранный регион - Екатеринбург')
elif number_with_city == 15:
    correct_url = 'https://ivanovo.ticketland.ru/'
    print('Выбранный регион - Ивановская область')
elif number_with_city == 16:
    correct_url = 'https://kostroma.ticketland.ru/'
    print('Выбранный регион - Костромская область')
elif number_with_city == 17:
    correct_url = 'https://izhevsk.ticketland.ru/'
    print('Выбранный регион - Ижевск - Удмуртия')
elif number_with_city == 18:
    correct_url = 'https://irkutsk.ticketland.ru/'
    print('Выбранный регион - Иркутская область')
elif number_with_city == 19:
    correct_url = 'https://i-ola.ticketland.ru/'
    print('Выбранный регион - Йошкар-Ола - Марий Эл')
elif number_with_city == 20:
    correct_url = 'https://kzn.ticketland.ru/'
    print('Выбранный регион - Казань - Татарстан')
elif number_with_city == 21:
    correct_url = 'https://kaliningrad.ticketland.ru/'
    print('Выбранный регион - Калининградская область')
elif number_with_city == 22:
    correct_url = 'https://klf.ticketland.ru/'
    print('Выбранный регион - Калужская область')
elif number_with_city == 23:
    correct_url = 'https://kamensk.ticketland.ru/'
    print('Выбранный регион - Каменск-Уральский')
elif number_with_city == 24:
    correct_url = 'https://cherksk.ticketland.ru/'
    print('Выбранный регион - Карачаево-Черкесская республика')
elif number_with_city == 25:
    correct_url = 'https://kuzbass.ticketland.ru/'
    print('Выбранный регион - Кузбасс')
elif number_with_city == 26:
    correct_url = 'https://kirov.ticketland.ru/'
    print('Выбранный регион - Кировская область')
elif number_with_city == 27:
    correct_url = 'https://krasn.ticketland.ru/'
    print('Выбранный регион - Красноярский край')
elif number_with_city == 27:
    correct_url = 'https://krasnodar.ticketland.ru/'
    print('Выбранный регион - Краснодар - Краснодарский край')
elif number_with_city == 28:
    correct_url = 'https://kurgan.ticketland.ru/'
    print('Выбранный регион - Краснодар - Курганская область')
elif number_with_city == 29:
    correct_url = 'https://kursk.ticketland.ru/'
    print('Выбранный регион - Краснодар - Курская область')
elif number_with_city == 30:
    correct_url = 'https://lipetsk.ticketland.ru/'
    print('Выбранный регион - Краснодар - Липецкая область')
elif number_with_city == 31:
    correct_url = 'https://murmansk.ticketland.ru/'
    print('Выбранный регион - Краснодар - Мурманская область')
elif number_with_city == 32:
    correct_url = 'https://nalchik.ticketland.ru/'
    print('Выбранный регион - Краснодар - Нальчик')
elif number_with_city == 33:
    correct_url = 'https://nnov.ticketland.ru/'
    print('Выбранный регион - Нижегородская область')
elif number_with_city == 34:
    correct_url = 'https://ntagil.ticketland.ru/'
    print('Выбранный регион - Нижний тагил')
elif number_with_city == 35:
    correct_url = 'https://nov.ticketland.ru/'
    print('Выбранный регион - Новгородская область')
elif number_with_city == 36:
    correct_url = 'https://nsk.ticketland.ru/'
    print('Выбранный регион - Новосибирская область')
elif number_with_city == 37:
    correct_url = 'https://obninsk.ticketland.ru/'
    print('Выбранный регион - Обнинск')
elif number_with_city == 38:
    correct_url = 'https://omsk.ticketland.ru/'
    print('Выбранный регион - Омская область')
elif number_with_city == 39:
    correct_url = 'https://orel.ticketland.ru/'
    print('Выбранный регион - Орловская область')
elif number_with_city == 40:
    correct_url = 'https://orenburg.ticketland.ru/'
    print('Выбранный регион - Оренбургская область')
elif number_with_city == 41:
    correct_url = 'https://penza.ticketland.ru/'
    print('Выбранный регион - Пензенская область')
elif number_with_city == 42:
    correct_url = 'https://perm.ticketland.ru/'
    print('Выбранный регион - Пермь')
elif number_with_city == 43:
    correct_url = 'https://kamchatka.ticketland.ru/'
    print('Выбранный регион - Петропавловск-Камчатский')
elif number_with_city == 44:
    correct_url = 'https://pskov.ticketland.ru/'
    print('Выбранный регион - Псков')
elif number_with_city == 45:
    correct_url = 'https://adigea.ticketland.ru/'
    print('Выбранный регион - республика Адыгея')
elif number_with_city == 46:
    correct_url = 'https://altairepublic.ticketland.ru/'
    print('Выбранный регион - республика Алтай')
elif number_with_city == 47:
    correct_url = 'https://petrozavodsk.ticketland.ru/'
    print('Выбранный регион - республика Карелия')
elif number_with_city == 48:
    correct_url = 'https://ykt.ticketland.ru/'
    print('Выбранный регион - республика Саха (Якутия)')
elif number_with_city == 49:
    correct_url = 'https://vladikavkaz.ticketland.ru/'
    print('Выбранный регион - республика Северная Осетия - Алания')
elif number_with_city == 50:
    correct_url = 'https://abakan.ticketland.ru/'
    print('Выбранный регион - республика Хакасия')
elif number_with_city == 51:
    correct_url = 'https://rnd.ticketland.ru/'
    print('Выбранный регион - Ростовская область')
elif number_with_city == 52:
    correct_url = 'https://ryazan.ticketland.ru/'
    print('Выбранный регион - Рязанская область')
elif number_with_city == 53:
    correct_url = 'https://komi.ticketland.ru/'
    print('Выбранный регион - республика Коми')

while 1:
    url = correct_url
    if is_first_passage is not True:
        url = url + f'show/jsGetPopular/?offset={i}'

    try:
        req = requests.get(url=url, headers=headers)
    except Exception:
        print('Сайт недоступен')
        exit(0)
    soup = BeautifulSoup(req.text, 'lxml')

    try:
        links = soup.find_all(class_='card__image-link')
    except Exception:
        links = 'Отсутствует'

    if links == []:
        break
    for link in links:
        link = 'https://www.ticketland.ru' + link.get('href')
        req = requests.get(url=link, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        try:
            title = soup.find(class_='pr-2').text
        except Exception:
            title = 'Отсутствует'
        title = title.strip().replace('​', '').replace('  ', ' ')
        print(title)
        print(link)
        try:
            date_and_time_all = soup.find_all(class_='show-card__date')
        except Exception:
            date_and_time_all = 'Отсутствует'
        try:
            places = soup.find_all(class_='show-card__place')
        except Exception:
            places = 'Отсутствует'
        try:
            prices = soup.find_all(class_='show-card__price')
        except Exception:
            prices = 'Отсутствует'
        for date_and_time, place, price in zip_longest(date_and_time_all, places, prices):

            date_and_time = (date_and_time.text.strip().replace('				', '')
                             .replace('\n', '').replace('                        ', ' ')
                             .replace('                    •	', ' ')
                             .replace('&nbsp;', ' ').replace(' ', ' ')
                             .replace('​', '').replace('  ', ' '))

            print(date_and_time)
            place = place.text.strip()

            place = (place.replace('            ', '').replace('\n', '')
                     .replace('•        ', ' ').replace('     ', ' ')
                     .replace('    ', ' ').replace('   ', ' ')
                     .replace(' ', ' ').replace('​', '').replace('  ', ' '))

            print(place)

            price = (price.text.replace('\n', '').replace('                ', '')
                     .replace('&nbsp;', ' ').replace(' ', ' ')
                     .replace('​', '').replace('  ', ' '))

            print(price)
            to_json.append(
                {
                    'название': title,
                    'ссылка': link,
                    'дата и время проведения': date_and_time,
                    'место проведения': place,
                    'цена': price,
                }
            )
    is_first_passage = False
    i += 24
    with open('tickets.json', 'w', encoding='utf-8') as file:
        json.dump(to_json, file, indent=4, ensure_ascii=False)
print('процесс завершился успешно')


