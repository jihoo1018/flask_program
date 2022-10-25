class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def print_menu():
        for i, j in enumerate(["종료", "등록", "목록", "삭제"]):
            print(f"{i}.{j}")
        return int(input("메뉴 선택: "))

    @staticmethod
    def main():
        Common.print_menu()

Common.main()