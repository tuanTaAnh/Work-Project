from read_data.read_csv import read_data, read_data_dt
import lightgbm as lgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from config import config
import pandas as pd
import numpy as np
from model.lgbm import Model as lgbmmodel
from model.random_forrest import Model as randomforestmodel
from model.gradientboosting import Model as gradientboostingmodel

trainpath = r"/Users/taanhtuan/Desktop/workproject/credict_scores/data/train.csv"
testpath = r"/Users/taanhtuan/Desktop/workproject/credict_scores/data/test.csv"


weight = 0.8


if __name__ == "__main__":

    train = pd.read_csv(trainpath)
    test = pd.read_csv(testpath)

    data = pd.concat([train, test], axis=0)

    data.Field_1.fillna(-999, inplace=True)

    datetime_data = data[data.Field_1 != -999]
    no_datetime_data = data[data.Field_1 == -999]
    # print(datetime_data)

    X_train_dt, Y_train_dt, X_test_dt, id_list_dt = read_data_dt(datetime_data, config.dropped_traincolumns)
    print("type(X_train_dt)", type(X_train_dt))
    print("type(Y_train_dt)", type(Y_train_dt))
    X_train_no_dt, Y_train_no_dt, X_test_no_dt, id_list_no_dt = read_data_dt(no_datetime_data, config.dropped_traincolumns)


    estimator1 = lgbmmodel(X_train_dt, Y_train_dt)
    estimator1.train()
    #
    # pred_dt = estimator1.predict(X_test_dt)
    #
    #
    # # estimator2 = lgbmmodel(X_train_no_dt, Y_train_no_dt)
    # # estimator2.train()
    # #
    # # pred_no_dt = estimator2.predict(X_test_no_dt)
    #
    # id_list_dt = id_list_dt.values.tolist()
    # id_list_no_dt = id_list_no_dt.values.tolist()
    #
    # id_list = np.concatenate([id_list_dt,id_list_no_dt])
    # id_list = pd.Series(id_list)


    # pred_list = np.concatenate([pred_dt,pred_no_dt])
    # pred_list = pd.Series(pred_list)
    #
    # label_list = {"id": id_list,"label": pred_list}
    #
    # test_df = pd.DataFrame(label_list)
    #
    # test_df.sort_values(by="id", inplace=True)
    #
    #
    # test_df.to_csv(r"D:\Projects\credict_scores\data\submission.csv", index=False, header=True,encoding='utf-8')















""""

    print("len(data_test_dt)",len(data_test_dt))
    print("len(pred1)",len(pred1))
    print("len(label_dt)",len(label_dt))
    print("len(X_test_dt)",len(X_test_dt))
    print()

    print("len(data_test_no_dt)",len(data_test_no_dt))
    print("len(label_no_dt)",len(label_no_dt))
    print("len(X_test_no_dt)",len(X_test_no_dt))
    print()


    print("len(data_test",len(data_test))
    
    
    
print(len(config.Field_45))
    for i, ele in enumerate(config.Field_45):
        print(i, " ", len(ele))

    X, Y, _ = read_data(trainpath,config.dropped_traincolumns,istrain=True)
    X_test, _, idtestlist = read_data(testpath,config.dropped_testcolumns,istrain=False)

    estimator1 = lgbmmodel(X,Y)
    estimator1 = randomforestmodel(X, Y)

    estimator1.train()
    print("DONE LGBM")

    pred1 = estimator1.predict(X_test)

    estimator = randomforestmodel(X, Y)

    estimator2 = gradientboostingmodel(X, Y)
    print("DONE GRADIENTBOOSTING")

    estimator2.train()

    pred2 = estimator2.predict(X_test)

    pred0 = (weight * pred1) + ((1 - weight) * pred2)

    testdata = {"id": idtestlist, "label": pred1}

    test_df = pd.DataFrame(testdata)

    test_df.to_csv (r"D:\Projects\credict_scores\data\submission.csv", index = False, header=True)


    print(len(idtestlist))
    print(len(y_pred_probs))
    for idx in range(len(idtestlist)):
        print(idtestlist[idx]," ",y_pred_probs[idx])


"""





