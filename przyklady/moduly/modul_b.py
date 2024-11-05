
x = 10
y = 20


if __name__ == '__main__':
    "to będzie wywołane tylko wtedy gdy modul uruchamiany jest bezpośrednio. Wtedy __name__ ma wartość __main__"
    input("wpisz cos: ")
    print(dir())
    print(__name__)