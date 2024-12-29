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
