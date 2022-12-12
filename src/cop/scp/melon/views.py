
from src.cop.scp.melon.services import MelonMusic


class MelonController:
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(arg):
        MelonMusic(arg)
