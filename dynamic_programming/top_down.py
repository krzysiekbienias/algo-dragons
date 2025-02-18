# house robery

def house_robbery(arr, i=0, lookup=None):
    """
    Description
    -----------
    Function that maximize money you may steal from row of house given that you cannot robber two consecutive
    properties.
    Parameters
    ----------
    arr :
    i :
    lookup :

    Returns
    -------

    """
    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    if i >= len(arr):
        return 0
    else:
        lookup[i] = max(arr[i] + house_robbery(arr, i + 2, lookup), house_robbery(arr, i + 1, lookup))
        return lookup[i]
