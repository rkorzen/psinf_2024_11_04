"""
Otworz jakis plik i wypisz jego zawartosc numerujac linie
"""

with open("cwiczenie_04.py") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i:3} {line.rstrip()}")

