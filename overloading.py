from functools import singledispatch

@singledispatch
def process(data):
    print("Ogólna wersja", data)

@process.register(int)
def _(data):
    print("Przetwarzam liczbę całkowitą", data)

@process.register(str)
def _(data):
    print("Przetwarzam napis", data)

process(10)      # Wypisze "Przetwarzam liczbę całkowitą 10"
process("hello") # Wypisze "Przetwarzam napis hello"
process([1, 2])  # Wypisze "Ogólna wersja [1, 2]"