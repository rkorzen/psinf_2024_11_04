# index   012345678910
napis = "Ala ma kota"

print(len(napis))

print(napis[10])  # wybieranie
print(napis[4])  # wybieranie

print(napis[-1])
print(napis[-2])


# wybieranie spoza zakresu:
# print(napis[11])
# tutaj sie spotkamy z IndexError bo nie ma obiektu na tym indeksie

# slicing
# indeksy:
# [pierwszy_zak_ktry_biore:pierwszy_znak_ktorego_nie_biore]
print(napis[3:8])
# [pierwszy_zak_ktry_biore:pierwszy_znak_ktorego_nie_biore;krok]
print(napis[3:8:2])

print(napis[0:8:2])
print(napis[:8:2])

print(napis[1::2])
print(napis[::-1])


print(sorted(napis))
# to sie nie uda
# bo napis jest niemutowalny
# nie da sie napisu zmienic
# napis[3] = "x"

print(dir(napis))
help(napis.count)
help(napis.index)
print(napis.count("a"))

print(napis.count("ma"))
print(napis.index("a", 3))
