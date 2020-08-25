from betting.data.football_uk import *
from betting.utility import run_in_parallel

from pathlib import Path
from urllib.request import urlretrieve

data_dir = Path('../../data/football_data_uk')

def download_csv(league):
	for season in FOOTBALL_DATA_SEASONS:
		print(league.name, season)
		league_dir = data_dir / f'{league.name}'
		league_dir.mkdir(exist_ok=True, parents=True)
		filepath = league_dir / f'{league.code}_{season}.csv'
		download_link = build_full_link(season, league.code, FOOTBALL_DATA_LINK)
		urlretrieve(download_link, filename=filepath)


if __name__=='__main__':
	run_in_parallel(download_csv, FOOTBALL_DATA_LEAGUES)

