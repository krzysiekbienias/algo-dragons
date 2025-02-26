def flatten(arr: list) -> list:
    """
        Recursively flattens a nested list into a single-level list.

        This function takes a list that may contain nested lists and returns a new
        list where all elements are flattened into a single level while preserving order.

        Parameters:
        ----------
        arr : list
            A list that may contain nested lists of arbitrary depth.

        Returns:
        -------
        list
            A flattened list containing all elements from the input list in order.

        Example:
        --------
        >>> flatten([1, [2, [3, 4], 5], 6])
        [1, 2, 3, 4, 5, 6]

        >>> flatten([[1, 2], [3, [4, [5, 6]]]])
        [1, 2, 3, 4, 5, 6]

        Notes:
        ------
        - The function uses recursion to handle nested lists of arbitrary depth.
        - It does not modify the original list; instead, it creates a new flattened list.
        - If `arr` contains elements that are not lists, they are directly appended to the result.
        """
    result_arr = []
    for el in arr:
        if isinstance(el, list):
            result_arr.extend(flatten(el))
        else:
            result_arr.append(el)
    return result_arr


def get_nth_fib(n, lookup=None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        lookup[n] = get_nth_fib(n - 1, lookup) + get_nth_fib(n - 2, lookup)
        return lookup[n]


# from algo ekspert
def permutations(arr: list) -> list:
    pass


def sum_of_digits(n: int) -> int:
    """
        Recursively calculates the sum of the digits of a given integer `n`.

        This function breaks down the number by extracting the last digit (`n % 10`)
        and recursively calling itself on the remaining digits (`n // 10`) until only
        a single-digit number remains.

        Parameters:
        ----------
        n : int
            A non-negative integer whose digits will be summed.

        Returns:
        -------
        int
            The sum of all digits in `n`.

        Example:
        --------
        >>> sum_of_digits(1234)
        10  # (1 + 2 + 3 + 4)

        >>> sum_of_digits(987)
        24  # (9 + 8 + 7)

        Notes:
        ------
        - The function uses a **recursive approach** to compute the sum of digits.
        - The **base case** occurs when `n` is a single-digit number (`n < 10`).
        - An **iterative approach** also exists, is implemented in number theory module.
        - If `n` is `0`, the function correctly returns `0` as the sum.
        """
    # there is also iterative version->number theory

    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def number_of_divisors(n: int, count=0, i=1) -> int:
    """
        Recursively calculates the number of divisors of a given integer `n`.

        This function iterates through all numbers from `1` to `n` to count how many
        of them divide `n` without a remainder using a recursive approach.

        Parameters:
        ----------
        n : int
            The number for which divisors are counted.
        count : int, optional
            The current count of divisors (default is 0).
        i : int, optional
            The current number being checked as a potential divisor (default is 1).

        Returns:
        -------
        int
            The total count of divisors of `n`.

        Example:
        --------
        >>> number_of_divisors(6)
        4

        >>> number_of_divisors(10)
        4

        Notes:
        ------
        - The function correctly increments `i` to progress through all numbers up to `n`.
        - This implementation uses recursion, which may result in a **stack overflow** for very large values of `n`.
        - An **iterative approach** may be more efficient in practice.
        """
    print(f"Calling number_of_divisors(n={n}, count={count}, i={i})")  # Log function entry
    if i > n:
        print(f"Base case reached! Returning count={count}")  # Log base case
        return count
    else:
        if n % i == 0:
            count += 1
            print(f"Divisor found: {i}, updated count={count}")
        i += 1  # increment index for next call
    return number_of_divisors(n, count, i)


# from AlgoExpert
def product_sum(array, depth=1):
    """
        Computes the **product sum** of a nested list, where each element is multiplied
        by its depth in the recursive structure.

        The function recursively traverses the nested list, summing elements while
        increasing the **depth multiplier** for deeper levels.

        Parameters:
        ----------
        arrays : list
            A list containing integers and/or nested lists of integers.
        depth : int, optional
            The current depth of recursion, used as a multiplier (default is 1).

        Returns:
        -------
        int
            The computed product sum.

        Example:
        --------
        >>> product_sum([1, 2, [3, 4], 5])
        22  # (1 + 2 + (3 + 4) * 2 + 5)

        >>> product_sum([1, [2, [3, 4], 5]])
        27  # (1 + (2 + (3 + 4) * 3 + 5) * 2)

        >>> product_sum([[[1, 2], 3], 4])
        19  # (((1 + 2) * 3 + 3) * 2 + 4)

        Notes:
        ------
        - Each **nested level** increases the depth multiplier by `1`.
        - The **base case** occurs when an element is an integer.
        - Uses **recursion** to handle arbitrary levels of nesting.
        - The function correctly accumulates `total_sum` rather than overwriting it.
        """
    total_sum = 0
    for el in array:
        if isinstance(el, list):
            total_sum += product_sum(el, depth + 1)
        else:
            total_sum += el
    return total_sum * depth


if __name__ == '__main__':
    number_of_divisors(10)
