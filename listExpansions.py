import pandas as pd

df = pd.read_csv("./hearthstone_collectible_cards.csv")
print(df.info())

print(df["set"].head())
for expansion in list(df["set"].unique()):
    print(f" - {expansion}")

