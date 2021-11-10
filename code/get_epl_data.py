import pandas as pd
import requests 
from bs4 import BeautifulSoup

from datetime import datetime

data = pd.read_csv("../data/E0.csv")

data.Date = pd.to_datetime(data.Date)
data['year'] = data.Date.dt.year
data.Time = pd.to_datetime(data.Time)

data['year'] = data.Date.dt.year 
data['month'] = data.Date.dt.month 
data['day'] = data.Date.dt.day
data['hour'] = data.Time.dt.hour
data['minute'] = data.Time.dt.minute

print(data.hour)

