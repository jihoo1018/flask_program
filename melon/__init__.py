from melon.domains import Melon
from melon.views import MelonController

if __name__=="__main__":
    melon = Melon()
    api = MelonController()
    while True:
        menu = input("0번:종료,1번:멜론차트")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("멜론차트")
            melon.domain = "https://www.melon.com/chart/index.htm?dayTime="
            melon.query_string = "2022110809"
            melon.parser = "lxml"
            melon.class_names=["ellipsis rank01", "ellipsis rank02"]
            melon.tag_name = "div"
            api.menu_1(melon)
        else:
            print("해당메뉴 없음")