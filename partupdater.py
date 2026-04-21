import fetcher as ft
import pandas as pd
import bs4
import time
from fullupdater import hero_file
import os

def missing():
    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    html = bs4.BeautifulSoup(ft.fetch_fandom_html(url), features='lxml')
    if not html:
        print('Could not pull Level 40 Stats Table.')
    else:
        print('Level 40 Stats Table pulled successfully.')

    rows = html.find_all('tr', class_="hero-filter-element")
    heroes = []
    for i in rows:
        heroes.append(i.find_all('a')[1].text)

    links = []
    for i in rows:
        links.append(i.find_all('a')[0].get('href'))
    pairs = dict(zip(heroes, links))

    exist = os.listdir('hero-pages')
    missing = {}

    for i in list(pairs.keys()):
        if ft.format_name(i) + '.html' not in exist:
            missing[i] = pairs[i]

    hero_file(missing)
    return

if __name__ == '__main__':
    missing()