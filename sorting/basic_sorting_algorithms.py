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


def insertion_sorting(array):
    """
        Sort a list of elements using the insertion sort algorithm.

        Insertion sort is an online algorithm that builds a sorted array one element
        at a time. It works by iterating through the input array and considering
        each element one at a time, inserting it into its correct position
        within the previously sorted elements.

        Parameters:
        array (list): A list of elements to be sorted. The elements can be of any
                      type that supports comparison (e.g., integers, floats, strings).

        Returns:
        list: The sorted list in ascending order.

        Example:
        >>> insertion_sorting([5, 2, 9, 1, 5, 6])
        [1, 2, 5, 5, 6, 9]

        >>> insertion_sorting(['banana', 'apple', 'cherry'])
        ['apple', 'banana', 'cherry']
        """
    # It is an online algorithm. Does not require all input data upfront
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


def merge(left_array: List[int], right_array: List[int]) -> List[int]:
    """
    Description
    Merge two sorted arrays into a new sorted arrays.
    Parameters
    ----------
    left_array
    right_array

    Returns
    -------

    """
    l, r, res = 0, 0, []
    while l < len(left_array) or r < len(right_array):
        al = left_array[l] if l < len(left_array) else float('inf')
        br = right_array[r] if r < len(right_array) else float('inf')
        if al < br:
            res.append(al)
            l += 1
        else:
            res.append(br)
            r += 1
    return res


def merge_sort(array: List[int]) -> List[int]:
    """
    Description
    -----------
    Merge two sorted arrays into a new sorted arrays.
    Parameters
    ----------
    array

    Returns
    -------

    """
    if len(array) <= 1:
        return array
    l = merge_sort(array[:len(array) // 2])
    r = merge_sort(array[len(array) // 2:])
    return merge(l, r)





if __name__ == '__main__':
    test_array = [8, 5, 2, 9, 6, 3]
    print('Isertion sorting')
    res = insertion_sorting(array=test_array)
    print(res)
    print('Merge sorting')
    res2 = merge_sort(array=test_array)
    print(res2)
