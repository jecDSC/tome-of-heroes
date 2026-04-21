import fetcher as ft
import pandas as pd
import bs4
import time

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

# Run this once to fetch the Level 40 Stats Table

# get_heroes_list produces a list of heroes and a list of their hero page links.
def get_heroes_list():
    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    heroes_html = ft.fetch_fandom_html(url)
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
        name = ft.format_name(i)
        
        # Pull HTML from site
        time.sleep(0.5)
        soup = ft.fetch_fandom_html(tome[i])
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

        print('Successfully saved ' + name)
        print(LINE_UP, end=LINE_CLEAR)

    print('Finished saving pages.')
    if fails:
        print("The following hero pages were not pulled successfully.")
        print(fails)
    return


if __name__ == '__main__':
    print("""=====================================================================================
Welcome to the page updater! Note that if you do not have a hero-page folder locally,
one will be created. Update time for all hero pages may take at least 20 minutes.    
=====================================================================================\n""")
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
            print('\n==================\nUpdater Terminated\n==================')
