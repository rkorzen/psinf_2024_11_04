numbers = [1, -2, 3, 4, -7, -5, 12]


def test_filter_list():
    assert filter_list(numbers, lambda x: x>0) == [1, 3, 4, 12]
    assert filter_list(numbers, lambda x: x % 2 == 0) == [2, 4, 12]
