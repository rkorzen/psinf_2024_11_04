from typing import Callable

numbers = [1, -2, 3, 4, -7, -5, 12]

def filter_list(numbers: list, func: Callable[[int], bool]) -> list:
    wynik = []
    for el in numbers:
        if func(el):
            wynik.append(el)
    return wynik




def test_filter_list():
    assert filter_list(numbers, lambda x: x>0) == [1, 3, 4, 12]
    assert filter_list(numbers, lambda x: x % 2 == 0) == [-2, 4, 12]
