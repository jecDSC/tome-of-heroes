import bs4
from fullupdater import fetch_fandom_html

def get_40_table():
    url = 'https://feheroes.fandom.com/wiki/Level_40_stats_table'
    heroes_html = fetch_fandom_html(url)
    if not heroes_html:
        print('Could not pull Level 40 Stats Table.')
        return
    else:
        print('Level 40 Stats Table pulled successfully.')

    heroes = bs4.BeautifulSoup(heroes_html, 'lxml')
    with open('lv40_heroes.html', 'w', encoding='utf-8') as file:
        file.write(str(heroes.prettify()))
    print('Stats Table HTML saved successfully!')

if __name__ == '__main__':
    get_40_table()