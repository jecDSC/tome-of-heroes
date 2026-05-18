# Tome of Heroes

Welcome to Tome of Heroes! This is a fan-made site to showcase some of my insights and analysis of data from Fire Emblem Heroes.
Includes an extensive dataset of Heroes from the game Fire Emblem Heroes.

Data and datasets are pulled from fandom.com, from the Fire Emblem Heroes fandom.

## Currently Added Data

- Level 40 Stats Table
- Release date and versions of Heroes pulled from individual hero pages

## Studies
- My own analysis into different aspects of the game.
- A Study on Speed Stat Ceiling Breaks has been added! Still a work in progress.
- More studies and statistical analysis being done on my local repository.
  
## Regarding Special Characters in Hero Names

- To be addressed

## Important Files

- fullupdater.py is used to locally save all hero pages from feheroes.fandom.com.
- partupdater.py is used to locally save select hero pages from feheroes.fandom.com. (in development)
- base40table.py is used to locally save the Level 40 Stats Table from feheroes.fandom.com, as well as create a basic information dataset saved locally as a csv file.
- fetcher.py holds the function used to fetch feheroes.fandom.com pages.
- appendto40table.py pulls data from the 1300+ locally-saved hero pages to append to a Level 40 Table csv. Currently, this file appends release date and version of each hero to the table.

## Executable File Manager

- Coming soon...
- Plan is try to combine fullupdater, partupdater, base40table, fetcher into an executable file.

## What's in data?

- It currently holds a Level 40 Stats Table built from the data available from feheroes.fandom.com, saved as a csv.
- If you use the File Manager programs, it locally saves a few datasets that are helpful in building the stats csv.

## A breakdown of the columns in lv40_table.csv

| Column | Contains |
| ------ | -------- |
| hero        | Name of the hero. |
| entry       | Fire Emblem game the hero is from. |
| move        | Move type of the hero. |
| weapon      | Weapon of the hero (color + weapon type). |
| hp          | Hit points stat of the hero. |
| atk         | Attack stat of the hero. |
| spd         | Speed stat of the hero. |
| def         | Defense stat of the hero. |
| res         | Resistance stat of the hero. |
| total       | Stat total of the hero. |
| color       | Weapon color of the hero. |
| weapon-type | Weapon type of the hero. |
| release     | Date the hero was added to the game. |
| version     | Game version when hero was added to the game. |
| majorver    | Major game version when hero was added to the game.

Columns that have not been listed are for the hero type (e.g. Duo, Special, etc.). Values for these columns are either a 0 (indicating False) or 1 (indicating True).

The dataset has also been posted on [Kaggle](https://www.kaggle.com/datasets/snoufoxx/fire-emblem-heroes-dataset/data). Go check it out!

## And who are you?

- I'm just a Fire Emblem fan who got into this series through Heroes back in February of 2019. I've only gained the skills to make this stuff in the last three years, and this was an idea that's been in the back of my mind for a while. My goals are simple: make an easily-accessible dataset of the 1300+ Heroes in the game, create visualizations out of the data, and do some simple analyses that may give insight into how much this game's changed in the last 10 years of so of this game being active.
