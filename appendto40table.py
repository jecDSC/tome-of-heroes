import fetcher as ft
import pandas as pd
import bs4

def append40():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    
    release = []
    version = []
    majorver = []

    print('\nPulling csv...\n')
    table40 = pd.read_csv('./data/lv40_table.csv')
    print('\nFetching release dates and versions...\n')

    for i in table40['hero']:
        # Format file name for call
        name = ft.format_name(i)
        
        with open('./hero-pages/' + name + '.html', encoding='utf-8') as fp:
                html = bs4.BeautifulSoup(fp, features='lxml')
                table = html.select('table.wikitable:not(.default)')
                release.append(table[0].find('time').text)
                version.append(table[0].find_all('a')[-1].text)
                majorver.append(int(float(table[0].find_all('a')[-1].text)))

        print('Saved ' + i)
        print(LINE_UP, end=LINE_CLEAR)

    table40['release'] = release
    table40['version'] = version
    table40['majorver'] = majorver

    table40.to_csv('./data/lv40_table.csv', index=False)
    print("""
=========================================
Release date and version have been
appended to the table.
=========================================
""")


if __name__ == "__main__":
    print("""
=========================================
Welcome to the Level 40 Table Updater!
Currently, this file is used to append 
date added and app version for each hero.
=========================================
""")
    append40()