import pandas as pd
import bs4
import requests
from urllib.parse import unquote
import time

# Run this once to fetch the Level 40 Stats Table

# fetch_fandom_html handles fetching pages from fandom.com.
def fetch_fandom_html(page_url):
    title = unquote(page_url.split('/wiki/', 1)[1]).split('?', 1)[0]
    try:
        response = requests.get(
            'https://feheroes.fandom.com/api.php',
            params={
                'action': 'parse',
                'page': title,
                'prop': 'text',
                'formatversion': '2',
                'format': 'json',
            },
            timeout=30,
        )
        response.raise_for_status()
        return response.json()['parse']['text']
    except requests.RequestException as e:
        print(f"Request failed for {title}: {e}")
        return None

# get_heroes_list produces a list of heroes and a list of their hero page links.
def get_heroes_list():
    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    heroes_html = fetch_fandom_html(url)
    if not heroes_html:
        print('Could not pull Level 40 Stats Table.')
        return
    else:
        print('Level 40 Stats Table pulled successfully.')

    heroes = bs4.BeautifulSoup(heroes_html, 'lxml')

    resp = input('Would you like to locally save the Level 40 Stats Table site? (y / n) - ')
    while resp != 'y' and resp != 'n':
        resp = input('Would you like to locally save the Level 40 Stats Table site? (y / n) - ')
    if resp == 'y':
        with open('data/lv40_heroes.html', 'w', encoding='utf-8') as file:
            file.write(str(heroes.prettify()))
    rows = heroes.find_all('tr', class_='hero-filter-element')

    heroes = []
    for i in rows:
        heroes.append(i.find_all('a')[1].text)

    links = []
    for i in rows:
        links.append(i.find_all('a')[0].get('href'))
    
    pd.DataFrame({'links':links}, index=heroes).to_csv('data/hero-links.csv')
    return dict(zip(heroes, links))

# This is for saving hero pages as local HTML files.
def hero_file(tome):
    fails = []
    for i in tome.keys():
        # Create file name
        temp = i.split()
        for j in range(len(temp)):
            temp[j] = temp[j].strip(':\'"')
            name = ''.join(temp)
        
        # Pull HTML from site
        time.sleep(0.5)
        soup = fetch_fandom_html(tome[i])
        if not soup:
            print(f'Skipping {i} because page request failed.')
            fails.append(i)
            continue
        soup = bs4.BeautifulSoup(soup, 'lxml')
        navbox = soup.find('div', class_= 'navbox')
        navbox.decompose()

        # Save page to file
        with open(f'hero-pages/{name}.html', 'w', encoding = 'utf-8') as file:
            file.write(str(soup))
        print(name, 'saved successfully.')

    print('Finished saving pages.')
    if fails:
        print("The following hero pages were not pulled successfully.")
        print(fails)
    return


if __name__ == '__main__':
    print("""=========================================================================================
= Welcome to the page updater! Note that if you do not have a hero-page folder locally, =
= one will be created. Update time for all hero pages may take at least 20 minutes.     =
=========================================================================================\n""")
    print('Attempting to fetch Level 40 Stats Table...')
    heroes_dict = get_heroes_list()
    if heroes_dict:
        resp = input('\nWould you like to start saving pages now? (y/n) --- ')
        if resp != 'y' and resp != 'n':
            while resp != 'y' and resp != 'n':
                resp = input('\nInvalid input. Would you like to start saving pages now? (y/n) --- ')
        if resp == 'y':
            hero_file(heroes_dict)
        else:
            print('\n======================\n= Updater Terminated =\n======================')
