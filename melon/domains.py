import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers=self.headers)
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title = {"class":"ellipsis rank01"}
        artist = {"class":"ellipsis rank02"}
        titles = soup.find_all(name="td",attrs=title)
        artists = soup.find_all(name ="td", attrs = artist)
        print(f"{i.find('a').text}: {j.find('a').text}" for i, j in zip(titles, artists))



