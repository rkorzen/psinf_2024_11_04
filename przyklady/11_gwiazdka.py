a, *b = 1, 2, 3

print(a, b)

*a, b = 1, 2, 3
print(a, b)

a, *b, c, d = 1, 2, 2, 3, 4, 5
print(a, b, c, d)


lista = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4]
print(lista)   # print([1, 2, 3, 4])
print(*lista)  # print(1, 2, 3, 4)

slownik = {"sep": "-", "end": "*"}

print(*lista, **slownik)  # print(1, 2, 3, 4, sep="-", end="*")


print(*lista, *lista2)


