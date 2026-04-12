import pandas as pd
import bs4
import requests
from urllib.parse import unquote
import time

# Run this once to fetch the Level 40 Stats Table


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

def get_heroes_list():

    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    heroes_html = fetch_fandom_html(url)
    if not heroes_html:
        print('Could not pull Level 40 Stats Table.')
        return [], []
    else:
        print('Level 40 Stats Table pulled successfully.')

    heroes = bs4.BeautifulSoup(heroes_html, 'lxml')
    rows = heroes.find_all('tr', class_='hero-filter-element')

    heroes = []
    for i in rows:
        heroes.append(i.find_all('a')[1].text)

    links = []
    for i in rows:
        links.append(i.find_all('a')[0].get('href'))
    
    return heroes, links

def hero_file(heroes, links):
    fails = []
    for i in range(len(heroes)):
        # Create file name
        temp = heroes[i].split()
        for j in range(len(temp)):
            temp[j] = temp[j].strip(':\'"')
            name = ''.join(temp)
        
        # Pull HTML from site
        time.sleep(0.5)
        soup = fetch_fandom_html(links[i])
        if not soup:
            print(f"Skipping {heroes[i]} because page request failed.")
            fails.append(heroes[i])
            continue
        soup = bs4.BeautifulSoup(soup, 'lxml')

        # Save page to file
        with open(F"hero-pages/{name}.html", "w", encoding = 'utf-8') as file:
            file.write(str(soup.prettify()))
        print(name, 'saved successfully.')

    print('Finished saving pages.')
    if fails:
        print("The following hero pages were not pulled successfully.")
        print(fails)
    return


if __name__ == '__main__':
    heroes, links = get_heroes_list()
    if heroes and links:
        hero_file(heroes, links)
