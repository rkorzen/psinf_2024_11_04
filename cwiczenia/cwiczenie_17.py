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


with open("../data/logi.csv") as f:
    print(f.read()[:10])