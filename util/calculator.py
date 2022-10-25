from util.common import Common


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def execute(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "잘못된 연산 입니다."
        print(f"{num1} {op} {num2} = {result}")


    @staticmethod
    def new_calc():
        num1 = int(input("숫자 : "))
        op = input("+, -, *, /, %")
        num2 = int(input("숫자 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def get_calc(ls):
        [(print(i))for i in ls]

    def __str__(self):
        print(f"{self.num1}{self.op}{self.num2}{self.result}")

    @staticmethod
    def delete_calc(ls, num1):
        del ls[[i for i, j in enumerate(ls)
                if j.num1 == num1][0]]



    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu
            if menu == 0:
                break
            elif menu == 1:
                print("등록")
                calculator = Calculator.new_calc()
                ls.append(calculator)
            elif menu == 2:
                print("목록")
                Calculator.get_calc(ls)
            elif menu == 3:
                print("삭제")
                Calculator.delete_calc(ls, int(input("삭제할 숫자: ")))
            else:
                print("없는 메뉴 입니다. 다시 선택해 주세요")


Calculator.main()