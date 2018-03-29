import binary_search as search


def test_binary_search():
    test_array = [1, 2, 3, 4, 5, 6, 7]
    test_value = 4
    will_it_blend = search.binary_search(test_array, test_value)
    print(will_it_blend)
    assert type(will_it_blend) is int
    assert will_it_blend == 3