import pandas as pd

df = pd.read_csv(r"/Users/taanhtuan/Desktop/workproject/ids 2018/02-14-2018.csv")

for col in df.columns:
    print(col)

print(len(df))