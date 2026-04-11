import pandas as pd
import bs4
import requests

# The function below fetches the list of all heroes currently in the game.
def heroes_list():
    heroes = requests.get('https://feheroes.fandom.com/wiki/Level_40_stats_table')
    heroes = bs4.BeautifulSoup(heroes.text, features='lxml')

    # Fetches list of all heroes.
    rows = heroes.find_all('tr', attrs={'class':'hero-filter-element'})
    return rows

    
def generate_links(rows):
    links = [] # This cell creates the links for each individual heroes' info pages
    for i in range(len(rows)):
        links.append("https://feheroes.fandom.com" + rows[i].find_all('a')[0].get('href'))


if __name__ == '__main__':
    print(heroes_list())