from moja_biblioteka import hello

def test_hello_exists():
    assert hello("Rafał") is None


def test_hello_print(capsys):
    hello("Rafał")
    captured = capsys.readouterr()
    assert captured.out == "Hello Rafał"