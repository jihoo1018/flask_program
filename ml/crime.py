import googlemaps
import numpy as np
import pandas as pd
import pickle

CRIME_MENUS = [ "EXIT", #0
                "SPEC",#1
                "MERGE",#2
                "INTERVAL",#3 18세이상만 사용함
                "NORMINAL",#4
                "ORDINAL",#5
                "PARTITION",#6
                "미완성: FIT",#7
                "미완성: PREDICATE"]
crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pas(),
    "4" : lambda t: t.categorical_variables(),
    "5" : lambda t: t.sampling(),
    "6" : lambda t: print(" ** No Function ** "),
    "7" : lambda t: print(" ** No Function ** "),
    "8" : lambda t: print(" ** No Function ** ")
}

class CrimeService():
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./data/pop_in_seoul.xls',
                                 skiprows=[0,2],usecols=['자치구','합계','한국인','등록외국인','65세이상고령자'])
        self.ls = [self.crime,self.cctv, self.pop]


    '''1. 데이터 정보 파악
    crime
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
       '절도 검거', '폭력 발생', '폭력 검거'],
      dtype='object')
      cctv
      Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')'''


    def spec(self):
        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                               f"--- 2.Features ---\n{x.columns}\n"
                               f"--- 3.Info ---\n{x.info}\n"
                               f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                               f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                               f"--- 6.Describe ---\n{x.describe()}\n"
                               f"--- 7.Describe All ---\n{x.describe(include='all')}"
                               ))(i) for i in self.ls]

    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역이름: {name} ")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f"서울 시내 경찰서는 총 {len(station_names)}개 이다")
        [print(f" {str(i)}") for i in station_names]

        gmap = (lambda x: googlemaps.Client(key=x))("")
        print(gmap.geocode("서울중부경찰서",language="ko"))
        print("###API 에서 주소추출 시작###")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmap.geocode(name,language="ko")
            print(f"name{i} = {_[0].get('formatted_address')}")
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv("./save/police_pos.csv", index= False)
        crime.to_pickle("./save/police_pos.pkl")
        print(pd.read_pickle('./save/police_pos.pkl'))


    def save_cctv_pas(self):
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]:'구별'},inplace=True)
        pop.rename(columns={
            pop.columns[0]:'구별',
            pop.columns[1]:'인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
        },inplace=True)
        pop.drop(index=26,inplace=True)
        print("*"*100)
        pop['외국인비율'] = pop['외국인'].astype(int)/pop['인구수'].astype(int)*100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        cctv.drop(['2013년도 이전','2014년','2015년','2016년'],axis=1,inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구별")
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
        """
        cctv_pop.to_pickle("./save/cctv_pop.pkl")
        print(pd.read_pickle('./save/cctv_pop.pkl'))


    def interval_variables(self):
        pass

    def ratio_variables(self):
        pass

    def norminal_variables(self):
        pass

    def ordinal_variables(self):
        pass

    def target(self):
        pass