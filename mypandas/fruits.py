"""
과일 판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
다만, 실행했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
"""
from util.common import Common


class Fruit(object):

    def __init__(self) -> None:
        self.menu = ["바나나","사과","망고"]

    @staticmethod
    def print():
        title = "###과일번호표###"
        aster = "*"*40
        fruit = input("과일 이름: ")
        print(title)
        print(aster)
        print(fruit)
        print(aster)



    @staticmethod
    def new_fruit():
        return input("과일이름: ")

    @staticmethod
    def get_fruit(ls):
        print([print(i) for i in ls])

    def __str__(self):
        return f"{self. fruit}"

    @staticmethod
    def delete_fruit(ls, fruit=None):
        del ls[[i for i, j in enumerate(ls)
                if j.fruit == fruit][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu
            if menu == 0:
                break
            elif menu == 1:
                print("추가")
                ls.append(Fruit.new_fruit())
            elif menu == 2:
                print("목록")
                Fruit.get_fruit(ls)
            elif menu == 3:
                print("삭제")
                Fruit.delete_fruit(ls, input("삭제할 과일 이름: "))
            else:
                print("없는 메뉴입니다. 다시 선택해주세요")

Fruit.main()

