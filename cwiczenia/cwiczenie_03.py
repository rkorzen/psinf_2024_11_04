lista: list[int] = [1, 2, 3, 4, 5, 11, 13, 12, 27, 23, 17]
wynik: list[int] = []

# napisz algorytm ktory wybierze z tej listy tylko liczby pierwsze
# wynik.append(2)
# 3 % 2 => 1
# for i in range(10):
#     print(i)
#
# for i in range(10, 20):
#     print(i)
#
# for i in range(10, 20, 2):
#     print(i)


for liczba in lista:
    if liczba < 2: continue

    dzielnik = 2
    while dzielnik < liczba:
        if liczba % dzielnik == 0: break
        dzielnik += 1
    else:
        wynik.append(liczba)

print(wynik)
