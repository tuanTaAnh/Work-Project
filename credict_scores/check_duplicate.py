from csv import DictReader

trainpath = r"D:\Projects\credict_scores\data\train.csv"
testpath = r"D:\Projects\credict_scores\data\test.csv"

def show_data(list,kind_list,key_list,num):
    for key in key_list:
        if kind_list[key] != "Number":
            print(key," : ",kind_list[key],end=": ")
            for item in list[:num]:
                print("{",item[key],end="} ")
            print()



def read_file(path):
    # open file in read mode
    with open(path, 'r',encoding="utf-8") as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = DictReader(read_obj)

        # convert csv.dict_reader to list of dicts
        customer_list = list(csv_dict_reader)

    return  customer_list




if __name__ == "__main__":
    customer_trainlist = read_file(trainpath)
    customer_testlist = read_file(testpath)


    for customer in customer_trainlist:
        del customer['label']
        del customer['brief']

    for customer in customer_testlist:
        del customer['brief']

    print(len(customer_trainlist[0].keys()))
    print(len(customer_testlist[0].keys()))


    count = 0
    count_d = 0

    for cus_train in customer_trainlist:
        for cus_test in customer_testlist:
            if cus_train == cus_test:
                count += 1
                print("+++"*10)
            else:
                count_d += 1

            if count_d%10000000 == 0:
                print(count_d)

    print(count)


