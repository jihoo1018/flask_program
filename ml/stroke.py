
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   id                 5110 non-null   int64
 1   gender             5110 non-null   object
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64
 4   heart_disease      5110 non-null   int64
 5   ever_married       5110 non-null   object
 6   work_type          5110 non-null   object
 7   Residence_type     5110 non-null   object
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object
 11  stroke             5110 non-null   int64
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

stroke_meta = {
    "id": "아이디",
    "gender": "성별",
    "age": "나이",
    "hypertension": "고혈압",
    "heart_disease": "심장병",
    "ever_married": "기혼여부",
    "work_type": "직종",
    "Residence_type": "거주형태",
    "avg_glucose_level": "평균혈당",
    "bmi": "체질량지수",
    "smoking_status": "흡연여부",
    "stroke":"뇌졸증"
}

class StrokeService():
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
        self.adult_stroke = None

    '''
        1.스펙보기
        '''

    def spec(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))

    '''
    2.한글 메타데이터
    '''

    def rename_meta(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        print(" --- 2.Features ---")
        print(self.my_stroke.columns)


    def menu_2(self):
        pd.set_option('display.max_columns',None)
        pd.set_option('display.max_rows', None)
        print(self.stroke.head(3))

    '''
    3. 타깃 변수(=종속 변수,dependent, y값) 설정
    입력 변수(=설명 변수, 확률 변수, X값)
    타깃 변수명: stroke(=뇌졸중)
    타깃 변수 값: 과거에 한번 이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''
    def menu_3(self):
        t = self.my_stroke
        interval = ['나이', '평균혈당', '체질량지수']
        print(f'--- 구간변수 타입 --- \n {t[interval].dtypes}')
        print(f'--- 결측값 있는 변수 --- \n {t[interval].isna().any()[lambda x: x]}')
        print(f'체질량 결측비율: {t["체질량지수"].isnull().mean():.2f}')
        # 체질량 결측비율: 0.03 는 무시한다
        pd.options.display.float_format = '{:.2f}'.format
        print(f'--- 구간변수 기초 통계량 --- \n{t[interval].describe()}')
        criterion = t['나이'] > 18
        self.adult_stroke = t[criterion]
        print(f'--- 성인객체스펙 --- \n{self.adult_stroke.shape}')
        # 평균혈당 232.64이하와 체질량지수 60.3이하를 이상치로 규정하고 제거함
        t = self.adult_stroke
        c1 = t['평균혈당'] <= 232.64
        c2 = t['체질량지수'] <= 60.3
        self.adult_stroke = self.adult_stroke[c1 & c2]
        print(f'--- 이상치 제거한 성인객체스펙 ---\n{self.adult_stroke.shape}')


    '''
    4.범주형 = ['성별', '심장병', '기혼여부', '직종', '거주형태',
                '흡연여부', '뇌졸중']
    '''

    def menu_4(self):
        t = self.adult_stroke
        category = {'성별', '심장병', '기혼여부', '직종', '거주형태', '흡연여부', '고혈압'}
        print(f"범주형변수 데이터타입\n{t[category].dtypes}")
        print(f"범주형 변수 결측값\n{t[category].isnull().sum()}")
        print(f"결측값이 있는 변수\n{t[category].isna().any()[lambda x:x]}")# 결측값이 없음
        t['성별'] = OrdinalEncoder().fit_transform(t['성별'].values.reshape(-1,1))
        t['기혼여부'] = OrdinalEncoder().fit_transform(t['기혼여부'].values.reshape(-1, 1))
        t['직종'] = OrdinalEncoder().fit_transform(t['직종'].values.reshape(-1, 1))
        t['거주형태'] = OrdinalEncoder().fit_transform(t['거주형태'].values.reshape(-1, 1))
        t['흡연여부'] = OrdinalEncoder().fit_transform(t['흡연여부'].values.reshape(-1, 1))

        self.stroke = t
        self.spec()
        print("### 프리 프로세스 종료 ###")
        t.to_csv('./save/stroke.csv')





    def menu_5(self):
        pass



    def menu_6(self):
        pass

    def menu_7(self):
        pass

    def menu_8(self):
        pass
