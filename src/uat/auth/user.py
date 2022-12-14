'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오
'''
from src.cmm.service.common import Common


class Member(object):
    def __init__(self, id, pw, name) ->None:
        self.id = id
        self.pw = pw
        self.name = name

    def print(self):
        print(f"{self.id},{self.pw}, {self.name}")

    @staticmethod
    def new_member():
        name = input("이름: ")
        id = input("id: ")
        pw = input("pw: ")
        return Member(name, id, pw)


    @staticmethod
    def get_member(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_member(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    def __str__(self):
        return f"{self.name}{self.id}{self.pw}"

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 1:
                print("###회원가입###")
                member = Member.new_member()
                ls.append(member)
            elif menu == 2:
                print("### 목록 ###")
                Member.get_member(ls)
            elif menu == 3:
                print('### 탈퇴###')
                Member.delete_member(ls,input("삭제할 이름: "))
            elif menu == 0:
                print('### 종료 ###')
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Member.main()