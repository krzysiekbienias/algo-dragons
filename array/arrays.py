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
    # The dictionary di ensures the relationship between the original array and sorted prices is preserved.
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
    result=[]
    numbers_in_scope=set(nums)
    for num in range(1,len(nums)+3):
        if num not in numbers_in_scope:
            result.append(num)
    return result



if __name__ == '__main__':
    subarray_sort(array=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(minimum_loss([20, 7, 8, 2, 5]))
    high_five([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]])

    array_one_t1 = [-1, 5, 10, 20, 28, 3]
    array_one_t2 = [26, 134, 135, 15, 17]
    smallest_difference(array_one_t1, array_one_t2)
