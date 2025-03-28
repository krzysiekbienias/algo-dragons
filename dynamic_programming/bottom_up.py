from typing import List
import math


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


def min_number_of_coins(amount: int, coins: List[int]) -> int|float:
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
    dp[0] = 0 # because to make amount 0 we need zero coins
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] != float("inf"):
        return dp[amount]
    else:
        return -1

def best_time_to_sell_and_buy()

if __name__ == '__main__':
    watter_area_t1 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    water_area(heights=watter_area_t1)
    print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print('the end')
