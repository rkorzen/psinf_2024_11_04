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
    cena=123.25,
    vat=20.22
)

wynik:
"cena produktu to 123.25\nstawka vat to 20.22",


"""

def formatuj(*args, **kwargs):
    text = "\n".join(args)
    for klucz in kwargs:
        text = text.replace(f"${klucz}", str(kwargs[klucz]))
    return text


def formatuj(*args, **kwargs):
    text = ""

    for t in args:
        text += t

    for klucz in kwargs:
        text = text.replace(f"${klucz}", str(kwargs[klucz]))
    return text


def test_formatuj():
    assert formatuj() == ""
    assert formatuj("napis 1") == "napis 1"
    assert formatuj("napis 1", "napis 2", ) == "napis 1\nnapis 2"
    assert formatuj(
        "cena produktu to $cena",
        "stawka vat to $vat",
        cena=123.25,
        vat=20.22
    ) == "cena produktu to 123.25\nstawka vat to 20.22"
