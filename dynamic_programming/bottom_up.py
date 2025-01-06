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


if __name__ == '__main__':
    watter_area_t1 = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    water_area(heights=watter_area_t1)
    print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print('the end')
