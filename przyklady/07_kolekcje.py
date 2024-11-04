# tuple - krotka
# list - lista
# set - zbior
# dict - slownik

napis = "1, 2.0, 3, 'a', (1, 2, 3)"
tupla = (1, 2.0, 3, "A", (1, 2, 3))
lista = [1, 2.0, 3, "A", (1, 2, 3)]
zbior = {1, 2.0, 3, "A", (1, 2, 3)}

print(napis[0])
print(tupla[0])
print(lista[0])

print(napis[1])
print(tupla[1])
print(lista[1])

print(napis[1:3])
print(tupla[1:3])
print(lista[1:3])
# print(zbior[1:3]) - to daje błąd
print(zbior)
print("A" in napis)
print("A" in tupla)
print("A" in lista)
print("A" in zbior)


# niemutowalnosc vs mutowalnosc
# napis[0] = "K"
# tupla[0] = "K"

lista[0] = "K"
print(lista)

lista.append(1000)
lista.append(1000)
print(lista)
zbior.add(1000)
zbior.add(1000)
print(zbior)
lista.append(1000)
# nie wszystko moze sie znaleźć w zbiorze

# zbior.add([1, 2, 3])
print(hash((1, 2, 3)))
# hash(lista)
# print(hash((1, 2, 3, [1, 2])))

print(dir(tupla))
print(dir(lista))
print(dir(zbior))

# zbior

a = {1, 2, 3, "x"}
b = {2, 3, 4}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)

print(len(set("Ala ma kota")))

# numbers = int | float
# zbior: set[numbers] = {1, 2, 2.2}

# slownik - dict
print(dict(), set())
print({}) # to jest pusty slownik
slownik = {1: "a", 2: "b", "c": 3}

print("a" in slownik)
print("a" in slownik.values())
print(1 in slownik.keys())
print(1 in slownik)
print(slownik["c"])
print(slownik.items())
print(dir(slownik))

if "g" in slownik:
    print(slownik["g"])

print(slownik.get("g", 0))


## czego nie omawiamy
# frozenset
# bytes
# bytearray