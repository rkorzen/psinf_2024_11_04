# pip install requests
import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

response = requests.get(url)
print(response.json())


"""
python kalkulator.py
ile: 100
czego: EUR

"""