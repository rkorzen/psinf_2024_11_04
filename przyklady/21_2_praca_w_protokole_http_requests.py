import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

response = requests.get(url)
print(response.json())
