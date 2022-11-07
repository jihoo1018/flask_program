from scrapper.services import BugsMusic


class MenuController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)