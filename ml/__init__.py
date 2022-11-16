from ml.crime import CRIME_MENUS, CrimeService, crime_menu
from ml.stroke import StrokeService, STROKE_MENUS, stroke_menu

'''if __name__ == '__main__':
    api = StrokeController()
    while True:
        menu = Common.menu(["종료", "문제제기", "데이터구하기" ,
                            "타깃변수 설정", "데이터처리", "시각화",
                            "모델링", "학습","예측"])
        if menu == "0":
            print("### 종료 ###")
            break

        elif menu == "1":
            print("### 문제제기 ###")
            api.menu_1()

        elif menu == "2":
            print("### 데이터구하기 ###")
            api.menu_2()

        elif menu == "3":
            print("### 타깃변수 설정 ###")
            api.menu_3()
        elif menu == "4":
            print("### 데이터처리 ###")
            api.menu_4()

        elif menu == "5":
            print("### 시각화 ###")
            api.menu_5()

        elif menu == "6":
            print("### 모델링 ###")

        elif menu == "7":
            print("### 학습 ###")

        elif menu == "8":
            print("### 예측 ###")

        else:
            print("### 해당 메뉴 없음 ###")'''


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

'''if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")'''
if __name__ == '__main__':
    while True:
        t = CrimeService()
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                crime_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")

