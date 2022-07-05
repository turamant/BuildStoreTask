import json

import requests


#URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

URL = "https://api.coingecko.com/api/v3/simple/price/?ids=bitcoin,ethereum,ripple,cardano&vs_currencies=usd,eur,gbp"

response = requests.get(URL)
data = json.loads(response.content.decode("utf-8"))

for k, v in data.items():
    print(k, "-", v)

