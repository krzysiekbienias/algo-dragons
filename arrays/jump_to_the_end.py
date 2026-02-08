from typing import List

"""
Greedy solution for the 'Jump to the End' problem.

This module provides a function that determines whether the last index
is reachable from the first index given max jump lengths at each position.
"""


def jump_to_the_end(arr: List[int]) -> bool:
    """
    Determines whether it is possible to jump to the end of a list of integers.

    This function evaluates if, starting from the 0th index in the input list, it
    is possible to reach the last index by following the jump lengths specified at
    each index. If it is possible, the function returns True; otherwise, it
    returns False.

    Parameters
    ----------
    arr : List[int]
        A list of non-negative integers, where the value at each index represents
        the maximum number of steps that can be taken from that position.

    Returns
    -------
    bool
        True if it is possible to reach the last index starting from the 0th index;
        False otherwise.

    Raises
    ------
    IndexError
        If the input list is empty.
    """
    if not arr:
        raise IndexError("you passed an empty array")
    destination = len(arr) - 1
    for i in range(destination, -1, -1):
        if i + arr[i] >= destination:
            destination = i
    return destination == 0
