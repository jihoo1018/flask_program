from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.url), arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    #디버깅
    k = range(1, len(titles))
    scrap = zip(k, titles, artists)
    [print(f"{k} 위 {i.find('a').text} : {j.find('a').text}") for k, i, j in scrap]
    #dict 로 변환
    for i in range(0, len(titles)):
        arg.dic[arg.titles[i]] = arg.artists[i]

    # csv 파일로 저장

    arg.dict_to_dataframe()
    arg.dataframe_to_csv()
