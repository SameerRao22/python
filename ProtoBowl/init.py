import requests
import json
from os import system

url = "https://www.quizdb.org/api/search?search%5Bquery%5D=&search%5Bfilters%5D%5Bcategory%5D%5B%5D=17&search%5Blimit%5D=false&download=json"
response = requests.get(url, headers={"Accept": "application/json"})
data1 = response.json()
with open("data.json", "r+") as d:
    json.dump(data1, d)