from util.dataset import Dataset
import pandas as pd


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
        this.context = "./data/"
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df


    def create_train(self):
        pass

    def create_labe(self):
        pass
