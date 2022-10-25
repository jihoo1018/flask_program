from glob import escape

from util.common import Common

class Bmi(object):
    def __init__(self, name, cm, kg) -> None:
        self.name = name
        self.cm = cm
        self.kg = kg
        self.biman = ""

    def execute(self):
        self.print_biman()
        self.get_biman()
        self.biman = self.get_biman()

    def get_bmi(self):
        kg = self.kg
        m = self.cm/100
        return kg / m ** 2

    def get_biman(self):
        bmi = self.get_bmi()
        biman = ""
        if bmi>= 35:
            biman = "고도비만"
        elif bmi>= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi>= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi>= 23:
            biman = "과체중"
        elif bmi>= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman


    def print_biman(self):
        name= self.name
        cm = self.cm
        kg = self.kg
        biman = self.biman
        title = "### 비만도계산 ###"
        aster = "*" *40
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        result = f"{name} {cm} {kg} {biman}"
        print(f"{title}\n {aster}\n {schema}\n {aster} \n {result} \n {aster} ")


    @staticmethod
    def new_profile():
        name = input("이름: ")
        kg = int(input("몸무게 : "))
        cm = int(input("키 :"))
        return Bmi(name, cm, kg)

    @staticmethod
    def get_profile(ls):
        [print(i) for i in ls]



    def __str__(self):
        return f"{self.name}{self.cm}{self.kg}{self.biman}"

    @staticmethod
    def delete_profile(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]



    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 0:
                break
            if menu == 1:
                print("등록")
                profile = Bmi.new_profile()
                ls.append(profile)
            if menu == 2:
                print("목록")
                Bmi.get_profile(ls)
            if menu == 3:
                print("삭제")
                Bmi.delete_profile(ls, input("삭제할 이름: "))
            else:
                print("없는 메뉴 입니다. 다시 선택해 주세요")

Bmi.main()
