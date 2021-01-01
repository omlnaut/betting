# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_scraping.ipynb (unless otherwise specified).

__all__ = ['get_html', 'cache', 'CACHE_DIR', 'find_links_by_func', 'find_links_by_pattern']

# Cell
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Cell
def get_html(url, encoding='utf-8', bs=True):
    'Get the html code for a given url. If bs=True (which is the default), return the parsed BeautifulSoup object instead.'
    response = urllib.request.urlopen(url)
    html = response.read().decode(encoding=encoding)
    if bs: return BeautifulSoup(html, features="lxml")
    else: return html

# Cell
CACHE_DIR = Path('../data/cache')
def cache(url, cache_name):
    chache_path = CACHE_DIR/cache_name
    if chache_path.is_file():
        bs = BeautifulSoup(chache_path.open(), features="lxml")
    else:
        bs = get_html(url)
        with chache_path.open('w') as f:
            f.write(str(bs))

    return bs

# Cell
def find_links_by_func(html, func=None, return_href=True):
    """Iterate over all links of the given html-BeautifulSoup-object.
    Return a list of all links for which func returns True.
    If no func is given, return all links
    If return_href=False, return a list of BeautifulSoup link objects"""
    if func is None:
        func = lambda target: True

    links = []
    for link in html.find_all('a'):
        target = link.get('href')
        if target:
            if func(target):
                if return_href: links.append(target)
                else: links.append(link)
    return links

# Cell
def find_links_by_pattern(html, pattern, return_href=True):
    """Iterate over all links of the given html-BeautifulSoup-object.
    Return a list of all links that match the given (regex)pattern.
    Patterns passed as string will be compiled to regex."""
    if isinstance(pattern, str):
        pattern = re.compile(pattern)
    return find_links_by_func(html, func=lambda target: pattern.match(target), return_href=return_href)