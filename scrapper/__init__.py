from scrapper.domains import MusicRanking
from scrapper.views import MenuController
from util.common import Common

if __name__ == '__main__':
    api = MenuController()
    m = MusicRanking()
    while True:
        menus = ["종료", "벅스뮤직 스크랩핑"]
        menu = Common.menu(menus)
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221101"
            m.parser = "lxml"
            m.class_names = ["title","artist"]
            m.tag_name = "p"
            api.menu_1(m)
        else:
            print("잘못된 선택 입니다")

