from calc import add, sub, mul, div, get_a


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 10) == 10

    assert add(1, 2, 3, 4, 5) == 15


def test_add_has_docstring():
    assert add.__doc__ is not None


def test_sub():
    assert sub(1, 2) == -1
    assert sub(-1, 1) == -2
    assert sub(-1, -1) == 0
    assert sub(0, 10) == -10
    assert sub(100, 2, 2, 2, 2 ) == 92

def test_sub_has_docstring():
    assert sub.__doc__ is not None


def test_mul():
    assert mul(1, 2) == 2
    assert mul(-1, 1) == -1
    assert mul(0, 10) == 0
    assert mul(2, 2, 2, 2) == 2 ** 4

def test_mul_has_docstring():
    assert mul.__doc__ is not None


def test_div():
    assert div(1, 2) == 0.5
    assert div(-1, 1) == -1
    assert div(0, 10) == 0

    assert div(16, 2, 2, 2) == 2


def test_div_has_docstring():
    assert div.__doc__ is not None


def test_get_data(monkeypatch):
    def give_me_10(_):
        return "10"

    monkeypatch.setattr("builtins.input", give_me_10)

    assert get_a() == 10
