"""

[1, 2, 3] => [1,2 , 3]

[1, [2, 3]] => [1, 2, 3]

[1, 2, [3, ,4], [1, 2, [1, 2, [1]]]] => [1, 2, 3, 4, 1, 2, 1, 2 1]

"""

# lista = [1, 2, 3, [1, 2]]
#
# for el in lista:
#     if type(el) == list:
#         print("to jest lista", el)
#
#
# for el in lista:
#     if isinstance(el, list):
#         print("to jest lista", el)


def splaszcz_liste(lista):
    wynik = []
    for el in lista:
        if isinstance(el, list):
            wynik.extend(splaszcz_liste(el))
        else:
            wynik.append(el)
    return wynik

print(splaszcz_liste([1, 2, 3, [1, 2, [1, 2]]]))

