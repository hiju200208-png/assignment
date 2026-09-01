import pandas as pd

file_path = r"C:\dev\assignment\chapter23\expenses.csv"

df = pd.read_csv(file_path)

print("전체 지출:", df["amount"].sum())
print(df.groupby("category")["amount"].sum())