from typing import List
import math


# ╔════════════════════════════════════════════════════════════════════╗
# ║                    House Robbery — AlgoExpert                       ║
# ╚════════════════════════════════════════════════════════════════════╝

def house_robbery(arr: List[int]) -> int:
    """
        Calculate the maximum robbery amount from non-adjacent houses using dynamic programming.

        Parameters
        ----------
        arr : List[int]
            Array of non-negative integers representing money in each house.
            Must contain at least 1 element.
            Example: [2, 7, 9, 3, 1]

        Returns
        -------
        int
            Maximum amount that can be robbed without alerting police.
            Example: For input [2,7,9,3,1], returns 12 (2 + 9 + 1)

        Notes
        -----
        Algorithm:
        - Uses dynamic programming with O(n) time and space complexity
        - Recurrence relation: dp[i] = max(dp[i-1], dp[i-2] + arr[i])
        - Base cases:
            * Single house: return arr[0]
            * Two houses: return max(arr[0], arr[1])

        Examples
        --------
        >>> house_robbery([2, 7, 9, 3, 1])
        12
        >>> house_robbery([1, 2, 3, 1])
        4
        >>> house_robbery([100, 1, 1, 100])
        200

        Raises
        ------
        ValueError
            If input array is empty (implicitly handled by IndexError in current implementation)
        """
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    return dp[len(arr)-1]


# 120 Triangle - leetcode - medium
def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)
    m = len(triangle[-1])
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]
    for row in range(1, n):
        for col in range(row + 1):
            min_above = math.inf
            if col == 0:  #we are on the left there is only one cell above with location (r-1,col)
                min_above = dp[row - 1][col]
                dp[row][col] = min_above + triangle[row][col]
            elif col == row:  #we are in the right edge so we might move from this location (r-1,col-1)
                min_above = dp[row - 1][col - 1]
                dp[row][col] = min_above + triangle[row][col]
            else:
                min_above = min(dp[row - 1][col - 1], dp[row - 1][col])
                dp[row][col] = min_above + triangle[row][col]
    return min(dp[n - 1])


def water_area(heights: List[int]) -> int:
    if len(heights) < 3:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    max_area = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]

            else:
                max_area += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]

            else:
                max_area += right_max - heights[right]
            right -= 1
    return max_area


# ╔════════════════════════════════════════════════════════════════════╗
# ║                    Minimum number of coins — LeetCode              ║
# ╚════════════════════════════════════════════════════════════════════╝

def min_number_of_coins(amount: int, coins: List[int]) -> int | float:
    """
        Calculates the minimum number of coins required to make up a given amount
        using the provided denominations. If it's not possible to form the amount,
        returns -1.

        This implementation uses bottom-up dynamic programming (tabulation).

        Parameters:
            coins (list[int]): A list of distinct positive integers representing coin denominations.
            amount (int): The total amount to form.

        Returns:
            int: The minimum number of coins needed to make up the given amount,
                 or -1 if the amount cannot be formed with the given coins.

        Example:
            coins = [1, 2, 5], amount = 11
            → returns 3 (5 + 5 + 1)

        Notes:
            - dp[i] represents the minimum number of coins required to make amount i.
            - dp[0] = 0 since no coins are needed to make amount 0.
            - If no combination can form the amount, the value stays as float('inf').

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # because to make amount 0 we need zero coins
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] != float("inf"):
        return dp[amount]
    else:
        return -1


# ╔════════════════════════════════════════════════════════════════════╗
# ║                    Knapsac 0-1 — AlgoExpert                        ║
# ╚════════════════════════════════════════════════════════════════════╝

def knapsack_0_1_problem(values: list[int], weights: list[int], k: int):
    dp = [[0] * (k + 1) for _ in range(len(values))]
    if k == 0:
        return 0
    # if capacity is above weights, we may pack in everything in the backpack
    if k > sum(weights):
        return sum(values)
    for j in range(weights[0], k + 1):
        dp[0][j] = values[0]

    for i in range(1, len(values)):
        for j in range(k + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(values[i] + dp[i - 1][j - weights[i]], dp[i - 1][j])
    return dp[len(weights)][k]


def knapsack_0_1_problem_with_items_monitor(values: list[int], weights: list[int], k: int):
    dp = [[0] * (k + 1) for _ in range(len(values))]

    """
    What selected[i][j] Represents?
    True: Item i was selected for the knapsack when the remaining capacity was j.
    False: Item i was skipped at capacity j.
    """
    selected = [[False] * (k + 1) for _ in range(len(values))]  # for tracking selection
    if k == 0:
        return 0
    # if capacity is above weights we may pack in everything in the backpack
    if k > sum(weights):
        return sum(values)
    for j in range(weights[0], k + 1):
        dp[0][j] = values[0]

    for i in range(1, len(values)):
        for j in range(k + 1):
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
                selected[i][j] = True
            else:
                dp[i][j] = max(values[i] + dp[i - 1][j - weights[i]], dp[i - 1][j])
                selected[i][j] = True
    # Backtrack to find selected items (1-based indices)
    res = []
    remaining_capacity = k
    for i in range(len(values) - 1, -1, -1):
        if selected[i][remaining_capacity]:
            res.append(i + 1)  # Convert to 1-based index
            remaining_capacity -= weights[i]

    return [dp[len(values) - 1][k], res]


if __name__ == '__main__':
    # [[1, 2], [4, 3], [5, 6], [6, 7]], 10)
    knapsack_0_1_problem_with_items_monitor(values=[1, 4, 5, 6], weights=[2, 3, 6, 7], k=10)
    watter_area_t1 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    water_area(heights=watter_area_t1)
    print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print('the end')
