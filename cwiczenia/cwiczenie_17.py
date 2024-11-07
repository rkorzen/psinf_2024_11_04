"""
Napisz program wczytujący plik z logami aktywności użytkowników
w systemie. Na podstawie wczytanych danych wyświetl informację o
sumarycznym czasie przebywania każdego użytkownika w systemie.
Przykład użycia:

$ python read_logs.py

Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s

"""

import csv
from collections import defaultdict
from pathlib import Path


last_login = {}
user_total_time = defaultdict(int)

# print(user_total_time["Rafał"])

path = Path(r"..\data\logi.csv")
print(path)
with open(path) as f:
    reader = csv.reader(f, delimiter=';')
    for nick, action, t  in reader:
        t = int(t)
        if action == "LOGIN":
            last_login[nick] = t

        elif action == "LOGOUT":
            user_total_time[nick] += t - last_login[nick]

print("Czas przebywania w systemie:")

# print(user_total_time)
# print(user_total_time.keys())
# print(user_total_time.items())
for nick, total_time in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(f"- {nick:10}: {total_time} s")


