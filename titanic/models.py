import pandas as pd
from util.dataset import Dataset


class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b = pd.read_csv("train.csv")
        return f'Train type: {type(b)}'
        #         print(f'Train columns: {b.columns}')
        #         print(f'Train head: {b.head()}')
        #         print(f'Train null의 갯수: {b.isnull().sum()}')



    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        return df

    def create_train(self):
        pass

    def create_label(self):
        pass
