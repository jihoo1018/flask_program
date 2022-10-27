from titanic.models import TitanicModel
from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common
api = TitanicController()

while True:
    menu = Common.menu(["종료", "시각화", "모델링", "머신 러닝", "배포"])
    if menu == "0":
        print("### 종료 ###")
        break

    elif menu == "1":
        print("### 시각화 ###")
        a = TitanicModel()
        b = a.new_model("train.csv")
        # print(f'Train type: {type(b)}')
        #         print(f'Train columns: {b.columns}')
        #         print(f'Train head: {b.head()}')
        #         print(f'Train null의 갯수: {b.isnull().sum()}')


        #   ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        #           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        # Age            177
        # Cabin          687
        # Embarked         2

        # plot = Plot("train.csv")
        # plot.draw_survived()
        # plot.draw_pclass()
        # plot.draw_sex()

    elif menu == "2":
        print("### 모델링 ###")
    elif menu == "3":
        print("### 머신 러닝 ###")
    elif menu == "4":
        print("### 배포 ###")
    else:
        print("### 해당 메뉴 없음 ###")