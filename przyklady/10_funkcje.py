"""
def nazwa(<argumenty>):
    <blok instrukcji>
    <return>
"""

def foo() -> int:
    print("Hello World")
    return 42

print(foo())


def foo(name: str) -> int:
    print(f"Hello {name}")
    return 42

# print(foo())
print(foo("Rafał"))
print(foo(name="Rafał"))

def foo(name: str = "World!") -> int:
    print(f"Hello {name}")
    return 42

print(foo())
print(foo("Rafał"))
print(foo(name="Rafał"))


####
numeric = int | float | complex  # 1 + 1j
def dodaj(a: numeric, b: numeric) -> numeric:
    """To jest docstring - dokumentacja funkcji
    Dodaje do siebie liczby i zwraca wynik.

    >>> dodaj(1, 2)
    3
    >>> dodaj(1.1, 2)
    3.1
    >>> dodaj(1+1j, 2+2j)
    (3+3j)
    """
    return a + b

x = dodaj
x(1, 2)
print(dir(dodaj))
print(dodaj.__doc__)
print(dodaj.__annotations__)
print(x.__name__)


if __name__ == "__main__":
    assert dodaj(1, 2) == 3
    assert dodaj(1.1, 2) == 3.1
    assert dodaj(1+1j, 2+2j) == 3+3j

