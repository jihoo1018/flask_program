import pandas as pd
from util.dataset import Dataset


'''  ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        #           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        #시각화를 통해 얻은 상관관계 변수(variable = feature = column) 는 
        pclass
        sex
        age
        fare
        embarked
        
        # ==null 값==
        # Age            177
        # Cabin          687
        # Embarked         2 
        '''


class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(fname=self.dataset.fname)
        return f'Train type: {type(b)}\n' \
               f'Train columns: {b.columns}\n' \
               f'Train head: {b.head()}\n' \
               f'Train null의 갯수: {b.isnull().sum()}'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)
    @staticmethod
    def create_train(this)->object:
        return this.train.drop('Survived', axis=1)


    @staticmethod
    def create_label(this) ->object:
        return this.train['Survived']


    @staticmethod
    def drop_features(this, *feature)-> object:
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this

    '''
    @staticmethod
    def pclass_ordinal(this) -> object: #1,2,3 등칸
        train = this.train
        test = this.test
        print(train['Pclass'])
        return this '''

    @staticmethod
    def sex_nominal(this) -> object: #female->1 , male ->0
        for i in [this.train, this.test]: #컴프리헨션 안됌, 리스트 중에는 안돼는 것도 존재함!
            i['Gender'] = i['Sex'].map({"male" : 0, "female" : 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object: #연령대 10대, 20대, 30대
        return this

    @staticmethod
    def fare_ordinal(this) -> object: # 비싼것, 보통, 저렴한것 (4등분, qcut 사용)
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'],4,["1","2","3","4"])
        return this


    @staticmethod
    def embarked_nominal(this) -> object: #승선항구 S,C,Q {"s" : 1, "c" : 2, "q" : 3}
        this.train = this.train.fillna({"Embarked":"S"})
        this.test = this.test.fillna({"Embarked": "S"})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this





if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.embarked_nominal(this)
    print(this.train.columns)
    print(this.train.head())