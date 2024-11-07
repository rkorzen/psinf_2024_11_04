import urllib.request
import json

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

with urllib.request.urlopen(url) as response:
    data = response.read()
    tabela = json.loads(data)


print(tabela)