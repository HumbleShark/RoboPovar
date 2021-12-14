import requests
from bs4 import BeautifulSoup


def get_ingr_list(dish_name):
    url = 'https://www.allrecipes.com/search/results/?search={}'.format(dish_name)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    dish = soup.select_one('.card__titleLink')
    d_url = dish['href']
    nr = requests.get(d_url)
    soup = BeautifulSoup(nr.content, 'html.parser')
    ingridients = soup.findAll('li', class_='ingredients-item')
    ingr_list = ''
    for li in ingridients:
        ingr_list += li.text + '\n'
    return ingr_list

