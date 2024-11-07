import urllib.request
import json
from dataclasses import dataclass


@dataclass
class Rate:
    currency: str
    code: str
    mid: float

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

with urllib.request.urlopen(url) as response:
    data = response.read()
    tabela = json.loads(data)


xxx = tabela[0]["rates"]

data = [Rate(**d) for d in xxx]

print(data)