def binary_search(array, target):
    l, r = 0, len(array)
    while r - l > 1:
        mid = (l + r) // 2
        if array[mid] < target:
            l = mid
        else:
            r = mid
    return array[l] == target


def binary_search_index(array, target):
    l, r = 0, len(array)
    while r - l > 1:
        mid = (l + r) // 2
        if array[mid] > target:
            r = mid
        else:
            l = mid
    return l if array[l] == target else -1


def search_in_sorted_matrix(matrix, target):
    """
    Searches for the target element in a 2D matrix where each row and column is sorted in ascending order.

    This function uses an efficient algorithm that starts from the top-right corner of the matrix
    and eliminates either a row or a column in each step based on the comparison with the target.
    This approach ensures a time complexity of O(m + n), where m is the number of rows and n is the
    number of columns.

    Args:
        matrix (List[List[int]]): A 2D list of integers where each row and each column is sorted
                                  in ascending order. The matrix must contain distinct elements.
        target (int): The integer value to search for in the matrix.

    Returns:
        List[int]: A list containing the indices [row, col] of the target element if found.
                   If the target is not found, returns [-1, -1].

    Example:
        >>> matrix = [
        ...     [1, 4, 7, 11],
        ...     [2, 5, 8, 12],
        ...     [3, 6, 9, 13],
        ...     [10, 14, 15, 16]
        ... ]
        >>> search_in_sorted_matrix(matrix, 5)
        [1, 1]
        >>> search_in_sorted_matrix(matrix, 20)
        [-1, -1]
    """
    # Initialize pointers to start at the top-right corner of the matrix
    row = 0
    col = len(matrix[0]) - 1  # Assumes the matrix is non-empty and rectangular

    # Traverse the matrix
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            # Target found, return its indices
            return [row, col]
        elif matrix[row][col] < target:
            # Target is greater, eliminate the current row
            row += 1
        else:
            # Target is smaller, eliminate the current column
            col -= 1

    # Target not found
    return [-1, -1]


def search_for_range(array, target):
    """
        Searches for the starting and ending positions of a target value in a sorted array.

        This function uses a two-pointer approach to find the range of indices where the target value appears.
        If the target is not found in the array, it returns [-1, -1].

        Parameters:
        -----------
        array : list of int
            A sorted list of integers in which to search for the target value.
        target : int
            The integer value to search for in the array.

        Returns:
        --------
        list of int
            A list containing two integers representing the starting and ending indices of the target value in the array.
            If the target is not found, returns [-1, -1].

        Examples:
        ---------
        >>> search_for_range([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        >>> search_for_range([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]
        """
    l = 0
    r = len(array) - 1

    # edge cases: target is outside the range of the array.
    if target < array[l] or target > array[r]:
        return [-1, -1]
    while l <= r:
        # Narrow down the search range by moving the pointers
        if array[l] < target < array[r]:
            l += 1
            r -= 1
        elif array[l] <= target < array[r]:
            r -= 1
            if l == r and target == array[r]:
                return [l, l]

        elif array[l] < target and array[r] <= target:
            l += 1
            if l == r and target == array[r]:
                return [r, r]
        else:
            return [l, r]
    return [-1, -1]


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]

    print(search_for_range([5, 7, 7, 8, 8, 10], 10))
    print(search_in_sorted_matrix(matrix=matrix, target=8))
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    print(binary_search_index(array, target))
