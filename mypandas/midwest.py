import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

LS = ["종료",
         "메타데이터 출력",
         "poptotal/popasian 변수를 total/asian로 이름변경",
         "전체 인구 대비 아시아 인구 백분율 변수 추가",
         "아시아 인구 백분율 전체 평균을 large/small 로 분류",
         "large/small 빈도표와 빈도막대그래프 작성"]
mdwest = pd.read_csv('./data/midwest.csv')
def MenuController():
    [print(f"{i}.{j}")for i,j in enumerate(LS)]
    return input("메뉴 입력: ")
if __name__ == "__main__":
    while True:
        menu = MenuController()
        if menu == "0":
            print("종료")
            break
        elif menu =="1":
            print("1.메타데이터 출력")
            print(mdwest)
        elif menu =="2":
            print("2.poptotal/popasian 변수를 total/asian로 이름변경")
            mdwest = mdwest.rename(columns={'poptotal':'total'})
            mdwest = mdwest.rename(columns ={'popasian':'asian'})
            print(mdwest)
        elif menu =="3":
            print("3.전체 인구 대비 아시아 인구 백분율 변수 추가")
            mdwest['all'] = (mdwest['asian']/mdwest['total'])*100
            print(mdwest['all'])
        elif menu =="4":
            print("4.아시아 인구 백분율 전체 평균을 large/small 로 분류")
            mdwest['all'].mean()
            mdwest['group'] = np.where(mdwest['all']>0.48,'large','small')
            print(mdwest['group'])
        elif menu =="5":
            print("5.large/small 빈도표와 빈도막대그래프 작성")
            count_group = mdwest['group'].value_counts()
            print(count_group)
            print(count_group.plot.bar(rot=0))
        else:
            print("잘못된 입력입니다. ")
