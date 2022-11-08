import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup

'''def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers=self.headers)
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title = {"class":"ellipsis rank01"}
        artist = {"class":"ellipsis rank02"}
        titles = soup.find_all(name="td",attrs=title)
        artists = soup.find_all(name ="td", attrs = artist)
        print(f"{i.find('a').text}: {j.find('a').text}" for i, j in zip(titles, artists))'''
def MelonMusic(arg):
    urlheader = urllib.request.Request(arg.domain +arg.query_string, headers={'User-Agent': "Mozilla/5.0"})
    htmlurl = urllib.request.urlopen(urlheader).read()
    soup = BeautifulSoup(htmlurl, arg.parser)
    # soup = BeautifulSoup(urlopen(arg.domain +arg.query_string), arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name,attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name,attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} :{k}") for i, j, k, in zip(range(1, len(titles)), titles,artists)]
    diction = {}
    for i,j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()

