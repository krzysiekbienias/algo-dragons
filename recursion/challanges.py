def has_adjacent_cells(string: str, i=1):
    """
    Check if a string contains adjacent identical characters using recursion.

    Parameters
    ----------
    string : str
        The input string to check.
    i : int, optional
        The current index in the recursion (default is 0).

    Returns
    -------
    bool
        True if the string contains adjacent identical characters, False otherwise.

    Notes
    -----
    - The function starts checking from index 0.
    - If two consecutive characters are the same, it returns True immediately.
    - If the index reaches or exceeds `len(s) - 1`, it returns False.
    - The recursion propagates the result back up the call stack.
    - Iterative version in module strings.
    """
    # two base cases
    if i >= len(str):
        return False
    elif string[i] == string[i + 1]:
        return True

    else:
        return has_adjacent_cells(string, i + 1)


def count_occurrence(arr, num, i=0):
    """
    Count the occurrences of a given number in an array using recursion.

    Parameters
    ----------
    arr : list
        The list of numbers to search.
    num : any
        The number to count occurrences of.
    i : int, optional
        The current index in the recursion (default is 0).

    Returns
    -------
    int
        The number of times `num` appears in `arr`.

    Notes
    -----
    - The function recursively checks each element of `arr`.
    - If the current element matches `num`, it adds 1 to the count.
    - The function terminates when `i` reaches the end of `arr`.
    - The index `i` should start at 0, not 1, to include the first element in the count.
    """
    if i == len(arr):
        return 0
    elif arr[i] == num:
        return 1 + count_occurrence(arr, num, i + 1)
    else:
        return 0 + count_occurrence(arr, num, i + 1)


def sum_of_digits(number):
    """
    Compute the sum of the digits of a given number using recursion.

    Parameters
    ----------
    number : int
        The non-negative integer whose digits will be summed.

    Returns
    -------
    int
        The sum of the digits of `number`.

    Notes
    -----
    - The function uses integer division (`// 10`) to remove the last digit in each recursive step.
    - The base case occurs when `number` is a single-digit value (`number < 10`).
    - The remainder operator (`% 10`) extracts the last digit of `number`, which is added to the sum.
    - Assumes `number` is non-negative; behavior for negative numbers is undefined.
    """
    if number < 10:

        return number
    return sum_of_digits(number // 10) + number % 10


def get_subsequences(s):
    """
    Generate all subsequences of a given string.

    Parameters
    ----------
    s : str
        The input string for which subsequences are generated.

    Returns
    -------
    list
        A list containing all subsequences of `s`.

    Notes
    -----
    - Uses recursion to generate subsequences.
    - At each step, two choices are made: include or exclude the current character.
    - The base case is when the end of the string is reached.
    """
    subsequences = []
    _generate_subsequences(s, 0, "", subsequences)
    return subsequences


def _generate_subsequences(s, i, subsequence, subsequences):
    """
    Recursive helper function to generate subsequences.

    Parameters
    ----------
    s : str
        The input string.
    i : int
        The current index in the recursion.
    subsequence : str
        The current subsequence being formed.
    subsequences : list
        The list that stores all generated subsequences.

    Notes
    -----
    - If `i` reaches the length of `s`, append the formed subsequence.
    - Otherwise, recursively call with and without the current character.
    """
    if i == len(s):
        subsequences.append(subsequence)
        return

    # Include the current character
    _generate_subsequences(s, i + 1, subsequence + s[i], subsequences)

    # Exclude the current character
    _generate_subsequences(s, i + 1, subsequence, subsequences)