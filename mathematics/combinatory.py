from math import comb


def pascal_triangle(n: int):
    """
    Description
    ----------
    Pascal's triangle.'
    Parameters
    ----------
    n

    Returns
    -------

    """
    triangle_arr = []
    for r in range(n):
        rows = []
        for i in range(r + 1):
            res = comb(r, i)
            rows.append(res)
        triangle_arr.append(rows)
    return triangle_arr


def power_set(input_set):
    """
    Generates the power set (all subsets) of the given set.

    The power set of a set with `n` elements contains `2^n` subsets,
    including the empty set and the set itself.

    Parameters:
    input_set (list): A list representing the input set.

    Returns:
    list of lists: A list containing all subsets of the input set.

    Example:
    >>> power_set([1, 2])
    [[], [1], [2], [1, 2]]
    """
    if len(input_set) == 0:
        return [[]]

    subsets = [[]]
    for element in input_set:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [element])
        subsets.extend(new_subsets)
    return subsets


def exponential_growth(n, factor, days):
    results = [n]
    i = 1
    while i <= days:
        results.append(n * factor)
        n = n * factor
        i += 1
    return results



if __name__ == '__main__':
    exponential_growth(10,2,4)
    power_set(input_set=[1, 2, 3])
