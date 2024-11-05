"""

>> formatuj(
    "napis 1",
    "napis 2",
)

wynik:
"napis 1\nnapis 2

>> formatuj(
    "cena produktu to $cena",
    "stawka vat to $vat",
    cena=123.25
    vat=20.22
)

wynik:
"cena produkty to 123.25\nstawka vat to 20.22",


"""

lista = ["A", "B"]
print("\n".join(lista))
