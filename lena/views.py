import cv2

from lena.models import LennaModel
from util.dataset import Dataset


dataset = Dataset()
model = LennaModel()

class LennaController(object):
    def __init__(self):
        pass

    def __str__(self):
        return f""

    def preprocess(self)->object:
        pass


    @staticmethod
    def modeling(fname):
        a = model.new_model(fname)
        cv2.imshow('A', a)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




