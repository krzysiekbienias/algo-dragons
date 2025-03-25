from typing import List


def top_five_average(marks, threshold=5):
    return sum(marks[:threshold]) // threshold


def high_five(items: List[List[int]]) -> List[List[int]]:
    performance_dict = {}
    results = []
    for item in items:
        if item[0] not in performance_dict:
            performance_dict[item[0]] = [item[1]]
        else:
            performance_dict[item[0]].append(item[1])
    for key in performance_dict:
        performance_dict[key].sort(reverse=True)
        results.append([key, top_five_average(performance_dict[key])])
    results_sorted = sorted(results, key=lambda x: x[0])
    return results_sorted


def kth_largest_element_in_array(array: List[int], k: int) -> List[int]:
    # version with sorting is in heap/challenges module
    array = sorted(array, reverse=True)
    return array[:k - 1]


#AlgoExpert
def tournament_winner(competitions, results):
    table = dict()
    for teams in competitions:
        for name in teams:
            table[name] = 0
    for competition, outcome in zip(competitions, results):
        winner = get_winner(competition, outcome)
        table[winner] += 3
    league_winner = max(table, key=table.get)
    return league_winner


def get_winner(teams, result):
    if result == 0:
        return teams[1]
    else:
        return teams[0]


# i don't know from which side it comes from.
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    l = 0
    p = len(nums) - 1
    while l < p:
        if nums[l] == nums[p] and abs(l - p) <= k:
            return True
        l += 1
    l = 0

    return False


def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    i, j = 0, 0
    min_diff = float('inf')
    closest_pair = []
    while i < len(array_one) and j < len(array_two):
        current_diff = abs(array_one[i] - array_two[j])
        if current_diff == 0:
            return [array_one[i], array_two[j]]
        min_diff = min(min_diff, current_diff)
        if current_diff <= min_diff:  # update closest pair only if differnece is smaller
            closest_pair = [array_one[i], array_two[j]]
        if array_one[i] < array_two[j]:
            i += 1
        else:
            j += 1
    return closest_pair


# AlgoExpert
def non_constructible_change(coins):
    coins.sort()
    if not coins:
        return 1
    current_change = 0
    for coin in coins:
        if coin > current_change:
            return current_change + 1
        current_change += coin
    # If we process all coins return next possible change [1,1,1,1]
    return current_change + 1


def minimum_loss(prices):
    """
        Computes the minimum loss when selling a house after purchasing it at a previous time.

        The function sorts the prices and keeps track of their original indices to ensure that
        only valid transactions (where selling occurs after buying) are considered.

        Parameters
        ----------
        prices : list of int
            A list of unique integers representing house prices at different time instances.

        Returns
        -------
        int
            The minimum loss possible when selling a house after purchasing it earlier.

        Notes
        -----
        - The prices are assumed to be unique.
        - Sorting is used to efficiently compute potential losses.
        - The function ensures that a valid sale occurs after the purchase.

        Examples
        --------
        >>> minimum_loss([20, 15, 10, 17, 12])
        2
        """
    # The dictionary di ensures the relationship between the original arrays and sorted prices is preserved.
    di = dict()
    for i, p in enumerate(prices):
        di[p] = i  # here the value is index and the key assumption in this challenge is that all prices are unique.
    prices.sort()
    min_loss = float('inf')
    for i in range(1, len(prices)):
        # Reject invalid order. invalid = selle before buy
        if di[prices[i - 1]] > di[prices[i]]:  # here we compare indexes
            min_loss = min(min_loss, prices[i] - prices[i - 1])
    return min_loss


def subarray_sort(array):
    """
       Finds the smallest subarray that, if sorted, will make the entire array sorted.

       This function identifies the left and right indices of the smallest unsorted
       subarray in a given list. If the array is already sorted, it returns [-1, -1].

       Parameters
       ----------
       array : list of int
           A list of integers that may be partially unsorted.

       Returns
       -------
       list of int
           A list containing two indices [l, r], where sorting `array[l:r+1]`
           would sort the entire array. If the array is already sorted, returns [-1, -1].

       Notes
       -----
       - The function first checks if the array is already sorted.
       - It then finds the first index (from the left) where the order is broken.
       - It finds the first index (from the right) where the order is broken.
       - Determines the min and max values in the unsorted subarray.
       - Expands the boundaries if necessary to ensure all misplaced elements are included.

       Examples
       --------
       >>> subarray_sort([1, 2, 4, 7, 10, 8, 6, 12, 14, 15])
       [3, 6]

       >>> subarray_sort([1, 2, 3, 4, 5])
       [-1, -1]

       >>> subarray_sort([1, 3, 2, 4, 5])
       [1, 2]
       """
    if sorted(array) == array:
        return [-1, -1]
    n = len(array)
    l = 0
    r = n - 1
    # 1. looking for index from left where order is broken
    while l < n and array[l] <= array[l + 1]:
        l += 1
    # 2. looking for index from right where order is broken.
    # Note that r is bounded from zero because we are going from
    while r > 0 and array[r] >= array[r - 1]:
        r -= 1
    # 3. find min and max in the unsorted subarray
    subarray_min = min(array[l:r + 1])
    subarray_max = max(array[l:r + 1])
    # 4. Expand the right boundary if needed pointers go to opposite direction
    while l > 0 and array[l - 1] > subarray_min:
        l -= 1
    while r < n - 1 and array[r + 1] < subarray_max:
        r += 1
    return [l, r]


def missing_numbers(nums):
    result = []
    numbers_in_scope = set(nums)
    for num in range(1, len(nums) + 3):
        if num not in numbers_in_scope:
            result.append(num)
    return result


def is_valid_subsequence(array, sequence):
    pass


# version where we may sort
def largest_range(arr):
    # edge case
    if not arr:
        return []
    result = []
    arr.sort()
    max_range = 0
    start = arr[0]
    for i in range(1, len(arr)):
        # case when we have duplicates
        if arr[i] == arr[i - 1]:
            continue
        elif arr[i] != arr[i - 1] + 1:  # gap in sequence.
            temp_range = arr[i - 1] - start + 1
            if temp_range > max_range:
                max_range = temp_range
                result = [start, arr[i - 1]]
            start = arr[i]  # new start range
    # final check for the last range
    length = arr[-1] - start + 1
    if length > max_range:
        result = [start, arr[-1]]
    return result


# compare with two-sum challenge
def three_sum(array, target):
    """
    Finds all unique triplets in the array that sum up to the given target.

    This function sorts the input array and uses a two-pointer approach to efficiently
    find triplets that add up to the target value, while handling duplicates to avoid
    redundant results.

    Parameters
    ----------
    array : list of int
        A list of integers that may contain duplicates.
    target : int
        The target sum for the three numbers.

    Returns
    -------
    list of list of int
        A list containing unique triplets [a, b, c] such that:
        a + b + c = target.

    Notes
    -----
    - The function first sorts the array to simplify searching and duplicate handling.
    - It iterates through each number and applies a two-pointer approach to find
      complementing pairs.
    - To ensure unique triplets, duplicate values are skipped.

    Examples
    --------
    >>> three_sum([1, 2, -2, -1, 0, 1, -1], 0)
    [[-2, 1, 1], [-1, 0, 1]]

    >>> three_sum([4, 3, 0, -1, -2, -3, 2, 1], 0)
    [[-3, 1, 2], [-2, -1, 3], [-1, 0, 1]]

    >>> three_sum([1, 2, 3, 4, 5], 10)
    []

    """

    array.sort()
    n = len(array)
    result = []
    for i in range(n - 2):  # to not get out of range exception.
        if i > 0 and array[i] == array[i - 1]:  # handle with duplicates in arrays
            continue
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
                while left < right and array[left] == array[left - 1]:  # if we have duplicates, we only traverse
                    left += 1
                while left < right and array[right] == array[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return result


def merge_overlapping_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges a list of overlapping intervals.

    Given a list of intervals represented as [start, end], this function merges all overlapping
    intervals and returns a list of the resulting non-overlapping intervals sorted by start time.

    Args:
        intervals (List[List[int]]): A list of intervals where each interval is a list [start, end].

    Returns:
        List[List[int]]: A list of merged, non-overlapping intervals sorted by their start times.

    Example:
        >>> merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])
        [[1, 2], [3, 8], [9, 10]]
    """
    results = []
    sorted_by_start = sorted(intervals, key=lambda x: x[0])
    current_start, current_end = sorted_by_start[0]
    for i in range(1, len(sorted_by_start)):
        next_start, next_end = sorted_by_start[i]
        if current_end < next_start:
            results.append([current_start, current_end])
            current_start, current_end = next_start, next_end

        else:

            current_end = max(current_end, next_end)
    results.append([current_start, current_end])

    return results


def zero_sum_array(nums):
    if nums == [0]:
        return True
    if len(nums) == 0:
        return False
    if sum(nums) == 0:
        return True

    seen_sum = set()
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if not prefix_sum in seen_sum:
            seen_sum.add(prefix_sum)
        elif prefix_sum == 0 or prefix_sum in seen_sum:
            return True
    return False


if __name__ == '__main__':
    zero_sum_array(nums=[])
    print(minimum_loss([20, 7, 8, 2, 5]))
    high_five([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]])

    array_one_t1 = [-1, 5, 10, 20, 28, 3]
    array_one_t2 = [26, 134, 135, 15, 17]
    smallest_difference(array_one_t1, array_one_t2)
