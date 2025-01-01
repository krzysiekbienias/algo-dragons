from typing import List


def minimum_waiting_time(queries):
    # minimum_waiting_time only considers the time queries spend waiting before they start execution.

    # Sort the list of queries in ascending order
    queries.sort()

    # Initialize total waiting time
    total_waiting_time = 0

    # Initialize accumulated waiting time for each query
    accumulated_waiting = 0

    # Loop through the queries, skipping the last one as it does not contribute to waiting time
    for i in range(len(queries) - 1):
        # Increase accumulated waiting by the duration of the current query
        accumulated_waiting += queries[i]

        # Add the current accumulated waiting to the total waiting time
        total_waiting_time += accumulated_waiting

    return total_waiting_time


def min_total_time(queries):
    #min_total_time considers the entire time span from the start of the first query to the completion of each query, sequentially.

    # Sort the queries in ascending order of their duration
    queries.sort()

    # Initialize the total time variable
    total_time = 0
    completion_time = 0

    # Iterate over the sorted queries and calculate the total time
    for query in queries:
        # Each query contributes to the total time as it completes
        completion_time += query
        total_time += completion_time

    return total_time


def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()
    # we need to determine which group will be in front based on height of the shortest person.
    if red_shirt_heights[0] < blue_shirt_heights[0]:
        for red, blue in zip(red_shirt_heights, blue_shirt_heights):
            if red >= blue:
                return False
    else:
        for red, blue in zip(red_shirt_heights, blue_shirt_heights):
            if blue >= red:
                return False

    return True


# 121 Best Time to Buy and Sell Stock

def best_time_to_buy_and_sell(prices: List[int]):
    if not prices:
        return 0  # Handle empty list case
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        # Update the minimum price seen so far
        min_price = min(min_price, price)
        # calulate profit if sold at the current price
        profit = price - min_price
        # update the maximum profit
        max_profit = max(max_profit, profit)
    return max_profit


# check if there is
def best_time_to_buy_and_sell_multiple_transactions(prices: List[int]):
    if not prices or len(prices) < 2:
        return 0
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit


if __name__ == '__main__':
    t1_queryies = [3, 2, 1, 2, 6]
    print(minimum_waiting_time(queries=t1_queryies))
    print(min_total_time(queries=t1_queryies))

    red_shirts = [5, 8, 1, 3, 4]
    blue_shirts = [6, 9, 2, 4, 5]
    class_photos(red_shirts, blue_shirts)
