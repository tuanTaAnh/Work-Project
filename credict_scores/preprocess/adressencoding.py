from read_data.read_csv import read_data
from config import config
from unidecode import unidecode
import pandas as pd

path = r"D:\Projects\credict_scores\data\train.csv"


def _word_standardization(word):
    word = word.lower()
    word = unidecode(word)

    return word


if __name__ == "__main__":
    data = pd.read_csv(path)

    count = 0

    for address in data["diaChi"]:
        if str(address) != "nan":
            processed = _word_standardization(address)

            if "huyen" in processed:
                processed = processed.split("huyen")[-1]
                # print(processed)
                continue

            if "tinh" in processed:
                processed = processed.split("tinh")[-1]
                # print(processed)
                continue

            if "t." in processed:
                processed = processed.split("t.")[-1]
                # print(processed)
                continue

            if "thanh pho" in processed:
                processed = processed.split("thanh pho")[-1]
                # print(processed)
                continue

            if "tp." in processed:
                processed = processed.split("thanh pho")[-1]
                # print(processed)
                continue

            if ", " in processed:
                processed = processed.split(", ")[-1]
                # print(processed)
                continue

            if "- " in processed:
                processed = processed.split("- ")[-1]
                # print(processed)
                continue

            count += 1
            print(processed)


    print("count",count)

