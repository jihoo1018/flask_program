'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''
from src.cmm.service.common import Common


class Contact(object):
    def __init__(self, name, pnum, mail, addr) -> None:
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr


    @staticmethod
    def new_contact():
        return Contact(input(" 이름 : "),input(" 전화 번호 : "), input(" 이메일 : "), input(" 주소 : "))

    def print_info(self):
        return f"{self.name},{self.pnum},{self.mail},{self.addr}"

    @staticmethod
    def get_contacts(ls):
        print([print(i) for i in ls])

    def __str__(self):
        print(f"{self.name},{self.pnumm}, {self.name}, {self.addr}")

    @staticmethod
    def delete_contact(ls, name):
        del ls[[i for i,j in enumerate(ls)
                if j.name == name][0]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 1:
                print("###등록###")
                ls.append(Contact.new_contact())
            elif menu == 2:
                print("###목록###")
                Contact.get_contacts(ls)
            elif menu == 3:
                print("###삭제###")
                Contact.delete_contact(ls, input("삭제할 이름: "))
            elif menu == 4:
                print("###종료###")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")


Contact.main()