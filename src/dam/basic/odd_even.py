import random

from src.cmm.service.common import Common


class Odd(object):
    def __init__(self) -> None:
        pass



    def print(self):
        rl = random()
        print(rl.get_random(10,100,10))
        for i in rl.get_random(10,100,10):
            if i % 2 == 0:
                print(f"짝수 : {i}")
            else:
                print(f"홀수: {i}")



    def new_odd(self):
        pass

    @staticmethod
    def get_odd():
        pass

    @staticmethod
    def delete_odd():
        pass





    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu
            if menu == 0:
                break
            elif menu == 1:
                print("추가")
                odd = Odd.new_odd()
                ls.append(odd)
            elif menu == 2:
                print("목록")
                Odd.get_odd(ls)
            elif menu == 3:
                print("삭제")
                Odd.delete_odd(ls)
            else:
                print("없는 메뉴입니다. 다시 선택해주세요")


    # [i for i in rl]
    # print([f"짝수 : {i}" if i %2 == 0 else f"홀수: {i}" for i in rl.get_random(10,100,10)])
    # [i if True else i for i in []]