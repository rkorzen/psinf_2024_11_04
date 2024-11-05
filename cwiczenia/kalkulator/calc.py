"""

$ python calc.py

Podaj operację jaka chcesz wykonać (+-/*): *
Podaj arg a: 10
Podaj arg b: 20
Wynik: 200

"""

def add(a, b):
    """Dodaje dwie liczby"""
    return a + b


def sub(a, b):
    """Odejmuje b od a"""
    return a - b


def mul(a, b):
    """Mnoży a i b"""
    return a * b


def div(a, b):
    """Dzieli a przez b"""
    return a / b


def get_a():
    a = int(input("Podaj arg a: "))
    return a


def get_data():
    op = input("Podaj operację jaka chcesz wykonać (+-/*): ")
    a = int(input("Podaj arg a: "))
    b = int(input("Podaj arg b: "))
    return op, a, b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def main():
    # dane = get_data()
    # op = dane[0]
    # a = dane[1]
    # b = dane[2]

    op, a, b = get_data()

    # if op == "+":
    #     result = add(a, b)
    # elif op == "-":
    #     result = sub(a, b)
    # ...

    # func = operations[op]
    # result = func(a, b)
    result = operations[op](a, b)
    print("Wynik:", result)


if __name__ == "__main__":
    main()
