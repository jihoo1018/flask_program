from melon.views import MenuController
from util.common import Common

if __name__ == '__main__':
    api = MenuController()
    while True:
        menus = ["종료", "멜론뮤직 스크랩핑"]
        menu = Common.menu(menus)
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            api.menu_1(arg="https://www.melon.com/chart/day/index.htm")
        else:
            print("잘못된 선택 입니다")