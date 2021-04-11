from unidecode import unidecode

path = r"/data/train.csv"


def _word_standardization(word):
    word = word.lower()
    word = unidecode(word)

    return word


def check(value,list):
    value = _word_standardization(str(value))

    if value == "nan":
        return -999


    # print("1."+value)
    # print(list)


    for i, kind in enumerate(list):
        for element in kind:
            if element in value:
                # print("2.",value)
                # print(i)
                # print("+++" * 5)
                # print(list)
                # print(i)
                # print("++++")
                return i
    #
    # print("10")
    # print("+++")
    #
    return len(list)+2

    # print("3.", value)
    # print("+++"*5)
