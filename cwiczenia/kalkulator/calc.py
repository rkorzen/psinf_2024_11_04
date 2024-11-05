"""

$ python calc.py

Podaj operację jaka chcesz wykonać (+-/*): *
Podaj arg a: 10
Podaj arg b: 20
Wynik: 200

"""

def add(a, b, *args):
    """Dodaje dwie liczby"""
    return a + b + sum(args)


def sub(a, b, *args):
    """Odejmuje b od a"""

    r = a - b
    for i in args:
        r -= i

    return r


def mul(a, b, *args):
    """Mnoży a i b"""
    r = a * b

    for i in args:
        r *= i

    return r


def div(a, b, *args):
    """Dzieli a przez b"""
    r = a / b

    for i in args:
        r /= i

    return r


def get_a():
    a = int(input("Podaj arg a: "))
    return a


def get_data():
    op = input("Podaj operację jaka chcesz wykonać (+-/*): ")
    a = int(input("Podaj arg a: "))
    b = int(input("Podaj arg b: "))
    pozostale = []
    while True:
        i = input("Podaj kolejną liczbę lub naciśnij enter by zakończyć: ")
        if not i: # not ""
            break
        pozostale.append(int(i))
    return op, a, b, pozostale

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

    op, a, b, pozostale = get_data()

    # if op == "+":
    #     result = add(a, b)
    # elif op == "-":
    #     result = sub(a, b)
    # ...

    # func = operations[op]
    # result = func(a, b)
    result = operations[op](a, b, *pozostale) # (1, 2, [1,2 ,3]) => (1, 2, 1, 2, 3)
    print("Wynik:", result)


if __name__ == "__main__":
    main()
