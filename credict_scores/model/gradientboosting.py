from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd

class Model:
    def __init__(self, X, Y):
        self.estimator = GradientBoostingClassifier(
            n_estimators=20,
            learning_rate = 0.05,
            max_features=2,
            max_depth = 2,
            random_state = 0
        )

        param_grid = {
            'n_estimators': [x for x in range(10, 40, 2)],
            'learning_rate': [0.05, 0.1, 0.25, 0.5, 0.75, 1]}

        self.gridsearch = GridSearchCV(self.estimator, param_grid)

        self.X_train = X
        self.Y_train = Y


    def train(self):
        self.gridsearch.fit(self.X_train, self.Y_train)


    def predict(self,X_test):
        Y_pred = self.gridsearch.predict(X_test)

        return Y_pred




