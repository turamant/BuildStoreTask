import json

import requests


URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(URL)
data = json.loads(response.content.decode("utf-8"))

print(data['time']['updated'])
print(data['chartName'])
print(data['bpi']['USD']['code'])
print(data['bpi']['USD']['rate'])

print(data['bpi']['EUR']['code'])
print(data['bpi']['EUR']['rate'])

print(data['bpi']['GBP']['code'])
print(data['bpi']['GBP']['rate'])
