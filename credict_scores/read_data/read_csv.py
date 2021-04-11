import pandas as pd
from preprocess.ogirinalencoding import check
from config import config
from preprocess.datetimeencoding import start_stop_proces

path = r"D:\Projects\credict_scores\data\train.csv"


def read_data_dt(data_df, dropped_columns):

    print("len(data_df)",len(data_df))
    # column maCv
    data_df["maCv"] = data_df["maCv"].apply(lambda x : check(x,config.maCv))

    # column gioiTinh
    data_df["gioiTinh"] = data_df["gioiTinh"].apply(lambda x: check(x, config.gioiTinh))

    # column info_social_sex
    data_df["info_social_sex"] = data_df["info_social_sex"].apply(lambda x: check(x, config.info_social_sex))

    # column brief
    data_df["brief"].replace("notfound", -999, inplace=True)
    data_df["brief"] = data_df["brief"].apply(lambda x: check(x, config.brief))

    # column Field_4
    data_df["Field_4"] = data_df["Field_4"].apply(lambda x : check(x,config.Field_4))

    # column Field_12
    data_df["Field_12"] = data_df["Field_12"].apply(lambda x: check(x, config.Field_12))

    # column Field_36
    data_df["Field_36"] = data_df["Field_36"].apply(lambda x: check(x, config.Field_36))

    # column Field_38
    data_df["Field_38"].replace("DN", -999, inplace=True)
    data_df["Field_38"].replace("TN", -999, inplace=True)
    data_df["Field_38"] = data_df["Field_38"].astype("float32")

    # column Field_45
    data_df["Field_45"] = data_df["Field_45"].apply(lambda x: check(x, config.Field_45))

    # column Field_47
    data_df["Field_47"] = data_df["Field_47"].apply(lambda x: check(x, config.Field_47))

    # column Field_54
    data_df["Field_54"].replace(" P. Tân Phú", None, inplace=True)
    data_df["Field_54"].replace("1", None, inplace=True)
    data_df["Field_54"] = data_df["Field_54"].apply(lambda x: check(x, config.Field_54))

    # column Field_55
    data_df["Field_55"] = data_df["Field_55"].apply(lambda x: check(x, config.Field_55))

    # column Field_56
    data_df["Field_56"] = data_df["Field_56"].apply(lambda x: check(x, config.Field_56))

    # column Field_61
    data_df["Field_61"] = data_df["Field_61"].apply(lambda x: check(x, config.Field_61))

    # column Field_62
    data_df["Field_62"].replace("Ngoài quốc doanh Quận 7",None,inplace=True)
    data_df["Field_62"] = data_df["Field_62"].apply(lambda x: check(x, config.Field_62))

    # column Field_65
    data_df["Field_65"].replace("5", None, inplace=True)
    data_df["Field_65"] = data_df["Field_65"].apply(lambda x: check(x, config.Field_65))

    # column Field_66
    data_df["Field_66"] = data_df["Field_66"].apply(lambda x: check(x, config.Field_66))

    # maCv, gioiTinh, info_social_sex,
    # Field_4, Field_12, Field_36, Field_47, Field_54, Field_55, Field_56, Field_61, Field_62, Field_65, Field_66



    column_f = start_stop_proces(pd.to_datetime(data_df["F_startDate"]).tolist(),pd.to_datetime(data_df["F_endDate"]).tolist(),is_hour=False)
    column_e = start_stop_proces(pd.to_datetime(data_df["E_startDate"]).tolist(), pd.to_datetime(data_df["E_endDate"]).tolist(),is_hour=False)
    column_c = start_stop_proces(pd.to_datetime(data_df["C_startDate"]).tolist(), pd.to_datetime(data_df["C_endDate"]).tolist(),is_hour=False)
    column_g = start_stop_proces(pd.to_datetime(data_df["G_startDate"]).tolist(), pd.to_datetime(data_df["G_endDate"]).tolist(),is_hour=False)
    column_a = start_stop_proces(pd.to_datetime(data_df["A_startDate"]).tolist(), pd.to_datetime(data_df["A_endDate"]).tolist(),is_hour=False)
    # column_12 = start_stop_proces(pd.to_datetime(data_df["Field_2"]).tolist(), pd.to_datetime(data_df["Field_1"]).tolist(),is_hour=True)
    column_43_44 = start_stop_proces(pd.to_datetime(data_df["Field_43"]).tolist(), pd.to_datetime(data_df["Field_44"]).tolist(), is_hour=True)
    # for f in column_f:
    #     print(f)


    data_df['columnf'] = column_f
    data_df['columne'] = column_e
    data_df['columnc'] = column_c
    data_df['columng'] = column_g
    data_df['columna'] = column_a
    data_df['column4344'] = column_43_44

    # Field_38, brief

    data_df.fillna(-999, inplace=True)

    Y_train = data_df.label[data_df.id < 53030]

    data = data_df.drop(dropped_columns, axis=1)

    X_train = data[data_df.id < 53030]

    X_test = data[data_df.id >= 53030]

    id_list = data_df.id[data_df.id >= 53030]

    return X_train, Y_train, X_test, id_list





def read_data(path,dropped_columns,istrain = True):
    data_df = pd.read_csv(path)

    # column maCv
    data_df["maCv"] = data_df["maCv"].apply(lambda x : check(x,config.maCv))

    # column gioiTinh
    data_df["gioiTinh"] = data_df["gioiTinh"].apply(lambda x: check(x, config.gioiTinh))

    # column info_social_sex
    data_df["info_social_sex"] = data_df["info_social_sex"].apply(lambda x: check(x, config.info_social_sex))

    # column brief
    data_df["brief"].replace("notfound", -999, inplace=True)
    data_df["brief"] = data_df["brief"].apply(lambda x: check(x, config.brief))

    # column Field_4
    data_df["Field_4"] = data_df["Field_4"].apply(lambda x : check(x,config.Field_4))

    # column Field_12
    data_df["Field_12"] = data_df["Field_12"].apply(lambda x: check(x, config.Field_12))

    # column Field_36
    data_df["Field_36"] = data_df["Field_36"].apply(lambda x: check(x, config.Field_36))

    # column Field_38
    data_df["Field_38"].replace("DN", -999, inplace=True)
    data_df["Field_38"].replace("TN", -999, inplace=True)
    data_df["Field_38"] = data_df["Field_38"].astype("float32")

    # column Field_45
    data_df["Field_45"] = data_df["Field_45"].apply(lambda x: check(x, config.Field_45))

    # column Field_47
    data_df["Field_47"] = data_df["Field_47"].apply(lambda x: check(x, config.Field_47))

    # column Field_54
    data_df["Field_54"].replace(" P. Tân Phú", None, inplace=True)
    data_df["Field_54"].replace("1", None, inplace=True)
    data_df["Field_54"] = data_df["Field_54"].apply(lambda x: check(x, config.Field_54))

    # column Field_55
    data_df["Field_55"] = data_df["Field_55"].apply(lambda x: check(x, config.Field_55))

    # column Field_56
    data_df["Field_56"] = data_df["Field_56"].apply(lambda x: check(x, config.Field_56))

    # column Field_61
    data_df["Field_61"] = data_df["Field_61"].apply(lambda x: check(x, config.Field_61))

    # column Field_62
    data_df["Field_62"].replace("Ngoài quốc doanh Quận 7",None,inplace=True)
    data_df["Field_62"] = data_df["Field_62"].apply(lambda x: check(x, config.Field_62))

    # column Field_65
    data_df["Field_65"].replace("5", None, inplace=True)
    data_df["Field_65"] = data_df["Field_65"].apply(lambda x: check(x, config.Field_65))

    # column Field_66
    data_df["Field_66"] = data_df["Field_66"].apply(lambda x: check(x, config.Field_66))

    # maCv, gioiTinh, info_social_sex,
    # Field_4, Field_12, Field_36, Field_47, Field_54, Field_55, Field_56, Field_61, Field_62, Field_65, Field_66


    column_f = start_stop_proces(pd.to_datetime(data_df["F_startDate"]),pd.to_datetime(data_df["F_endDate"]),is_hour=False)
    column_e = start_stop_proces(pd.to_datetime(data_df["E_startDate"]), pd.to_datetime(data_df["E_endDate"]),is_hour=False)
    column_c = start_stop_proces(pd.to_datetime(data_df["C_startDate"]), pd.to_datetime(data_df["C_endDate"]),is_hour=False)
    column_g = start_stop_proces(pd.to_datetime(data_df["G_startDate"]), pd.to_datetime(data_df["G_endDate"]),is_hour=False)
    column_a = start_stop_proces(pd.to_datetime(data_df["A_startDate"]), pd.to_datetime(data_df["A_endDate"]),is_hour=False)
    column_12 = start_stop_proces(pd.to_datetime(data_df["Field_2"]), pd.to_datetime(data_df["Field_1"]),is_hour=True)
    column_43_44 = start_stop_proces(pd.to_datetime(data_df["Field_43"]), pd.to_datetime(data_df["Field_44"]), is_hour=True)
    # for f in column_f:
    #     print(f)


    data_df['columnf'] = column_f
    data_df['columne'] = column_e
    data_df['columnc'] = column_c
    data_df['columng'] = column_g
    data_df['columna'] = column_a
    data_df['column4344'] = column_43_44

    # Field_38, brief

    data_df.fillna(-999, inplace=True)

    if istrain == True: labels = data_df["label"]
    else: labels = []

    idlist = data_df["id"]


    data = data_df.drop(dropped_columns, axis=1)
    # data = data_df.T.drop_duplicates(keep="first").T


    # for idx in data_df["brief"]:
    #     if idx != -999:
    #         print("+", idx, "+")

    return data, labels, idlist

"""
[53030 rows x 103 columns]
[53030 rows x 99 columns]
[53030 rows x 149 columns]
"""



if __name__ == "__main__":
    read_data(path)


