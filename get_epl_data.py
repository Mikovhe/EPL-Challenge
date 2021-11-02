import pandas as pd
import requests 
from bs4 import BeautifulSoup

url = "https://www.football-data.co.uk/englandm.php"

data =requests.get(url)
print(data.status_code)
soup = BeautifulSoup(data.text,'html.parser')


print(soup.prettify)

