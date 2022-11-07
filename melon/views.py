from melon.domains import Melon


class MenuController:
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(arg):
        melon = Melon(arg)
        melon.scrap()