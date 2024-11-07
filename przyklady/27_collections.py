from collections import defaultdict, Counter, namedtuple


text = "ala ma kota"

print(Counter(text))

elementy = ["A", "A", "A", "V", "C"]

print(Counter(elementy))


Osoba = namedtuple("Osoba", "imie wiek miasto")

os = Osoba("Rafał", 44, "Warszawa")

print(os)
print(os.imie)

print(dir(os))