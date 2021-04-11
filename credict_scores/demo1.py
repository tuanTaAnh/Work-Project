import pandas as pd

trainpath = r"D:\Projects\credict_scores\data\train.csv"
testpath = r"D:\Projects\credict_scores\data\test.csv"




def start_stop_proces(start_list,stop_list, is_hour = True):
    days_list = []
    num_of_list = len(start_list)
    for idx in range(num_of_list):
        print(idx,": ",str(start_list[idx])," ", str(stop_list[idx]))

        if str(start_list[idx]) == "NaT" and str(stop_list[idx]) == "NaT":
            print("+++"*10)
            days_list.append(-999)
            continue

        if str(start_list[idx]) == "NaT":
            delta = (-stop_list[idx])
        elif  str(stop_list[idx]) == "NaT":
            delta = (start_list[idx])
        else:
            delta = (stop_list[idx]-start_list[idx])

        # print(int(delta.days))
        days_list.append(int(delta.days))



    return days_list


if __name__ == "__main__":

    # train = pd.read_csv(trainpath)
    # test = pd.read_csv(testpath)
    #
    # data = pd.concat([train, test], axis=0)
    #
    # column_f = start_stop_proces(pd.to_datetime(data["F_startDate"]).tolist(), pd.to_datetime(data["F_endDate"]).tolist(), is_hour=False)
    #
    # data['columnf'] = column_f

    labels = ["111","222","333"]
    id_list = [1,2,3]
    label_dt = {}

    label_dt = [{"label": label, "id": id}
                for (label,id)in zip(labels, id_list) ]

    for label in label_dt:
        print(label)
