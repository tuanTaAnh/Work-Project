from datetime import datetime
path = r"D:\Projects\credict_scores\data\train.csv"

def show_data(list,kind_list,key_list,num):
    for key in key_list:
        if kind_list[key] != "Number":
            print(key," : ",kind_list[key],end=": ")
            for item in list[:num]:
                print("{",item[key],end="} ")
            print()

from unidecode import unidecode

def _word_standardization(word):
    word = word.lower()
    word = unidecode(word)

    return word


from csv import DictReader

def check_kind(item_list,flag):
    # if flag == 1:
    #     print(len(item_list))
    #     print(item_list)

    for item in item_list:
        if  item.count("-") > 2 and item.count("/") > 2:
            return "Date_time"

    for item in item_list:
        try:
            int(item)
            return "Number"
        except:
            # if flag == 1:  print("Not Int: ", item)
            pass

    for item in item_list:
        try:
            float(item)
            return "Number"
        except:
            # if flag == 1:  print("Not Float: ", item)
            pass

    empty_flag = False
    for item in item_list:
        if item != "": empty_flag = True

    if empty_flag == False: return "Empty"

    for item in item_list:
        if item == "female" or item == "male" : return "SEX"

    return "Address"

def get_kind(key_list, list, num):
    kind_list = {}
    for key in key_list:
        item_list = []
        flag = 0
        if key == "Field_78": flag = 1
        for item in list[:num]:
            item_list.append(item[key])
        kind = check_kind(item_list,flag)
        # if flag == 1: print(kind)
        kind_list[key] = kind

    return kind_list


def read_file(path):
    # open file in read mode
    with open(path, 'r',encoding="utf-8") as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)

        # convert csv.dict_reader to list of dicts
        customer_list = list(csv_dict_reader)

    key_list = []
    row0 = customer_list[0]
    for key in row0.keys():
        key_list.append(key)

    # row0 = csv_list[0]
    # for key in row0.keys():
    #     print(key," : ",row0[key])

    kind_list = get_kind(key_list, customer_list, 20)

    return  kind_list, key_list, customer_list


if __name__ == "__main__":
    kind_list, key_list, csv_list = read_file(path)


    list_Field = {}
    for item in csv_list:
        if item["diaChi"] != "":
            list_Field[item["diaChi"]] = 0

    # num = 0
    # for ii, item in enumerate(csv_list):
    #     if item["diaChi"] != "":
    #         # print(_word_standardization(item["Field_54"]))
    #         # if _word_standardization(item["Field_62"]) == "ii": print("++++"*10)
    #         list_Field[item["diaChi"]] += 1
    #
    # count = 0
    # print("len(list_Field.keys())",len(list_Field.keys()))
    #
    # print(type(list_Field))
    # for key in list_Field:
    #     print(key," ,",list_Field[key])

    # for key in list_Field:
    #     print(list_Field[key])
        # print("[",end=" ")
        # for idx in num_dict[key]:
        #     count += 1
        #     idx = _word_standardization(idx)
        #     print(" '" + idx + "', ",end = " ")
        #     if count%5 == 0:
        #         print()
        # print("],", end=" ")
        # print()

    for ii, item in enumerate(csv_list[:200]):
        print(ii)
        for key in item.keys():
            if "partner" in key and "C" in key:
                print(item[key],end=" ")
        print()



        # count += 1
        # key = _word_standardization(key)
        # print("[" + key + "],",end = " ")
        # if count%5 == 0:
        #     print()
    # print("count",count)








# import pandas as pd
# df = pd.DataFrame(list())
# df.to_csv('submission.csv')


# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.interpolate
# import scipy.integrate
#
# predictions = [0.9, 0.3, 0.8, 0.75, 0.65, 0.6, 0.78, 0.7, 0.05, 0.4, 0.4, 0.05, 0.5, 0.1, 0.1]
# actual = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#
# def gini(actual, pred):
#     assert (len(actual) == len(pred))
#     all = np.asarray(np.c_[actual, pred, np.arange(len(actual))], dtype=np.float)
#     all = all[np.lexsort((all[:, 2], -1 * all[:, 1]))]
#     totalLosses = all[:, 0].sum()
#     giniSum = all[:, 0].cumsum().sum() / totalLosses
#
#     giniSum -= (len(actual) + 1) / 2.
#     return giniSum / len(actual)
#
#
# def gini_normalized(actual, pred):
#     return gini(actual, pred) / gini(actual, actual)




""""
2019-10-14    T01:37:41.959Z
2019-10-14    T01:37:41.959Z

2019-09-30  T15:43:53.146Z
2019-09-30  T15:43:53.146Z


+

2019-09-10    T09:20:40.066Z
2019-09-11    T07:53:44Z


2017-01-01      T10:42:50.57Z
2018-10-01      T09:06:45.302Z


+
2019-10-21     T03:29:30.074Z
2019-10-21     T04:17:26Z

2016-12-31    T14:33:50.683Z
2018-02-08    T04:30:17.373Z


10/29/2018
+

2019-10-04     T01:19:20Z
2019-11-21     T19:10:05Z



+



2019-01-18   T01:23:51.351Z
2019-01-25   T09:08:25Z


+



"""


























""""


kind_list, key_list, csv_list = read_file(path)

    list_Field = {}
    for item in csv_list:
        if item["Field_68"] != "":
            list_Field[item["Field_68"]] = 0

    num = 0
    for ii, item in enumerate(csv_list):
        if item["Field_68"] != "":
            # print(_word_standardization(item["Field_54"]))
            # if _word_standardization(item["Field_62"]) == "ii": print("++++"*10)
            list_Field[item["Field_68"]] += 1
        else:
            num += 1
    print("num: ",num)

    count = 0
    for key in list_Field.keys():
        print("|"+_word_standardization(key)+"| ","|"+str(list_Field[key])+"|")
        # count += 1
        # key = _word_standardization(key)
        # print("[" + key + "],",end = " ")
        # if count%5 == 0:
        #     print()

"""


""""

from csv import DictReader

def check_kind(item_list,flag):
    # if flag == 1:
    #     print(len(item_list))
    #     print(item_list)

    for item in item_list:
        if  item.count("-") > 2 and item.count("/") > 2:
            return "Date_time"

    for item in item_list:
        try:
            int(item)
            return "Number"
        except:
            # if flag == 1:  print("Not Int: ", item)
            pass

    for item in item_list:
        try:
            float(item)
            return "Number"
        except:
            # if flag == 1:  print("Not Float: ", item)
            pass

    empty_flag = False
    for item in item_list:
        if item != "": empty_flag = True

    if empty_flag == False: return "Empty"

    for item in item_list:
        if item == "female" or item == "male" : return "SEX"

    return "Address"

def get_kind(key_list, list, num):
    kind_list = {}
    for key in key_list:
        item_list = []
        flag = 0
        if key == "Field_78": flag = 1
        for item in list[:num]:
            item_list.append(item[key])
        kind = check_kind(item_list,flag)
        # if flag == 1: print(kind)
        kind_list[key] = kind

    return kind_list


def read_file(path):
    # open file in read mode
    with open(path, 'r',encoding="utf-8") as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)

        # convert csv.dict_reader to list of dicts
        customer_list = list(csv_dict_reader)

    key_list = []
    row0 = customer_list[0]
    for key in row0.keys():
        key_list.append(key)

    # row0 = csv_list[0]
    # for key in row0.keys():
    #     print(key," : ",row0[key])

    kind_list = get_kind(key_list, customer_list, 20)

    return  kind_list, key_list, customer_list

"""

