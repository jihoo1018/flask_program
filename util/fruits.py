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
    def print_menu():
        print("1. 과일 등록")
        print("2. 과일 목록")
        print("3. 과일 삭제")
        print("0. 종료")
        menu = input("메뉴 선택: ")
        return int(menu)


    @staticmethod
    def new_fruit():
        return input("과일이름: ")

    @staticmethod
    def get_fruit(ls):
        print([i.print_info() for i in ls])

    def print_info(self):
        return f"{self. fruit}"

    @staticmethod
    def delete_fruit(ls):
        del ls[[i for i, j in enumerate(ls)
                if j.fruit == fruit][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Fruit.print_menu
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

