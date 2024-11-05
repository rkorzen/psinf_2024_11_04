# def second(el):
#     return el[1]
#
# print(second("1a"))


second = lambda el: el[1]

print(second("1a"))
print((lambda el: el[1])("1a"))


lista = [(10, "a"), (5, "b"), (1, "c")]

print(sorted(lista, key=second))
print(sorted(lista, key=lambda x: x[1]))