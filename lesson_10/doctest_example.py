

def square(x):
    """
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-1)
    1
    """
    return x*x


def remove_elements(l, e):
    """
    >>> remove_elements([1, 2, 3, 4, 5], 3)
    [1, 2, 4, 5]
    >>> remove_elements([1, 2, 3, 1, 2], 1)
    [2, 3, 2]
    >>> remove_elements([1, 2, 3, 4, 5], 7)
    [1, 2, 3, 4, 5]
    """
    return [x for x in l if x != e]

