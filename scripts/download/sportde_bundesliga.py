from betting.data.sportde import *
from betting.scraping import *
from pathlib import Path
from multiprocessing import Pool

save_path = Path('../../data/sportde/bundesliga')
start_link = 'https://www.sport.de/fussball/deutschland-bundesliga/se580/2006-2007/ergebnisse-und-tabelle'
start_bs = get_html(start_link)
season_urls = season_links_from_page(start_bs)

target_seasons = [[season, season_urls[season]] for season in season_urls.keys() if 20>=int(season[:2])>=5]

def process_season(info):
	season, url = info
	print(season)
	standings, matchdays, games = scrape_season(season, url)
	save_season(standings, matchdays, games, 'bundesliga', save_path)

if __name__=='__main__':
	with Pool(6) as p:
		p.map(process_season, target_seasons)