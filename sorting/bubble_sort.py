from typing import List


def bubble_sort(arr: List[int]):
    """
        Sorts a list of integers in ascending order using the Bubble Sort algorithm.

        The algorithm repeatedly steps through the list, compares adjacent elements,
        and swaps them if they are in the wrong order. This process is repeated until
        the list is sorted. An optimization is included to terminate early if no swaps
        occur in a pass, indicating that the list is already sorted.

        Parameters:
        arr (List[int]): The list of integers to be sorted. Sorting is done in place.

        Returns:
        None: The function modifies the input list in place.

        Example:
        >>> nums = [5, 3, 8, 4, 2]
        >>> bubble_sort(nums)
        >>> print(nums)
        [2, 3, 4, 5, 8]

        Time Complexity:
        - Best case: O(n) (already sorted, due to early termination)
        - Average case: O(n²)
        - Worst case: O(n²) (reverse sorted)

        Space Complexity:
        - O(1) (in-place sorting)
    """
    changed = False
    for u in range(len(arr) - 1, 0, -1):
        for i in range(u):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True
        if not changed:
            break
