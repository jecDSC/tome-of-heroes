import pandas as pd
import bs4
import os

def append40():
    release = []
    version = []
    pages = os.listdir('./hero-pages')

    print('\nFetching release dates and versions...\n')
    for i in pages:
        with open('./hero-pages/' + i, encoding='utf-8') as fp:
                html = bs4.BeautifulSoup(fp, features='lxml')
                table = html.select('table.wikitable:not(.default)')
                release.append(table[0].find('time').text)
                version.append(table[0].find_all('a')[-1].text)
        print('Saved ' + i)

    print('\nPulling csv and appending...\n')
    table40 = pd.read_csv('./data/lv40_table.csv')
    table40['release'] = release
    table40['version'] = version

    table40.to_csv('./data/lv40_table.csv')
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