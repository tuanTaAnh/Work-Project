from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class Model:
    def __init__(self, X, Y):
        self.random_forest = RandomForestClassifier(n_estimators=100,oob_score=True,max_features=5)
        self.X_train = X
        self.Y_train = Y


    def train(self):
        self.random_forest.fit(self.X_train, self.Y_train)


    def predict(self,X_test):
        Y_pred = self.random_forest.predict_proba(X_test)[:, 1]

        return Y_pred