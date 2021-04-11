import lightgbm as lgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd


class Model:
    def __init__(self, X, Y):
        self.estimator = lgb.LGBMClassifier(
                        learning_rate=0.125,
                        metric='binary_logloss',
                        n_estimators=20,
                        num_leaves=38
                        )

        param_grid = {
            'n_estimators': [x for x in range(24, 40, 2)],
            'learning_rate': [0.10, 0.125, 0.15, 0.175, 0.2]}

        self.gridsearch = GridSearchCV(self.estimator, param_grid)

        self.X_train, self.X_validation, self.y_train, self.y_validation = train_test_split(X, Y, test_size=0.1, random_state=21)

    def train(self):
        print("X_train.shape", self.X_train.shape)
        print("X_validation.shape", self.X_validation.shape)
        print("y_train.shape", self.y_train.shape)
        print("y_validation.shape", self.y_validation.shape)
        for y in self.y_train:
            print(y, end="; ")
        print("\nEND")
        self.gridsearch.fit(self.X_train, self.y_train,
                       eval_set=[(self.X_validation, self.y_validation)],
                       eval_metric=['auc', 'binary_logloss'],
                       early_stopping_rounds=5)

    def predict(self,X_test):
        print(X_test)
        Y_pred = self.gridsearch.predict_proba(X_test)[:, 1]

        return Y_pred


