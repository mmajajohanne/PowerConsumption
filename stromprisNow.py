import requests
from pandas.io.json import json_normalize
import pandas as pd
import datetime
now = datetime.datetime.now()
from urllib.parse import urlparse, urlunparse

u = urlparse('https://www.hvakosterstrommen.no/api/v1/prices/2023/01-05_NO1.json')
u._replace(path="/api/v1/prices/"+str(now.year)+"/"+str(now.month)+"-"+str(now.day)+"_NO1.json")
url = urlunparse(u)

df = pd.read_json(url)

print("Strømprisen i Oslo akkurat nå er", df["NOK_per_kWh"][now.hour],"NOK per KWh") 

