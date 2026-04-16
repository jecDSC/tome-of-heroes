from fetcher import fetch_fandom_html
import pandas as pd
import bs4

def get_40_table():
    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    heroes_html = fetch_fandom_html(url)
    if not heroes_html:
        print('Could not pull Level 40 Stats Table.')
        return
    else:
        print('Level 40 Stats Table pulled successfully.')

    heroes = bs4.BeautifulSoup(heroes_html, 'lxml')
    with open('data/lv40_heroes.html', 'w', encoding='utf-8') as file:
        file.write(str(heroes))
    print('Stats Table HTML saved successfully!')
    return

def build_table():
    with open('data/lv40_heroes.html', encoding='utf-8') as fp:
        html = bs4.BeautifulSoup(fp, features='lxml')

    lv40_table = pd.DataFrame(columns=['hero', 'entry', 'move', 'weapon', 'hp', 'atk', 'spd', 'def',
                                       'res', 'total', 'color', 'weapon-type'])
    
    for i in html.find_all('tr', class_="hero-filter-element"):
        td = i.find_all('td')
        wp = i.get('data-weapon-type')
        lv40_table.loc[lv40_table.shape[0]] = [
            i.find('a').get('title'),
            i.find_all('img')[1].get('alt'),
            i.get('data-move-type'),
            wp,
            td[5].text,
            td[6].text,
            td[7].text,
            td[8].text,
            td[9].text,
            td[10].text,
            wp.split()[0],
            wp.split()[1]
        ]

    lv40_table.to_csv('data/lv40_table.csv')
    print('Level 40 Table stored as csv!')
    

if __name__ == '__main__':
    get_40_table()
    build_table()
