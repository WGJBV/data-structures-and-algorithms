def binary_search(array, value):
    result = -1
    for i in array:
        if array[i] == value:
            result = i
            return result
    return result
