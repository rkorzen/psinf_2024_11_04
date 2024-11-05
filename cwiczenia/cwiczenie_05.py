"""

Zliczanie znakow





"""




def test_zlicz_znaki():

    assert zlicz_znaki("") == 0
    assert zlicz_znaki("123") == 0
    assert zlicz_znaki("12<3") == 1
    assert zlicz_znaki("1<23") == 2

    assert zlicz_znaki("1<23>3") == 2
    assert zlicz_znaki("a<b<c>>") == 1 + 2
    assert zlicz_znaki("a<b<cd>>") == 1 + 2 + 2
    assert zlicz_znaki("a<b<c<d>>>") == 1 + 2 + 3

    assert zlicz_znak("a<a>sasas<b<c>>") == 1 + 1 + 2

    assert zlicz_znaki("1<23>3", start="[", end="]") == 0
    assert zlicz_znaki("1[23]3", start="[", end="]") == 1 + 1
    assert zlicz_znaki("1[2<3]3", start="[", end="]") == 1 + 1 + 1


