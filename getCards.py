import requests 
import pandas as pd

url = "https://api.hearthstonejson.com/v1/190920/enUS/cards.collectible.json"

response = requests.get(url)
response.encoding="utf-8"
data = response.json()

df = pd.DataFrame.from_dict(data)
csv = df.to_csv("hearthstone_collectible_cards.csv", encoding="utf-8", index=False)
