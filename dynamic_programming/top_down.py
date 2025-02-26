# house robery

def house_robbery(arr, i=0, lookup=None):
    """
        Solves the House Robber problem using recursion with memoization.

        The function determines the maximum sum of non-adjacent elements that can be stolen
        from a list of houses, ensuring that two consecutive houses are not robbed.

        Parameters:
        ----------
        arr : list[int]
            A list of strictly positive integers representing the amount of money in each house.
        i : int, optional
            The current index in the arrays during recursion (default is 0).
        lookup : dict, optional
            A dictionary for memoization to store previously computed results (default is None).

        Returns:
        -------
        int
            The maximum amount of money that can be robbed without triggering alarms.

        Example:
        --------
        >>> house_robbery([2, 7, 9, 3, 1])
        12

        Explanation:
        - The optimal choice is to rob houses at indices `[1, 3]`, yielding `7 + 3 = 12`.
        """

    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    if i >= len(arr):
        return 0
    else:
        lookup[i] = max(arr[i] + house_robbery(arr, i + 2, lookup), house_robbery(arr, i + 1, lookup))
        return lookup[i]


def subsets_sum(arr, k, i=0, lookup=None):
    """
        Counts the number of subsets in the given arrays that sum up to the target value `k`
        using a recursive approach with memoization.

        Parameters:
        ----------
        arr : list[int]
            A list of strictly positive integers representing the set of numbers.
        k : int
            The target sum to be achieved using subsets of `arr`.
        i : int, optional
            The current index in the arrays during recursion (default is 0).
        lookup : dict, optional
            A dictionary for memoization to store previously computed results (default is None).

        Returns:
        -------
        int
            The number of subsets whose sum equals `k`.

        Example:
        --------
        >>> subsets_sum([2, 3, 5, 6, 8, 10], 10)
        3
        """
    lookup = {} if lookup is None else lookup
    print(f"Calling subsets_sum(arr, k={k}, i={i})")

    if (i, k) in lookup:
        print(f"Returning memoized result for ({i}, {k}): {lookup[(i, k)]}")
        return lookup[(i, k)]

    # Base case: valid subset found
    if k == 0:
        print(f"Found a valid subset at ({i}, {k})!")
        return 1

    # Base case: invalid subset (end of arrays or k < 0)
    if i == len(arr) or k < 0:
        print(f"No valid subset for ({i}, {k}). Returning 0")
        return 0

    # Recursive calls
    print(f"Exploring include {arr[i]} at index {i}, new k = {k - arr[i]}")
    include = subsets_sum(arr, k - arr[i], i + 1, lookup)

    print(f"Exploring exclude {arr[i]} at index {i}, k remains {k}")
    exclude = subsets_sum(arr, k, i + 1, lookup)

    # Memoize and return the result
    lookup[(i, k)] = include + exclude
    print(f"Computed subsets_sum({i}, {k}) = {lookup[(i, k)]}")
    return lookup[(i, k)]

if __name__ == "__main__":
    subset = subsets_sum([1,2,3], k=3)
    print('the end')