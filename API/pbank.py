import re
import json
import requests

URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

req = requests.get(URL)
#print(req)
#print(req.text)
j = json.loads(req.text)
#{'base_ccy': 'UAH', 'buy': '27.65000', 'sale': '28.05000', 'ccy': 'USD'}
for c in j:
    print(c['base_ccy'], c['ccy'], c['sale'], c['buy'])

