import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

LS = ["종료" ,
      "mpg 앞부분 확인",
      "mpg 뒷부분 확인",
      "행 열 출력",
      "데이터 속성 확인",
      "요약 통계량 출력",
      "문자 변수 요약 통계량 함께 출력",
      "manufacturer을 company 로 변경",
      "test 변수 생성",
      #cty 와 hwy 변수 merge 하여 total 변수 생성, 20이상이면 pass 미만이면 fail 저장
      "test 빈도표 만들기",
      "test 빈도 막대 그래프 그리기",
      # mpg 144페이지 문제
      "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교",
      "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
      "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
      #mpg 150 페이지 문제
      #메타데이터가 category,cty 데이터는 해당 raw 데이터인 객체생성후 다음 문제 풀이
      "suv/컴팩 자동차 중 어떤 자동차의 도서연비 평균이 더 높은가?",
      #mpg 153 페이지 문제
      "아우디차에서 고속도로 연비 1~5위를 출력하시오",
      #mpg 158페이지 문제
      "평균연비가 가장 높은 자동차 1~3위를 출력하시오"]

def MenuController():
    [print(f"{i}.{j}") for i, j in enumerate(LS)]
    return input("메뉴 입력: ")
class Mpg():
    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')
    def tes_t(self):
        mpg = self.mpg
        mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
        mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
        print(mpg['test'])

    def ct(self):
        tes_t= self.tes_t
        tes_t.value_counts()

    def draw_graph(self):
        self.ct().plot.bar(rot=0)
        plt.show()
        plt.savefig('./save/mpg_graph.png')

    def avg_compare(self):
        mpg = self.mpg
        avg_a = mpg.query('displ<=4')
        avg_b = mpg.query('displ>=5')
        aa = avg_a['hwy'].mean()
        bb = avg_b['hwy'].mean()
        return aa ,bb

    def company_compare(self):
        mpg = self.mpg
        mpg_audi = mpg.query('manufacturer == "audi"')
        mpg_toyota = mpg.query('manufacturer == "toyota"')
        audi = mpg_audi['cty'].mean()
        toyota = mpg_toyota['cty'].mean()
        return audi, toyota

    def company_avg(self):
        mpg = self.mpg
        compa = mpg.query('manufacturer in ["chevrolet","ford","honda"]')
        return compa['hwy'].mean()

    def new_data(self):
        mpg = self.mpg
        new_data = mpg[['class','cty']]
        return new_data

    def new_data_avg(self):
        new_data = self.new_data()
        new_data = new_data.rename(columns={'class': 'category'})
        suv = new_data.query('category == "suv"')['cty'].mean()
        compact = new_data.query('category == "compact"')['cty'].mean()
        return suv, compact

    def audi_hwy(self):
        mpg = self.mpg
        mpg_audi = mpg.query('manufacturer == "audi"')
        return mpg_audi.sort_values('hwy').head(5)

    def most_avg(self):
        mpg = self.mpg
        mpg_new = mpg.copy()
        mpg_new_2 = mpg_new.assign(total = mpg_new['hwy']+mpg_new['cty'])
        mpg_avg = mpg_new_2.assign(mean = mpg_new_2['total']/2)
        mpg_head = mpg_avg.sort_values('mean',ascending = False).head(3)
        print(mpg_head)


if __name__ =="__main__":
    while True:
        mg = Mpg()
        menu = MenuController()
        if menu == "0":
            print("종료")
            break
        elif menu =="1":
            print("1.mpg 앞부분 확인")
            print(mpg.head())
        elif menu =="2":
            print("2.mpg 뒷부분 확인")
            print(mpg.tail())
        elif menu =="3":
            print(" 3.행 열 출력")
            print(mpg.shape)
        elif menu =="4":
            print("4.데이터 속성 확인")
            print(mpg.info())
        elif menu =="5":
            print("5.요약 통계량 출력")
            print(mpg.describe())
        elif menu =="6":
            print("6.문자 변수 요약 통계량 함께 출력")
            print(mpg.describe(include="all"))
        elif menu == "7":
            print("7.manufacturer을 company 로 변경")
            mpg = mpg.rename(columns={'manufacturer': 'company'})
            print(mpg)
        elif menu =="8":
            print("8.test 변수 생성")
            mg.tes_t()
        elif menu =="9":
            print("9.test 빈도표 만들기")
            print(mg.ct())
        elif menu =="10":
            print("10.test 빈도 막대 그래프 그리기")
            print(mg.draw_graph())
        elif menu =="11":
            print("11.displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교")
            print(mg.avg_compare())
        elif menu =="12":
            print("12.아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색")
            print(mg.company_compare())
        elif menu =="13":
            print("13.쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균")
            print(mg.company_avg())
        elif menu =="14":
            print("14.suv/컴팩 자동차 중 어떤 자동차의 도서연비 평균이 더 높은가?")
            print(mg.new_data().head())
            print(mg.new_data_avg())
        elif menu =="15":
            print("15.아우디차에서 고속도로 연비 1~5위를 출력하시오")
            print(mg.audi_hwy())
        elif menu =="16":
            print("16.평균연비가 가장 높은 자동차 1~3위를 출력하시오")
            mg.most_avg()
        else:
            print("잘못된 입력값입니다.")

