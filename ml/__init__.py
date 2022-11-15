from ml.stroke import StrokeService



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

ls = ["종료", "데이터구하기", "한글화" ,
        "타깃변수 설정", "데이터처리", "샘플링",
        "모델링", "학습","예측"]
switch = {
    "1": lambda t: t.spec(),
    "2": lambda t: t.rename_meta(),
    "3": lambda t: t.menu_3(),
    "4": lambda t: t.menu_4(),
    "5": lambda t: t.sampling(),
    "6": lambda t: t.menu_6(),
    "7": lambda t: t.menu_7(),
    "8": lambda t: t.menu_8()
        }
if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(ls)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                switch[menu](t)
            except KeyError:
                print(" ### Error ### ")