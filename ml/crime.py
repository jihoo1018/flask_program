import googlemaps
import pandas as pd

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
    "3" : lambda t: t.turn_xls(),
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
        self.pop = pd.read_excel('./data/pop_in_seoul.xls',skiprows=[0,2])
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

    def turn_xls(self):
        pop = self.pop
        pop = pop.iloc[:,[1,3,6,9,13]]
        print(pop.head(3))




    def rename_meta(self):
        pass

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