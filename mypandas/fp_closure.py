'''from dataclasses import dataclass

@dataclass
class OOP:
    x = 30

    def foo(self):
        x = self.x
        print("OOP 출력: "+str(x))

x = 10
def foo():
    global x
    x = x +20
    print("FP 출력: "+str(x))'''



def A():
    x = 10
    def B():
        nonlocal x
        x = 20
    B()
    print(x)

A()

def A1():
    x = 10
    y = 100
    def B1():
        x = 20
        def C1():
            nonlocal x
            nonlocal y
            x = x+30
            y = y+300
            print(x)
            print(y)
        C1()
    B1()
A1()

x = 1
def A2():
    x = 10
    def B2():
        x = 20
        def C2():
            global x
            x = x+30
            print(x)
        C2()
    B2()
A2()

def calc():
    a = 3
    b = 5
    # return lambda x:a *x +b
    ## total = 0
    def mul_add(x):
        ## nonlocal total
        ## total = total +a *x +b
        ## print(total)
        return a * x +b
    return mul_add

c = calc()
print(c(1),c(2),c(3),c(4),c(5))


def calc2():
    a = 3
    b = 5
    t = 0
    def mul_add(x):
        nonlocal t
        t = t+ ( a * x + b)
        print("클로저 1 결과:"+str(t))

    def mul_add_2(x):
        nonlocal t
        t = t + (a * x -b)
        print("클로저 2 결과:" + str(t))



    return {"덧셈1 ": mul_add, "덧셈 2" :mul_add_2}


if __name__ == '__main__':
    # f = OOP()
    # f.foo()
    # foo()
    # print("전역출력: " + str(x))
    # A()
    c = calc2()
    # print(c(1), c(2), c(3), c(4), c(5), )
    print( "클로저 1: "+str(c["덧셈1 "](2)))
    print( " 클로저 2: "+str(c["덧셈 2"](2)))