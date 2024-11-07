
lista = [1, 2, 3]

print("-".join(map(str, lista)))

print("ala ma kota".encode())

print("zażółć gęśla jaźń".encode())

print("zażółć gęśla jaźń".encode("CP1250"))

moje_bytes = b'za\xbf\xf3\xb3\xe6 g\xea\x9cla ja\x9f\xf1'

print(moje_bytes)
print(moje_bytes.decode("CP1250"))


with open("dane_w_cp1250.txt", "w", encoding="cp1250") as f:
    f.write("""
A
B
C
Ą
ę
""")

from pprint import pprint
pprint(dir(str))

import requests
import json
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

# Przykładowy URL API
url = "https://jsonplaceholder.typicode.com/users/1"

# Wysłanie zapytania do API i pobranie danych JSON
response = requests.get(url)
data = response.json()
filtered_data = {key: data[key] for key in User.__annotations__.keys() if key in data}

print(data)

# Konwersja słownika JSON na obiekt klasy User
user = User(**filtered_data)

print(user)