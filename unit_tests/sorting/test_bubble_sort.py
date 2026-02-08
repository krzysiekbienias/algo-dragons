import pytest
from sorting.bubble_sort import bubble_sort
# from your_module import bubble_sort


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),                              # empty
        ([1], [1]),                            # single element
        ([1, 2, 3, 4], [1, 2, 3, 4]),           # already sorted
        ([4, 3, 2, 1], [1, 2, 3, 4]),           # reverse sorted
        ([3, 1, 2], [1, 2, 3]),                 # small unsorted
        ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),     # example-like
        ([2, 2, 2], [2, 2, 2]),                 # all equal
        ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),     # duplicates
        ([0, -1, 5, -10, 3], [-10, -1, 0, 3, 5])# negatives + zero
    ],
)
def test_bubble_sort_sorts_in_place(arr, expected):
    bubble_sort(arr)
    assert arr == expected


def test_bubble_sort_returns_none():
    arr = [2, 1]
    result = bubble_sort(arr)
    assert result is None


def test_bubble_sort_does_not_change_length():
    arr = [3, 2, 1, 2]
    n = len(arr)
    bubble_sort(arr)
    assert len(arr) == n