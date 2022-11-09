import pandas as pd
LS = ["종료" ,"mpg 앞부분 확인", "mpg 뒷부분 확인", "행 열 출력", "데이터 속성 확인", "요약 통계량 출력", "문자 변수 요약 통계량 함께 출력"]
m = pd.read_csv('./data/mpg.csv')
def MenuController():
    [print(f"{i}.{j}") for i, j in enumerate(LS)]
    return input("메뉴 입력: ")
if __name__ =="__main__":
    while True:
        menu = MenuController()
        if menu == "0":
            print("종료")
            break
        elif menu =="1":
            print("1.mpg 앞부분 확인")
            print(m.head())
        elif menu =="2":
            print("2.mpg 뒷부분 확인")
            print(m.tail())
        elif menu =="3":
            print(" 3.행 열 출력")
            print(m.shape)
        elif menu =="4":
            print("4.데이터 속성 확인")
            print(m.info())
        elif menu =="5":
            print("5.요약 통계량 출력")
            print(m.describe())
        elif menu =="6":
            print("6.문자 변수 요약 통계량 함께 출력")
            print(m.describe(include="all"))
        else:
            print("잘못된 입력값입니다.")

