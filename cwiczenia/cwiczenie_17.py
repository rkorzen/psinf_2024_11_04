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
from collections import defaultdict

last_login = {}
user_total_time = defaultdict(int)

print(user_total_time["Rafał"])


with open("../data/logi.csv") as f:

    for line in f:
        nick, action, t = line.strip().split(";")
        t = int(t)
        if action == "LOGIN":
            last_login[nick] = t

        elif action == "LOGOUT":
            user_total_time[nick] += + t - last_login[nick]

print(user_total_time)



