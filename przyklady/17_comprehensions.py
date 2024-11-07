
liczby = range(500)

szesciany = {}

for liczba in liczby:
    if liczba % 2 == 0:
        szesciany[liczba] = liczba ** 3

print(szesciany)

print({liczba: liczba ** 3 for liczba in liczby if liczba % 2 == 0})


tabliczka = []
for x in range(1, 11):
    row = []
    for y in range(1, 11):
        row.append(x * y)
    tabliczka.append(row)

print(tabliczka)

from pprint import pprint

pprint([[x*y for y in range(1, 11)] for x in range(1, 11)])



pprint(((liczba,liczba ** 3) for liczba in liczby if liczba % 2 == 0))


lista = [[liczba,liczba ** 3] for liczba in liczby if liczba % 2 == 0]
gen_expr = ((liczba,liczba ** 3) for liczba in liczby if liczba % 2 == 0)

import sys

print(sys.getsizeof(lista))
print(sys.getsizeof(gen_expr))