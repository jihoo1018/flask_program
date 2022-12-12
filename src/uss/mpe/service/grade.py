"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
유관순 90 90 92 272 90.6 A
********************************
"""
from src.cmm.service.common import Common


class Grade(object):

    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.set_total()
        self.set_avg()
        self.set_grade()

    def set_total(self):
        self.total = self.ko + self.en + self.ma

    def set_avg(self):
        self.avg = self.total / 3

    def set_grade(self):
        avg = self.avg
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        else: grade = "F"
        self.grade = grade

    def __str__(self):
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.total} {self.avg} {self.grade}")

    @staticmethod
    def new_grade():
        return Grade(input("이름: "),
                    int(input("국어: ")),
                    int(input("영어: ")),
                    int(input("수학: ")))

    @staticmethod
    def print_table(ls):
        print("### 성적표 ###")
        print("********************************")
        print("이름 국어 영어 수학 총점 평균 학점")
        print("*******************************")
        [print(i) for i in ls]
        print("********************************")


    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 1:
                print(" ### 성적 등록 ### ")
                ls.append(Grade.new_grade())
            elif menu == 2:
                print(" ### 성적 출력 ### ")
                Grade.print_table(ls)
            elif menu == 3:
                print(" ### 성적 삭제 ### ")
                Grade.delete_grade(ls, input("삭제할 이름: "))
            elif menu == 4:
                print(" ### 종료 ### ")

                break

Grade.main()