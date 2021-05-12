from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sys


import io


url = "https://data.world/alexandra/chord-progressions"

urlData = requests.get(url).content
df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
df = pd.DataFrame(df)

print(df.head)