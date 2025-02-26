from typing import List


def bubble_sort(arr: List[int]):
    changed=False
    for u in range(len(arr)-1, 0, -1):
        for i in range(u):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed=True
        if not changed:
            break





def insertion_sorting(array):
    #cards analogy
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
    test_array = [8,5,2,9,6,3]
    print('Isertion sorting')
    res=insertion_sorting(array=test_array)
    print(res)
    print('Merge sorting')
    res2=merge_sort(array=test_array)
    print(res2)
