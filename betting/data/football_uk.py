# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_data.ipynb (unless otherwise specified).

__all__ = ['FOOTBALL_DATA_LINK', 'unique_seasons', 'FOOTBALL_DATA_SEASONS', 'FOOTBALL_DATA_LEAGUE_CODES',
           'FOOTBALL_DATA_LEAGUE_NAMES', 'build_full_link']

# Cell
import urllib.parse
import re
import functools
from dataclasses import dataclass

# Cell
FOOTBALL_DATA_LINK = r'https://www.football-data.co.uk/data.php'

# Cell
def unique_seasons(html):
    'Returns a list of all unique seasons for which result.csv files are found in the given html'
    csv_links = find_links_by_pattern(html, 'mmz4281/\d{4}/\w*\d\.csv')
    return set(csv_link.split('/')[1] for csv_link in csv_links)

# Cell
FOOTBALL_DATA_SEASONS = ['1314', '9900', '1112', '9697', '0708', '1920', '9798', '1819', '0405', '9596', '0001', '1213', '0203', '0102', '0809', '1617', '1516', '1718', '1011', '0506', '0607', '9899', '0304', '1415', '0910']

# Cell
FOOTBALL_DATA_LEAGUE_CODES = ['E0', 'E0', 'D1', 'I1', 'SP1', 'F1', 'N1', 'B1', 'P1', 'T1', 'G1']
FOOTBALL_DATA_LEAGUE_NAMES = ['england', 'scotland', 'germany', 'italy', 'spain', 'france', 'netherlands', 'belgium', 'portugal', 'turkey', 'greece']

# Cell
def build_full_link(season, league_code, mainpage_link):
    file_url = f'mmz4281/{season}/{league_code}.csv'
    return urllib.parse.urljoin(mainpage_link, file_url)