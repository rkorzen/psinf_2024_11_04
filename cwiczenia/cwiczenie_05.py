"""

Zliczanie znakow





"""

def zlicz_znaki(napis, start="<", end=">"):
    waga = 0
    zliczenia = 0
    for znak in napis:
        if znak == start:
            waga += 1
            continue
        elif znak == end:
            waga -= 1
            continue
        zliczenia += waga
    return zliczenia



def test_zlicz_znaki():
    assert zlicz_znaki("") == 0
    assert zlicz_znaki("123") == 0
    assert zlicz_znaki("12<3") == 1
    assert zlicz_znaki("1<23") == 2

    assert zlicz_znaki("1<23>3") == 2
    assert zlicz_znaki("a<b<c>>") == 1 + 2
    assert zlicz_znaki("a<b<cd>>") == 1 + 2 + 2
    assert zlicz_znaki("a<b<cccc<d>>>") == 1 + 2 + 2 + 2 + 2 + 3

    assert zlicz_znaki("a<a>sasas<b<c>>") == 1 + 1 + 2

    assert zlicz_znaki("1<23>3", start="[", end="]") == 0
    assert zlicz_znaki("1[23]3", start="[", end="]") == 1 + 1
    assert zlicz_znaki("1[2<3]3", start="[", end="]") == 1 + 1 + 1
