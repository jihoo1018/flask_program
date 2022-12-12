
import pandas as pd

from src.cmm.service.dataset import Dataset


class BicycleModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        pass

    def prerprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = "../../../static/data/dam/bicycle/"
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df


    def create_train(self):
        pass

    def create_labe(self):
        pass
