import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class WineQualityDeterminator():
    random_forest = RandomForestClassifier(n_estimators=300, max_depth=10)

    @classmethod
    def train(cls):
        wines = pd.read_csv("data/winequality.csv")

        predictors = [
            "fixed acidity",
            "volatile acidity",
            # "citric acid",
            "residual sugar",
            "chlorides",
            # "free sulfur dioxide",
            "total sulfur dioxide",
            # "density",
            # "pH",
            "sulphates",
            "alcohol",
        ]

        wines['q2'] = pd.cut(wines['quality'], [0, 5, 6, 9], labels=['0', '1', '2'])

        wines.q2 = pd.Categorical(wines.q2).codes

        X = wines[predictors].values
        Y = wines['q2'].values

        cls.random_forest.fit(X, Y)

    @classmethod
    def determinate(cls, wines_properties):
        return str(cls.random_forest.predict(wines_properties)[0])
